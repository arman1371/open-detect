# Architecture

This document maps each part of Wang & He's Uni-Detect (SIGMOD 2019) onto
this codebase, and explains the production/Databricks-specific decisions
that the paper doesn't have to make.

## 1. The core statistical idea (paper Section 2.2)

Given a target table/column `D` and a large background corpus `T`, Uni-Detect
asks: is there a small subset `O` of `D` (up to `epsilon` rows/values) whose
removal would make the rest of `D` look a lot more "typical" of `T`? If so,
`O` is a likely error.

This is formalized as a likelihood-ratio test between:

- `H0`: `D` is normal (statistically like `T`)
- `H1`: `D` is normal *except for* an abnormal subset `O`; `D \ O` is like `T`

```
LR = P(D | T) / P(D_perturbed | T)
```

`P(D | T)` can't be evaluated directly (we'll never see a table byte-identical
to `D` in `T`), so it's estimated via a **metric function** `m` that maps a
table/column to a number, plus a **featurization** `F` that restricts `T` to
the sub-corpus most comparable to `D`. Equation (12) gives the smoothed,
range-based estimator this codebase implements directly:

```
ratio = count(T' in S(T): m(T') >= theta1  AND  m(T'_perturbed) <= theta2)
        --------------------------------------------------------------
        count(T' in S(T): m(T') >= theta2)
```

(shown here for the `DECREASING` family; see below for `INCREASING`.)

## 2. Code map

| Paper concept | Code |
|---|---|
| Definition 1 (unsupervised error-detection) | `unidetect.core.enums.ErrorType` |
| Definition 2 (epsilon-perturbation) | `unidetect.perturbation.perturb_*` |
| Definition 3 (LR test) | `unidetect.corpus.store.CorpusStatsStore.batch_score` |
| Section 2.2.2 (featurization / subsetting) | `unidetect.featurization` |
| Definition 4 (Uni-Detect instantiation) | `unidetect.detectors.base.BaseDetector` (template method) + per-type metric/perturbation/featurization |
| Section 3.1 (numeric outliers: max-MAD) | `unidetect.metrics.outliers`, `unidetect.detectors.numeric_outlier` |
| Section 3.2 (spelling: MPD) | `unidetect.metrics.spelling`, `unidetect.detectors.spelling` |
| Section 3.3 (uniqueness: UR) | `unidetect.metrics.uniqueness`, `unidetect.detectors.uniqueness` |
| Section 3.4 (FD: FR) | `unidetect.metrics.functional_dependency`, `unidetect.detectors.functional_dependency` |
| Theorem 1 (monotonicity) | Generalized into `ComparisonDirection` (see below) — the same proof holds for either direction by symmetry |
| "System Architecture": offline learning + online lookup | `unidetect.corpus.builder.CorpusStatsBuilder` (offline) / `unidetect.corpus.store.CorpusStatsStore` (online) |

## 3. Generalizing Equation (12): `ComparisonDirection`

The paper instantiates the smoothed ratio four times, with two different
inequality conventions depending on whether the metric grows or shrinks once
the anomalous subset is removed:

- **`INCREASING`** (uniqueness's `UR`, FD's `FR`, spelling's `MPD`): the
  metric moves *up* toward its "boring" value once the errors are dropped.
  ```
  ratio = count(before <= theta1 AND after >= theta2) / count(before <= theta2)
  ```
- **`DECREASING`** (outliers' `max-MAD`): the metric moves *down* once the
  outlier is dropped.
  ```
  ratio = count(before >= theta1 AND after <= theta2) / count(before >= theta2)
  ```

`unidetect.strategies` is the single source of truth for which family each
`ErrorType` belongs to, and `CorpusStatsStore.batch_score` implements both
formulas as one parameterized Spark query. This isn't just deduplication —
it's the same generalization Theorem 1's monotonicity proof already implies
by symmetry, made explicit in code so a fifth error type only needs to
declare its direction, not reimplement the ratio.

## 4. Why the corpus statistics table is the whole "model"

Section 2.2.3 ("System Architecture") describes two phases: an expensive
offline MapReduce-like job that "memorizes" surprising (before, after,
ratio) transitions as rules, and a cheap online phase that looks predictions
up rather than recomputing them. This codebase keeps that split explicit:

- `CorpusStatsBuilder` runs the *same* metric+perturbation+featurization
  code the online detectors use, but against every column/pair in the
  background corpus, and writes one row per corpus column to a Delta table
  partitioned by `error_type`:

  ```
  unidetect_corpus_stats(error_type, feature_bucket, theta_before, theta_after, table_id)
  ```

- `CorpusStatsStore.batch_score` never re-touches raw corpus data. It reads
  only this table, restricted (via partition pruning) to the requested
  `error_type`, and computes every candidate's ratio with one join +
  conditional aggregation — a single Spark job scores an entire batch of
  target columns at once.

This is also why rebuilding statistics for one `ErrorType` is cheap and
independent of the others: `CorpusStatsBuilder.write` uses Delta's
`replaceWhere` to overwrite only the partitions for the error types being
rebuilt.

## 5. Featurization as Unity-Catalog-scale corpus subsetting

Figure 5's "cube diagram" (data type × row count × uniqueness/prevalence ×
...) is implemented as coarse, bounded-cardinality string buckets
(`unidetect.featurization.bucket_by_edges` and friends), combined into a
`FeatureBucket` whose `as_key()` is the corpus table's grouping/partition
key. Coarse, bounded buckets are a deliberate scaling decision: they keep
`GROUP BY feature_bucket` tractable no matter how large the background
corpus grows, at the cost of some resolution the paper's exact-value
`Pm(D|T)` formalism has in principle (Section 2.2.2 already motivates this
trade-off: "T is already big enough so that sparsity is not an issue").

## 6. Deviations from a literal reading of the paper, and why

1. **The corpus `T`** is instantiated as "the tables already registered in
   Unity Catalog" rather than a 100M-table web crawl — the natural
   enterprise analogue, and the one this library is built to consume
   directly via `unidetect.catalog.list_tables_matching`.

2. **FD's `FR` metric.** The PDF's extracted formula for `FR` (and for the
   `Conforming-pair-ratio` baseline it's compared against) drops a
   comparison operator — a common artifact of extracting math from academic
   PDFs. `unidetect.metrics.functional_dependency` implements the standard,
   well-established row-based compliance ratio consistent with the paper's
   own stated intuition ("closer to 1 indicates likely violations, similar
   to UR") and its Figure 4(c) worked example (`FR = 4/6`), which the test
   suite reproduces exactly (`tests/test_metrics.py::TestFunctionalDependency`).

3. **MPD blocking.** An exact all-pairs minimum-edit-distance scan is
   `O(n^2)` per column, which does not scale to real Delta table columns.
   `unidetect.metrics.spelling` blocks candidates by (prefix, length bucket)
   before comparing pairwise, trading a small amount of recall on
   adversarial inputs for near-linear expected runtime — the right call for
   an unattended, automated detector.

4. **Corpus ingestion sampling.** `CorpusIngestor` caps how many values are
   materialized per column (`DataFrame.limit`, applied *before*
   aggregation) rather than collecting entire columns, so profiling a
   background corpus is bounded in cost regardless of individual table
   size.

## 7. Explainability

Every candidate carries an `evidence_json` blob (offending duplicate
values, the outlier value, the closest misspelled pair, the violating
`(lhs, rhs)` examples) produced at the same time as its metric computation,
so a `Detection` is never just a bare score — it's traceable back to the
paper's own style of "here's the actual pair/value/row that's surprising"
explanation (Figures 2 and 4 in the paper).
