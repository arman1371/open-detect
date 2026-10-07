# Uni-Detect

**Corpus-driven statistical error detection on Spark and Unity Catalog.** Wang & He, SIGMOD 2019.

Uni-Detect finds four kinds of error in tables with no per-table configuration, no declared
constraints, and no labeled data:

| `ErrorType` | What it finds |
|---|---|
| `uniqueness` | Duplicate values in a column that should be unique |
| `functional_dependency` | Rows that violate a `A -> B` dependency between two columns |
| `numeric_outlier` | Numeric values far outside the column's distribution |
| `spelling` | Misspelled values (near-duplicates of a more common value) |

## How it works

For a target column, Uni-Detect asks a **what-if** question: *would removing a small subset of
values make this column look much more like the columns in a large background corpus?* If so, that
subset is a likely error. The answer is a likelihood ratio estimated from corpus statistics:
**the smaller the ratio, the more surprising the column, and the more likely a real error.**

Work is split into two phases:

1. **Offline.** `build_corpus_statistics` scans a background corpus and writes a compact Delta
   table of statistics. Run it occasionally (weekly, say).
2. **Online.** `detect` scores target tables by looking those statistics up. It is fast enough
   for interactive use.

!!! info "What is the corpus?"
    The paper's corpus is 100M+ web tables. Here it is the tables your organization already has
    in Unity Catalog: a whole catalog, a few schemas, or an allow-list. Governed tables play the
    same role: a large sample of what clean tables look like.

## Install

On Databricks, Spark and Delta are already there:

```bash
pip install unidetect
```

Locally, add the `spark` extra and use **JDK 17**; see [Installation](../getting-started/installation.md).

## Usage on Databricks

```python
from unidetect import UniDetectConfig, UnityCatalogLocation
from unidetect.pipeline import UniDetect
from unidetect.catalog import list_tables_matching

config = UniDetectConfig(
    location=UnityCatalogLocation(catalog="main", schema="data_quality"),
)
ud = UniDetect(config)    # picks up the active SparkSession

# Offline: build the background corpus statistics once
corpus_tables = list_tables_matching(spark, catalog="main")   # every table in main.*
ud.build_corpus_statistics(corpus_tables)

# Online: scan one or more tables
detections = ud.detect(["main.sales.orders"])
detections.show()
```

`location` is where `unidetect` keeps its **own** tables (corpus statistics, token statistics,
and optionally detections). It is not the data being scanned.

To restrict the work to certain error types:

```python
from unidetect import ErrorType

ud.build_corpus_statistics(corpus_tables, error_types=[ErrorType.UNIQUENESS, ErrorType.SPELLING])
ud.detect(["main.sales.orders"], error_types=[ErrorType.UNIQUENESS])
```

Rebuilding is incremental per error type: each call only overwrites the partitions it touches.

### Reading the detections

`detect` returns a Spark `DataFrame`, ranked most-surprising first:

| Column | Meaning |
|---|---|
| `error_type` | `uniqueness`, `functional_dependency`, `numeric_outlier` or `spelling` |
| `table_id`, `column_names`, `row_ids` | What is flagged |
| `lr_ratio` | Laplace-smoothed likelihood ratio. **Smaller is more surprising.** |
| `surprisal` | `-log(lr_ratio)`, for "bigger is worse" ranking UIs |
| `is_significant` | `lr_ratio <= alpha` |
| `support` | How many corpus rows the ratio was estimated from. Low support means low trust. |
| `evidence_json` | Type-specific explanation (the offending pair, duplicate values, outlier value, violating rows) |

```python
import json

for row in detections.where("is_significant").limit(10).collect():
    print(row["error_type"], row["table_id"], row["column_names"], json.loads(row["evidence_json"]))
```

Persist results to the configured detections table:

```python
ud.write_detections(detections)   # appends to <catalog>.<schema>.unidetect_detections
```

### Through the registry

`get_algorithm("uni_detect", config)` wraps the pipeline and flattens its output into the common
[`AlgorithmResult`](../reference/algorithms.md) schema, so it can be compared or unioned with
other algorithms.

```python
from unidetect.algorithms import get_algorithm

algo = get_algorithm("uni_detect", config)
result = algo.detect(["main.sales.orders"])    # data = table names; table_id is ignored
result.errors()
```

Each detection spanning several columns or rows (a duplicate group, an FD violation) becomes one
`CellResult` per (column, row), all sharing the same `evidence`. `score` is the surprisal.

## Configuration

See [`UniDetectConfig`](../reference/uni-detect.md#unidetect.config.UniDetectConfig).

| Setting | Default | Notes |
|---|---|---|
| `location` | required | `UnityCatalogLocation(catalog, schema)` for the library's own tables |
| `alpha` | `0.05` | Significance level. Lower gives fewer, higher-confidence detections. |
| `epsilon` | `0.01` | Maximum perturbation size for row-level error types |
| `laplace_smoothing` | `1.0` | Keeps zero-support buckets from yielding a perfect `0` ratio |
| `max_mpd_block_size` | `500` | Bounds pairwise spelling comparisons on skewed columns |
| `max_fd_column_pairs_per_table` | `200` | Bounds FD candidates per table |
| `corpus_stats_table`, `token_stats_table`, `detections_table` | `unidetect_*` | Unqualified names of the library's tables |

## A fully local example

You can run the whole flow on a laptop with a throwaway local Spark session and synthetic tables.
It needs the `spark` extra, `delta-spark`, and JDK 17.

??? example "examples/quickstart.py"

    ```python
    --8<-- "examples/quickstart.py"
    ```

```bash
python examples/quickstart.py
```

## Operational notes

- **Corpus size matters.** With a small or homogeneous corpus, many buckets have low `support`
  and ratios are not trustworthy. Check `support` before acting on a detection.
- **Functional dependencies are the hardest case.** The paper itself reports lower precision for
  FD errors; so does the [benchmark](../benchmarks.md).
- **Missing statistics.** Scanning before building the corpus raises `CorpusNotFoundError`.
