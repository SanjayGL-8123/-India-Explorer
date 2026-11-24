import json
import logging
import os
import re
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from lgd_service import LGDService, slugify

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("api")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
SEED_FILE = Path(__file__).parent / "seed.json"

# In-memory dataset fallback in case MongoDB is offline
IN_MEMORY_PLACES: List[Dict[str, Any]] = []
IN_MEMORY_MAP: Dict[str, Dict[str, Any]] = {}

if SEED_FILE.exists():
    try:
        with open(SEED_FILE, "r", encoding="utf-8") as f:
            IN_MEMORY_PLACES = json.load(f)
            for p in IN_MEMORY_PLACES:
                p.setdefault("path", p.get("name", ""))
                IN_MEMORY_MAP[p["id"]] = p
        logger.info(f"Loaded {len(IN_MEMORY_PLACES)} fallback records from seed.json.")
    except Exception as e:
        logger.warning(f"Could not load seed.json fallback: {e}")

# Initialize LGD service (connects to frontend/lgd)
lgd_service = LGDService()

# MongoDB Client with short 1s timeout to avoid hanging when offline
mongo_client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=1000, connectTimeoutMS=1000)
db = mongo_client["india"]["places"]

_last_mongo_check: float = 0.0
_mongo_available: bool = False


def is_mongodb_available() -> bool:
    global _last_mongo_check, _mongo_available
    now = time.time()
    # Check at most once every 15 seconds to keep API responses instantaneous
    if now - _last_mongo_check < 15.0:
        return _mongo_available

    _last_mongo_check = now
    try:
        mongo_client.admin.command("ping")
        _mongo_available = True
    except Exception:
        _mongo_available = False
    return _mongo_available


ALLOWED_ORIGINS_RAW = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173,http://localhost:8080,http://127.0.0.1:5173,http://127.0.0.1:8080,http://localhost:3000,http://127.0.0.1:3000",
)
ALLOWED_ORIGINS = [o.strip() for o in ALLOWED_ORIGINS_RAW.split(",") if o.strip()]

app = FastAPI(
    title="India Explorer API",
    description="REST API for exploring India's states, union territories, districts, and heritage attractions.",
    version="2.0.0",
)

# CORS middleware with explicit origins and wildcard support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if "*" in ALLOWED_ORIGINS else ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# In-memory IP-based rate limiting (120 requests/minute)
hits: Dict[str, List[float]] = defaultdict(list)
RATE_LIMIT_WINDOW = 60.0
RATE_LIMIT_MAX = 120


@app.middleware("http")
async def security_and_rate_limit(req: Request, call_next):
    # Handle preflight OPTIONS immediately with CORS headers
    if req.method == "OPTIONS":
        res = Response(status_code=204)
        origin = req.headers.get("origin", "*")
        res.headers["Access-Control-Allow-Origin"] = origin
        res.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        res.headers["Access-Control-Allow-Headers"] = "*"
        res.headers["Access-Control-Allow-Credentials"] = "true"
        return res

    client_host = "127.0.0.1"
    if req.client and req.client.host:
        client_host = req.client.host
    elif "x-forwarded-for" in req.headers:
        client_host = req.headers["x-forwarded-for"].split(",")[0].strip()

    now = time.time()
    hits[client_host] = [t for t in hits[client_host] if now - t < RATE_LIMIT_WINDOW]

    if len(hits[client_host]) >= RATE_LIMIT_MAX:
        origin = req.headers.get("origin", "*")
        return JSONResponse(
            status_code=429,
            headers={"Access-Control-Allow-Origin": origin},
            content={"error": "Too many requests. Please slow down and try again."},
        )

    hits[client_host].append(now)

    try:
        response: Response = await call_next(req)
    except Exception as exc:
        logger.error(f"Middleware caught exception: {exc}")
        origin = req.headers.get("origin", "*")
        return JSONResponse(
            status_code=500,
            headers={"Access-Control-Allow-Origin": origin},
            content={"error": "Internal server error"},
        )

    # Security headers
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


@app.exception_handler(HTTPException)
async def http_exception_handler(req: Request, exc: HTTPException):
    origin = req.headers.get("origin", "*")
    return JSONResponse(
        status_code=exc.status_code,
        headers={"Access-Control-Allow-Origin": origin},
        content={"error": exc.detail},
    )


@app.exception_handler(PyMongoError)
async def mongo_exception_handler(req: Request, exc: PyMongoError):
    logger.error(f"MongoDB error: {exc}")
    origin = req.headers.get("origin", "*")
    return JSONResponse(
        status_code=503,
        headers={"Access-Control-Allow-Origin": origin},
        content={"error": "Database service error. Please check MongoDB connection."},
    )


