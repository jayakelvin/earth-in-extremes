# Case 001 Data

Large raw datasets used in this case are not stored in the repository.

Instead, this directory contains small processed datasets where redistribution
is permitted, together with documentation and scripts for retrieving the
original source data.

## Data principles

- Original providers remain the authoritative source.
- Raw data are not redistributed unless licensing clearly permits it.
- Dataset versions and retrieval dates are recorded.
- Processing from raw data to derived products is documented.
- Small processed datasets may be included when doing so materially improves
  reproducibility and complies with the source terms.

## Planned core datasets

- IMD/RSMC New Delhi tropical cyclone track and operational advisories
- NASA GPM IMERG V07 precipitation
- NOAA OISST V2.1 sea-surface temperature
- ERA5 atmospheric reanalysis

Additional datasets will be added only when required by the scientific
questions.

## Available processed data

`processed/imd_senyar_track_preliminary.csv` contains the 17 positional Senyar
records extracted from the preliminary IMD 2025 best-track worksheet. Source
worksheet row numbers are retained in the CSV so that every record can be
checked against the unchanged workbook.

Recreate the file from the repository root with:

```text
python cases/001-senyar-sumatra/scripts/process/extract_imd_senyar_track.py
```

The source workbook, extraction method, exclusions and quality-control checks
are documented in `../metadata/imd_best_track.md`.

## IMERG retrieval status

No GPM IMERG files are currently stored locally. The first retrieval window is
defined in `../metadata/gpm_imerg.md`, but the preferred Final V07 product does
not yet cover the Senyar period in NASA's live catalogue. Late V07 has been
selected for a clearly labelled provisional analysis. Its first source granule
will be retained under `raw/gpm/imerg_late_v07/` after authenticated retrieval.
