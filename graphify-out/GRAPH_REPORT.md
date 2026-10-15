# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 152 files · ~120,970 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1694 nodes · 4147 edges · 88 communities (67 shown, 21 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 553 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `43e9bde4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- registry.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- fmdv_v
- CorpusIngestor
- FailureCounts
- wiki_subset/generate_report.py
- check_failure_threshold
- algorithms/__init__.py
- metrics/spelling.py
- AutoValidateConfig
- check_drift
- RahaConfig
- catalog.py
- ErrorType
- Commit conventions and releases
- patterns.py
- PatternIndex
- collections_abc
- test_metrics.py
- infer_column_data_type
- pytest
- tokenize
- FailureCountsAccumulatorParam
- _score_single_column
- AlgorithmResult
- .detect
- raha/strategies.py
- pandas
- MetricObservation
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- API reference
- FeatureBucket
- GroundTruthLabeler
- real_world_gov benchmark results
- json
- numpy
- wiki_subset/README.md
- RahaDetector
- test_package_init.py
- featurization.py
- make_evidence_json
- algorithms/index.md
- propagate_labels
- .detect
- docs/index.md
- main
- fmdv
- argparse
- raha/detector.py
- enums.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- UniDetect
- Auto-Validate
- OpenDetectError
- Raha
- Comparing algorithms
- CorpusStatsStore
- log_transform_fits_better
- Auto-Validate
- algorithms/uni-detect.md
- Benchmark: real_world_gov
- get_spec
- Detection
- Uni-Detect
- Custom labelers (Raha)
- is_float_like
- `auto_validate`
- CorpusStatsBuilder
- `raha`
- clean_column
- algorithms.md
- indexable_values
- build_spark
- open-detect

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 105 edges
2. `ErrorType` - 81 edges
3. `UniDetectConfig` - 74 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 39 edges
6. `UniDetect` - 37 edges
7. `AutoValidateAlgorithm` - 36 edges
8. `RahaConfig` - 33 edges
9. `PatternIndex` - 31 edges
10. `UnityCatalogLocation` - 31 edges

