# Methodology

## Purpose

Earth in Extremes is built around evidence-based, reproducible analysis of significant meteorological, oceanographic, hydrological, and related natural-hazard events.

The purpose of this document is to define the minimum scientific and reproducibility standards expected for every case study in this repository.

The project does not require every case to use the same datasets or methods. It does require every case to make clear:

- what was observed
- what was calculated
- what came from a model or reanalysis
- what is interpretation
- what remains uncertain

---

## 1. Start with a scientific question

Each case should begin with a focused question that can reasonably be investigated using available data.

Examples:

> Why was the heaviest rainfall displaced from the tropical-cyclone centre?

> How did rainfall intensity evolve before and after landfall?

> How well did a forecast represent the observed storm track?

> How rapidly did river levels respond to extreme rainfall?

The question should determine the datasets and methods.

The analysis should not begin with a preferred explanation and then search for evidence to support it.

---

## 2. Evidence categories

Earth in Extremes distinguishes between different forms of evidence.

### Observation

A quantity measured directly or estimated from an observing system.

Examples include:

- rain-gauge observations
- weather-station measurements
- radar observations
- tide-gauge measurements
- satellite radiances
- buoy observations
- river-gauge measurements

Remote-sensing products may involve retrieval algorithms and should therefore not automatically be treated as equivalent to direct in-situ measurements.

### Derived quantity

A value calculated from observations or model data using a documented method.

Examples include:

- rolling precipitation accumulations
- anomalies
- storm-centre distance
- integrated water-vapour transport
- return periods
- forecast errors

The calculation must be described clearly enough to reproduce.

### Model or forecast output

Numerical weather prediction or other model output represents a model estimate of the atmospheric or oceanic state.

Forecast values must not be described as observations.

### Reanalysis

Reanalysis products combine numerical models and observations through data assimilation.

They provide a physically consistent reconstruction of the atmosphere or ocean, but they are not direct observations.

### Interpretation

Interpretation connects evidence to physical processes.

Interpretation must be consistent with the available data and established scientific understanding.

Where evidence is incomplete, the wording should reflect that uncertainty.

---

## 3. Source hierarchy

Whenever practical, data and factual information should come from the original authoritative source.

Preferred sources include:

1. national meteorological, hydrological, geological, or oceanographic agencies
2. international operational centres and Earth-observation programmes
3. original scientific datasets
4. peer-reviewed scientific literature
5. official emergency-management or infrastructure agencies
6. high-quality secondary sources when primary information is unavailable

News articles may help identify impacts or events worth investigating, but they should not normally be the primary scientific source for meteorological conclusions.

Secondary sources should not be used when the same information can reasonably be verified from the original provider.

---

## 4. Event verification

Before an event becomes an official Earth in Extremes case, the basic event metadata should be verified.

This includes, where relevant:

- event name and identifier
- geographical region
- event start and end period
- official classification
- cyclone number or storm identifier
- landfall time and location
- observed intensity
- warning level
- reported precipitation or wind extremes
- documented impacts

Where preliminary operational information is used, it should be identified as preliminary.

If a later post-analysis or quality-controlled dataset becomes available, the case should be updated when scientifically important.

---

## 5. Data provenance

Every dataset used in a case should be documented.

At minimum, record:

**Provider**  
The organisation responsible for the dataset.

**Dataset or product name**  
The official dataset or product identifier where available.

**Version**  
Dataset or algorithm version where relevant.

**Variables**  
The exact variables used.

**Temporal coverage**  
Start and end times.

**Temporal resolution**  
For example 10-minute, hourly, daily, or 6-hourly.

**Spatial domain**  
The geographical area analysed.

**Spatial resolution**  
Where applicable.

**Access date**  
Especially important for operational or mutable datasets.

**Access method**  
API, direct download, archive, FTP, cloud storage, etc.

**License or terms of use**  
Where known.

