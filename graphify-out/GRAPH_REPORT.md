# Graph Report - open-detect  (2026-11-05)

## Corpus Check
- 181 files · ~136,512 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 227, (none) 2, .properties 1)
- WARNING: 232 of 439 files seen (53%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2497 nodes · 5607 edges · 139 communities (115 shown, 24 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 683 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b74c0136`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- test_spelling_detector.py
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- InsufficientDataError
- PatternIndex
- algorithms/index.md
- FailureCounts
- fd_violation_strategies
- numpy
- new_cluster
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- pandas
- registry.py
- patterns.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- list_tables_matching
- perturb_numeric_outlier
- ConfigurationError
- dataset_utils.py
- CellResult
- .detect
- list_algorithms
- gaussian_outlier_strategies
- main
- pytest
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- Comparing algorithms
- test_raha_strategies.py
- warnings
- real_world_gov benchmark results
- conftest.py
- score
- featurization.py
- Benchmark: WIKI subset
- ErrorDetectionAlgorithm
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- builder.py
- test_auto_validate_fmdv_v.py
- algorithm.py
- ErrorType
- confusion_metrics
- fmdv
- updates
- Labeler
- jobs
- UniDetect
- README.md — Uni-Detect overview
- _coerce_numeric
- build
- uses
- CorpusStatsBuilder
- env
- docs/index.md
- CorpusStatsStore
- dry_run
- _score_single_column
- FeatureBucket
- CorpusIngestor
- variables
- Auto-Validate
- TestAttempt
- dev
- test_console_scripts.py
- Commit conventions and releases
- algorithms/raha.md
- UnityCatalogLocation
- Current Status: BLOCKED
- test_auto_validate_index.py
- wiki_subset/generate_report.py
- json
- test
- collections_abc
- release.yml
- release
- Running on Databricks
- Raha
- pypi
- Current Status: BLOCKED
- infer_column_data_type
- TestConfigThreshold
- with
- on
- profile.py
- steps
- perturb_spelling
- propagate_labels
- test_hygiene.py
- Uni-Detect
- OpenDetectError
- sonarqube
- algorithms/uni-detect.md
- docs
- force
- get_spec
- TestConfigureLogging
- reference/index.md
- select_fd_column_pairs
- open-detect
- argparse
- test_package_init.py
- _require_columns
- test_corpus_and_detectors.py
- `uni_detect`
- `raha`
- test_corpus_ingestion.py
- _default_classifier_factory
- __getattr__
- test_metrics.py
- config
- _StubDetector
- SparkJobCounter
- redact_evidence
- metrics/spelling.py
- hierarchy.py
- test_bench_snapshot.py
- perturbation.py
- snapshot.py
- min_pairwise_edit_distance
- main
- Auto-Validate
- Performance Baseline — OPE-87
- uniqueness_ratio

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 118 edges
2. `ErrorType` - 85 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 46 edges
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
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `Operational notes` --references--> `CorpusNotFoundError`  [INFERRED]
  docs/algorithms/uni-detect.md → src/open_detect/algorithms/uni_detect/exceptions.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (139 total, 24 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (11): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+3 more)

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.16
Nodes (11): _drop_nulls(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order() (+3 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "InsufficientDataError"
Cohesion: 0.13
Nodes (7): InsufficientDataError, require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), ValidationError, TestFunctionalDependency

### Community 8 - "PatternIndex"
Cohesion: 0.07
Nodes (16): Variants, _clean(), fmdv_h(), InferredPattern, min_conforming(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+8 more)

### Community 10 - "FailureCounts"
Cohesion: 0.20
Nodes (5): compute(), compute(), _score_fd_pair(), FailureCounts, TestPerElementFunctions

### Community 11 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 12 - "numpy"
Cohesion: 0.12
Nodes (5): ColumnFeatures, _compact_dtype(), HeuristicLabeler, _resolve_position(), TestHeuristicLabeler

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "check_drift"
Cohesion: 0.12
Nodes (4): check_drift(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (11): ColumnPredictions, train_and_predict(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler() (+3 more)

### Community 18 - "pandas"
Cohesion: 0.12
Nodes (11): main(), build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype (+3 more)

### Community 19 - "registry.py"
Cohesion: 0.16
Nodes (10): The registry, _constant_factory(), get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), UnknownAlgorithmError (+2 more)

### Community 20 - "patterns.py"
Cohesion: 0.07
Nodes (13): generality_weight(), generalize(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns() (+5 more)

### Community 21 - "permissions"
Cohesion: 0.07
Nodes (28): if, permissions, runs-on, steps, types, types, jobs, claude (+20 more)

### Community 22 - "with"
Cohesion: 0.09
Nodes (26): UV_PYTHON, jobs, real-world-gov, wiki-subset, name, on, workflow_dispatch, env (+18 more)

### Community 23 - "update-graph"
Cohesion: 0.08
Nodes (24): concurrency, cancel-in-progress, group, jobs, update-graph, name, on, push (+16 more)

### Community 24 - "check_failure_threshold"
Cohesion: 0.19
Nodes (4): Configuration, DataQualityError, check_failure_threshold(), TestCheckFailureThreshold

### Community 25 - "with"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 29 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 30 - "CellResult"
Cohesion: 0.11
Nodes (5): Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "list_algorithms"
Cohesion: 0.11
Nodes (12): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, get_algorithm() (+4 more)

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.27
Nodes (8): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only(), test_module_shims_are_identity_preserving(), test_unknown_exception_attr_raises()

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.09
Nodes (22): comparison_table_markdown(), maybe_scope(), require_uni_detect(), UniDetectProfile, git_commit(), spark_session(), SparkUnavailable, _build_config() (+14 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.07
Nodes (16): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm (+8 more)

### Community 38 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 39 - "test_raha_strategies.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 40 - "warnings"
Cohesion: 0.14
Nodes (3): __getattr__(), __getattr__(), test_old_except_clause_catches_new_error()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.14
Nodes (9): A fully local example, How it works, Install, Operational notes, Uni-Detect, _delta_jars(), _download(), spark() (+1 more)

### Community 43 - "score"
Cohesion: 0.25
Nodes (8): Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The shared result schema, score()

### Community 44 - "featurization.py"
Cohesion: 0.09
Nodes (13): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+5 more)

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "ErrorDetectionAlgorithm"
Cohesion: 0.23
Nodes (6): API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (9): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_unknown_algorithm_raises(), TestPluginDiscovery, worker() (+1 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.10
Nodes (20): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+12 more)

### Community 50 - "builder.py"
Cohesion: 0.07
Nodes (6): get_spark(), configure_logging(), get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 51 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.10
Nodes (9): _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV, TestFmdvVh, TestLargeGroups, TestMinConforming (+1 more)

### Community 52 - "algorithm.py"
Cohesion: 0.18
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "ErrorType"
Cohesion: 0.10
Nodes (14): ColumnDataType, ComparisonDirection, ErrorType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation (+6 more)

### Community 54 - "confusion_metrics"
Cohesion: 0.09
Nodes (16): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+8 more)

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Labeler"
Cohesion: 0.07
Nodes (23): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results (+15 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.21
Nodes (7): build_spark(), main(), _run(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.13
Nodes (15): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, artifacts, open_detect_wheel, bundle, name, build (+7 more)

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 67 - "CorpusStatsStore"
Cohesion: 0.13
Nodes (4): CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "test_auto_validate_index.py"
Cohesion: 0.10
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.22
Nodes (13): grouped_bar_chart(), comparison_charts(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row() (+5 more)

### Community 84 - "json"
Cohesion: 0.27
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "collections_abc"
Cohesion: 0.07
Nodes (17): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, compute(), _score_pair(), NumericOutlierDetector, compute(), _score_column() (+9 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 101 - "test_hygiene.py"
Cohesion: 0.17
Nodes (3): _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSpark

### Community 102 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 103 - "OpenDetectError"
Cohesion: 0.17
Nodes (9): Errors, IndexNotBuiltError, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error(), test_open_detect_error_is_catchable_broadly(), test_relocated_exceptions_importable_from_every_path() (+1 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_spec"
Cohesion: 0.12
Nodes (6): _require_min_rows(), all_specs(), get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 111 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 115 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 116 - "test_package_init.py"
Cohesion: 0.22
Nodes (3): test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 118 - "test_corpus_and_detectors.py"
Cohesion: 0.33
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 119 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 120 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 268 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 297 - "SparkJobCounter"
Cohesion: 0.15
Nodes (9): ScopeStats, SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported() (+1 more)

### Community 458 - "redact_evidence"
Cohesion: 0.24
Nodes (3): _hash_value(), redact_evidence(), TestRedactEvidence

### Community 527 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "hierarchy.py"
Cohesion: 0.07
Nodes (19): _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), _append_literal(), _char_class(), _class_of_token(), _is_numeric() (+11 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.18
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 639 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 667 - "snapshot.py"
Cohesion: 0.16
Nodes (10): _nice_ceiling(), _rounded_top_rect(), _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main() (+2 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 711 - "main"
Cohesion: 0.18
Nodes (5): main(), parse_args(), test_main_installs_logging(), TestMain, TestParseArgs

### Community 1123 - "Auto-Validate"
Cohesion: 0.22
Nodes (7): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly, Errors

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 880 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `PatternIndex`, `score`, `ErrorDetectionAlgorithm`, `check_drift`, `hierarchy.py`, `test_auto_validate_fmdv_v.py`, `test_auto_validate_index.py`, `confusion_metrics`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 35 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 35 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11411411411411411 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `FailureCounts`, `_StubDetector`, `main`, `real_world_gov/run_benchmark.py`, `conftest.py`, `featurization.py`, `ErrorDetectionAlgorithm`, `builder.py`, `algorithm.py`, `UniDetect`, `CorpusStatsBuilder`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `main`, `collections_abc`, `test_hygiene.py`, `get_spec`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._