## Surprising Connections (you probably didn't know these)
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `Writing a class` --references--> `Labeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `The simplest labeler: a function` --references--> `CallableLabeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (88 total, 21 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.05
Nodes (23): Bug Fixes, CHANGELOG, Refactoring, Unreleased, v0.2.0 (2026-10-08), v0.2.1 (2026-10-14), ensure_schema_exists(), UniDetectConfig (+15 more)

### Community 2 - "registry.py"
Cohesion: 0.15
Nodes (10): get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), test_builtin_algorithms_are_registered(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy() (+2 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.08
Nodes (14): _score_pair(), _score_column(), _score_column(), _score_column(), _max_drop(), perturb_functional_dependency(), perturb_numeric_outlier(), perturb_spelling() (+6 more)

### Community 8 - "fmdv_v"
Cohesion: 0.11
Nodes (9): Variants, _coarse_class(), _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestFmdvV, TestFmdvVh (+1 more)

### Community 9 - "CorpusIngestor"
Cohesion: 0.18
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 10 - "FailureCounts"
Cohesion: 0.14
Nodes (8): compute(), compute(), _score_fd_pair(), FailureCounts, compute(), _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 12 - "check_failure_threshold"
Cohesion: 0.19
Nodes (4): Configuration, check_failure_threshold(), DataQualityError, TestCheckFailureThreshold

### Community 13 - "algorithms/__init__.py"
Cohesion: 0.17
Nodes (6): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), UniDetectAlgorithm, __getattr__()

### Community 14 - "metrics/spelling.py"
Cohesion: 0.05
Nodes (22): drop_nulls(), require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), mad_scores(), MADResult, max_mad() (+14 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.09
Nodes (9): AutoValidateConfig, build_pattern_index(), _iter_corpus_columns(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex (+1 more)

### Community 16 - "check_drift"
Cohesion: 0.14
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "catalog.py"
Cohesion: 0.14
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 19 - "ErrorType"
Cohesion: 0.12
Nodes (10): all_specs(), ErrorTypeSpec, ColumnDataType, ComparisonDirection, ErrorType, CorpusColumnRecord, CorpusPairRecord, __getattr__() (+2 more)

### Community 20 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 21 - "patterns.py"
Cohesion: 0.05
Nodes (21): _char_class(), _class_of_token(), generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize() (+13 more)

### Community 24 - "test_metrics.py"
Cohesion: 0.17
Nodes (3): duplicate_value_indices(), InsufficientDataError, TestDuplicateValueIndices

### Community 25 - "infer_column_data_type"
Cohesion: 0.11
Nodes (6): infer_column_data_type(), is_integer_like(), is_mixed_alphanumeric(), TestDataTypeInference, TestIntegerLike, TestMixedAlphanumeric

### Community 26 - "pytest"
Cohesion: 0.09
Nodes (6): get_logger(), log_duration(), test_error_message_is_preserved(), test_open_detect_error_is_catchable_broadly(), TestGetLogger, TestLogDuration

### Community 27 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 29 - "_score_single_column"
Cohesion: 0.27
Nodes (4): _coerce_numeric(), _score_single_column(), TestCoerceNumeric, TestScoreSingleColumn

### Community 30 - "AlgorithmResult"
Cohesion: 0.13
Nodes (10): Through the registry, Auto-Validate: learn patterns from clean columns, Quickstart, Reading results, Uni-Detect: score tables in Unity Catalog, Combine, Why a common interface, AlgorithmResult (+2 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "pandas"
Cohesion: 0.08
Nodes (14): InferredPattern, _fmdv_h_single(), _fmdv_single_segment(), _infer_cmp(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), _append_literal() (+6 more)

### Community 35 - "MetricObservation"
Cohesion: 0.29
Nodes (4): Candidate, MetricObservation, TestCandidate, TestMetricObservation

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.09
Nodes (14): git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.08
Nodes (12): Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm, _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells() (+4 more)

### Community 38 - "API reference"
Cohesion: 0.16
Nodes (10): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+2 more)

### Community 40 - "GroundTruthLabeler"
Cohesion: 0.17
Nodes (5): Raha: find errors with a few labels, CallableLabeler, GroundTruthLabeler, TestCallableLabeler, TestGroundTruthLabeler

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "json"
Cohesion: 0.18
Nodes (5): confusion_metrics(), run_auto_validate(), _metrics(), run_raha(), _metrics()

### Community 44 - "numpy"
Cohesion: 0.19
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 45 - "wiki_subset/README.md"
Cohesion: 0.22
Nodes (7): Algorithm comparison, By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`, WIKI-subset benchmark results

### Community 46 - "RahaDetector"
Cohesion: 0.19
Nodes (7): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 48 - "featurization.py"
Cohesion: 0.12
Nodes (11): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 49 - "make_evidence_json"
Cohesion: 0.11
Nodes (7): make_evidence_json(), compute(), compute(), compute(), compute(), _StubDetector, TestDetectorFailureGate

### Community 52 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 54 - "main"
Cohesion: 0.21
Nodes (5): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestParseArgs

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.52
Nodes (3): candidates(), main(), select()

### Community 57 - "raha/detector.py"
Cohesion: 0.20
Nodes (5): Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, Labeler, TestHeuristicLabeler

### Community 58 - "enums.py"
Cohesion: 0.10
Nodes (6): FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, get_spark(), TestGetSpark

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.14
Nodes (14): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Expected weakness: read Auto-Validate's low recall honestly, Layout, Reading the results without JSON, Running the benchmark, Scoring auto_validate (+6 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 61 - "UniDetect"
Cohesion: 0.24
Nodes (5): main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 62 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 63 - "OpenDetectError"
Cohesion: 0.16
Nodes (10): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, The shared result schema, Errors, UnknownAlgorithmError (+2 more)

### Community 64 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 65 - "Comparing algorithms"
Cohesion: 0.40
Nodes (5): Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 66 - "CorpusStatsStore"
Cohesion: 0.08
Nodes (16): A fully local example, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks, Job arguments (+8 more)

### Community 68 - "Auto-Validate"
Cohesion: 0.13
Nodes (10): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, Configuration, Detector (+2 more)

### Community 69 - "algorithms/uni-detect.md"
Cohesion: 0.20
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.12
Nodes (14): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types (+6 more)

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Custom labelers (Raha)"
Cohesion: 0.33
Nodes (6): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class

### Community 77 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "algorithms.md"
Cohesion: 0.50
Nodes (3): Registry, Registry and results, Result types

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 530 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `FailureCounts`, `algorithms/__init__.py`, `collections_abc`, `pytest`, `_score_single_column`, `MetricObservation`, `wiki_subset/run_benchmark.py`, `API reference`, `FeatureBucket`, `builder.py`, `featurization.py`, `make_evidence_json`, `.detect`, `main`, `enums.py`, `UniDetect`, `CorpusStatsStore`, `get_spec`, `Detection`, `CorpusStatsBuilder`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11095305832147938 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `UniDetectConfig`, `pandas`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `API reference`, `fmdv_v`, `json`, `check_drift`, `fmdv`, `OpenDetectError`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 50 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._