import json
import logging
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger("lgd_service")


def slugify(text: str) -> str:
    """Converts a name to a URL-friendly slug."""
    text = text.lower().strip()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


class LGDService:
    """
    Connects the India Explorer backend directly to the Local Government Directory (LGD)
    dataset, covering all 28 states, 8 union territories, 766 districts, 6,924 taluks (sub-districts),
    and 662,026 official census villages across India.
    """

    def __init__(self, lgd_dir: Optional[Path] = None):
        self.lgd_dir = lgd_dir or self._discover_lgd_dir()
        self.states: Dict[str, Dict[str, Any]] = {}
        self.districts: Dict[str, Dict[str, Any]] = {}
        self.taluks: Dict[str, Dict[str, Any]] = {}
        self.taluk_villages: Dict[str, List[Dict[str, Any]]] = {}
        self.village_index: Dict[int, Tuple[str, str]] = {}  # code -> (name, taluk_id)
        self.alias_map: Dict[str, str] = {}  # alternative slugs/codes -> canonical id

        # State and UT counts
        self.state_count = 0
        self.ut_count = 0
        self.district_count = 0
        self.taluk_count = 0
        self.village_count = 0

        self.initialized = False
        if self.lgd_dir and self.lgd_dir.exists():
            self._load_and_index()

    def _discover_lgd_dir(self) -> Path:
        """Finds the LGD directory relative to backend or environment variable."""
        env_path = os.getenv("LGD_DIR")
        if env_path and Path(env_path).exists():
            return Path(env_path)

        candidates = [
            Path(__file__).resolve().parent.parent / "frontend" / "lgd",
            Path(__file__).resolve().parent / "data" / "lgd",
            Path("c:/Users/Sanjay G L/Downloads/india-explorer/india-explorer/frontend/lgd"),
        ]
        for c in candidates:
            if c.exists() and (c / "india.json").exists():
                return c
        return candidates[0]

    def _load_and_index(self):
        """Loads and indexes the LGD dataset into memory."""
        try:
            logger.info(f"Indexing LGD dataset from {self.lgd_dir}...")
            # 1. Load india.json metadata
            india_file = self.lgd_dir / "india.json"
            if india_file.exists():
                with open(india_file, "r", encoding="utf-8") as f:
                    india_meta = json.load(f)
                    for s in india_meta.get("states", []):
                        sid = s.get("id")
                        if sid:
                            self.states[sid] = s
                            if s.get("type") == "union territory":
                                self.ut_count += 1
                            else:
                                self.state_count += 1

            # 2. Load all state files
            state_files = [f for f in self.lgd_dir.glob("*.json") if f.name != "india.json"]
            for fpath in state_files:
                with open(fpath, "r", encoding="utf-8") as f:
                    sdata = json.load(f)

                state_id = sdata.get("id") or slugify(sdata.get("name", fpath.stem))
                state_name = sdata.get("name", state_id.title())
                state_code = sdata.get("code")

                # Map state aliases
                self.alias_map[state_id] = state_id
                self.alias_map[slugify(state_name)] = state_id
                if state_code:
                    self.alias_map[f"state-{state_code}"] = state_id

                districts_list = sdata.get("districts", [])
                for dist in districts_list:
                    dist_code = dist.get("code")
                    dist_name = dist.get("name", "")
                    dist_slug = slugify(dist_name)
                    # Canonical district ID: slug-code (e.g. bagalkote-524)
                    dist_id = f"{dist_slug}-{dist_code}"

                    taluks_list = dist.get("taluks", [])
                    village_count_for_dist = sum(len(t.get("villages", [])) for t in taluks_list)

                    dist_record = {
                        "id": dist_id,
                        "name": dist_name,
                        "type": "district",
                        "code": dist_code,
                        "parent": state_id,
                        "path": f"{dist_name}, {state_name}, India",
                        "state_name": state_name,
                        "state_id": state_id,
                        "summary": (
                            f"Official district of {state_name} comprising {len(taluks_list)} "
                            f"sub-districts (taluks) and {village_count_for_dist:,} census villages."
                        ),
                        "census_year": "2011",
                        "taluk_count": len(taluks_list),
                        "village_count": village_count_for_dist,
                        "source": "Local Government Directory (LGD), Government of India",
                        "updated": "2024-11",
                    }
                    self.districts[dist_id] = dist_record
                    self.district_count += 1

                    # Register aliases
                    self.alias_map[dist_id] = dist_id
                    self.alias_map[f"district-{dist_code}"] = dist_id
                    # Only register raw slug if not already registered (to avoid cross-state collision)
                    if dist_slug not in self.alias_map:
                        self.alias_map[dist_slug] = dist_id

                    for taluk in taluks_list:
                        taluk_code = taluk.get("code")
                        taluk_name = taluk.get("name", "")
                        taluk_slug = slugify(taluk_name)
                        taluk_id = f"{taluk_slug}-{taluk_code}"

                        villages_list = taluk.get("villages", [])
                        taluk_record = {
                            "id": taluk_id,
                            "name": taluk_name,
                            "type": "taluk",
                            "code": taluk_code,
                            "parent": dist_id,
                            "district_name": dist_name,
                            "district_id": dist_id,
                            "state_name": state_name,
                            "state_id": state_id,
                            "path": f"{taluk_name} Taluk, {dist_name} District, {state_name}, India",
                            "summary": (
                                f"Sub-district (taluk/tehsil) in {dist_name} district, {state_name}. "
                                f"Administers {len(villages_list):,} census villages."
                            ),
                            "census_year": "2011",
                            "village_count": len(villages_list),
                            "source": "Local Government Directory (LGD), Government of India",
                            "updated": "2024-11",
                        }
                        self.taluks[taluk_id] = taluk_record
                        self.taluk_count += 1

                        self.alias_map[taluk_id] = taluk_id
                        self.alias_map[f"taluk-{taluk_code}"] = taluk_id
                        if taluk_slug not in self.alias_map:
                            self.alias_map[taluk_slug] = taluk_id

                        # Store compact village list
                        self.taluk_villages[taluk_id] = villages_list

                        for vill in villages_list:
                            v_code = vill.get("code")
                            v_name = vill.get("name", "")
                            if v_code:
                                self.village_index[v_code] = (v_name, taluk_id)
                                self.village_count += 1

            self.initialized = True
            logger.info(
                f"LGD Service loaded successfully: {self.state_count} States, {self.ut_count} UTs, "
                f"{self.district_count} Districts, {self.taluk_count} Taluks, {self.village_count:,} Villages."
            )
        except Exception as e:
            logger.error(f"Failed to load LGD dataset: {e}", exc_info=True)

    def resolve_id(self, pid: str) -> Optional[str]:
        """Resolves an ID, slug, or code to canonical ID."""
        pid = pid.strip().lower()
        if pid in self.alias_map:
            return self.alias_map[pid]
        # Match village code patterns: village-123456 or v-123456 or pure digits
        v_match = re.search(r"(?:village-|v-)?(\d{4,8})$", pid)
        if v_match:
            v_code = int(v_match.group(1))
            if v_code in self.village_index:
                return f"village-{v_code}"
        return pid

    def get_place(self, pid: str) -> Optional[Dict[str, Any]]:
        """Returns place details for any LGD entity (state, district, taluk, village)."""
        canon_id = self.resolve_id(pid)
        if not canon_id:
            return None

        # 1. District
        if canon_id in self.districts:
            d = dict(self.districts[canon_id])
            d["breadcrumbs"] = self.build_breadcrumbs(d)
            return d

        # 2. Taluk
        if canon_id in self.taluks:
            t = dict(self.taluks[canon_id])
            t["breadcrumbs"] = self.build_breadcrumbs(t)
            return t

        # 3. Village
        v_match = re.search(r"village-(\d+)$", canon_id)
        if v_match:
            v_code = int(v_match.group(1))
            if v_code in self.village_index:
                v_name, taluk_id = self.village_index[v_code]
                taluk = self.taluks.get(taluk_id, {})
                dist_name = taluk.get("district_name", "")
                state_name = taluk.get("state_name", "")
                v_record = {
                    "id": f"village-{v_code}",
                    "name": v_name,
                    "type": "village",
                    "code": v_code,
                    "parent": taluk_id,
                    "path": f"{v_name}, {taluk.get('name', '')} Taluk, {dist_name} District, {state_name}, India",
                    "summary": (
                        f"Official census village under {taluk.get('name', '')} sub-district, "
                        f"{dist_name} district, {state_name}. Identified by Census / LGD code {v_code}."
                    ),
                    "census_year": "2011",
                    "profile": {
                        "Village LGD Code": str(v_code),
                        "Sub-District / Taluk": taluk.get("name", ""),
                        "District": dist_name,
                        "State / UT": state_name,
                        "Census Status": "Inhabited Census Village (Census 2011)",
                    },
                    "source": "Local Government Directory (LGD), Government of India (Census 2011)",
                    "updated": "2024-11",
                }
                v_record["breadcrumbs"] = self.build_breadcrumbs(v_record)
                return v_record

        return None

    def get_children(self, pid: str, skip: int = 0, limit: int = 50) -> Dict[str, Any]:
        """
        Returns children for a place.
        For a state -> returns districts.
        For a district -> returns taluks.
        For a taluk -> returns paginated villages.
        """
        canon_id = self.resolve_id(pid) or pid

        # 1. State -> Districts
        state_key = self.alias_map.get(canon_id, canon_id)
        if state_key in self.states or canon_id in self.states:
            dists = [
                {
                    "id": d["id"],
                    "name": d["name"],
                    "type": "district",
                    "parent": d["parent"],
                    "summary": f"{d['name']} district with {d['taluk_count']} taluks and {d['village_count']:,} villages.",
                    "path": d["path"],
                    "code": d["code"],
                    "taluk_count": d["taluk_count"],
                    "village_count": d["village_count"],
                }
                for d in self.districts.values()
                if d["parent"] == state_key or d.get("state_id") == state_key
            ]
            dists.sort(key=lambda x: x["name"])
            return {
                "items": dists,
                "total": len(dists),
                "skip": 0,
                "limit": len(dists),
                "has_more": False,
            }

        # 2. District -> Taluks
        if canon_id in self.districts:
            taluks = [
                {
                    "id": t["id"],
                    "name": t["name"],
                    "type": "taluk",
                    "parent": canon_id,
                    "summary": f"{t['name']} taluk comprising {t['village_count']:,} villages.",
                    "path": t["path"],
                    "code": t["code"],
                    "village_count": t["village_count"],
                }
                for t in self.taluks.values()
                if t["parent"] == canon_id or t.get("district_id") == canon_id
            ]
            taluks.sort(key=lambda x: x["name"])
            return {
                "items": taluks,
                "total": len(taluks),
                "skip": 0,
                "limit": len(taluks),
                "has_more": False,
            }

        # 3. Taluk -> Villages (Paginated)
        if canon_id in self.taluks:
            raw_villages = self.taluk_villages.get(canon_id, [])
            total = len(raw_villages)
            paginated = raw_villages[skip : skip + limit]
            t_obj = self.taluks[canon_id]

            items = [
                {
                    "id": f"village-{v['code']}",
                    "name": v["name"],
                    "type": "village",
                    "parent": canon_id,
                    "code": v["code"],
                    "path": f"{v['name']}, {t_obj['name']} Taluk, {t_obj['district_name']}, India",
                    "summary": f"Census village (LGD code: {v['code']}) in {t_obj['name']} taluk.",
                }
                for v in paginated
            ]
            return {
                "items": items,
                "total": total,
                "skip": skip,
                "limit": limit,
                "has_more": (skip + limit) < total,
            }

        return {"items": [], "total": 0, "skip": 0, "limit": limit, "has_more": False}

    def build_breadcrumbs(self, place: Dict[str, Any]) -> List[Dict[str, str]]:
        """Constructs breadcrumbs from country down to place."""
        crumbs: List[Dict[str, str]] = [
            {"id": "india", "name": "India", "type": "country"}
        ]
        ptype = place.get("type")

        if ptype == "state" or ptype == "union-territory":
            crumbs.append({"id": place["id"], "name": place["name"], "type": ptype})
            return crumbs

        if ptype == "district":
            state_id = place.get("parent") or place.get("state_id", "")
            state_info = self.states.get(state_id, {})
            crumbs.append({
                "id": state_id,
                "name": state_info.get("name") or place.get("state_name", state_id.title()),
                "type": state_info.get("type", "state"),
            })
            crumbs.append({"id": place["id"], "name": place["name"], "type": "district"})
            return crumbs

        if ptype == "taluk":
            dist_id = place.get("parent") or place.get("district_id", "")
            dist_info = self.districts.get(dist_id, {})
            state_id = dist_info.get("parent", "")
            state_info = self.states.get(state_id, {})
            crumbs.append({
                "id": state_id,
                "name": state_info.get("name") or dist_info.get("state_name", "State"),
                "type": state_info.get("type", "state"),
            })
            crumbs.append({
                "id": dist_id,
                "name": dist_info.get("name", "District"),
                "type": "district",
            })
            crumbs.append({"id": place["id"], "name": place["name"], "type": "taluk"})
            return crumbs

        if ptype == "village":
            taluk_id = place.get("parent", "")
            taluk_info = self.taluks.get(taluk_id, {})
            dist_id = taluk_info.get("parent", "")
            dist_info = self.districts.get(dist_id, {})
            state_id = dist_info.get("parent", "")
            state_info = self.states.get(state_id, {})
            crumbs.append({
                "id": state_id,
                "name": state_info.get("name") or dist_info.get("state_name", "State"),
                "type": state_info.get("type", "state"),
            })
            crumbs.append({
                "id": dist_id,
                "name": dist_info.get("name", "District"),
                "type": "district",
            })
            crumbs.append({
                "id": taluk_id,
                "name": taluk_info.get("name", "Taluk"),
                "type": "taluk",
            })
            crumbs.append({"id": place["id"], "name": place["name"], "type": "village"})
            return crumbs

        return crumbs

    def search(self, q: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Fast search over LGD districts, taluks, and villages."""
        q_lower = q.lower().strip()
        if len(q_lower) < 2:
            return []

        results: List[Dict[str, Any]] = []

        # 1. Search districts first
        for d in self.districts.values():
            if q_lower in d["name"].lower():
                results.append({
                    "id": d["id"],
                    "name": d["name"],
                    "type": "district",
                    "parent": d["parent"],
                    "path": d["path"],
                    "summary": f"{d['name']} district with {d['taluk_count']} taluks",
                })
                if len(results) >= limit:
                    return results

        # 2. Search taluks
        for t in self.taluks.values():
            if q_lower in t["name"].lower():
                results.append({
                    "id": t["id"],
                    "name": t["name"],
                    "type": "taluk",
                    "parent": t["parent"],
                    "path": t["path"],
                    "summary": f"{t['name']} taluk, {t['district_name']}",
                })
                if len(results) >= limit:
                    return results

        # 3. Search villages (by prefix or code)
        if q_lower.isdigit():
            # Code lookup
            code = int(q_lower)
            if code in self.village_index:
                vname, taluk_id = self.village_index[code]
                t = self.taluks.get(taluk_id, {})
                results.append({
                    "id": f"village-{code}",
                    "name": vname,
                    "type": "village",
                    "parent": taluk_id,
                    "path": f"{vname}, {t.get('name', '')} Taluk, India",
                    "summary": f"Village (LGD Code: {code})",
                })
        else:
            count = 0
            for code, (vname, taluk_id) in self.village_index.items():
                if vname.lower().startswith(q_lower):
                    t = self.taluks.get(taluk_id, {})
                    results.append({
                        "id": f"village-{code}",
                        "name": vname,
                        "type": "village",
                        "parent": taluk_id,
                        "path": f"{vname}, {t.get('name', '')} Taluk, {t.get('district_name', '')}, India",
                        "summary": f"Census village under {t.get('name', '')} taluk",
                    })
                    count += 1
                    if len(results) >= limit or count >= 10:
                        break

        return results[:limit]

    def stats(self) -> Dict[str, int]:
        """Returns consolidated entity counts."""
        return {
            "states": self.state_count,
            "union_territories": self.ut_count,
            "districts": self.district_count,
            "taluks": self.taluk_count,
            "villages": self.village_count,
            "total": (
                1
                + self.state_count
                + self.ut_count
                + self.district_count
                + self.taluk_count
                + self.village_count
            ),
        }
