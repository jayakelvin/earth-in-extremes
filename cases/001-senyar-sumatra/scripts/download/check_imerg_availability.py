"""Check NASA CMR for IMERG V07 coverage of the Senyar analysis window.

This script queries catalogue metadata only. It does not download or modify data.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


CMR_BASE = "https://cmr.earthdata.nasa.gov/search"
PRODUCTS = {"final": "GPM_3IMERGHH", "late": "GPM_3IMERGHHL"}
VERSION = "07"
DEFAULT_START = "2025-11-20T00:00:00Z"
DEFAULT_END = "2025-12-02T23:59:59Z"
USER_AGENT = "earth-in-extremes/Case-001 IMERG availability check"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default=DEFAULT_START, help="UTC interval start")
    parser.add_argument("--end", default=DEFAULT_END, help="UTC interval end")
    parser.add_argument(
        "--product",
        choices=("final", "late", "both"),
        default="both",
        help="IMERG run to inspect",
    )
    return parser.parse_args()


def get_json(endpoint: str, parameters: dict[str, str]) -> tuple[dict[str, Any], int]:
    url = f"{CMR_BASE}/{endpoint}?{urlencode(parameters)}"
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
        hits = int(response.headers.get("CMR-Hits", len(payload["feed"]["entry"])))
    return payload, hits


def collection_for(short_name: str) -> dict[str, Any]:
    payload, _ = get_json(
        "collections.json",
        {"short_name": short_name, "version": VERSION, "page_size": "10"},
    )
    matches = [
        entry
        for entry in payload["feed"]["entry"]
        if entry.get("short_name") == short_name and entry.get("version_id") == VERSION
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected one CMR collection for {short_name} V{VERSION}; found {len(matches)}"
        )
    return matches[0]


def edge_granule(concept_id: str, temporal: str, sort_key: str) -> dict[str, Any] | None:
    payload, _ = get_json(
        "granules.json",
        {
            "concept_id": concept_id,
            "temporal": temporal,
            "page_size": "1",
            "sort_key": sort_key,
        },
    )
    entries = payload["feed"]["entry"]
    return entries[0] if entries else None


def inspect_product(label: str, start: str, end: str) -> dict[str, Any]:
    collection = collection_for(PRODUCTS[label])
    temporal = f"{start},{end}"
    _, hits = get_json(
        "granules.json",
        {
            "concept_id": collection["id"],
            "temporal": temporal,
            "page_size": "1",
        },
    )
    first = edge_granule(collection["id"], temporal, "+start_date")
    last = edge_granule(collection["id"], temporal, "-start_date")
    return {
        "run": label,
        "short_name": collection["short_name"],
        "version": collection["version_id"],
        "collection_concept_id": collection["id"],
        "collection_time_end": collection.get("time_end"),
        "requested_start_utc": start,
        "requested_end_utc": end,
        "granule_count": hits,
        "first_granule": first.get("title") if first else None,
        "last_granule": last.get("title") if last else None,
    }


def main() -> None:
    args = parse_args()
    labels = ("final", "late") if args.product == "both" else (args.product,)
    result = {
        "checked_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "catalogue": "NASA Common Metadata Repository (CMR)",
        "results": [inspect_product(label, args.start, args.end) for label in labels],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
