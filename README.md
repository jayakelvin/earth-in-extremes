# Earth in Extremes

**Observe the event. Understand the physics. Explore the impacts.**

Earth in Extremes is an open, reproducible project for investigating significant weather and natural-hazard events using publicly accessible data and documented scientific methods.

The aim is to move beyond weather headlines and isolated extreme values by asking focused meteorological and oceanographic questions:

- How did the event develop?
- Which physical processes were important?
- Where and when were the strongest conditions observed?
- How well did forecasts represent the event?
- How did the hazard translate into real-world impacts?

The emphasis is on transparent analysis that others can inspect, reproduce, question, and improve.

## Scientific standard

Every case follows three core principles:

**Evidence first.**  
Claims should be supported by authoritative observations, documented calculations, model data, or scientific literature.

**Reproducible by design.**  
Where possible, the data sources, retrieval procedures, processing steps, and analysis code are provided so others can reproduce the work.

**Uncertainty stated explicitly.**  
Observations, remote-sensing estimates, forecasts, reanalysis products, derived quantities, and scientific interpretations are treated as different forms of evidence.

Detailed standards are documented in [`METHODOLOGY.md`](METHODOLOGY.md).

## What this project covers

Earth in Extremes may investigate:

- tropical cyclones and typhoons
- extreme precipitation and flooding
- severe convection
- storms and windstorms
- heatwaves and cold spells
- drought and wildfire weather
- snow and ice
- monsoon extremes
- coastal flooding and storm surge
- waves and ocean-atmosphere events
- compound hazards
- unusual atmospheric circulation
- forecast verification

Where supported by evidence, case studies may also examine impacts on infrastructure, transport, cities, drainage systems, coastal environments, agriculture, and renewable-energy systems.

## How a case works

A typical case follows:

**Question → Data → Quality control → Analysis → Physical interpretation → Impacts → Limitations**

For events investigated prospectively:

**Forecast → Archived prediction → Observation → Verification**

Not every case needs every step. A small, well-supported analysis is preferable to a large analysis with weak or unsupported conclusions.

## Data philosophy

The project prioritizes openly accessible and authoritative data.

Potential sources include:

- national meteorological and hydrological agencies
- ECMWF Open Data
- Copernicus Climate Data Store and ERA5
- EUMETSAT
- NASA and JAXA Earth-observation products
- GPM IMERG
- Himawari satellite products
- public weather-radar archives
- river and tide gauges
- openly licensed geospatial datasets

The exact datasets used are determined by the scientific question of each case.

Data are not redistributed when licensing or access conditions prohibit it. In those situations, retrieval instructions or scripts are provided instead.

## Cases

Cases are added only after the event, available data, and scientific question have been verified.

Each completed case should document:

- event period and geographical domain
- scientific question
- authoritative data sources
- dataset products and versions where available
- processing and quality-control steps
- assumptions and derived quantities
- figures and interpretation
- uncertainties and limitations
- references
- reproducible code

### Case catalogue

No case has been published yet.

The first case is currently being evaluated and will be added only after source and data verification.

## Repository structure

The repository will grow gradually as analyses are developed.

```text
earth-in-extremes/
├── README.md
├── METHODOLOGY.md
├── CONTRIBUTING.md
├── CITATION.cff
└── cases/
    └── ...
```

Individual case directories will contain only the files required for that investigation.

## Contributing

Corrections, reproducibility improvements, additional authoritative datasets, methodological suggestions, and scientifically justified alternative interpretations are welcome.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidance.

## Citation

Citation information is provided in [`CITATION.cff`](CITATION.cff).

Individual cases may include additional citation information for datasets, software, and scientific literature.

## Important note

Earth in Extremes is an independent scientific and educational project.

It is **not an operational weather-warning service**. For warnings, emergency information, and safety decisions, always follow the responsible national or local authorities.

## About

Earth in Extremes is developed by **Jaya Kelvin**, a meteorologist and oceanographer working with weather, climate, extreme events, and geospatial data.

The project is developed gradually, with priority given to scientific quality, transparency, and reproducibility rather than publication speed.
