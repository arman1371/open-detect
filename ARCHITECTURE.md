# Architecture

This document maps each part of two papers -- Wang & He's Uni-Detect
(SIGMOD 2019) and Mahdavi et al.'s Raha (SIGMOD 2019) -- onto this codebase,
and explains the decisions each paper's translation into a shared library
required.

## 0. The multi-algorithm framework

`unidetect.algorithms` (`src/unidetect/algorithms/`) is what turns this
repository from a single paper's implementation into a library of
interchangeable error-detection algorithms:

- `algorithms/base.py` -- `ErrorDetectionAlgorithm`, the one-method contract
  (`detect(...) -> AlgorithmResult`) every algorithm implements, and
  `AlgorithmResult`/`CellResult`, the shared, flattened (table, row, column)
  output schema every algorithm's result gets normalized into regardless of
  how it was computed internally.
- `algorithms/registry.py` -- maps a name (`"uni_detect"`, `"raha"`, ...) to
  a class, resolved lazily so that requesting one algorithm never imports
  another's optional dependencies (`pyspark` for Uni-Detect, `scikit-learn`
  for Raha). Third-party algorithms register the same way via the
  `unidetect.algorithms` Python entry-point group, with no changes to this
  repository.
- `algorithms/uni_detect_algorithm.py` -- adapts the pre-existing
  `unidetect.pipeline.UniDetect` (Sections 1-7 below) to this contract by
  flattening its Spark output.
- `algorithms/raha/` -- Raha's own implementation (Section 8 below), built
  directly against the shared contract since it has no pre-existing
  standalone pipeline to adapt.

Deliberately not unified: each algorithm's `detect()` input type. Uni-Detect
scores tables already registered in Unity Catalog against a background
corpus (`Sequence[str]` of table names); Raha scores one in-memory table
(`pandas.DataFrame`). Forcing both into one input shape would mean
distorting one paper's actual operating model to match the other's --
instead, only the *output* is unified, which is what actually lets results
from different algorithms be compared, unioned, or displayed together.

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

---

# Raha (Mahdavi et al., SIGMOD 2019)

## 8. Code map

Raha's Algorithm 1 maps onto `src/unidetect/algorithms/raha/` module-by-step:

| Algorithm 1 step | Paper section | Code |
|---|---|---|
| Line 1: configure strategies | Section 4.1 | `strategies.py` (`histogram_outlier_strategies`, `gaussian_outlier_strategies`, `pattern_character_strategies`, `fd_violation_strategies`) |
| Line 2: generate feature vectors | Section 4.2 | `features.py` (`build_column_features`, `build_all_features`) |
| Lines 3-11: cluster + sample tuples | Section 4.3 | `clustering.py` (`cluster_column`, `sample_tuple`) |
| Line 9: label a tuple | Appendix C | `labeling.py` (`Labeler` and its implementations) |
| Lines 12-14: propagate labels | Section 4.4 | `labeling.py::propagate_labels` |
| Lines 15-16: train + predict per column | Section 4.4 | `classifier.py::train_and_predict` |
| Whole algorithm | Section 3-4 | `detector.py::RahaDetector.detect` |

## 9. Strategy families and what each feature means

A "feature" of a cell's feature vector is one strategy's binary verdict on
that cell (Definition 1). Three of the paper's four families are
implemented, each producing a parameter grid rather than one fixed
threshold, per Section 4.1:

- **Histogram outlier (`s_tf`)** -- flags a cell whose value is rare in its
  column (relative frequency below a threshold), at 9 thresholds
  (`0.1, ..., 0.9`).
- **Gaussian outlier (`s_dist`)** -- flags a numeric cell far from its
  column's mean in standard deviations, at 9 thresholds following the
  paper's 68-95-99.7 rule (`1, 1.3, ..., 3`). Only generated for columns
  that are mostly numeric.
- **Pattern violation (bag-of-characters, `s_ch`)** -- one strategy per
  distinct character in the column, flagging cells that contain it (e.g. a
  stray `-` in a digit-only column), capped at the most frequent
  `max_pattern_characters` to bound the feature space on free-text columns.
