# Graph Report - open-detect  (2026-11-05)

## Corpus Check
- 181 files · ~135,678 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 227, (none) 2, .properties 1)
- WARNING: 232 of 439 files seen (53%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2487 nodes · 5580 edges · 133 communities (110 shown, 23 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 679 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4b69700c`
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
- auto_validate/detector.py
- algorithms/uni-detect.md
- FailureCounts
- fd_violation_strategies
- uni_detect/text_utils.py
- new_cluster
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- pandas
- list_algorithms
- hierarchy.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- list_tables_matching
- perturb_numeric_outlier
- ConfigurationError
- real_world_gov/run_benchmark.py
- AlgorithmResult
- .detect
- get_algorithm_class
- gaussian_outlier_strategies
- main
- pytest
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- concepts.md
- numpy
- warnings
- real_world_gov benchmark results
- spark_session.py
- score
- build_uniqueness_bucket
- `auto_validate`
- ErrorDetectionAlgorithm
- FailureCountsAccumulatorParam
- fresh_registry
- CHANGELOG
- builder.py
- CallableLabeler
- .detect
- open_detect/__init__.py
- confusion_metrics
- fmdv
- updates
- labeling.py
- jobs
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- build
- uses
- UniDetect
- env
- choosing-an-algorithm.md
- CorpusStatsStore
- dry_run
- _score_single_column
- FeatureBucket
- test_algorithms_registry.py
- variables
- Auto-Validate
- TestAttempt
- dev
- test_package_init.py
- Commit conventions and releases
- reference/index.md
- UnityCatalogLocation
- Current Status: BLOCKED
- clean_column
- wiki_subset/generate_report.py
- MetricObservation
- test
- ErrorType
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
- CellResult
- steps
- perturb_spelling
- propagate_labels
- Detection
- Uni-Detect
- OpenDetectError
- sonarqube
- open_detect_wheel
- docs
- force
- get_spec
- log_duration
- Registry and results
- table_exists
- open-detect
- test_metrics.py
- config
- _StubDetector
- SparkJobCounter
- detectors/base.py
- metrics/spelling.py
- index.py
- test_bench_snapshot.py
- perturbation.py
- snapshot.py
- _is_null
- min_pairwise_edit_distance
- parse_args
- main
- Auto-Validate
- Uni-Detect
- Performance Baseline — OPE-87
- uniqueness_ratio

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
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `As a plugin package (no changes to `open-detect`)` --references--> `list_algorithms()`  [INFERRED]
  docs/guides/writing-an-algorithm.md → src/open_detect/algorithms/registry.py
- `Operational notes` --references--> `CorpusNotFoundError`  [INFERRED]
  docs/algorithms/uni-detect.md → src/open_detect/algorithms/uni_detect/exceptions.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (133 total, 23 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

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
Cohesion: 0.14
Nodes (7): InsufficientDataError, require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), ValidationError, TestFunctionalDependency

### Community 8 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (19): Variants, _clean(), fmdv_h(), InferredPattern, min_conforming(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+11 more)

### Community 10 - "FailureCounts"
Cohesion: 0.18
Nodes (7): compute(), compute(), _score_fd_pair(), compute(), compute(), FailureCounts, TestPerElementFunctions

### Community 11 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (12): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _build_index(), TestFmdvV, TestFmdvVh, _time_corpus() (+4 more)

### Community 16 - "check_drift"
Cohesion: 0.12
Nodes (4): check_drift(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.14
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "pandas"
Cohesion: 0.13
Nodes (11): Scoring raha, build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype (+3 more)

### Community 19 - "list_algorithms"
Cohesion: 0.15
Nodes (10): Check it works, Installation, Installing from source, Pick your extra, _constant_factory(), list_algorithms(), _load_entry_points(), register_lazy() (+2 more)

### Community 20 - "hierarchy.py"
Cohesion: 0.05
Nodes (26): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches() (+18 more)

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
Cohesion: 0.21
Nodes (5): list_tables(), list_tables_matching(), TestListTables, TestListTablesMatching, fake_sql()

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 29 - "real_world_gov/run_benchmark.py"
Cohesion: 0.11
Nodes (14): git_commit(), spark_session(), SparkUnavailable, dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames() (+6 more)

### Community 30 - "AlgorithmResult"
Cohesion: 0.13
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Reading results, Uni-Detect: score tables in Unity Catalog, AlgorithmResult, _good_plugin_class(), detect(), TestAlgorithmResult

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "get_algorithm_class"
Cohesion: 0.15
Nodes (6): get_algorithm(), get_algorithm_class(), test_registered_under_raha(), test_get_algorithm_constructs_with_args(), test_unknown_algorithm_raises(), TestPluginDiscoveryViaRealDistInfo

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 34 - "main"
Cohesion: 0.11
Nodes (8): main(), parse_args(), get_spark(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs, TestGetSpark

### Community 35 - "pytest"
Cohesion: 0.25
Nodes (9): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only(), test_module_shims_are_identity_preserving(), test_old_except_clause_catches_new_error() (+1 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.09
Nodes (15): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, main(), main(), _build_config(), _load_corpus_tables() (+7 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.08
Nodes (11): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm (+3 more)

### Community 38 - "concepts.md"
Cohesion: 0.25
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 39 - "numpy"
Cohesion: 0.25
Nodes (9): _compact_dtype(), _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column() (+1 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "spark_session.py"
Cohesion: 0.13
Nodes (7): candidates(), main(), select(), _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "score"
Cohesion: 0.18
Nodes (11): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+3 more)

### Community 44 - "build_uniqueness_bucket"
Cohesion: 0.10
Nodes (10): compute(), _score_pair(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_uniqueness_bucket() (+2 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 46 - "ErrorDetectionAlgorithm"
Cohesion: 0.10
Nodes (14): API reference, main(), ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, register_algorithm() (+6 more)

### Community 48 - "fresh_registry"
Cohesion: 0.21
Nodes (4): _FakeEntryPoint, fresh_registry(), TestPluginDiscovery, worker()

### Community 49 - "CHANGELOG"
Cohesion: 0.10
Nodes (20): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+12 more)

### Community 51 - "CallableLabeler"
Cohesion: 0.24
Nodes (6): Raha: find errors with a few labels, The simplest labeler: a function, CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 52 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "open_detect/__init__.py"
Cohesion: 0.16
Nodes (6): ColumnDataType, ComparisonDirection, CorpusColumnRecord, CorpusPairRecord, __getattr__(), TestCorpusRecords

### Community 54 - "confusion_metrics"
Cohesion: 0.08
Nodes (20): confusion_metrics(), canonical_column(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate (+12 more)

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "labeling.py"
Cohesion: 0.09
Nodes (14): Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, Writing a class, ColumnFeatures, GroundTruthLabeler (+6 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.20
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "UniDetect"
Cohesion: 0.05
Nodes (22): build_spark(), main(), CorpusStatsBuilder, _stats_schema_without_error_type(), CorpusIngestor, select_fd_column_pairs(), __getattr__(), _run() (+14 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "choosing-an-algorithm.md"
Cohesion: 0.18
Nodes (8): Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "CorpusStatsStore"
Cohesion: 0.13
Nodes (4): CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 71 - "test_algorithms_registry.py"
Cohesion: 0.20
Nodes (4): real_plugin_path(), test_builtin_algorithms_are_registered(), test_register_lazy_is_lazy(), _write_distinfo_plugin()

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_package_init.py"
Cohesion: 0.16
Nodes (6): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.14
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "reference/index.md"
Cohesion: 0.20
Nodes (5): Errors, Configuration, Detector, Labelers, Raha

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.14
Nodes (22): grouped_bar_chart(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row() (+14 more)

### Community 84 - "MetricObservation"
Cohesion: 0.29
Nodes (4): Candidate, MetricObservation, TestCandidate, TestMetricObservation

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "ErrorType"
Cohesion: 0.12
Nodes (13): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, _score_column(), SpellingDetector, UniquenessDetector, bucket_token_length() (+5 more)

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
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

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

### Community 97 - "CellResult"
Cohesion: 0.17
Nodes (5): open-detect, What is in the box, Why a common interface, CellResult, TestCellResultEvidence

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 102 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 103 - "OpenDetectError"
Cohesion: 0.12
Nodes (14): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError (+6 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_spec"
Cohesion: 0.10
Nodes (7): _require_min_rows(), compute(), _score_column(), FailureTracker, get_spec(), TestScoreFdPair, TestGetSpec

### Community 110 - "log_duration"
Cohesion: 0.10
Nodes (4): log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 111 - "Registry and results"
Cohesion: 0.67
Nodes (3): Registry, Registry and results, Result types

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 268 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 297 - "SparkJobCounter"
Cohesion: 0.15
Nodes (9): ScopeStats, SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported() (+1 more)

### Community 458 - "detectors/base.py"
Cohesion: 0.16
Nodes (6): _hash_value(), make_evidence_json(), redact_evidence(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestRedactEvidence

### Community 527 - "metrics/spelling.py"
Cohesion: 0.24
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "index.py"
Cohesion: 0.07
Nodes (11): _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), indexable_values(), fpr_column(), impurity(), _date_index() (+3 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.18
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 639 - "perturbation.py"
Cohesion: 0.12
Nodes (9): _score_column(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency (+1 more)

### Community 667 - "snapshot.py"
Cohesion: 0.16
Nodes (10): _nice_ceiling(), _rounded_top_rect(), _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main() (+2 more)

### Community 697 - "_is_null"
Cohesion: 0.22
Nodes (5): _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 711 - "main"
Cohesion: 0.36
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 1123 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1159 - "Uni-Detect"
Cohesion: 0.40
Nodes (5): A fully local example, How it works, Install, Operational notes, Uni-Detect

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 876 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **23 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `Uni-Detect`, `FailureCounts`, `_StubDetector`, `real_world_gov/run_benchmark.py`, `main`, `wiki_subset/run_benchmark.py`, `build_uniqueness_bucket`, `ErrorDetectionAlgorithm`, `builder.py`, `.detect`, `open_detect/__init__.py`, `UniDetect`, `CorpusStatsStore`, `parse_args`, `_score_single_column`, `FeatureBucket`, `main`, `detectors/base.py`, `MetricObservation`, `Detection`, `get_spec`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11025641025641025 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `wiki_subset/run_benchmark.py`, `AutoValidateAlgorithm`, `OpenDetectError`, `auto_validate/detector.py`, `ErrorDetectionAlgorithm`, `check_drift`, `index.py`, `fmdv`, `_is_null`, `ConfigurationError`, `real_world_gov/run_benchmark.py`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._