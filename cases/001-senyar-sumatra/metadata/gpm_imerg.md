# GPM IMERG Metadata

## Intended role in Case 001

I will use IMERG to reconstruct the timing, spatial distribution and persistence of precipitation around northern Sumatra and the Strait of Malacca. IMERG is a satellite-based precipitation estimate. It will not be described as a rain-gauge observation, and comparisons with BMKG stations will retain the distinction between a point measurement and a `0.1°` grid-cell estimate.

## Target product

**Provider:** NASA Global Precipitation Measurement mission / GES DISC  
**Product:** GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree × 0.1 degree V07  
**Short name:** `GPM_3IMERGHH`  
**Current processing label:** `V07B`  
**Temporal resolution:** 30 minutes  
**Spatial resolution:** `0.1° × 0.1°`

The Final Run is the preferred research product because it incorporates the monthly gauge adjustment. NASA describes its normal latency as approximately 3.5 months, but catalogue availability must be verified rather than inferred from that nominal latency.

## First retrieval window

**Time:** `2025-11-20 00:00 UTC`–`2025-12-02 23:59 UTC`  
**Domain:** `90°E–110°E, 10°S–12°N`

The window begins with the first precursor circulation identified in the reviewed IMD operational sequence on 20 November. It continues through 2 December to retain the post-Senyar rainfall environment and the period of concurrent regional disturbance. This first retrieval is deliberately regional; it is not a climatological baseline.

The primary field will be the half-hourly precipitation rate in `mm h⁻¹`. Exact in-file variable names, dimensions, missing-value conventions and coordinate ordering will be checked against an acquired granule before processing code is written.

## Availability check

On **2026-09-26**, the live NASA Common Metadata Repository identified the Final V07 collection as:

```text
C2723754847-GES_DISC
```

Its latest catalogued half-hourly granule ended at `2025-09-30 23:59:59 UTC`. The Senyar retrieval window therefore returned no Final Run granules.

The corresponding Late Run collection is:

```text
GPM_3IMERGHHL V07
C2723754845-GES_DISC
```

The catalogue returns all **624** expected Late Run granules for the 13-day Senyar window, from `2025-11-20 00:00 UTC` through `2025-12-02 23:30 UTC`. They are not interchangeable with the gauge-adjusted Final Run.

On **2026-09-26**, I selected Late V07 for a clearly labelled provisional analysis so that the retrieval and processing workflow can be developed without implying that the Final product is available. Results intended for publication will be regenerated with Final V07 when it reaches the event period.

Catalogue availability can be checked without downloading data:

```powershell
.\.venv\Scripts\python.exe cases\001-senyar-sumatra\scripts\download\check_imerg_availability.py
```

## Retrieval status

**Provisional Late Run retrieval authorized; authenticated download pending. Final Run replacement remains required.**

The first raw-granule download was attempted on 2026-09-26, but the local Earthdata netrc file did not contain usable Earthdata credentials. No IMERG source data were downloaded or added to the repository. After Earthdata authentication is configured, the first granule can be retrieved with:

```powershell
.\.venv\Scripts\python.exe cases\001-senyar-sumatra\scripts\download\download_imerg_late_sample.py
```

I will inspect that source granule before defining the regional subsetting and aggregation code.

## Authoritative sources

- [NASA IMERG Final Run overview](https://gpm.nasa.gov/taxonomy/term/1417)
- [NASA IMERG V07 technical documentation](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation)
- [NASA GES DISC `GPM_3IMERGHH` collection](https://disc.gsfc.nasa.gov/datasets?keywords=GPM_3IMERGHH_07&page=1)
- [NASA IMERG V07 release notes](https://gpm.nasa.gov/resources/documents/imerg-v07-release-notes)