- **Rule/FD violation (`s_{a->a'}`)** -- for every other column `a`, flags
  cells of the target column `a'` whose `a`-group contains more than one
  distinct `a'` value, following Section 4.1's formal `j = index of a'`
  assignment (see the fidelity note in `strategies.py` about the paper's own
  inconsistent illustrative example).
- **Not implemented: knowledge-base violation (`s_r`).** Requires a live
  external knowledge base (DBpedia in the paper) and network access to an
  entity-relationship store -- out of scope for a library meant to run
  against arbitrary, possibly offline/private data. The paper itself notes
  Raha "is not limited to these categories" (Section 2.2); a fifth family
  can be added later as another function returning
  `dict[str, np.ndarray[bool]]` without touching clustering, labeling, or
  classification.

`features.py` drops constant features per column (Section 4.2's
post-processing step) before assembling the matrix Raha clusters on.

## 10. Clustering, sampling, and labeling

`RahaDetector.detect` runs Algorithm 1's `while |L| < labels_budget` loop
directly: each iteration re-clusters every column at `k` (starting at 2,
incrementing by 1 per iteration -- Section 4.3), draws one tuple via the
softmax rule of Equation 3 (`clustering.py::sample_tuple`, favoring
under-labeled clusters), and asks the configured `Labeler` to label it.

`Labeler` (`labeling.py`) is the paper's Appendix-C human-labeling step made
pluggable:

- `GroundTruthLabeler` -- compares against a known-clean table; for
  evaluation/benchmarking.
- `CallableLabeler` -- wraps any function, e.g. a real UI or CLI prompt; the
  paper's actual intended use.
- `HeuristicLabeler` -- a documented deviation from the paper: a no-human
  fallback (majority vote of a cell's own fired strategies) so the pipeline
  can still run with zero interaction. Strictly weaker than a real label,
  since it mostly reinforces what the strategies already say; see its
  docstring.

After sampling, `propagate_labels` implements Section 4.4's cluster-based
label propagation with both conflict-resolution policies the paper
describes (`"homogeneity"`: skip clusters with contradicting labels;
`"majority"`: resolve them by vote, ties going to "dirty" as the
conservative choice for a class-imbalanced task) -- user labels always
override propagated ones for their own cell.

## 11. Classification and cell-level output

`classifier.py::train_and_predict` fits one classifier per column
(`RahaConfig.classifier_factory`, defaulting to `GradientBoostingClassifier`
per the paper's Section 6.1 setup) on the propagated labels and predicts
every remaining cell's `P(dirty)`. Degenerate cases (no labels, a
single-class label set, or a column with no informative features -- none of
which a real scikit-learn classifier can fit) fall back to the labeled
rows' majority vote rather than raising.

`RahaDetector.detect` then assembles the final `AlgorithmResult`: a directly
labeled or propagated cell keeps that exact label (`score` 1.0/0.0), while
every other cell gets the classifier's prediction and probability, each
tagged with `evidence.source` (`"user_label"` / `"propagated"` /
`"classifier"`) and `evidence.fired_strategies` (which strategies flagged
that specific cell) for explainability, in the same spirit as Uni-Detect's
`evidence_json` (Section 7 above).

## 12. Deviations from a literal reading of the paper, and why

1. **Histogram outlier normalization.** The published `s_tf` formula
   normalizes by `sum_i' TF(d[i',j])`, which algebraically is `sum_v
   count(v)^2`, not the column size. Plugging that literal denominator into
   the paper's own worked example (Section 2.2) does not reproduce the
   stated result; the natural reading -- relative frequency `count(v) /
   |d|` -- reproduces it exactly, and is what `strategies.py` implements.
   Same class of PDF-math-extraction artifact as Uni-Detect's FD formula
   (Section 6.2 above).
2. **Knowledge-base violation detection is omitted** (Section 9 above).
3. **Historical strategy filtering (paper Section 5) is not implemented.**
   It is a runtime optimization -- pruning strategies unlikely to help based
   on similarity to previously cleaned columns -- not part of the core
   detection result, and requires a corpus of historical cleaned datasets
   this library has no equivalent source for today. `RahaConfig` and the
   strategy functions are structured so this could be added later as a
   pre-filtering step over `features.py`'s strategy dict, without changing
   the clustering/labeling/classification pipeline.
4. **Bag-of-characters strategies are capped** (`max_pattern_characters`,
   default 128) rather than one-per-distinct-character unboundedly, since a
   free-text column can have an effectively unbounded character vocabulary;
   the most frequent characters are kept on the assumption that a rare
   character is already exposed by the histogram outlier strategies on the
   whole value.

# Auto-Validate (Song & He, SIGMOD 2021)

## Code map

| Algorithm / Eqn | Paper section | Code |
|---|---|---|
| Generalization hierarchy, tokenizer | Sec 2.1 | `hierarchy.py` (`tokenize`, `matches`, `generalize`, `token_count`, `generality_weight`) |
| `P(v)`, Algorithm 1 (GeneratePatterns) | Sec 2.1, Alg 1 | `patterns.py` (`iter_patterns`, `patterns_of`, `sorted_patterns`) |
| Impurity `Imp_D(h)` (Eqn 1), FPR_D = Imp_D (Eqns 2-3) | Sec 2.4, Def 1, 2, 3 | `metrics.py` (`impurity`, `fpr_column`) |
| Corpus FPR_T (Eqn 4), Cov_T, tau-pruned index | Sec 2.4 | `index.py` (`PatternIndex`, `build_pattern_index`, `clean_column`, `indexable_values`) |
| FMDV (Eqns 5-7) | Sec 2 | `fmdv.py::fmdv` |
| FMDV-H (Eqns 12-16) | Sec 4 | `fmdv.py::fmdv_h` |
| FMDV-V (Eqns 8-11) | Sec 3 | `fmdv_v.py::fmdv_v` |
| FMDV-VH (paper-spec §5.5) | Sec 4 | `fmdv_v.py::fmdv_vh` |
| Drift test (Sec 4) | Sec 5.4 | `drift.py::check_drift` |
| Detector, registry | — | `detector.py::AutoValidateAlgorithm` (OPE-26) |

## Config

`AutoValidateConfig` (`config.py`): `variant="fmdv_vh"`, `r=0.05`, `m=100`,
`tau=8`, `theta=0.1`, `drift_significance=0.01`.  The paper has no
`alpha`/`beta`/`epsilon`.  `m=100` is the paper's recommendation for a
7.2M-column corpus; small corpora must override explicitly.

## Public API

- `build_pattern_index(corpus, config)` — offline scan of `T`.
- `fmdv(values, index, config)` — Eqn 5-7: `min FPR_T(h)` over
  `H(C)=∩P(v)\{" .* "}` s.t. `FPR_T(h)<=r` and `Cov_T(h)>=m`.
- `fmdv_h(values, index, config)` — Eqn 12-16: same but hypothesis space is
  `∪P(v)\{" .* "}` with `(1-theta)|C|` coverage on the query column.
- `fmdv_v(values, index, config)` — Eqn 8-11: vertical cuts via DP.
- `fmdv_vh(values, index, config)` — FMDV-H per segment, then FMDV-V.
- `check_drift(train, test, pattern, significance)` — two-tailed Fisher's
  exact test on non-conforming counts (column-level alert only).
- `InferredPattern(pattern, fpr_t, cov_t, theta_c, variant)` — result of any
  variant.
- `DriftResult(theta_train, theta_test, p_value, drifted)` — drift test result.
- `AutoValidateAlgorithm` — end-to-end detector registered as `"auto_validate"`.

### Detector API

`AutoValidateAlgorithm(ErrorDetectionAlgorithm)` implements:

- `__init__(config=None)` — accepts an `AutoValidateConfig` instance.
- `build_index(corpus: Iterable[Series|DataFrame]) -> PatternIndex` — builds
  the offline index and stores it on `self._index`.
- `infer_pattern(column: Series) -> tuple[str|None, float, int, float, str|None]`
  — returns `(pattern, fpr_t, cov_t, theta_c, reason)` where `reason` is
  ``None`` on success or an explanation string on infeasibility.
- `detect(data: DataFrame, *, table_id="table", columns=None, **kw) -> AlgorithmResult`
  — scans the dirty table, infers a pattern per column, produces one
  `CellResult` per non-null cell. `is_error = (value not in L(pattern))`.
  Evidence keys: `pattern`, `fpr_t`, `cov_t`, `theta_c`, `variant`, `r`, `m`, `tau`.
  Infeasible columns produce cells with `pattern=None, reason="no_feasible_pattern"`.
- `IndexNotBuiltError` — raised when `detect` or `infer_pattern` is called
  before `build_index`.

Registry: `_load_auto_validate()` → `register_lazy("auto_validate", ...)` in
`src/unidetect/algorithms/__init__.py`.  `unidetect.algorithms` import path
never imports scipy/pyspark/sklearn — those are lazy-loaded only when the
algorithm is actually constructed.

## Fidelity notes

1. **FMDV-H exact search vs. paper greedy.**  The paper says the decision
   version of FMDV-H is NP-hard (Thm 1) and uses a greedy.  The paper-spec
   description of the greedy is vague, so we implement an exact search over
   all candidate patterns in `∪P(v)`.  This solves Eqn 12-16 exactly; the
   greedy is omitted rather than approximated.
2. **Tie-breaking.**  The paper is silent.  We break ties by
   `(FPR_T ascending, impurity on C ascending, Cov_T descending, lexicographic
   pattern)`.  This favors general patterns with more corpus evidence and is
   deterministic.
3. **MSA approximation.**  Exact multi-sequence alignment (Carrillo & Lipman
   1988) is exponential.  We group values by coarse token-class signature
   (`<symbol>`, `<num>`, `<letter>` runs).  Within each group alignment is
   exact (same class sequence means positional alignment needs no gaps).
   This is exact when all values share one coarse signature (typical for
   homogeneous machine-generated data, per the paper's own assumption) and
   an approximation otherwise.
4. **FMDV-VH composition order.**  The paper (§5.5) says "horizontal first
   then vertical".  Our interpretation: partition values by coarse signature
   into vertical groups, then within each group apply FMDV-H (theta
   tolerance), then DP across groups.  The per-group H-cut tolerates
   outliers before vertical segmentation.
5. **No corpus-free fallback.**  `fmdv`/`fmdv_h`/`fmdv_v`/`fmdv_vh` require
   a `PatternIndex`; without one, callers must raise `IndexNotBuiltError`.
   This follows from the paper's requirement that `T` be a background
   corpus of columns.
6. **Score definition (non-paper).**  The paper has no per-cell score
   (Section 6.4).  We set `score = 1 - FPR_T(h)` for flagged cells and
   `0.0` for unflagged cells — a ranking-only extension documented here.
7. **Drift test not wired into `detect`.**  `detect` does not call
   `check_drift` because a single-table scan has no "future" column to
   compare against.  This is a fidelity question for the independent
   reviewer (paper-spec §8.8).
8. **`P(v)` for T-side counting uses all values (weighted by multiplicity).**
   Impurity is computed over every value in the column, not distinct values
   only, consistent with Eqn 1.
9. **Pattern matching at detection time.**  `detect` uses `matches(pattern, value)`
   from `hierarchy.py` to determine `is_error`.  When the inferred pattern
   is generic (e.g. `<alphanum>+<symbol>+<alphanum>+<symbol>+<alphanum>+` for
   email-like input with low corpus diversity), the pattern may match non-email
   values too — this is inherent to the hierarchy's granularity, not a bug.
10. **Infeasible columns get no flags.**  When `infer_pattern` returns
   `(None, 0.0, 0, 0.0, "no_feasible_pattern")`, the detector produces one
   `CellResult` per non-null cell with `is_error=False` and evidence
   `{"pattern": None, "reason": "no_feasible_pattern", ...}`.  This avoids
   false positives when the corpus is too small or too diverse for any
   pattern to satisfy the `r`/`m` thresholds.

## Scope exclusions

- **Corpus-free mode**: undefined in the paper; omitted.
- **ML pattern profiler**: the paper uses a dedicated "profiler" tool; this
  library uses the mathematically defined hierarchy directly.
- **NL-content columns**: excluded by the paper (footnote on Section 2.1).
- **Multi-column constraints**: the basic algorithm is single-column.
- **Pattern unions**: unsupported in the paper's own profiler.
- **Spark implementation**: deferred.
- **Index persistence / parallel offline build**: speed-only, deferred.
- **Benchmarks**: OPE-22.
