# Uni-Detect

A production Databricks / Unity Catalog implementation of **Uni-Detect**, the
unified, corpus-driven error-detection framework from:

> Pei Wang and Yeye He. *Uni-Detect: A Unified Approach to Automated Error
> Detection in Tables.* SIGMOD 2019.
> https://doi.org/10.1145/3299869.3319855

Uni-Detect finds **uniqueness-constraint violations, functional-dependency
violations, numeric outliers, and spelling mistakes** in tables without any
per-table configuration: no hand-tuned thresholds, no declared constraints,
no labeled training data. Instead, it reasons statistically against a large
background corpus of tables using a **"what-if" perturbation test**: would a
small, hypothetical edit make this table look a lot more like the rest of
the world's tables? If so, that edit points at a likely error.

This repository turns the paper's method into a library you can run against
tables already registered in **Unity Catalog**, using **Spark/Delta Lake**
as the compute and storage layer, in two phases:

1. **Offline** — `UniDetect.build_corpus_statistics(...)` scans a background
   corpus (by default, "every table this catalog already governs") and
   materializes a small Delta table of corpus statistics.
2. **Online** — `UniDetect.detect(...)` scores any target table(s) against
   those statistics and returns a ranked, explainable list of likely errors,
   fast enough for interactive or per-scan use.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for how each part of the paper maps
onto the code.

## Install

This project uses [uv](https://docs.astral.sh/uv/) for package and
dependency management.

```bash
uv sync       # local development, including pyspark + delta-spark for tests
# or, on a Databricks cluster / job (Spark and Delta are already provided):
pip install unidetect
```

## Quickstart

```python
from unidetect import UniDetectConfig, UnityCatalogLocation
from unidetect.pipeline import UniDetect
from unidetect.catalog import list_tables_matching

config = UniDetectConfig(
    location=UnityCatalogLocation(catalog="main", schema="data_quality"),
)
ud = UniDetect(config)  # uses the active (Databricks-provided) SparkSession

# Offline: build the background corpus statistics once (e.g. weekly)
corpus_tables = list_tables_matching(spark, catalog="main")  # every table main.* governs
ud.build_corpus_statistics(corpus_tables)

# Online: scan any table(s) for errors, at interactive speed
detections = ud.detect(["main.sales.orders"])
detections.show()
```

Each row of `detections` carries:

| column | meaning |
|---|---|
| `error_type` | `uniqueness` / `functional_dependency` / `numeric_outlier` / `spelling` |
| `table_id`, `column_names`, `row_ids` | what's flagged |
| `lr_ratio` | the (Laplace-smoothed) likelihood ratio from the paper's hypothesis test — **smaller is more surprising / more likely a real error** |
| `surprisal` | `-log(lr_ratio)`, for descending-is-worse ranking UIs |
| `is_significant` | `lr_ratio <= alpha` |
| `support` | how many corpus rows the ratio was estimated from |
| `evidence_json` | type-specific explanation (offending value pair, duplicate values, outlier value, violating rows) |

## Running the detectors as Databricks Jobs

`databricks.yml` defines two [Databricks Asset Bundle](https://docs.databricks.com/en/dev-tools/bundles/)
jobs:

- `build_corpus_statistics_job` — the offline learning phase, scheduled weekly.
- `run_detection_job` — the online scan, scheduled (or triggered) per table set.

```bash
databricks bundle deploy -t dev
databricks bundle run build_corpus_statistics_job -t dev
databricks bundle run run_detection_job -t dev -- --target-tables main.sales.orders
```

Or run the equivalent notebooks interactively: `notebooks/01_build_corpus_statistics.py`
and `notebooks/02_run_detection.py`.

## What "the corpus" means here

The paper's corpus `T` is 100M+ web tables. The natural Unity Catalog
analogue — and the one this library targets — is **the set of tables an
organization already has registered**: a whole catalog, a set of schemas, or
a curated allow-list. For most organizations this is thousands to millions
of governed tables spanning many domains, which plays the same statistical
role: a large background sample of "what clean tables look like" to reason
against. See `unidetect/catalog.py::list_tables_matching`.

## Design

- `unidetect.metrics` — the four pure-Python/NumPy metric functions (`UR`,
  `max-MAD`, `MPD`, `FR`), independently unit-tested against the paper's own
  worked numeric examples.
- `unidetect.perturbation` — the epsilon-perturbation for each error type
  (Definition 2).
- `unidetect.featurization` — the corpus sub-setting / bucketing dimensions
  (Figure 5).
- `unidetect.strategies` — the single source of truth for which direction
  each metric moves in after perturbation (generalizes Equation 12 into one
  formula, `INCREASING` vs `DECREASING`).
- `unidetect.corpus` — offline ingestion + statistics builder, and the
  online batch likelihood-ratio store, both Spark/Delta-native.
- `unidetect.detectors` — one class per error type, sharing a template
  method (`BaseDetector.detect`) that wires metric → perturbation →
  featurization → corpus lookup → ranked, explainable output.
- `unidetect.pipeline.UniDetect` — the public facade.

## Testing

```bash
make test        # full suite (Spark/Delta integration tests auto-skip if
                  # a local Delta-enabled Spark session cannot be started)
make test-fast    # pure-Python unit tests only, no Spark/JVM required
```

**JDK version:** run the Spark/Delta integration tests under **JDK 17**
(`JAVA_HOME` pointed at a JDK 17 install). The Arrow Java version bundled
with PySpark 3.5's `pandas_udf`/`mapInPandas` support does not work under
JDK 21+ (`sun.misc.Unsafe or java.nio.DirectByteBuffer.<init> not
available`) — this is a PySpark/Arrow/JDK compatibility limitation, not
something this library's tests can work around. Databricks runtimes ship
their own compatible JDK, so this only matters for local development; CI
(`.github/workflows/ci.yml`) already pins JDK 17 via `actions/setup-java`.

## Benchmark

[`benchmarks/`](benchmarks/README.md) tracks detection quality against a
small, deterministic dataset inspired by the paper's own **WIKI** evaluation
corpus (a subset of Wikipedia-domain tables). It runs on every push/PR via
[`.github/workflows/benchmark.yml`](.github/workflows/benchmark.yml) and
prints a version-over-version comparison against a checked-in baseline, so a
change's effect on precision/recall/F1 (and on whether true errors rank as
more surprising than false positives) is visible before it merges. See
[`benchmarks/README.md`](benchmarks/README.md) for details and how to update
the baseline.

## Fidelity notes

Two places in the published paper have PDF-extraction artifacts (a dropped
comparison operator in the FD formula, in both the paper's own metric
definition and the `Conforming-pair-ratio` baseline it's compared against —
a common casualty of academic-PDF math extraction). Where this happens, this
implementation uses the standard, well-established literature definition
consistent with the paper's own stated intuition and worked example; the
exact convention chosen is documented in the relevant module's docstring
(see `unidetect/metrics/functional_dependency.py`).

## License

Apache-2.0
