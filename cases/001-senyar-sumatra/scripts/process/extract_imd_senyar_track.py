"""Extract the preliminary IMD Senyar track from the source workbook.

The input workbook is treated as read-only. The output contains only rows with
valid positions; narrative event rows remain in the source workbook and are
reported by this script for audit purposes.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path
from typing import Any

from openpyxl import load_workbook


CASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = (
    CASE_DIR
    / "data"
    / "raw"
    / "imd"
    / "78b4b0_Best_Tracks__Data__1982-2026_.xlsx"
)
DEFAULT_OUTPUT = CASE_DIR / "data" / "processed" / "imd_senyar_track_preliminary.csv"
SHEET_NAME = "2025"
STORM_NAME = "SENYAR"

OUTPUT_FIELDS = (
    "source_sheet",
    "source_row",
    "system_number",
    "basin",
    "name",
    "time_utc",
    "latitude_deg_n",
    "longitude_deg_e",
    "ci_number",
    "central_pressure_hpa",
    "maximum_sustained_wind_kt",
    "pressure_drop_hpa",
    "grade",
)


def parse_date(value: Any) -> datetime:
    """Parse the date representations present in the 2025 worksheet."""
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        return datetime.strptime(value.strip(), "%d-%m-%Y")
    raise ValueError(f"unsupported date value: {value!r}")


def parse_time(value: Any) -> tuple[int, int]:
    """Return hour and minute from an HHMM cell stored as text or a number."""
    if isinstance(value, bool) or not isinstance(value, (str, int, float)):
        raise ValueError(f"unsupported time value: {value!r}")
    if isinstance(value, float) and not value.is_integer():
        raise ValueError(f"non-integral time value: {value!r}")
    text = str(int(value) if isinstance(value, (int, float)) else value).strip()
    if not text.isdigit() or len(text) > 4:
        raise ValueError(f"not an HHMM value: {value!r}")
    text = text.zfill(4)
    hour, minute = int(text[:2]), int(text[2:])
    if hour > 23 or minute > 59:
        raise ValueError(f"invalid HHMM value: {value!r}")
    return hour, minute


def optional_number(value: Any, field: str) -> int | float | str:
    """Normalize a numeric cell while preserving an explicit missing marker."""
    if value is None or (isinstance(value, str) and not value.strip()):
        return ""
    if isinstance(value, bool):
        raise ValueError(f"invalid {field}: {value!r}")
    if isinstance(value, (int, float)):
        return value
    text = str(value).strip()
    if text == "-":
        return ""
    try:
        number = float(text)
    except ValueError as exc:
        raise ValueError(f"invalid {field}: {value!r}") from exc
    return int(number) if number.is_integer() else number


def extract(input_path: Path) -> tuple[list[dict[str, Any]], list[tuple[int, str]]]:
    """Extract positional Senyar records and return excluded narrative rows."""
    workbook = load_workbook(input_path, read_only=True, data_only=True)
    if SHEET_NAME not in workbook.sheetnames:
        raise ValueError(f"worksheet {SHEET_NAME!r} not found")

    worksheet = workbook[SHEET_NAME]
    records: list[dict[str, Any]] = []
    narrative_rows: list[tuple[int, str]] = []
    current_system_number: str | int | None = None

    for source_row, row in enumerate(worksheet.iter_rows(min_row=2, values_only=True), 2):
        system_number, basin, name, date_value, time_value = row[:5]
        if system_number not in (None, ""):
            current_system_number = system_number
        if str(name or "").strip().upper() != STORM_NAME:
            continue

        latitude, longitude = row[5:7]
        if not isinstance(latitude, (int, float)) or isinstance(latitude, bool):
            narrative_text = next(
                (
                    str(value).strip()
                    for value in (time_value, latitude, longitude)
                    if isinstance(value, str) and not str(value).strip().isdigit()
                ),
                "",
            )
            narrative_rows.append((source_row, narrative_text))
            continue
        if not isinstance(longitude, (int, float)) or isinstance(longitude, bool):
            raise ValueError(f"row {source_row}: invalid longitude {longitude!r}")

        date = parse_date(date_value)
        hour, minute = parse_time(time_value)
        timestamp = date.replace(hour=hour, minute=minute)
        record = {
            "source_sheet": SHEET_NAME,
            "source_row": source_row,
            "system_number": current_system_number,
            "basin": str(basin).strip(),
            "name": str(name).strip().title(),
            "time_utc": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "latitude_deg_n": latitude,
            "longitude_deg_e": longitude,
            "ci_number": optional_number(row[7], "CI number"),
            "central_pressure_hpa": optional_number(row[8], "central pressure"),
            "maximum_sustained_wind_kt": optional_number(row[9], "wind speed"),
            "pressure_drop_hpa": optional_number(row[10], "pressure drop"),
            "grade": str(row[11]).strip(),
        }
        records.append(record)

    workbook.close()
    if not records:
        raise ValueError("no positional Senyar records found")

    timestamps = [record["time_utc"] for record in records]
    if timestamps != sorted(timestamps) or len(timestamps) != len(set(timestamps)):
        raise ValueError("timestamps are not strictly increasing and unique")
    for record in records:
        if not -90 <= float(record["latitude_deg_n"]) <= 90:
            raise ValueError(f"invalid latitude in source row {record['source_row']}")
        if not -180 <= float(record["longitude_deg_e"]) <= 180:
            raise ValueError(f"invalid longitude in source row {record['source_row']}")

    return records, narrative_rows


def write_csv(records: list[dict[str, Any]], output_path: Path) -> None:
    """Write records deterministically as UTF-8 CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    records, narrative_rows = extract(args.input)
    write_csv(records, args.output)
    print(f"Wrote {len(records)} positional records to {args.output}")
    print(f"Excluded {len(narrative_rows)} narrative source rows:")
    for source_row, text in narrative_rows:
        print(f"  {SHEET_NAME}!{source_row}: {text}")


if __name__ == "__main__":
    main()