Raw data should not be redistributed when the source licence does not permit redistribution.

In such cases, provide retrieval instructions or code instead.

---

## 6. Time conventions

Time handling must be explicit.

UTC should be preferred internally for analysis unless there is a strong reason to use local time.

Local time may be shown in figures when it improves communication, but the timezone must be stated.

Ambiguous timestamps should be avoided.

For example:

`2026-09-21 06:00 UTC`

is preferable to:

`06:00 on 21 September`

when readers could interpret the time differently.

Daylight-saving transitions should be handled explicitly where relevant.

---

## 7. Accumulation periods

Accumulated variables must be defined precisely.

For precipitation, distinguish between a fixed-period total and a rolling accumulation.

For hourly precipitation $P(t)$, a rolling 24-hour accumulation can be written as:

```math
P_{24}(t)
=
\sum_{i=0}^{23} P(t-i)
```

for hourly data.

A calendar-day precipitation total is not necessarily equal to the maximum rolling 24-hour accumulation.

The accumulation definition must therefore accompany reported extremes.

The same principle applies to 3-, 6-, 12-, 48-, or 72-hour totals.

---

## 8. Quality control

Data should be inspected before analysis.

Depending on the dataset, checks may include:

- missing values
- duplicate timestamps
- impossible or implausible values
- quality-control flags
- unit consistency
- station relocation or metadata changes
- accumulation resets
- coordinate consistency
- temporal gaps
- spatial coverage limitations

Quality-control decisions should be documented.

Measurements should not be silently corrected or removed.

---

## 9. Comparing datasets

Different observing systems represent different spatial and temporal scales.

For example, a rain gauge measures precipitation at a point, while a satellite precipitation product represents an area.

A direct comparison therefore requires care.

When comparing two datasets, document differences in:

- spatial resolution
- temporal resolution
- measurement or retrieval method
- accumulation period
- quality-control procedure

Interpolation or resampling methods should be explicitly described.

Agreement between datasets does not necessarily mean either dataset represents absolute truth.

---

## 10. Forecast verification

Forecast verification should compare archived forecasts with observations or other appropriate reference datasets.

Where possible, preserve the forecast exactly as it existed before the event.

Relevant quantities may include:

```math
E_d
=
d\left(
\mathbf{x}_{forecast},
\mathbf{x}_{observed}
\right)
```

for positional error, where $d$ represents geographical distance.

Additional metrics may include:

- track error
- intensity error
- precipitation bias
- timing error
- spatial displacement
- threshold exceedance
- categorical verification scores

The chosen metric should match the scientific question.

Forecast verification must not rely on forecasts retrieved after they have been replaced by analysis or reanalysis products.

---

## 11. Anomalies and climatology

An anomaly should always specify its reference climatology.

For a variable $X$:

```math
X' = X - \overline{X}_{clim}
```

where $\overline{X}_{clim}$ is the climatological reference value.

The reference period, dataset, spatial resolution, and temporal aggregation should be stated.

Percentile-based extremes should likewise state the reference period and percentile calculation method.

An event should not be described as unprecedented or record-breaking without an appropriate observational record or authoritative source supporting that statement.

---

## 12. Return periods and rarity

Return-period analysis requires sufficient data and an appropriate statistical method.

A return period must not be inferred simply because an observed value appears unusual.

If extreme-value analysis is performed, document:

- observational record length
- distribution or statistical model
- fitting method
- threshold or block definition
- confidence intervals
- assumptions about stationarity

Large return-period estimates derived from short observational records should be interpreted cautiously.

---

## 13. Physical interpretation

Physical explanations should follow the evidence.

For example, heavy rainfall near mountainous terrain does not by itself demonstrate orographic enhancement.

Supporting evidence might include:

- low-level wind direction
- moisture transport
- terrain orientation
- rainfall distribution
- atmospheric stability
- vertical motion
- persistence of the flow
- relevant scientific literature

