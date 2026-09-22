# Graph Report - open-detect  (2026-09-22)

## Corpus Check
- 112 files · ~92,052 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 226, (none) 3, .properties 1)

## Summary
- 1048 nodes · 2333 edges · 60 communities (57 shown, 3 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 202 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `567d275f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- detectors/base.py
- UnityCatalogLocation
- algorithms/__init__.py
- dataset_utils.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- graphify SKILL.md — main pipeline skill
- outliers.py
- UniDetect
- enums.py
- perturbation.py
- wiki_subset/generate_report.py
- min_pairwise_edit_distance
- fd_compliance_ratio
- uniqueness_ratio
- CorpusStatsBuilder
- builder.py
- RahaConfig
- perturb_numeric_outlier
- pipeline.py
- log_duration
- ErrorType
- list_tables_matching
- unidetect/config.py
- main
- infer_column_data_type
- main
- spark_session.py
- unidetect
- detector.py
- cluster_column
- common/__init__.py
- gaussian_outlier_strategies
- test_featurization.py
- UniDetectConfig
- wiki_subset/run_benchmark.py
- UniDetectError
- collections_abc
- _score_single_column
- labeling.py
- `raha`
- Benchmark: WIKI subset
- select_datasets.py
- spark_session
- `raha`
- CallableLabeler
- Benchmark: real_world_gov
- unidetect/__init__.py
- real_world_gov/run_benchmark.py
- train_and_predict
- .detect
- build_column_features
- FeatureBucket
- README.md — Uni-Detect overview
- fd_violation_strategies
- Detection
- drop_nulls
- duplicate_value_indices
- FD metric deviation from literal paper formula

## God Nodes (most connected - your core abstractions)
1. `ErrorType` - 66 edges
2. `UniDetectConfig` - 46 edges
3. `UniDetect` - 34 edges
4. `RahaConfig` - 30 edges
5. `UnityCatalogLocation` - 26 edges
6. `ARCHITECTURE.md — Uni-Detect paper-to-code map` - 26 edges
7. `CorpusIngestor` - 21 edges
8. `CorpusStatsStore` - 21 edges
9. `RahaDetector` - 20 edges
10. `FeatureBucket` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/pipeline.py
- `Scoring raha` --references--> `GroundTruthLabeler`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/algorithms/raha/labeling.py
- `Running the benchmark` --references--> `CorpusStatsBuilder`  [INFERRED]
  benchmarks/real_world_gov/README.md → src/unidetect/corpus/builder.py
- `Scoring raha` --references--> `Labeler`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/algorithms/raha/labeling.py
- `WIKI-subset benchmark methodology redesign` --semantically_similar_to--> `functional_dependency metric (FR, Section 3.4)`  [INFERRED] [semantically similar]
  benchmarks/README.md → ARCHITECTURE.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **graphify Skill Reference Documentation Set** — _claude_skills_graphify_skill, _claude_skills_graphify_references_add_watch, _claude_skills_graphify_references_exports, _claude_skills_graphify_references_extraction_spec, _claude_skills_graphify_references_github_and_merge, _claude_skills_graphify_references_hooks, _claude_skills_graphify_references_query, _claude_skills_graphify_references_transcribe, _claude_skills_graphify_references_update [EXTRACTED 1.00]
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (60 total, 3 thin omitted)

### Community 0 - "detectors/base.py"
Cohesion: 0.10
Nodes (28): pyspark_sql, BaseDetector, make_evidence_json(), ABC, DataFrame, Shared detection template implementing Uni-Detect's Definition 4 end-to-end.…, Template-method base class for a single error-type detector., Return a DataFrame with the columns in :data:`CANDIDATE_COLUMNS`. (+20 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.17
Nodes (10): ensure_schema_exists(), Create the catalog/schema if they do not already exist. Requires ``CREATE…, A fully-qualified Unity Catalog three-level namespace., UnityCatalogLocation, ConfigurationError, Raised when a :class:`~unidetect.config.UniDetectConfig` is invalid., Raised for failures interacting with Unity Catalog (naming, permissions)., UnityCatalogError (+2 more)

### Community 2 - "algorithms/__init__.py"
Cohesion: 0.06
Nodes (50): importlib, AlgorithmResult, CellResult, ErrorDetectionAlgorithm, ABC, Any, DataFrame, Algorithm-agnostic contract every registered error-detection algorithm… (+42 more)

### Community 3 - "dataset_utils.py"
Cohesion: 0.17
Nodes (15): canonical_column(), dataset_paths(), load_changes(), load_csv(), Path, Shared helpers for reading the real_world_gov benchmark's checked-in CSVs.…, Strip ``dirty.csv``'s SQL-type-hint suffix (e.g. ``"zip(double precision)"``).…, Read a CSV into (canonical header, rows), treating ``""`` cells as null. (+7 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (20): ARCHITECTURE.md — Uni-Detect paper-to-code map, ComparisonDirection generalization (INCREASING/DECREASING), Bounded corpus ingestion sampling, Coarse feature-bucket featurization (Figure 5 cube diagram), MPD blocking optimization for spelling metric, Offline/online corpus-statistics architecture split, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase) (+12 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.13
Nodes (29): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+21 more)

### Community 6 - "graphify SKILL.md — main pipeline skill"
Cohesion: 0.10
Nodes (24): .claude/CLAUDE.md — graphify trigger, graphify reference: add-watch.md, graphify reference: exports.md, graphify reference: extraction-spec.md, graphify reference: github-and-merge.md, graphify reference: hooks.md, graphify reference: query.md, graphify reference: transcribe.md (+16 more)

### Community 7 - "outliers.py"
Cohesion: 0.14
Nodes (16): dataclasses, FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), ndarray (+8 more)

### Community 8 - "UniDetect"
Cohesion: 0.06
Nodes (26): Methodology: uni_detect -- mapping real dirty data onto its four error types, CorpusIngestor, DataFrame, SparkSession, Build the ``corpus_column_pairs`` DataFrame used for FD statistics., Global token -> distinct-table document-frequency (``Prev(C)`` input). A…, Builds ``corpus_columns``, ``corpus_column_pairs`` and ``token_stats``.…, Build the ``corpus_columns`` DataFrame from a list of UC table FQNs. Each… (+18 more)

### Community 9 - "enums.py"
Cohesion: 0.20
Nodes (11): ColumnDataType, Core enumerations shared across the unidetect package., Coarse data-type classification used for featurization (paper Fig. 5). This is…, CorpusColumnRecord, CorpusPairRecord, Core value types shared by metrics, featurization, corpus building and…, One row of the canonical corpus-column representation (see…, One row of the canonical corpus column-pair representation, used for FD. (+3 more)

### Community 10 - "perturbation.py"
Cohesion: 0.15
Nodes (13): _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, Per-error-type instantiations of epsilon-perturbation (paper Definition 2).…, Drop minority rows from the smallest violating LHS groups (paper Section 3.4)., Drop duplicate occurrences (paper Example 2). (+5 more)

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (35): grouped_bar_chart(), _nice_ceiling(), Pure-stdlib SVG bar-chart rendering shared by every benchmark's report.…, A bar path rounded at the top (far end from the baseline) only., _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), Cross-algorithm comparison table + chart rendering. Shared by every benchmark… (+27 more)

### Community 12 - "min_pairwise_edit_distance"
Cohesion: 0.21
Nodes (5): differing_token_lengths(), min_pairwise_edit_distance(), Lengths of whitespace-delimited tokens that differ between two values. Used by…, ``MPD(C) = min_{u != v in C} Edit(u, v)`` -- the closest pair by edit distance.…, TestSpelling

### Community 13 - "fd_compliance_ratio"
Cohesion: 0.26
Nodes (4): fd_compliance_ratio(), minority_violation_rows(), Rows to drop to repair the *smallest* FD-violating groups first. For each LHS…, TestFunctionalDependency

### Community 14 - "uniqueness_ratio"
Cohesion: 0.43
Nodes (3): ``UR(C) = num-distinct-values(C) / num-total-values(C)``. A ``UR`` close to 1.0…, uniqueness_ratio(), TestUniquenessRatio

### Community 15 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (8): CorpusStatsBuilder, compute(), DataFrame, SparkSession, Persist a stats DataFrame, replacing only its own ``error_type`` partition(s).…, Builds and persists the ``unidetect_corpus_stats`` Delta table. Parameters…, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType

### Community 16 - "builder.py"
Cohesion: 0.13
Nodes (16): Offline "learning" phase: materialize corpus statistics (paper Sec. 2.2.3). For…, bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+8 more)

### Community 17 - "RahaConfig"
Cohesion: 0.13
Nodes (19): Score every dataset's dirty table with Raha. Returns ``(targets,…, run_raha(), Score every eval target with Raha. Returns ``(targets, column_metrics,…, run_raha(), main(), Standalone quickstart: run Raha against a small dirty in-memory table. Run with…, RahaConfig, Configuration for :class:`~unidetect.algorithms.raha.detector.RahaDetector`.… (+11 more)

### Community 18 - "perturb_numeric_outlier"
Cohesion: 0.47
Nodes (3): perturb_numeric_outlier(), Drop the single most outlying value by MAD-score (paper Section 3.1)., TestPerturbNumericOutlier

### Community 19 - "pipeline.py"
Cohesion: 0.13
Nodes (13): argparse, functools, Databricks Job entrypoint: offline Uni-Detect corpus-statistics build. Intended…, Databricks Job entrypoint: online Uni-Detect error scanning. Example:…, Public, high-level API: :class:`UniDetect`. This is the single entry point most…, get_spark(), SparkSession, Spark session helpers. Kept deliberately tiny: on Databricks,… (+5 more)

### Community 20 - "log_duration"
Cohesion: 0.15
Nodes (12): itertools, Logger, logging, Turn a set of Unity Catalog tables into the canonical corpus representation.…, get_logger(), log_duration(), Structured logging helpers. Uses the standard :mod:`logging` module so behavior…, Return a namespaced logger under the ``unidetect`` hierarchy. Parameters… (+4 more)

### Community 21 - "ErrorType"
Cohesion: 0.16
Nodes (13): Enum, ComparisonDirection, ErrorType, Direction in which a metric moves once the anomalous subset is removed. Uni-…, The four error classes Uni-Detect is instantiated for (paper Section 3). Each…, all_specs(), ErrorTypeSpec, get_spec() (+5 more)

### Community 22 - "list_tables_matching"
Cohesion: 0.16
Nodes (10): list_tables(), list_tables_matching(), SparkSession, Return fully-qualified names of every table in ``catalog.schema``., Return fully-qualified table names across one or more schemas in ``catalog``.…, table_exists(), TestListTables, TestListTablesMatching (+2 more)

### Community 23 - "unidetect/config.py"
Cohesion: 0.18
Nodes (10): pytest, Unity Catalog convenience helpers. Thin wrappers around Spark SQL DDL/catalog…, Central configuration for a Uni-Detect deployment. A single…, Online scoring: batch likelihood-ratio lookups against materialized corpus…, CorpusNotFoundError, Exception hierarchy for unidetect. All library-raised exceptions derive from…, Raised when the corpus statistics table has not been built yet., Unit tests for catalog.py using a mocked SparkSession (no real cluster… (+2 more)

### Community 24 - "main"
Cohesion: 0.27
Nodes (5): main(), parse_args(), Namespace, TestMain, TestParseArgs

### Community 25 - "infer_column_data_type"
Cohesion: 0.07
Nodes (17): ``Prev(C)`` (paper Sec. 3.3): average, over values and their tokens, of how…, token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), Split a value into alphanumeric tokens, discarding punctuation/whitespace., True for values like 'ICAO123', 'SKU-9981', 'AB12CD34' -- typical ID/code… (+9 more)

### Community 26 - "main"
Cohesion: 0.22
Nodes (6): main(), parse_args(), Namespace, Unit tests for jobs/build_corpus_statistics.py (argument parsing +…, TestMain, TestParseArgs

### Community 27 - "spark_session.py"
Cohesion: 0.13
Nodes (17): Local, Delta-enabled Spark session bootstrap shared by every benchmark.…, contextlib, os, shutil, subprocess, tempfile, _delta_jars(), _download() (+9 more)

### Community 30 - "detector.py"
Cohesion: 0.16
Nodes (14): ClassifierMixin, numpy, pandas, sklearn_base, Per-column classification (paper Section 4.4, Algorithm 1 lines 12-16). Raha…, _default_classifier_factory(), Tunable knobs for the Raha algorithm. Mirrors the paper's own default parameter…, The paper's default classifier (Section 6.1: "We use Gradient Boosting"). (+6 more)

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (11): scipy_cluster_hierarchy, scipy_spatial_distance, cluster_column(), ndarray, Clustering-based sampling (paper Section 4.3). Two pieces of Algorithm 1's…, Cut a column's feature matrix into (up to) ``k`` clusters. Uses cosine-…, Draw the next tuple to label per the softmax rule of Equation (3). ``P(t) =…, sample_tuple() (+3 more)

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.14
Nodes (13): Series, gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), ndarray, Bag-of-characters pattern-violation strategies ``s_ch`` (Section 4.1). One…, Stringify a column, mapping every null-like value to one sentinel category.… (+5 more)

### Community 34 - "test_featurization.py"
Cohesion: 0.28
Nodes (4): log_transform_fits_better(), Heuristic for the "whether logarithm-transform better fits the data" dimension.…, Unit tests for featurization.py and text_utils.py., TestLogFit

### Community 35 - "UniDetectConfig"
Cohesion: 0.08
Nodes (21): Running the benchmark, SparkSession, Tunable knobs for both the offline corpus builder and the online detectors.…, UniDetectConfig, CorpusStatsStore, DataFrame, SparkSession, Score a batch of candidates against the corpus for one error type. Parameters… (+13 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.16
Nodes (15): confusion_metrics(), Confusion-matrix scoring shared by every benchmark's evaluation targets. Every…, Precision/recall/F1/accuracy over ``rows``' boolean…, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+7 more)

### Community 37 - "UniDetectError"
Cohesion: 0.24
Nodes (10): InsufficientDataError, Exception, Base class for all unidetect errors., Raised when a target column/table does not have enough data to score., UniDetectError, parametrize, Unit tests for the exception hierarchy (no Spark required)., test_all_errors_derive_from_unidetect_error() (+2 more)

### Community 38 - "collections_abc"
Cohesion: 0.20
Nodes (12): collections, collections_abc, rapidfuzz_distance, Sized, Shared helpers for metric-function implementations., require_min_size(), FD-compliance-ratio metric (paper Section 3.4, ``FR``). Note on fidelity to the…, _blocking_key() (+4 more)

### Community 39 - "_score_single_column"
Cohesion: 0.16
Nodes (8): pyspark_sql_types, _coerce_numeric(), compute(), _score_single_column(), Canonical Delta table schemas used by the corpus builder and store. Keeping…, Unit tests for the pure-Python helpers in corpus/builder.py.…, TestCoerceNumeric, TestScoreSingleColumn

### Community 40 - "labeling.py"
Cohesion: 0.24
Nodes (10): Scoring raha, ColumnFeatures, A single column's feature matrix ``V_j`` and the strategy each column came from., HeuristicLabeler, Labeler, ABC, Labeling (paper Appendix C) and label propagation through clusters (Section…, Supplies the ``dirty``/``clean`` label for every cell of a sampled tuple. (+2 more)

### Community 41 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 42 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 43 - "select_datasets.py"
Cohesion: 0.60
Nodes (5): candidates(), main(), Path, Reproduces how this benchmark's 5 datasets were picked from Matelda's DGov_NTR…, select()

### Community 44 - "spark_session"
Cohesion: 0.33
Nodes (6): Any, Exception, Raised only when a local Delta-enabled Spark session cannot be started at all.…, Start a local, single-process, Delta-enabled Spark session for a benchmark run.…, spark_session(), SparkUnavailable

### Community 45 - "`raha`"
Cohesion: 0.20
Nodes (9): Algorithm comparison, By dataset (cell-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level), Evaluated columns (column-level), `raha`, real_world_gov benchmark results (+1 more)

### Community 46 - "CallableLabeler"
Cohesion: 0.18
Nodes (5): CallableLabeler, DataFrame, Return ``{column_name: is_error}`` for every column of ``df.loc[row_index]``., Wraps a plain function as a :class:`Labeler` -- the interactive/UI escape…, TestCallableLabeler

### Community 47 - "Benchmark: real_world_gov"
Cohesion: 0.29
Nodes (7): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Layout, Methodology: raha, Reading the results, Which 5 datasets, and why

### Community 48 - "unidetect/__init__.py"
Cohesion: 0.26
Nodes (8): Candidate, MetricObservation, The (before, after) reading of a metric function around a perturbation.…, A single perturbation hypothesis awaiting a likelihood-ratio score. One…, __getattr__(), unidetect: a library of pluggable, paper-backed error detection algorithms.…, TestCandidate, TestMetricObservation

### Community 49 - "real_world_gov/run_benchmark.py"
Cohesion: 0.26
Nodes (10): git_commit(), Path, _build_config(), main(), _print_comparison(), Runs the real_world_gov benchmark for every available registered algorithm (see…, Score every dataset's dirty table with Uni-Detect. Returns (targets, metrics,…, _register_table() (+2 more)

### Community 50 - "train_and_predict"
Cohesion: 0.24
Nodes (8): ColumnPredictions, Per-row predictions for one column. ``score`` is ``P(dirty)`` in ``[0, 1]``., Fit ``m_j`` on the labeled rows and predict every row of the column. Falls back…, train_and_predict(), _features(), ndarray, TestClassifierTrainingPath, TestDegenerateCases

### Community 51 - ".detect"
Cohesion: 0.24
Nodes (6): Any, DataFrame, Run Algorithm 1 against a single in-memory table. Parameters ---------- data:…, propagate_labels(), Propagate a column's user labels to the rest of their clusters (Section 4.4).…, TestPropagateLabels

### Community 52 - "build_column_features"
Cohesion: 0.25
Nodes (10): build_all_features(), build_column_features(), DataFrame, Run every applicable strategy family on ``column_name`` and assemble ``V_j``.…, :func:`build_column_features` for every column of ``df``., Unit tests for algorithms/raha/features.py., test_build_all_features_covers_every_column(), test_drops_constant_features() (+2 more)

### Community 53 - "FeatureBucket"
Cohesion: 0.27
Nodes (4): FeatureBucket, A discretized point in the featurization "cube" (paper Figure 5). Instances of…, Stable string encoding, used as a Delta partition/grouping column., TestFeatureBucket

### Community 54 - "README.md — Uni-Detect overview"
Cohesion: 0.31
Nodes (8): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, UniDetect pipeline facade

### Community 55 - "fd_violation_strategies"
Cohesion: 0.38
Nodes (4): fd_violation_strategies(), DataFrame, Rule-violation (functional dependency) strategies ``s_{a->a'}`` (Section 4.1).…, TestFdViolationStrategies

### Community 56 - "Detection"
Cohesion: 0.38
Nodes (4): Detection, Any, A scored, ranked prediction ready to be surfaced to a user or written to UC., TestDetection

### Community 57 - "drop_nulls"
Cohesion: 0.40
Nodes (4): drop_nulls(), Remove ``None``/``NaN``-like values, preserving order. Real-world corpus…, _T, TestDropNulls

### Community 58 - "duplicate_value_indices"
Cohesion: 0.50
Nodes (3): duplicate_value_indices(), Indices of values that participate in at least one duplicate group. This is the…, TestDuplicateValueIndices

### Community 59 - "FD metric deviation from literal paper formula"
Cohesion: 1.00
Nodes (3): FD metric deviation from literal paper formula, WIKI-subset benchmark methodology redesign, functional_dependency metric (FR, Section 3.4)

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **37 isolated node(s):** `unidetect`, `Which 5 datasets, and why`, `Layout`, `Duration methodology`, `Reading the results` (+32 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 306 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `detectors/base.py`, `algorithms/__init__.py`, `UniDetectConfig`, `wiki_subset/run_benchmark.py`, `generate_dataset.py`, `_score_single_column`, `UniDetect`, `enums.py`, `CorpusStatsBuilder`, `unidetect/__init__.py`, `real_world_gov/run_benchmark.py`, `builder.py`, `pipeline.py`, `FeatureBucket`, `unidetect/config.py`, `Detection`, `main`, `main`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `detectors/base.py`, `UnityCatalogLocation`, `algorithms/__init__.py`, `wiki_subset/run_benchmark.py`, `generate_dataset.py`, `_score_single_column`, `UniDetect`, `CorpusStatsBuilder`, `builder.py`, `real_world_gov/run_benchmark.py`, `unidetect/__init__.py`, `pipeline.py`, `unidetect/config.py`, `main`, `main`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `RahaConfig` connect `RahaConfig` to `UnityCatalogLocation`, `algorithms/__init__.py`, `train_and_predict`, `build_column_features`, `detector.py`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `UniDetect` (e.g. with `run_uni_detect()` and `Why not download the real WIKI corpus in CI?`) actually correct?**
  _`UniDetect` has 13 INFERRED edges - model-reasoned connections that need verification._