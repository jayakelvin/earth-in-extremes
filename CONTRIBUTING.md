# Contributing to Earth in Extremes

Contributions that improve the scientific accuracy, reproducibility, transparency, or usability of Earth in Extremes are welcome.

This project values careful scientific reasoning over publication speed.

## Useful contributions

Contributions may include:

- corrections to factual or scientific errors
- improvements to data-retrieval workflows
- additional authoritative open datasets
- improvements to quality control
- reproducibility fixes
- methodological improvements
- alternative scientific interpretations supported by evidence
- improved visualisation methods
- documentation improvements
- fixes to code or software environments

Suggestions for new cases are also welcome when an event presents a clear scientific question that can reasonably be investigated using accessible data.

## Scientific standard

Contributions should follow the principles defined in [`METHODOLOGY.md`](METHODOLOGY.md):

**Evidence first. Reproducible by design. Uncertainty stated explicitly.**

In particular:

- factual claims should be traceable to reliable sources
- primary or authoritative sources should be preferred
- observations, model output, reanalysis, remote-sensing estimates, and derived quantities should be distinguished
- calculations should be documented
- physical interpretations should follow the evidence
- uncertainty and important limitations should be stated
- unsupported causal claims should be avoided

A result does not need to support the original hypothesis.

Scientifically valid negative or unexpected results are welcome.

## Sources

Preferred sources include:

1. national meteorological, hydrological, oceanographic, or geological agencies
2. international operational forecasting and Earth-observation centres
3. original scientific datasets
4. peer-reviewed literature
5. official infrastructure or emergency-management agencies

News reports may provide useful context or information about impacts but should not normally serve as the scientific basis of an analysis when a primary source is available.

## Data

Before adding a dataset, please document where possible:

- provider
- product or dataset name
- version
- variables used
- temporal coverage
- temporal resolution
- spatial resolution
- access method
- access date
- licence or terms of use

Do not upload data that cannot legally be redistributed.

When redistribution is restricted, provide retrieval instructions or scripts instead.

## Code

Code should favour readability and reproducibility.

Please:

- avoid undocumented hard-coded local paths
- document important assumptions
- retain physical units in variable names or metadata where practical
- use clear variable names
- separate data retrieval from analysis when possible
- document major dependencies
- preserve time-zone information
- avoid silently modifying or discarding observations

Numerical results used in figures or documentation should be reproducible from the available workflow.

## Figures

Scientific figures should clearly identify, where relevant:

- variable
- units
- valid time
- accumulation period
- data source
- geographical domain
- observational or model status

Visual design should improve communication without exaggerating the evidence.

## AI-assisted contributions

AI tools may assist with programming, documentation, or workflow development, but generated output should not be treated as a scientific source.

The contributor remains responsible for verifying:

- factual statements
- citations
- equations
- code behaviour
- dataset descriptions
- scientific interpretations

Unverified generated claims or fabricated references should not be submitted.

## Corrections

If you identify an error, please open an issue or submit a pull request.

Scientific corrections are encouraged, including corrections that change a previous interpretation.

Material corrections should explain:

1. what was incorrect
2. what has been changed
3. why the correction is necessary
4. whether the scientific conclusions are affected

## Pull requests

A useful pull request should explain:

- what is being changed
- why the change is needed
- which data or sources support it
- whether results or figures change

Small, focused pull requests are preferred when practical.

## Discussion

Alternative interpretations are welcome when they are scientifically justified.

Disagreement should focus on evidence, methods, assumptions, and uncertainty rather than authority or opinion.

The goal of Earth in Extremes is not to preserve a particular interpretation.

The goal is to improve the analysis.