Preferred wording should reflect the strength of evidence.

Strong evidence:

> The observations and wind field indicate persistent upslope flow during the period of maximum rainfall.

More limited evidence:

> The rainfall distribution is consistent with possible orographic enhancement, although additional analysis would be required to quantify its contribution.

Avoid language implying certainty that the analysis does not support.

---

## 14. Causality and attribution

Correlation does not establish causation.

A case should not attribute an individual event to climate change solely because it was extreme.

Formal attribution requires an appropriate attribution methodology or reference to a scientifically credible attribution study.

Similarly, infrastructure impacts should not automatically be attributed to a meteorological variable without evidence connecting the hazard and the observed damage.

---

## 15. Figures

Every scientific figure should be interpretable independently of accompanying social-media text.

Where relevant, include:

- variable name
- units
- valid time
- accumulation period
- geographical domain
- data source
- colour-bar definition
- coordinate information
- observational or model status
- important methodological notes

Colour scales should not exaggerate small differences.

Maps should use appropriate projections.

Different panels intended for direct comparison should normally use consistent scales.

Decorative visual elements should not obscure the scientific information.

---

## 16. Reproducibility

A completed case should aim to allow another researcher or technically capable reader to reproduce the analysis.

Where practical, provide:

```text
case/
├── README.md
├── config/
├── scripts/
├── notebooks/
├── figures/
└── references/
```

Raw datasets may be excluded when redistribution is impractical or prohibited.

Instead, include retrieval scripts or clear download instructions.

Hard-coded local paths should be avoided.

Configuration values such as study domain, event dates, and station identifiers should preferably be stored separately from analysis code.

---

## 17. Software environment

Python analyses should document the main software dependencies.

A completed workflow should eventually include a reproducible environment definition such as:

`environment.yml`

or

`requirements.txt`

Important package versions should be recorded when version differences could affect results.

Random processes must use documented seeds when reproducibility requires them.

---

## 18. Interpretation versus result

Case documentation should distinguish clearly between:

**Result**

> Maximum rolling 24-hour precipitation at Station X was 312.4 mm.

and:

**Interpretation**

> The timing suggests that the largest accumulation occurred before the cyclone's closest approach.

and:

**Hypothesis**

> Persistent moisture convergence ahead of the cyclone may have contributed to this rainfall maximum.

These statements carry different levels of certainty and should not be presented as equivalent.

---

## 19. Negative results

An analysis does not need to confirm the original hypothesis.

If the available evidence does not support an expected mechanism, that finding should be reported.

Examples include:

> No clear relationship was found between cyclone-centre distance and rainfall intensity.

or:

> Satellite precipitation underestimated the observed station accumulation during the event.

Negative or unexpected results are scientifically valuable when methods and limitations are transparent.

---

## 20. Corrections

Scientific transparency includes correcting mistakes.

If a material error is identified after publication:

1. correct the analysis
2. document the change
3. explain whether conclusions were affected
4. preserve an appropriate version history through Git

Corrections should not be hidden simply because the analysis has already been shared publicly.

---

## 21. Case acceptance standard

Before a case is considered complete, it should satisfy the following checks:

- event identity has been verified
- primary data sources are documented
- time and spatial domains are explicit
- units are checked
- quality-control steps are documented
- calculations are reproducible
- observations and models are distinguished
- interpretation follows evidence
- uncertainties and limitations are stated
- figures contain appropriate attribution
- important claims are supported by sources
- code can be rerun without undocumented manual steps
- data licensing has been considered

A case does not need to contain every possible analysis.

A small, well-supported investigation is preferable to a large analysis containing unsupported conclusions.

---

## Guiding principle

Earth in Extremes follows a simple standard:

**Evidence first. Reproducible by design. Uncertainty stated explicitly.**

The purpose is not to produce the fastest explanation of an event.

The purpose is to produce an explanation that can be examined, reproduced, challenged, and improved.
