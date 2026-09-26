# Data Inventory

## Case 001 — Cyclone Senyar and the 2025 Sumatra Floods

**Status:** dataset planning

This document defines the datasets considered for Case 001 before large-scale downloading begins.

The objective is to use the smallest set of scientifically appropriate datasets required to answer the research questions.

Datasets are classified as:

- **Essential** — required for the core case
- **Supporting** — strengthens interpretation or validation
- **Optional** — useful only if the core analysis indicates a clear need

---

# 1. Analysis strategy

The analysis uses three nested spatial scales.

| Domain | Approximate extent | Primary purpose |
|---|---|---|
| Indo-Pacific | 70°E–160°E, 20°S–30°N | Climate background and large-scale circulation |
| Maritime Continent | 90°E–150°E, 15°S–20°N | Tropical waves, surrounding disturbances and moisture pathways |
| Sumatra–Malacca | 92°E–108°E, 8°S–10°N | Senyar genesis, rainfall and local processes |

Different datasets and temporal resolutions may be used at each scale.

Downloading hourly data for the full Indo-Pacific domain is unnecessary unless later analysis demonstrates a specific need.

---

# 2. Tropical cyclone chronology and track

## IMD / RSMC New Delhi

**Priority:** Essential

**Purpose**

Establish the authoritative operational chronology of Senyar and reconstruct:

- precursor disturbance
- depression stage
- cyclone genesis
- storm centre positions
- intensity evolution
- land interaction
- weakening
- operational forecast evolution

**Products**

RSMC New Delhi 2025 system archive:

- national bulletins
- RSMC bulletins
- observed and forecast track graphics
- TCFP diagnostic reports
- extended-range cyclogenesis outlooks
- annual cyclone report

**Primary period**

20–28 November 2025

with particular focus on:

25–27 November 2025.

**Variables / information**

- valid time
- latitude
- longitude
- classification
- central pressure
- maximum sustained wind
- movement direction
- movement speed
- forecast positions

**Access**

Public RSMC New Delhi archive.

**Important limitation**

Operational intensity estimates may differ from later post-event analyses and from estimates produced by other agencies.

Wind averaging conventions must be documented before comparing intensity estimates.

---

# 3. Indonesian operational observations

## BMKG

**Priority:** Essential for validation and event context

**Purpose**

Provide authoritative Indonesian information on:

- Senyar
- observed rainfall
- climate background
- tropical waves
- warnings
- regional impacts

**Relevant products**

- Senyar press releases
- weekly weather outlooks
- monthly climate bulletin
- atmospheric dynamics analyses
- available station precipitation

**Confirmed observations already identified**

Examples include:

- BPP Kuala, Bireuen: 411 mm/day
- Aceh Utara: 310.8 mm/day
- Medan: 262.2 mm/day
- Tapanuli Tengah: 229.7 mm/day
- Padang Pariaman: 154 mm/day

These values must retain their original station/location and accumulation-period metadata.

**Data redistribution**

To be verified product by product.

BMKG data should not be uploaded to this repository unless redistribution rights are clear.

When necessary, provide:

- original source citation
- retrieval instructions
- permitted derived results

instead of raw data.

---

# 4. Satellite precipitation

## NASA GPM IMERG Final Run V07

**Priority:** Essential

**Purpose**

Reconstruct the spatial and temporal evolution of rainfall independently of individual gauges.

**Product**

IMERG Final Run Version 07.

**Resolution**

Spatial:

\[
0.1^\circ \times 0.1^\circ
\]

Temporal:

\[
30\text{ minutes}
\]

NASA describes IMERG as combining precipitation estimates from multiple passive-microwave and infrared sensors. The Final Run additionally incorporates monthly gauge information and is intended as the research-quality retrospective product.

**Core period**

20 November–2 December 2025

A longer window may later be used for antecedent rainfall.

**Core domain**

Approximately:

\[
90^\circ E-110^\circ E,\quad
10^\circ S-12^\circ N
\]

The domain may be expanded where necessary.

**Variables**

Primary:

- precipitation rate

Potential quality information:

- precipitation source
- probability of liquid precipitation
- observation time / sensor information

Only variables necessary to the analysis should be retrieved.

**Derived products**

- 30-minute rainfall evolution
- hourly precipitation
- 3-hour accumulation
- 6-hour accumulation
- 12-hour accumulation
- rolling 24-hour accumulation
- event accumulation
- rainfall persistence
- spatial maximum

**Access**

NASA GES DISC / GPM data services.

Free Earthdata registration may be required.

**Important limitation**

IMERG is a satellite-based precipitation estimate.

It must not be described as a rain-gauge observation.

Comparison with BMKG gauges should consider the difference between a point measurement and a 0.1° grid-cell estimate.

---

# 5. Atmospheric circulation

## ERA5

**Priority:** Essential

**Provider**

Copernicus Climate Change Service / ECMWF.

**Resolution**

Standard gridded ERA5:

\[
0.25^\circ \times 0.25^\circ
\]

Temporal:

hourly.

ERA5 pressure-level data are available on 37 pressure levels from 1000 to 1 hPa.

