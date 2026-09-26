"""Download one authenticated IMERG Late V07 granule for structure inspection.

The sample is retained as immutable raw source data. Regional subsetting and
processing are intentionally deferred until the actual HDF5 structure has been
inspected.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import unquote, urlparse

import earthaccess
from earthaccess.exceptions import LoginStrategyUnavailable


CASE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = CASE_ROOT / "data" / "raw" / "gpm" / "imerg_late_v07"
SHORT_NAME = "GPM_3IMERGHHL"
VERSION = "07"
DEFAULT_START = "2025-11-20T00:00:00Z"
DEFAULT_END = "2025-11-20T00:29:59Z"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default=DEFAULT_START, help="UTC granule start")
    parser.add_argument("--end", default=DEFAULT_END, help="UTC granule end")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def authenticated_login() -> None:
    try:
        auth = earthaccess.login(strategy="netrc", persist=False)
    except LoginStrategyUnavailable as error:
        raise RuntimeError(
            "Earthdata credentials were not found in the local netrc file. "
            "Configure a machine entry for urs.earthdata.nasa.gov before retrying."
        ) from error
    if not auth.authenticated:
        raise RuntimeError("Earthdata authentication did not succeed")


def download_filename(granule: object) -> str:
    https_links = [link for link in granule.data_links() if link.startswith("https://")]
    if not https_links:
        raise RuntimeError("NASA CMR did not return an HTTPS data link for the granule")
    return Path(unquote(urlparse(https_links[0]).path)).name


def main() -> None:
    args = parse_args()
    authenticated_login()
    granules = earthaccess.search_data(
        short_name=SHORT_NAME,
        version=VERSION,
        temporal=(args.start, args.end),
    )
    if len(granules) != 1:
        raise RuntimeError(
            f"Expected one {SHORT_NAME} V{VERSION} granule; found {len(granules)}"
        )

    filename = download_filename(granules[0])
    target = args.output_dir / filename
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if target.exists():
        print(f"Existing raw granule retained: {target}")
        return

    downloaded = earthaccess.download(granules, local_path=args.output_dir, threads=1)
    if len(downloaded) != 1 or not target.exists():
        raise RuntimeError("Earthaccess did not produce the expected granule")
    print(f"Downloaded raw granule: {target}")


if __name__ == "__main__":
    main()
