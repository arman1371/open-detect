# Graph Report - open-detect  (2026-10-20)

## Corpus Check
- 164 files · ~131,912 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 2031 nodes · 4935 edges · 102 communities (76 shown, 26 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 620 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `eea92960`
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
- fd_compliance_ratio
- auto_validate/detector.py
- CallableLabeler
- FailureCounts
- numpy
- UniDetect
- test_auto_validate_fmdv_v.py
- collections_abc
- AutoValidateConfig
- check_drift
- RahaConfig
- fd_violation_strategies
- registry.py
- hierarchy.py
- patterns.py
- real_world_gov/generate_report.py
- make_evidence_json
- check_failure_threshold
- json
- uni_detect/config.py
- perturb_numeric_outlier
- ConfigurationError
- dataset_utils.py
- AlgorithmResult
- .detect
- gaussian_outlier_strategies
- main
- pytest
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- UnknownAlgorithmError
- pandas
- warnings
- real_world_gov benchmark results
- conftest.py
- list_algorithms
- featurization.py
- `raha`
- tokenize
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- min_pairwise_edit_distance
- algorithms/raha.md
- propagate_labels
- ErrorDetectionAlgorithm
- FeatureBucket
- Benchmark: real_world_gov
- fmdv
- argparse
- raha/detector.py
- CellResult
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- algorithms/index.md
- Benchmarks
- select_fd_column_pairs
- test_corpus_ingestion.py
- docs/index.md
- CorpusStatsStore
- builder.py
- _score_single_column
- infer_column_data_type
- test_package_init.py
- ErrorType
- Uni-Detect
- TestAttempt
- Auto-Validate
- test_console_scripts.py
- Commit conventions and releases
- auto_validate/metrics.py
- UnityCatalogLocation
- Current Status: BLOCKED
- clean_column
- wiki_subset/generate_report.py
- uni_detect/core/models.py
- Detection
- log_transform_fits_better
- open-detect
- algorithms/uni-detect.md
- Running on Databricks
- HeuristicLabeler
- is_integer_like
- Current Status: BLOCKED
- uni_detect/text_utils.py
- TestConfigThreshold
- `auto_validate`
- indexable_values
- reference/index.md
- open_detect/__init__.py
- uni_detect/core/enums.py
- detectors/base.py

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 115 edges
2. `ErrorType` - 85 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 45 edges
6. `UnityCatalogLocation` - 39 edges
7. `UniDetect` - 38 edges
8. `ConfigurationError` - 36 edges
9. `AutoValidateAlgorithm` - 35 edges
10. `RahaConfig` - 34 edges

## Surprising Connections (you probably didn't know these)
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `Writing a class` --references--> `Labeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (102 total, 26 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.10
Nodes (15): _build_row(), _drop_nulls(), _original_row_ids(), perturb_spelling(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions() (+7 more)

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.13
Nodes (10): git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "fd_compliance_ratio"
Cohesion: 0.09
Nodes (11): fd_compliance_ratio(), minority_violation_rows(), uniqueness_ratio(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestFunctionalDependency (+3 more)

### Community 8 - "auto_validate/detector.py"
Cohesion: 0.09
Nodes (11): InferredPattern, _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_v(), fmdv_vh(), _infer_cmp(), _segment_dp() (+3 more)

### Community 9 - "CallableLabeler"
Cohesion: 0.10
Nodes (13): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust (+5 more)

### Community 10 - "FailureCounts"
Cohesion: 0.16
Nodes (7): compute(), compute(), _score_fd_pair(), compute(), FailureCounts, compute(), TestPerElementFunctions

### Community 11 - "numpy"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 12 - "UniDetect"
Cohesion: 0.06
Nodes (20): Methodology: uni_detect -- mapping real dirty data onto its four error types, build_spark(), main(), CorpusStatsBuilder, _stats_schema_without_error_type(), CorpusIngestor, UniDetect, config() (+12 more)

### Community 13 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.10
Nodes (10): min_conforming(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV, TestFmdvVh, TestLargeGroups (+2 more)

### Community 14 - "collections_abc"
Cohesion: 0.06
Nodes (21): _score_column(), build_outlier_bucket(), drop_nulls(), require_min_size(), FDResult, mad_scores(), MADResult, max_mad() (+13 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "check_drift"
Cohesion: 0.10
Nodes (7): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 19 - "registry.py"
Cohesion: 0.15
Nodes (9): _constant_factory(), get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name() (+1 more)

### Community 20 - "hierarchy.py"
Cohesion: 0.09
Nodes (15): _conforms(), _append_literal(), _char_class(), _class_of_token(), generalize(), _is_numeric(), _iter_runs(), matches() (+7 more)

### Community 21 - "patterns.py"
Cohesion: 0.09
Nodes (12): generality_weight(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns(), matching_pattern() (+4 more)

### Community 22 - "real_world_gov/generate_report.py"
Cohesion: 0.17
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main() (+5 more)

### Community 23 - "make_evidence_json"
Cohesion: 0.07
Nodes (11): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), _score_column(), compute(), finite_floats() (+3 more)

### Community 26 - "uni_detect/config.py"
Cohesion: 0.08
Nodes (13): list_tables(), list_tables_matching(), table_exists(), main(), parse_args(), _run(), test_main_installs_logging(), TestMain (+5 more)

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.24
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 29 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.25
Nodes (9): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only(), test_module_shims_are_identity_preserving(), test_old_except_clause_catches_new_error() (+1 more)

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (13): confusion_metrics(), _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate(), run_raha() (+5 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (26): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+18 more)

### Community 38 - "UnknownAlgorithmError"
Cohesion: 0.11
Nodes (17): Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema (+9 more)

### Community 39 - "pandas"
Cohesion: 0.13
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.20
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "list_algorithms"
Cohesion: 0.12
Nodes (13): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+5 more)

### Community 44 - "featurization.py"
Cohesion: 0.13
Nodes (9): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_spelling_bucket(), build_uniqueness_bucket(), TestBucketing (+1 more)

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (9): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_get_algorithm_constructs_with_args(), TestPluginDiscovery, worker() (+1 more)

### Community 49 - "min_pairwise_edit_distance"
Cohesion: 0.05
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+20 more)

### Community 50 - "algorithms/raha.md"
Cohesion: 0.33
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (9): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), UniDetectAlgorithm, __getattr__(), _config(), _row() (+1 more)

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.29
Nodes (7): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Which 5 datasets, and why

### Community 55 - "fmdv"
Cohesion: 0.09
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "raha/detector.py"
Cohesion: 0.10
Nodes (12): Scoring raha, main(), RahaDetector, GroundTruthLabeler, Labeler, _resolve_position(), _values_equal(), test_empty_dataframe_returns_no_cells() (+4 more)

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 63 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 66 - "docs/index.md"
Cohesion: 0.19
Nodes (6): At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box, Why a common interface

### Community 67 - "CorpusStatsStore"
Cohesion: 0.12
Nodes (5): CorpusStatsStore, CorpusNotFoundError, config(), TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "builder.py"
Cohesion: 0.15
Nodes (3): _require_min_rows(), InsufficientDataError, FailureTracker

### Community 71 - "test_package_init.py"
Cohesion: 0.22
Nodes (3): test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 72 - "ErrorType"
Cohesion: 0.11
Nodes (11): ErrorType, BaseDetector, FunctionalDependencyDetector, _score_pair(), NumericOutlierDetector, _score_column(), SpellingDetector, UniquenessDetector (+3 more)

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 76 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.16
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.23
Nodes (12): comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart() (+4 more)

### Community 84 - "uni_detect/core/models.py"
Cohesion: 0.16
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 88 - "algorithms/uni-detect.md"
Cohesion: 0.24
Nodes (4): Getting started, Installation, Installing from source, Pick your extra

### Community 89 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - "HeuristicLabeler"
Cohesion: 0.18
Nodes (11): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions? (+3 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "uni_detect/text_utils.py"
Cohesion: 0.17
Nodes (4): is_float_like(), is_mixed_alphanumeric(), TestFloatLike, TestMixedAlphanumeric

### Community 95 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 97 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 103 - "open_detect/__init__.py"
Cohesion: 0.09
Nodes (18): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, Errors, DataQualityError (+10 more)

### Community 109 - "uni_detect/core/enums.py"
Cohesion: 0.12
Nodes (7): ComparisonDirection, all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 110 - "detectors/base.py"
Cohesion: 0.10
Nodes (6): configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 634 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `wiki_subset/run_benchmark.py`, `FailureCounts`, `UniDetect`, `collections_abc`, `make_evidence_json`, `json`, `uni_detect/config.py`, `main`, `real_world_gov/run_benchmark.py`, `list_algorithms`, `featurization.py`, `ErrorDetectionAlgorithm`, `FeatureBucket`, `CorpusStatsStore`, `builder.py`, `_score_single_column`, `uni_detect/core/models.py`, `Detection`, `open_detect/__init__.py`, `uni_detect/core/enums.py`, `detectors/base.py`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11095305832147938 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `UnknownAlgorithmError`, `auto_validate/detector.py`, `list_algorithms`, `test_auto_validate_fmdv_v.py`, `check_drift`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._