**Licence**

CC BY.

**Access**

Copernicus Climate Data Store.

---

## 5.1 Pressure-level variables

Initial variables:

- u-component of wind
- v-component of wind
- specific humidity
- temperature
- geopotential
- vertical velocity

Potential pressure levels:

\[
1000,\;925,\;850,\;700,\;500,\;300,\;200\text{ hPa}
\]

Not every variable requires every level.

### Candidate derived diagnostics

#### Relative vorticity

\[
\zeta =
\frac{\partial v}{\partial x}
-
\frac{\partial u}{\partial y}
\]

#### Horizontal divergence

\[
\nabla_h\cdot\mathbf{V}
=
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
\]

#### Vertical wind shear

For example:

\[
\mathbf{V}_{200}-\mathbf{V}_{850}
\]

#### Moisture transport

\[
\mathbf{Q}
=
\frac{1}{g}
\int_{p_t}^{p_s}
q\mathbf{V}\,dp
\]

where \(q\) is specific humidity and \(\mathbf{V}\) is horizontal wind.

The exact integration method and pressure bounds must be documented before calculation.

---

## 5.2 Single-level variables

Candidate variables:

- mean sea-level pressure
- total-column water vapour
- total precipitation
- 10-m wind components

Sea-surface temperature will preferably come from NOAA OISST rather than mixing ERA5 SST into the main ocean analysis.

---

# 6. ERA5 retrieval strategy

ERA5 will be downloaded differently for each scale.

## Indo-Pacific context

Approximate domain:

70°E–160°E  
20°S–30°N

Temporal resolution:

initially daily means or selected synoptic times.

Purpose:

- broad circulation
- monsoon environment
- surrounding disturbances

No full month of hourly fields should initially be downloaded.

---

## Maritime Continent

Approximate domain:

90°E–150°E  
15°S–20°N

Temporal resolution:

initially 6-hourly:

00, 06, 12 and 18 UTC.

Core period:

15 November–2 December 2025.

Purpose:

- vorticity evolution
- moisture pathways
- surrounding tropical systems
- synoptic circulation

---

## Sumatra–Malacca

Approximate domain:

92°E–108°E  
8°S–10°N

Temporal resolution:

hourly where scientifically useful.

Core period:

23–28 November 2025.

Purpose:

- cyclogenesis
- low-level convergence
- vorticity
- moisture transport
- vertical shear
- rainfall environment

This nested approach reduces storage and computation while retaining the temporal detail required near Senyar.

---

# 7. Sea-surface temperature

## NOAA OISST Version 2.1

**Priority:** Essential

**Provider**

NOAA National Centers for Environmental Information.

**Product**

Daily Optimum Interpolation Sea Surface Temperature Version 2.1.

**Resolution**

\[
0.25^\circ
\]

daily.

**Coverage**

September 1981–present.

**Purpose**

Investigate:

- SST during Senyar genesis
- SST anomalies
- warm-water distribution around Sumatra and the Strait of Malacca
- large-scale Indian Ocean and Maritime Continent ocean state

**Variables**

- SST
- SST anomaly
- sea-ice concentration not relevant to this case

**Study periods**

Event:

November 2025.

Potential climatological baseline:

to be defined before anomaly calculation.

A standard climatological period should be chosen deliberately rather than using whichever anomaly field is easiest to download.

**Access**

NOAA NCEI direct download, THREDDS, ERDDAP or cloud services.

**Important limitation**

OISST is an optimally interpolated blended analysis combining satellite and in-situ observations.

It is not a direct point measurement of SST.

---

# 8. Large-scale convection

## NOAA Interpolated OLR

**Priority:** Supporting

**Purpose**

Diagnose broad-scale tropical convection and assist with tropical-wave analysis.

**Resolution**

\[
2.5^\circ\times2.5^\circ
\]

daily.

**Coverage**

1979–near present.

**Variables**

Outgoing longwave radiation.

Low OLR is generally associated with high, cold cloud and deep tropical convection, but OLR should not be interpreted directly as precipitation amount.

**Potential analyses**

- OLR anomaly
- longitude–time diagrams
- convective propagation
- relationship with tropical-wave activity

**Access**

NOAA Physical Sciences Laboratory.

---

# 9. Madden–Julian Oscillation

## Bureau of Meteorology RMM index

**Priority:** Supporting

**Provider**

Australian Bureau of Meteorology.

**Variables**

- RMM1
- RMM2
- MJO amplitude
- MJO phase

**Purpose**

Place November 2025 within the established Wheeler–Hendon MJO framework.

The RMM index combines tropical OLR and upper- and lower-tropospheric zonal winds.

**Use**

Context only initially.

RMM phase alone will not be used to claim that the MJO caused Senyar or the Sumatra rainfall.

**Access**

BoM MJO monitoring archive and downloadable RMM data.

---

# 10. Equatorial-wave diagnostics

**Priority:** Supporting, potentially essential later

Candidate waves:

- Kelvin
- equatorial Rossby
- mixed Rossby–gravity

Potential sources:

