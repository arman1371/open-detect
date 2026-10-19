# Graph Report - open-detect  (2026-10-19)

## Corpus Check
- 157 files · ~129,136 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1948 nodes · 4758 edges · 104 communities (83 shown, 21 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 619 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d43e1802`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- test_spelling_detector.py
- wiki_subset/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- auto_validate/detector.py
- UniDetect
- FailureCounts
- check_failure_threshold
- CorpusIngestor
- fmdv_v
- outliers.py
- AutoValidateConfig
- InferredPattern
- RahaConfig
- _StubDetector
- FailureCountsAccumulatorParam
- matches
- hierarchy.py
- real_world_gov/generate_report.py
- get_spec
- test_metrics.py
- open_detect/exceptions.py
- builder.py
- perturb_numeric_outlier
- ConfigurationError
- ErrorType
- AlgorithmResult
- numpy
- raha/strategies.py
- main
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- RahaDetector
- pandas
- perturb_spelling
- real_world_gov benchmark results
- conftest.py
- enums.py
- `auto_validate`
- InsufficientDataError
- ValidationError
- list_algorithms
- CHANGELOG
- algorithms/raha.md
- .detect
- ErrorDetectionAlgorithm
- docs/index.md
- Benchmark: real_world_gov
- _build_index
- argparse
- raha/detector.py
- CellResult
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- algorithms/index.md
- Benchmarks
- select_fd_column_pairs
- score
- algorithms/uni-detect.md
- CorpusStatsStore
- detectors/base.py
- TestAttempt
- confusion_metrics
- .detect
- pipeline.py
- Uni-Detect
- Raha
- Auto-Validate
- _require_columns
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- Current Status: BLOCKED
- clean_column
- wiki_subset/generate_report.py
- open_detect/__init__.py
- bucket_by_edges
- test_corpus_ingestion.py
- open-detect
- get_algorithm
- FeatureBucket
- HeuristicLabeler
- log_transform_fits_better
- Current Status: BLOCKED
- infer_column_data_type
- TestConfigThreshold
- _score_single_column
- DataQualityError
- API reference
- Running on Databricks
- is_float_like
- `raha`
- indexable_values
- Choosing an algorithm
- OpenDetectError

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 115 edges
2. `ErrorType` - 85 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 45 edges
6. `UnityCatalogLocation` - 39 edges
7. `UniDetect` - 38 edges
8. `AutoValidateAlgorithm` - 36 edges
9. `ConfigurationError` - 36 edges
10. `RahaConfig` - 33 edges

## Surprising Connections (you probably didn't know these)
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `As a plugin package (no changes to `open-detect`)` --references--> `list_algorithms()`  [INFERRED]
  docs/guides/writing-an-algorithm.md → src/open_detect/algorithms/registry.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (104 total, 21 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.19
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.12
Nodes (11): comparison_table_markdown(), git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main() (+3 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 8 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (14): Variants, _clean(), fmdv(), fmdv_h(), min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_vh() (+6 more)

### Community 9 - "UniDetect"
Cohesion: 0.25
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.18
Nodes (7): compute(), _score_fd_pair(), compute(), compute(), FailureCounts, compute(), TestPerElementFunctions

### Community 12 - "CorpusIngestor"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 13 - "fmdv_v"
Cohesion: 0.08
Nodes (11): _coarse_signature(), fmdv_v(), _infer_cmp(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV (+3 more)

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (11): AutoValidateConfig, build_pattern_index(), _iter_corpus_columns(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (9): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 20 - "matches"
Cohesion: 0.17
Nodes (5): matches(), fpr_column(), impurity(), matching_pattern(), TestMatching

### Community 21 - "hierarchy.py"
Cohesion: 0.06
Nodes (22): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), _parse() (+14 more)

### Community 22 - "real_world_gov/generate_report.py"
Cohesion: 0.16
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main() (+5 more)

### Community 23 - "get_spec"
Cohesion: 0.10
Nodes (7): compute(), _score_pair(), _score_column(), compute(), get_spec(), TestScoreFdPair, TestGetSpec

### Community 24 - "test_metrics.py"
Cohesion: 0.16
Nodes (6): uniqueness_ratio(), _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking, TestUniquenessRatio

### Community 25 - "open_detect/exceptions.py"
Cohesion: 0.07
Nodes (6): list_tables(), table_exists(), TestListTables, TestTableExists, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 26 - "builder.py"
Cohesion: 0.09
Nodes (7): _require_min_rows(), configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.17
Nodes (5): _validate_edges(), main(), ConfigurationError, test_main_installs_logging(), TestMain

### Community 29 - "ErrorType"
Cohesion: 0.13
Nodes (7): list_tables_matching(), parse_args(), _run(), ErrorType, TestParseArgs, TestListTablesMatching, fake_sql()

### Community 30 - "AlgorithmResult"
Cohesion: 0.17
Nodes (3): Combine, AlgorithmResult, TestAlgorithmResult

### Community 31 - "numpy"
Cohesion: 0.14
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (10): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies (+2 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (26): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+18 more)

### Community 38 - "RahaDetector"
Cohesion: 0.31
Nodes (5): RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 39 - "pandas"
Cohesion: 0.15
Nodes (8): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.21
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 44 - "enums.py"
Cohesion: 0.08
Nodes (13): _score_column(), bucket_row_count(), bucket_token_length(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket(), all_specs() (+5 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "InsufficientDataError"
Cohesion: 0.17
Nodes (8): require_min_size(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance(), InsufficientDataError

### Community 47 - "ValidationError"
Cohesion: 0.15
Nodes (5): fd_compliance_ratio(), FDResult, minority_violation_rows(), ValidationError, TestFunctionalDependency

### Community 48 - "list_algorithms"
Cohesion: 0.12
Nodes (12): get_algorithm_class(), list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), test_builtin_algorithms_are_registered(), test_register_lazy_is_lazy() (+4 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.10
Nodes (20): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+12 more)

### Community 50 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (11): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+3 more)

### Community 53 - "docs/index.md"
Cohesion: 0.29
Nodes (3): open-detect, What is in the box, Why a common interface

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.17
Nodes (10): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark, Which 5 datasets, and why (+2 more)

### Community 55 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "raha/detector.py"
Cohesion: 0.07
Nodes (21): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results (+13 more)

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 63 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "score"
Cohesion: 0.12
Nodes (16): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat (+8 more)

### Community 67 - "CorpusStatsStore"
Cohesion: 0.14
Nodes (4): CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "detectors/base.py"
Cohesion: 0.15
Nodes (5): _hash_value(), make_evidence_json(), redact_evidence(), FailureTracker, TestRedactEvidence

### Community 70 - "confusion_metrics"
Cohesion: 0.18
Nodes (5): confusion_metrics(), run_auto_validate(), _metrics(), run_raha(), _metrics()

### Community 71 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 72 - "pipeline.py"
Cohesion: 0.11
Nodes (7): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, get_spark(), TestGetSpark

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.29
Nodes (11): _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart(), render_markdown() (+3 more)

### Community 84 - "open_detect/__init__.py"
Cohesion: 0.20
Nodes (3): __getattr__(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 85 - "bucket_by_edges"
Cohesion: 0.19
Nodes (4): bucket_by_edges(), bucket_leftness(), bucket_token_prevalence(), TestBucketing

### Community 88 - "get_algorithm"
Cohesion: 0.20
Nodes (7): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 89 - "FeatureBucket"
Cohesion: 0.10
Nodes (11): Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, TestCandidate, TestCorpusRecords (+3 more)

### Community 90 - "HeuristicLabeler"
Cohesion: 0.29
Nodes (4): ColumnFeatures, HeuristicLabeler, _resolve_position(), TestHeuristicLabeler

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.08
Nodes (10): token_prevalence(), infer_column_data_type(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence, TestIntegerLike (+2 more)

### Community 95 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 96 - "DataQualityError"
Cohesion: 0.25
Nodes (7): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, DataQualityError

### Community 97 - "API reference"
Cohesion: 0.25
Nodes (4): Registry, Registry and results, Result types, API reference

### Community 98 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 100 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 102 - "Choosing an algorithm"
Cohesion: 0.67
Nodes (3): At a glance, Choosing an algorithm, Rules of thumb

### Community 103 - "OpenDetectError"
Cohesion: 0.12
Nodes (15): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Errors, IndexNotBuiltError, OpenDetectError (+7 more)

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 616 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `wiki_subset/run_benchmark.py`, `UniDetect`, `FailureCounts`, `_StubDetector`, `get_spec`, `open_detect/exceptions.py`, `builder.py`, `ConfigurationError`, `main`, `real_world_gov/run_benchmark.py`, `enums.py`, `ErrorDetectionAlgorithm`, `CorpusStatsStore`, `detectors/base.py`, `.detect`, `pipeline.py`, `CorpusStatsBuilder`, `open_detect/__init__.py`, `FeatureBucket`, `_score_single_column`, `DataQualityError`, `API reference`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11095305832147938 - nodes in this community are weakly interconnected._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `verify_build_config`, `test_spelling_detector.py`, `wiki_subset/run_benchmark.py`, `UniDetect`, `FailureCounts`, `get_spec`, `open_detect/exceptions.py`, `builder.py`, `perturb_numeric_outlier`, `ConfigurationError`, `ErrorType`, `main`, `real_world_gov/run_benchmark.py`, `enums.py`, `CHANGELOG`, `ErrorDetectionAlgorithm`, `Benchmark: real_world_gov`, `CorpusStatsStore`, `detectors/base.py`, `.detect`, `pipeline.py`, `CorpusStatsBuilder`, `UnityCatalogLocation`, `open_detect/__init__.py`, `TestConfigThreshold`, `_score_single_column`, `DataQualityError`, `API reference`, `OpenDetectError`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._