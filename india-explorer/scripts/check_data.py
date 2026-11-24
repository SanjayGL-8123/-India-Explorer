import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent / "backend"
DATA_DIR = BASE_DIR / "data"
STATES_FILE = DATA_DIR / "states.json"
DIST_DIR = DATA_DIR / "districts"
PLACES_DIR = DATA_DIR / "places"

URL_REGEX = re.compile(
    r"^https?://[^\s\"<>]+$"
)


def run_checks():
    print("=" * 60)
    print("INDIA EXPLORER - STAGE 2 DATA VALIDATION REPORT")
    print("=" * 60)

    records = []
    seen_ids = set()
    errors = []
    warnings = []

    # 1. Load states
    if not STATES_FILE.exists():
        print(f"CRITICAL: {STATES_FILE} does not exist.")
        sys.exit(1)

    with open(STATES_FILE, "r", encoding="utf-8") as f:
        states = json.load(f)
        for s in states:
            if s["id"] in seen_ids:
                errors.append(f"Duplicate id found in states.json: '{s['id']}'")
            seen_ids.add(s["id"])
            records.append(s)

    # 2. Load districts
    dist_count = 0
    for fpath in sorted(DIST_DIR.glob("*.json")):
        with open(fpath, "r", encoding="utf-8") as f:
            dists = json.load(f)
            for d in dists:
                if d["id"] in seen_ids:
                    errors.append(f"Duplicate id found in {fpath.name}: '{d['id']}'")
                seen_ids.add(d["id"])
                records.append(d)
                dist_count += 1

    # 3. Load places
    places_count = 0
    for fpath in sorted(PLACES_DIR.glob("*.json")):
        with open(fpath, "r", encoding="utf-8") as f:
            places = json.load(f)
            for p in places:
                if p["id"] in seen_ids:
                    errors.append(f"Duplicate id found in {fpath.name}: '{p['id']}'")
                seen_ids.add(p["id"])
                records.append(p)
                places_count += 1

    all_ids = {r["id"] for r in records}

    # 4. Check Parent Integrity
    orphan_parents = 0
    for r in records:
        pid = r.get("parent", "")
        # Root 'india' has empty parent or self
        if r["id"] == "india" and not pid:
            continue
        if not pid:
            warnings.append(f"Record '{r['id']}' ({r.get('type')}) has empty parent.")
        elif pid not in all_ids:
            errors.append(f"Record '{r['id']}' has non-existent parent '{pid}'.")
            orphan_parents += 1

    # 5. Check URL format
    invalid_urls = 0
    for r in records:
        wiki = r.get("wiki")
        if wiki and not URL_REGEX.match(wiki):
            errors.append(f"Invalid URL in '{r['id']}': {wiki}")
            invalid_urls += 1

    # Summary Statistics
    states_count = sum(1 for r in records if r.get("type") == "state")
    uts_count = sum(1 for r in records if r.get("type") == "union-territory")
    districts_count = sum(1 for r in records if r.get("type") == "district")
    temples_places_count = sum(1 for r in records if r.get("type") == "place")

    print(f"\nTotal Records Loaded: {len(records)}")
    print(f"  • Country (Root):    1")
    print(f"  • States:            {states_count} (Expected: 28)")
    print(f"  • Union Territories: {uts_count} (Expected: 8)")
    print(f"  • Districts:         {districts_count}")
    print(f"  • Places / Temples:  {temples_places_count}")
    print("-" * 60)
    print(f"Parent Check:         {'PASSED' if orphan_parents == 0 else f'FAILED ({orphan_parents} orphans)'}")
    print(f"Unique IDs Check:     {'PASSED' if len(records) == len(all_ids) else 'FAILED'}")
    print(f"URL Formats Check:    {'PASSED' if invalid_urls == 0 else f'FAILED ({invalid_urls} invalid)'}")
    print("=" * 60)

    if errors:
        print("\nERRORS DETECTED:")
        for err in errors[:10]:
            print(f"  [ERROR] {err}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors.")
        sys.exit(1)
    else:
        print("\nAll integrity checks passed successfully! Zero errors found.")


if __name__ == "__main__":
    run_checks()