- BoM tropical atmospheric-wave monitoring
- independently filtered NOAA OLR
- ERA5 wind fields

## Preferred approach

Begin with authoritative BoM/BMKG diagnostics.

Only perform our own Wheeler–Kiladis-style filtering if it materially improves the scientific investigation.

Independent filtering requires methodological choices concerning:

- climatology removal
- symmetric/antisymmetric decomposition
- zonal wavenumbers
- frequency ranges
- windowing
- spectral filtering

These choices must be documented.

We should not introduce complex filtering merely to make the analysis appear sophisticated.

---

# 11. Topography

## Copernicus DEM

**Priority:** Supporting

Potential product:

Copernicus DEM GLO-30 or GLO-90.

**Purpose**

Investigate the spatial relationship between:

- rainfall
- low-level flow
- terrain
- Barisan Mountains

**Preferred initial product**

GLO-90 may be sufficient for synoptic-scale precipitation analysis and offers simpler access.

GLO-30 can be considered if finer terrain representation materially improves the rainfall analysis.

**Important**

A spatial relationship between rainfall and terrain does not by itself prove orographic enhancement.

The atmospheric flow must also support an upslope mechanism.

---

# 12. Disaster impacts

## BNPB

**Priority:** Essential for the impact section

**Product**

Kompilasi Data Kejadian dan Dampak Bencana Bansor Sumatera 2025.

**Available information includes**

- affected locations
- evacuation locations
- disaster impact information

**Purpose**

Connect the physical hazard with documented impacts.

**Access**

Portal Satu Data Bencana Indonesia.

**Important**

Impact values are time-dependent.

Every casualty, affected-population or displacement figure must retain its reporting date.

---

# 13. Regional disaster information

## ASEAN AHA Centre

**Priority:** Supporting

**Purpose**

Document impacts beyond Indonesia, particularly:

- Malaysia
- southern Thailand
- regional flooding and landslides

This allows us to determine whether the precipitation environment associated with Senyar was part of a wider regional event.

AHA Centre assessments should not be interpreted as evidence that Senyar alone caused all regional flooding.

---

# 14. Flood extent from satellite imagery

**Priority:** Optional initially

Candidate sources:

- Sentinel-1 SAR
- Sentinel-2 optical imagery
- Landsat

**Purpose**

Possible later investigation of:

- flood extent
- before/after conditions
- affected river valleys
- relationship between rainfall and inundation

Sentinel-1 is particularly useful where cloud cover prevents optical imaging.

This analysis should be added only after the meteorological core is complete.

---

# 15. Forecast verification

**Priority:** Later phase**

The first forecast-verification dataset should be:

## IMD operational forecast archive

Available material includes:

- forecast positions
- genesis outlooks
- TCFP reports
- extended-range outlooks

These products preserve what forecasters expected before the event evolved.

Potential metrics include:

### Genesis-location error

### Track error

\[
E(t)
=
d\left(
\mathbf{x}_{forecast}(t),
\mathbf{x}_{observed}(t)
\right)
\]

### Intensity error

### Forecast evolution between successive bulletins

Full ensemble forecast datasets may be considered later, but only if open access and reproducibility are straightforward.

---

# 16. Initial dataset priority

## Phase A — Start here

1. IMD Senyar chronology and track
2. GPM IMERG Final V07
3. NOAA OISST V2.1

These three datasets establish:

**where Senyar was → where the rain fell → what ocean surface it developed over**

---

## Phase B — Atmospheric diagnosis

4. ERA5 pressure-level fields
5. ERA5 single-level fields

These address:

**why the environment may have supported Senyar and extreme rainfall**

---

## Phase C — Tropical-scale context

6. NOAA OLR
7. BoM RMM
8. BMKG/BoM equatorial-wave diagnostics

These address:

**how the wider tropical environment evolved**

---

## Phase D — Terrain and impacts

9. Copernicus DEM
10. BNPB impact data
11. AHA Centre regional information

---

## Phase E — Optional extensions

12. Sentinel flood mapping
13. detailed forecast verification
14. additional station observations
15. ensemble-prediction analysis

---

# 17. Data-storage policy

Large raw datasets should generally not be committed to GitHub.

Recommended structure:

```text
data/
├── raw/
├── interim/
└── processed/
```

These directories should normally be excluded through `.gitignore`.

The repository should instead contain:

```text
scripts/download/
scripts/process/
config/
metadata/
```

where practical.

Small processed datasets may be committed only when:

- redistribution is permitted
- provenance is documented
- they materially improve reproducibility

---

# 18. Metadata requirement

Every downloaded dataset should eventually have a metadata record containing:

- provider
- product
- version
- DOI where available
- retrieval date
- spatial subset
- temporal subset
- variables
- units
- original resolution
- processing performed
- licence
- citation

The data filename alone is not considered sufficient provenance.

---

# 19. First download

The first dataset to retrieve will be:

**IMD / RSMC New Delhi Senyar operational track and chronology.**

Reason:

It is small, authoritative, and establishes the temporal framework used by every subsequent dataset.

No atmospheric or precipitation analysis should begin until the storm chronology and reference timestamps are fixed.
