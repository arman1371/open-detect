# unidetect

A library of pluggable, paper-backed **error detection algorithms** for
tabular data. Each algorithm is a faithful implementation of a published
error-detection paper, registered under a short name so you can pick one (or
run several and compare) without learning a new API per paper:

| Algorithm | Paper | Operating model |
|---|---|---|
| `uni_detect` | Wang & He, *Uni-Detect*, SIGMOD 2019 | Corpus-driven, unsupervised, Spark/Unity Catalog-native |
| `raha` | Mahdavi et al., *Raha*, SIGMOD 2019 | Semi-supervised (≤20 labels), single-table, pandas-native |

```python
from unidetect.algorithms import get_algorithm

raha = get_algorithm("raha")
result = raha.detect(my_dataframe, table_id="orders")
result.errors()  # every cell either algorithm calls dirty, in one common schema
```

Both algorithms return the same `AlgorithmResult` (see
[`unidetect/algorithms/base.py`](src/unidetect/algorithms/base.py)), so
results are comparable and unionable regardless of which algorithm produced
them, even though the two papers' underlying methods have nothing in common.
See [`ARCHITECTURE.md`](ARCHITECTURE.md) for how each part of each paper maps
onto the code, and [Adding a new algorithm](#adding-a-new-algorithm) below
for how a third algorithm plugs in.

## Install

This project uses [uv](https://docs.astral.sh/uv/) for package and
dependency management.

```bash
uv sync       # local development, including pyspark + delta-spark for tests
# or, on a Databricks cluster / job (Spark and Delta are already provided):
pip install unidetect
```

## Uni-Detect (Wang & He, SIGMOD 2019)

Uni-Detect finds **uniqueness-constraint violations, functional-dependency
violations, numeric outliers, and spelling mistakes** in tables without any
per-table configuration: no hand-tuned thresholds, no declared constraints,
no labeled training data. Instead, it reasons statistically against a large
background corpus of tables using a **"what-if" perturbation test**: would a
small, hypothetical edit make this table look a lot more like the rest of
the world's tables? If so, that edit points at a likely error. It runs
against tables already registered in **Unity Catalog**, using **Spark/Delta
Lake** as the compute and storage layer, in two phases:

1. **Offline** — `UniDetect.build_corpus_statistics(...)` scans a background
   corpus (by default, "every table this catalog already governs") and
   materializes a small Delta table of corpus statistics.
2. **Online** — `UniDetect.detect(...)` scores any target table(s) against
   those statistics and returns a ranked, explainable list of likely errors,
   fast enough for interactive or per-scan use.

### Quickstart

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

### Running the detectors as Databricks Jobs

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

### What "the corpus" means here

The paper's corpus `T` is 100M+ web tables. The natural Unity Catalog
analogue — and the one this library targets — is **the set of tables an
organization already has registered**: a whole catalog, a set of schemas, or
a curated allow-list. For most organizations this is thousands to millions
of governed tables spanning many domains, which plays the same statistical
role: a large background sample of "what clean tables look like" to reason
against. See `unidetect/catalog.py::list_tables_matching`.

### Uni-Detect design

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

## Raha (Mahdavi et al., SIGMOD 2019)

Raha is **semi-supervised and single-table**: it needs no background corpus,
just the dirty table itself and a small labeling budget (≤20 tuples by
default). It runs an ensemble of error-detection *strategies* (outlier
detection, pattern violation, rule/FD violation) at many parameter settings
to build a feature vector per cell, clusters cells of each column by feature
similarity, samples one tuple per iteration for labeling, propagates that
label through its cluster, and trains one classifier per column to predict
the rest.

```bash
pip install "unidetect[raha]"   # adds scikit-learn + scipy
```

```python
import pandas as pd
from unidetect.algorithms.raha import RahaConfig, RahaDetector, GroundTruthLabeler

dirty = pd.read_csv("dirty.csv")
detector = RahaDetector(RahaConfig(labeling_budget=20))

# Any Labeler answers "is this cell dirty?" for the tuples Raha samples.
# GroundTruthLabeler is for evaluation, when a clean reference is available:
labeler = GroundTruthLabeler(pd.read_csv("clean.csv"))
# For a real, unlabeled dataset, wire up a person instead:
#   labeler = CallableLabeler(lambda df, row: ask_a_human(df.loc[row]))

result = detector.detect(dirty, table_id="my_table", labeler=labeler)
for cell in result.errors():
    print(cell.table_id, cell.row_index, cell.column_name, cell.score)
```

Omit `labeler` to fall back to `HeuristicLabeler`, a no-human default that
lets the pipeline run end-to-end with zero interaction (see its docstring
for why this is strictly weaker than a real label).

### Raha design

- `unidetect.algorithms.raha.strategies` — the outlier/pattern/rule
  detection strategy families (Section 4.1), each a parameter grid of
  strategy functions.
- `unidetect.algorithms.raha.features` — assembles each column's feature
  matrix `V_j` from every strategy (Section 4.2).
- `unidetect.algorithms.raha.clustering` — hierarchical agglomerative
  clustering per column plus the softmax tuple sampler (Section 4.3,
  Equation 3).
- `unidetect.algorithms.raha.labeling` — the pluggable `Labeler` interface,
  and cluster-based label propagation with homogeneity/majority conflict
  resolution (Section 4.4).
- `unidetect.algorithms.raha.classifier` — per-column classifier training +
  prediction (Section 4.4).
- `unidetect.algorithms.raha.detector.RahaDetector` — Algorithm 1
  end-to-end, registered as `"raha"`.

Not implemented: knowledge-base violation detection (needs a live external
KB like DBpedia — out of scope for a library meant to run offline/on private
data) and the historical strategy-filtering runtime optimization (Section 5,
an optional speed-up, not part of the core detection result). Both are
documented as scope decisions in the relevant module docstrings.

## Adding a new algorithm

`unidetect.algorithms` is a registry (`unidetect/algorithms/registry.py`):
implement `ErrorDetectionAlgorithm` (`unidetect/algorithms/base.py`),
returning results as `AlgorithmResult`, then either register it in-tree
(`register_lazy("my_algo", ...)`) or, for an out-of-tree package, declare it
as an entry point:

```toml
[project.entry-points."unidetect.algorithms"]
my_algorithm = "my_package.module:MyAlgorithmClass"
```

Installing that package makes `"my_algorithm"` show up in
`list_algorithms()` automatically — no changes to this repository required.

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

**Uni-Detect.** Two places in the published paper have PDF-extraction
artifacts (a dropped comparison operator in the FD formula, in both the
paper's own metric definition and the `Conforming-pair-ratio` baseline it's
compared against — a common casualty of academic-PDF math extraction). Where
this happens, this implementation uses the standard, well-established
literature definition consistent with the paper's own stated intuition and
worked example; the exact convention chosen is documented in the relevant
module's docstring (see `unidetect/metrics/functional_dependency.py`).

**Raha.** The histogram outlier strategy's published normalization formula
has the same kind of extraction artifact; the natural reading (relative
value frequency) is the one that reproduces the paper's own worked example
exactly, and is what this implementation uses (see
`unidetect/algorithms/raha/strategies.py`). Knowledge-base violation
detection and historical strategy filtering (Sections 2.2 and 5) are out of
scope, as documented in the Raha design section above.

## License

Apache-2.0