SLUG_REGEX = re.compile(r"^[a-z0-9-_.]{1,128}$")
LIGHT_PROJECTION = {
    "_id": 0,
    "id": 1,
    "name": 1,
    "type": 1,
    "parent": 1,
    "summary": 1,
    "path": 1,
}


def build_breadcrumbs(place: Dict[str, Any], use_mongo: bool) -> List[Dict[str, str]]:
    """Build breadcrumb hierarchy from the place up to India."""
    crumbs: List[Dict[str, str]] = []
    current: Optional[Dict[str, Any]] = place

    visited = set()
    while current and current.get("id") not in visited:
        visited.add(current.get("id"))
        crumbs.append({
            "id": current.get("id", ""),
            "name": current.get("name", ""),
            "type": current.get("type", ""),
        })
        parent_id = current.get("parent")
        if not parent_id or parent_id == current.get("id") or parent_id == "india":
            if parent_id == "india" and current.get("id") != "india":
                crumbs.append({"id": "india", "name": "India", "type": "country"})
            break

        current = None
        if use_mongo:
            current = db.find_one({"id": parent_id}, {"_id": 0, "id": 1, "name": 1, "type": 1, "parent": 1})
        if not current:
            current = IN_MEMORY_MAP.get(parent_id)
        if not current and lgd_service.initialized:
            lgd_p = lgd_service.get_place(parent_id)
            if lgd_p:
                current = {
                    "id": lgd_p["id"],
                    "name": lgd_p["name"],
                    "type": lgd_p.get("type", ""),
                    "parent": lgd_p.get("parent", ""),
                }

    crumbs.reverse()
    return crumbs


@app.get("/api/health")
def health_check():
    """Health check endpoint indicating API and database status."""
    mongo_ok = is_mongodb_available()
    lgd_ok = lgd_service.initialized
    return {
        "status": "ok",
        "database": "mongodb" if mongo_ok else "in-memory-fallback",
        "lgd_service": "connected" if lgd_ok else "offline",
        "total_records": (
            (db.estimated_document_count() if mongo_ok else len(IN_MEMORY_PLACES))
            + (lgd_service.village_count if lgd_ok else 0)
        ),
    }


@app.get("/api/stats")
def stats():
    """Returns overview statistics of all places in the system."""
    lgd_counts = lgd_service.stats() if lgd_service.initialized else {}

    if is_mongodb_available():
        places_count = db.count_documents({"type": "place"})
    else:
        places_count = sum(1 for p in IN_MEMORY_PLACES if p.get("type") == "place")

    states_count = lgd_counts.get("states", 28)
    ut_count = lgd_counts.get("union_territories", 8)
    districts_count = lgd_counts.get("districts", 766)
    taluks_count = lgd_counts.get("taluks", 6924)
    villages_count = lgd_counts.get("villages", 662026)
    total_count = lgd_counts.get("total", 669753) + places_count

    return {
        "total": total_count,
        "states": states_count,
        "union_territories": ut_count,
        "districts": districts_count,
        "taluks": taluks_count,
        "villages": villages_count,
        "landmarks": places_count,
    }


@app.get("/api/children/{pid}")
def get_children(pid: str, skip: int = 0, limit: int = 100, response: Response = None):
    """Returns direct children of a given place id with LGD integration."""
    pid = pid.strip().lower()
    if not SLUG_REGEX.match(pid):
        raise HTTPException(status_code=400, detail="Invalid place identifier")

    # 1. India -> All States & UTs
    if pid == "india":
        states_list = []
        if is_mongodb_available():
            states_list = list(db.find({"parent": "india"}, LIGHT_PROJECTION).sort("name", 1))
        if not states_list:
            states_list = [
                {
                    "id": p["id"],
                    "name": p["name"],
                    "type": p.get("type", ""),
                    "parent": p.get("parent", ""),
                    "summary": p.get("summary", ""),
                    "path": p.get("path", ""),
                }
                for p in IN_MEMORY_PLACES
                if p.get("parent") == "india"
            ]
        # Enrich with LGD stats if available
        if lgd_service.initialized:
            for s in states_list:
                sid = s["id"]
                meta = lgd_service.states.get(sid, {})
                if meta:
                    s["districts_count"] = meta.get("districts", 0)
                    s["taluk_count"] = meta.get("taluks", 0)
                    s["village_count"] = meta.get("villages", 0)
        return states_list

    # 2. Check LGD children (for states, districts, and taluks)
    if lgd_service.initialized:
        lgd_res = lgd_service.get_children(pid, skip=skip, limit=limit)
        if lgd_res.get("items"):
            # If pid is a state, check if we have richer district objects in DB / seed to overlay
            canon_pid = lgd_service.resolve_id(pid)
            if pid in lgd_service.states or canon_pid in lgd_service.states:
                for item in lgd_res["items"]:
                    dist_slug = slugify(item["name"])
                    raw_d = IN_MEMORY_MAP.get(dist_slug) or IN_MEMORY_MAP.get(item["name"].lower())
                    if raw_d:
                        if raw_d.get("summary"):
                            item["summary"] = raw_d["summary"]
                        if raw_d.get("profile"):
                            item["profile"] = raw_d["profile"]

            # Also check if any places/temples exist under this district in DB/seed
            extra_places = [
                {
                    "id": p["id"],
                    "name": p["name"],
                    "type": p.get("type", "place"),
                    "parent": pid,
                    "summary": p.get("summary", ""),
                    "path": p.get("path", ""),
                }
                for p in IN_MEMORY_PLACES
                if p.get("parent") in (pid, canon_pid) and p.get("type") == "place"
            ]

            all_items = extra_places + lgd_res["items"]
            if response:
                response.headers["X-Total-Count"] = str(lgd_res["total"] + len(extra_places))
                response.headers["X-Has-More"] = "true" if lgd_res["has_more"] else "false"
            return all_items

    # 3. Fallback to DB or in-memory
    if is_mongodb_available():
        children_cursor = db.find({"parent": pid}, LIGHT_PROJECTION).sort("name", 1)
        return list(children_cursor)

    kids = [
        {
            "id": p["id"],
            "name": p["name"],
            "type": p.get("type", ""),
            "parent": p.get("parent", ""),
            "summary": p.get("summary", ""),
            "path": p.get("path", ""),
        }
        for p in IN_MEMORY_PLACES
        if p.get("parent") == pid
    ]
    kids.sort(key=lambda x: x["name"])
    return kids


