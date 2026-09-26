# IMD Best Track Metadata

## Provider

India Meteorological Department (IMD)  
Regional Specialised Meteorological Centre – Tropical Cyclones, New Delhi

## Dataset

**Best Tracks Data (1982–2026)**

## 2025 status

**Preliminary**

The IMD Best Track archive identifies the 2025 dataset as:

> Preliminary Tracks of Cyclones and Depressions for the year 2025

I therefore treat the 2025 records used in this case as preliminary rather than as a finalized post-season best track.

If IMD publishes a finalized 2025 dataset, I will compare the updated Senyar records with the preliminary version used here and document any changes that affect the analysis.

## Purpose in Case 001

I use this dataset to establish the reference chronology and track of Cyclonic Storm Senyar.

Where available, the extracted Senyar dataset contains:

- UTC timestamp
- latitude
- longitude
- system classification
- maximum sustained wind
- central pressure

The reference track provides the temporal framework for the precipitation, oceanic, atmospheric, and impact analyses developed later in the case.

## Source

**Provider:** IMD / RSMC New Delhi

**Best Track archive:**  
https://rsmcnewdelhi.imd.gov.in/report.php?internal_menu=MzM

**Direct workbook:**  
https://rsmcnewdelhi.imd.gov.in/download.php?path=uploads%2Fbest-track%2F78b4b0_Best_Tracks__Data__1982-2026_.xlsx

## Original file

`78b4b0_Best_Tracks__Data__1982-2026_.xlsx`

The raw workbook is retained unchanged.

## Access date

**2026-09-26**

## Local storage

The original workbook is stored locally under:

```text
data/raw/imd/78b4b0_Best_Tracks__Data__1982-2026_.xlsx
```

## Processing

The processing script reads the `2025` worksheet and selects rows whose trimmed, case-normalized storm name is `SENYAR`:

```text
scripts/process/extract_imd_senyar_track.py
```

It writes the positional records to:

```text
data/processed/imd_senyar_track_preliminary.csv
```

The processed dataset preserves the source worksheet and row number. Dates and times are combined as UTC timestamps. The storm name is stripped of surrounding whitespace, the system number is carried forward from the first Senyar row, and the workbook's `-` missing-value marker is written as an empty CSV field. The source units are retained for position, central pressure, maximum sustained wind and pressure drop; no unit conversion or interpolation is applied.

The worksheet does not state the wind averaging convention alongside these records. IMD's official tropical-cyclone guidance defines maximum sustained surface wind using a 3-minute averaging period, so I interpret the workbook values using that convention. I retain the values as reported and do not convert them to another averaging period. Comparisons with other agencies must state and account for any difference in wind averaging.

Source:

[IMD frequently asked questions on tropical cyclones](https://rsmcnewdelhi.imd.gov.in/images/pdf/faq.pdf)

Three named Senyar rows contain narrative event descriptions rather than positions. These record landfall in Indonesia, emergence into the Strait of Malacca and weakening into a well-marked low-pressure area. They remain available in the unchanged source workbook but are not represented as track points in the processed CSV.

## Quality control

The extraction checks that:

- at least one positional Senyar record is found
- latitude and longitude are numeric and within valid geographical ranges
- timestamps are unique and strictly increasing
- numeric missing-value markers are not interpreted as measurements

The current extraction contains 17 positional records from 2025 worksheet rows 266–284, excluding narrative rows 271 and 278. The sequence begins at `2025-11-25 03:00 UTC` and ends at `2025-11-27 15:00 UTC`. Narrative row 285 records the subsequent weakening but does not contain a position.

## Important distinction

This preliminary reference track is separate from IMD operational forecast bulletins. Operational advisories will be archived independently if forecast verification is added to the case.
