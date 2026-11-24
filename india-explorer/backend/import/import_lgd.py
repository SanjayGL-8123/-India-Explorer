import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

try:
    from pymongo import MongoClient, UpdateOne
except ImportError:
    MongoClient = None
    UpdateOne = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("import_lgd")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
IMPORT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = IMPORT_DIR.parent
LGD_DIR = (BACKEND_DIR.parent / "frontend" / "lgd").resolve()
ERRORS_LOG = IMPORT_DIR / "errors.log"

BATCH_SIZE = 5000


def log_error(msg: str):
    with open(ERRORS_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")


def slugify(text: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "-", text.lower().strip()).strip("-")


def import_state_file(fpath: Path, collection, state_filter: str = None) -> Dict[str, int]:
    """Imports districts, taluks, and villages from one state JSON file into MongoDB."""
    counts = {"districts": 0, "taluks": 0, "villages": 0, "errors": 0}

    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        log_error(f"Failed to read file {fpath.name}: {e}")
        counts["errors"] += 1
        return counts

    state_id = data.get("id") or slugify(data.get("name", fpath.stem))
    state_name = data.get("name", state_id.title())
    state_type = data.get("type", "state")

    if state_filter and state_filter.lower() not in (state_id.lower(), slugify(state_name)):
        return counts

    logger.info(f"Processing state: {state_name} ({state_id})...")

    # Upsert state record
    state_doc = {
        "id": state_id,
        "name": state_name,
        "type": state_type,
        "parent": "india",
        "path": f"{state_name}, India",
        "code": data.get("code"),
        "source": "Local Government Directory (LGD), Government of India",
        "updated": "2024-11",
    }
    if collection is not None:
        collection.update_one({"id": state_id}, {"$set": state_doc}, upsert=True)

    batch_ops = []

    def flush_batch():
        if batch_ops and collection is not None:
            try:
                collection.bulk_write(batch_ops, ordered=False)
            except Exception as be:
                log_error(f"Bulk write error in {state_id}: {be}")
            batch_ops.clear()

    districts = data.get("districts", [])
    for dist in districts:
        dist_code = dist.get("code")
        dist_name = dist.get("name", "")
        dist_slug = slugify(dist_name)
        dist_id = f"{dist_slug}-{dist_code}"

        taluks = dist.get("taluks", [])
        v_count = sum(len(t.get("villages", [])) for t in taluks)

        dist_doc = {
            "id": dist_id,
            "name": dist_name,
            "type": "district",
            "parent": state_id,
            "path": f"{dist_name}, {state_name}, India",
            "code": dist_code,
            "taluk_count": len(taluks),
            "village_count": v_count,
            "census_year": "2011",
            "summary": f"Official district of {state_name} with {len(taluks)} taluks and {v_count:,} census villages.",
            "source": "Local Government Directory (LGD), Government of India",
            "updated": "2024-11",
        }
        counts["districts"] += 1
        if collection is not None:
            batch_ops.append(UpdateOne({"id": dist_id}, {"$set": dist_doc}, upsert=True))
            if len(batch_ops) >= BATCH_SIZE:
                flush_batch()

        for t in taluks:
            t_code = t.get("code")
            t_name = t.get("name", "")
            t_slug = slugify(t_name)
            t_id = f"{t_slug}-{t_code}"

            villages = t.get("villages", [])
            t_doc = {
                "id": t_id,
                "name": t_name,
                "type": "taluk",
                "parent": dist_id,
                "path": f"{t_name} Taluk, {dist_name} District, {state_name}, India",
                "code": t_code,
                "village_count": len(villages),
                "census_year": "2011",
                "summary": f"Sub-district (taluk) in {dist_name} district, {state_name}.",
                "source": "Local Government Directory (LGD), Government of India",
                "updated": "2024-11",
            }
            counts["taluks"] += 1
            if collection is not None:
                batch_ops.append(UpdateOne({"id": t_id}, {"$set": t_doc}, upsert=True))
                if len(batch_ops) >= BATCH_SIZE:
                    flush_batch()

            for v in villages:
                v_code = v.get("code")
                v_name = v.get("name", "")
                v_id = f"village-{v_code}"

                v_doc = {
                    "id": v_id,
                    "name": v_name,
                    "type": "village",
                    "parent": t_id,
                    "path": f"{v_name}, {t_name} Taluk, {dist_name} District, {state_name}, India",
                    "code": v_code,
                    "census_year": "2011",
                    "summary": f"Inhabited census village (LGD code: {v_code}) in {t_name} taluk.",
                    "source": "Local Government Directory (LGD), Government of India (Census 2011)",
                    "updated": "2024-11",
                }
                counts["villages"] += 1
                if collection is not None:
                    batch_ops.append(UpdateOne({"id": v_id}, {"$set": v_doc}, upsert=True))
                    if len(batch_ops) >= BATCH_SIZE:
                        flush_batch()

    flush_batch()
    logger.info(
        f"Completed {state_name}: {counts['districts']} districts, "
        f"{counts['taluks']} taluks, {counts['villages']:,} villages."
    )
    return counts


def main():
    parser = argparse.ArgumentParser(description="Import LGD states, districts, taluks, and villages into MongoDB.")
    parser.add_argument("--state", type=str, help="Import a specific state (e.g. karnataka, goa, bihar)")
    parser.add_argument("--all", action="store_true", help="Import all states and UTs")
    parser.add_argument("--dry-run", action="store_true", help="Count and validate without inserting into MongoDB")
    args = parser.parse_args()

    if not args.state and not args.all:
        logger.error("Please specify either --state <name> or --all.")
        parser.print_help()
        sys.exit(1)

    if not LGD_DIR.exists():
        logger.error(f"LGD directory not found at: {LGD_DIR}")
        sys.exit(1)

    collection = None
    if not args.dry_run:
        if MongoClient is None:
            logger.error("pymongo is not installed. Please install pymongo to import into MongoDB.")
            sys.exit(1)
        try:
            client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=2000)
            client.admin.command("ping")
            collection = client["india"]["places"]
            logger.info(f"Connected to MongoDB at {MONGO_URL}.")
        except Exception as e:
            logger.warning(f"Could not connect to MongoDB ({e}). Running dry-run validation.")
            args.dry_run = True

    state_files = sorted([f for f in LGD_DIR.glob("*.json") if f.name != "india.json"])
    total_stats = {"districts": 0, "taluks": 0, "villages": 0, "states": 0}

    start_time = time.time()
    for fpath in state_files:
        counts = import_state_file(fpath, collection, state_filter=args.state)
        if counts["districts"] > 0 or counts["taluks"] > 0:
            total_stats["states"] += 1
            total_stats["districts"] += counts["districts"]
            total_stats["taluks"] += counts["taluks"]
            total_stats["villages"] += counts["villages"]

    elapsed = time.time() - start_time
    logger.info(
        f"\n========================================\n"
        f"IMPORT SUMMARY REPORT\n"
        f"========================================\n"
        f"States/UTs processed: {total_stats['states']}\n"
        f"Total Districts:      {total_stats['districts']:,}\n"
        f"Total Taluks:         {total_stats['taluks']:,}\n"
        f"Total Villages:       {total_stats['villages']:,}\n"
        f"Elapsed Time:         {elapsed:.2f} seconds\n"
        f"Errors Logged:        {ERRORS_LOG}\n"
        f"========================================"
    )


if __name__ == "__main__":
    main()
