import json
import logging
import os
import sys
from pathlib import Path
try:
    from pymongo import MongoClient, TEXT, ASCENDING
except ImportError:
    MongoClient = None
    TEXT = "text"
    ASCENDING = 1

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("seed")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
BACKEND_DIR = Path(__file__).resolve().parent
DATA_DIR = BACKEND_DIR / "data"
STATES_FILE = DATA_DIR / "states.json"
DIST_DIR = DATA_DIR / "districts"
PLACES_DIR = DATA_DIR / "places"
SEED_JSON = BACKEND_DIR / "seed.json"


def load_all_data():
    all_records = []
    seen_ids = set()

    # 1. States and Country
    if STATES_FILE.exists():
        with open(STATES_FILE, "r", encoding="utf-8") as f:
            states = json.load(f)
            for s in states:
                if s["id"] not in seen_ids:
                    s.setdefault("path", s.get("name", ""))
                    all_records.append(s)
                    seen_ids.add(s["id"])
        logger.info(f"Loaded {len(states)} records from {STATES_FILE.name}")

    # 2. Districts
    if DIST_DIR.exists():
        dist_count = 0
        for fpath in sorted(DIST_DIR.glob("*.json")):
            with open(fpath, "r", encoding="utf-8") as f:
                dists = json.load(f)
                for d in dists:
                    if d["id"] not in seen_ids:
                        d.setdefault("path", f"{d.get('name', '')}, India")
                        all_records.append(d)
                        seen_ids.add(d["id"])
                        dist_count += 1
        logger.info(f"Loaded {dist_count} districts from {DIST_DIR}")

    # 3. Places and Temples
    if PLACES_DIR.exists():
        places_count = 0
        for fpath in sorted(PLACES_DIR.glob("*.json")):
            with open(fpath, "r", encoding="utf-8") as f:
                places = json.load(f)
                for p in places:
                    if p["id"] not in seen_ids:
                        p.setdefault("path", f"{p.get('name', '')}, India")
                        all_records.append(p)
                        seen_ids.add(p["id"])
                        places_count += 1
        logger.info(f"Loaded {places_count} places/temples from {PLACES_DIR}")

    logger.info(f"Consolidated total of {len(all_records)} unique records.")
    return all_records


def seed_database():
    records = load_all_data()

    # Always update backend/seed.json as fallback cache
    with open(SEED_JSON, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    logger.info(f"Synchronized {len(records)} records to {SEED_JSON.name}")

    # Connect to MongoDB
    logger.info(f"Connecting to MongoDB at {MONGO_URL}...")
    try:
        client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=3000)
        client.admin.command("ping")
    except Exception as e:
        logger.warning(
            f"Could not connect to MongoDB ({e}). "
            f"Consolidated seed.json written successfully for in-memory operation."
        )
        return records

    db = client["india"]
    collection = db["places"]

    logger.info(f"Connected to MongoDB. Clearing existing collection...")
    collection.delete_many({})

    logger.info(f"Inserting {len(records)} places into 'india.places'...")
    collection.insert_many(records)

    logger.info("Creating indexes (id [unique], parent, type, (type, parent), and text index on name)...")
    collection.create_index("id", unique=True)
    collection.create_index("parent")
    collection.create_index("type")
    collection.create_index([("type", ASCENDING), ("parent", ASCENDING)])
    collection.create_index([("name", TEXT), ("path", TEXT)])

    logger.info(f"Successfully seeded {len(records)} records into MongoDB collection 'india.places'.")
    return records


if __name__ == "__main__":
    seed_database()
