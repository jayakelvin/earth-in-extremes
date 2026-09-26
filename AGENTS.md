# Earth in Extremes — Working Instructions

## Project purpose

Earth in Extremes is a scientifically grounded portfolio project examining extreme weather events through meteorological analysis, geospatial data, documented evidence, and clear scientific communication.

The work should demonstrate professional meteorological reasoning rather than merely collect datasets or produce attractive visualizations.

## Scientific standard

All work must be:

- evidence-first;
- scientifically defensible;
- transparent about uncertainty;
- reproducible where practical;
- careful about the distinction between observations, derived results, interpretations, and hypotheses;
- appropriately sourced;
- explicit about preliminary, operational, provisional, and finalized data;
- conservative when the available evidence does not support a strong conclusion.

Do not invent or infer missing data, filenames, paths, dates, metadata, units, methods, sources, or results. Inspect the actual repository files before referring to them.

When evidence is incomplete, state what is known, what is uncertain, and what would be needed to resolve the uncertainty.

## Repository practice

Before editing:

1. Inspect the repository structure.
2. Read the relevant existing documents.
3. Check the current Git state.
4. Identify the actual source files and metadata.
5. Preserve unrelated work and uncommitted changes.

Treat raw data as immutable. Do not modify, rename, move, or overwrite raw source files unless explicitly instructed.

Prefer small, reviewable changes. Maintain the repository’s established directory structure, naming conventions, and documentation style.

Do not add unnecessary infrastructure, metadata, checksums, abstractions, or process overhead unless they provide a clear scientific or reproducibility benefit.

## Sources and provenance

For every substantive scientific claim:

- identify the supporting evidence;
- prefer authoritative primary sources;
- distinguish source-reported facts from the project’s own analysis;
- preserve exact units and temporal conventions;
- document relevant access dates, dataset versions, and preliminary/final status;
- do not cite a source that has not been inspected.

Provenance documentation should be lean and useful. Normally record the provider, product or dataset name, source URL, access date, original filename, status, and role in the analysis.

## Analysis

Check:

- variable definitions and units;
- coordinate conventions;
- time zones and timestamp formats;
- missing values and quality flags;
- spatial and temporal resolution;
- dataset limitations;
- whether comparisons are scientifically like-for-like.

Do not treat correlation as causation. Do not overstate precision or certainty. Explain methodological choices that could materially affect the interpretation.

## Writing voice

Write repository documents in the author’s existing voice, inferred from the surrounding material.

The preferred voice is:

- clear, direct, and measured;
- scientifically literate without sounding academic for its own sake;
- explanatory rather than promotional;
- confident when evidence is strong;
- explicit and calm about uncertainty;
- concise enough to remain readable, but detailed where scientific reasoning requires it.

Avoid inflated claims, generic AI phrasing, excessive headings, unnecessary repetition, and performative technical complexity.

Preserve first-person phrasing where the existing documents use it. The final text should sound like a meteorologist carefully explaining their own work.

## Case 001 — Cyclonic Storm Senyar

Maintain Case 001 as an evidence-led case study. Establish the storm chronology and reference track before using them to frame precipitation, oceanic, atmospheric, and impact analyses.

Keep preliminary IMD records clearly identified as preliminary. If finalized records become available, compare them with the version used in the analysis and document material changes.

Do not fill gaps in the Senyar record from memory or assumption. Inspect the actual local data and authoritative sources first.

## Collaboration

When a proposed change involves scientific interpretation, explain the evidence and reasoning clearly enough for the author to evaluate it.

Ask for direction when a missing choice would materially change the scientific meaning, project structure, or authorial position. Otherwise, make conservative, reversible progress and report exactly what changed.