@app.get("/api/place/{pid}")
def get_place(pid: str):
    """Returns full details of a specific place including breadcrumbs."""
    pid = pid.strip().lower()
    if not SLUG_REGEX.match(pid):
        raise HTTPException(status_code=400, detail="Invalid place identifier")

    use_mongo = is_mongodb_available()
    place = None
    if use_mongo:
        place = db.find_one({"id": pid}, {"_id": 0})
    if not place:
        raw_place = IN_MEMORY_MAP.get(pid)
        place = dict(raw_place) if raw_place else None

    # If place found, check if LGD has extra details (like LGD code or taluk count)
    if place:
        if lgd_service.initialized:
            lgd_info = lgd_service.get_place(pid)
            if lgd_info:
                if "code" in lgd_info:
                    place.setdefault("lgd_code", lgd_info["code"])
                if "taluk_count" in lgd_info:
                    place.setdefault("taluk_count", lgd_info["taluk_count"])
                if "village_count" in lgd_info:
                    place.setdefault("village_count", lgd_info["village_count"])
        place["breadcrumbs"] = build_breadcrumbs(place, use_mongo)
        return place

    # If not found in DB/seed, check LGD service
    if lgd_service.initialized:
        lgd_place = lgd_service.get_place(pid)
        if lgd_place:
            return lgd_place

    raise HTTPException(status_code=404, detail="Place not found")


@app.get("/api/search")
def search_places(q: str = ""):
    """Fast search across places, states, districts, and landmarks."""
    clean_q = re.sub(r"[^\w\s-]", "", q).strip()[:50]
    if len(clean_q) < 2:
        return []

    results = []
    seen_ids = set()

    if is_mongodb_available():
        regex_pattern = re.escape(clean_q).replace(r"\ ", ".*")
        query = {
            "$or": [
                {"name": {"$regex": regex_pattern, "$options": "i"}},
                {"path": {"$regex": regex_pattern, "$options": "i"}},
                {"summary": {"$regex": regex_pattern, "$options": "i"}},
            ]
        }
        for item in db.find(query, LIGHT_PROJECTION).limit(20):
            if item["id"] not in seen_ids:
                results.append(item)
                seen_ids.add(item["id"])
    else:
        q_lower = clean_q.lower()
        for p in IN_MEMORY_PLACES:
            if (
                q_lower in p.get("name", "").lower()
                or q_lower in p.get("path", "").lower()
                or q_lower in p.get("summary", "").lower()
            ):
                if p["id"] not in seen_ids:
                    results.append({
                        "id": p["id"],
                        "name": p["name"],
                        "type": p.get("type", ""),
                        "parent": p.get("parent", ""),
                        "summary": p.get("summary", ""),
                        "path": p.get("path", ""),
                    })
                    seen_ids.add(p["id"])
                if len(results) >= 20:
                    break

    # If fewer than 20 results, augment with LGD search (districts, taluks, villages)
    if len(results) < 20 and lgd_service.initialized:
        lgd_matches = lgd_service.search(clean_q, limit=20 - len(results))
        for m in lgd_matches:
            if m["id"] not in seen_ids:
                results.append(m)
                seen_ids.add(m["id"])

    return results
