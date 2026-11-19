# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-19)

## Corpus Check
- 199 files · ~165,884 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3151 nodes · 6834 edges · 168 communities (139 shown, 29 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 880 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ece396c8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_bench_snapshot.py
- UnknownAlgorithmError
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- pytest
- README.md — Uni-Detect overview
- PRD: Teams Notification Trigger for Scan Context
- FailureCounts
- PRD: User Feedback Tooltips
- TeamsNotifier
- new_cluster
- fmdv_v
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- test_algorithms_registry.py
- perturbation.py
- auto_validate/detector.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- make_evidence_json
- UnityCatalogLocation
- ErrorDetectionAlgorithm
- _ensure_sequence_of_str
- UniDetectConfig
- cluster_column
- warnings
- gaussian_outlier_strategies
- main
- ScoringJobCounter
- algorithms/uni-detect.md
- build_column_features
- build_metadata.py
- collections_abc
- metrics/functional_dependency.py
- real_world_gov benchmark results
- .detect
- test_build_corpus_statistics.py
- get_notification_config
- Benchmark: WIKI subset
- GroundTruthLabeler
- select_fd_column_pairs
- KnownIndexLabeler
- CHANGELOG
- PatternIndex
- Running on Databricks
- spark_session.py
- wiki_subset/generate_report.py
- TestConfigThreshold
- fmdv.py
- updates
- Scoring auto_validate
- jobs
- .build_corpus_statistics
- featurization.py
- _coerce_numeric
- build
- uses
- wiki_subset/run_benchmark.py
- env
- confusion_metrics
- .batch_score
- dry_run
- _score_single_column
- MetricObservation
- CorpusIngestor
- variables
- dataset_utils.py
- PRD: API Validation Framework for open-detect
- dev
- clean_column
- Commit conventions and releases
- labeling.py
- ErrorType
- Current Status: BLOCKED
- _aggregate_scored_rows
- _config
- 7.2 Key Features
- test
- test_bench_snapshot.py
- release.yml
- release
- test_raha_strategies.py
- log_transform_fits_better
- pypi
- Current Status: BLOCKED
- config
- get_algorithm_class
- with
- on
- FailureCountsAccumulatorParam
- steps
- argparse
- CallableLabeler
- _segment_dp
- 7.2 Key Features
- score
- sonarqube
- __getattr__
- infer_column_data_type
- docs
- force
- test_cache_lifecycle.py
- ConfigurationError
- _check_expected_type
- bucket_by_edges
- test_deprecated_shims.py
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_package_init.py
- uni_detect/core/models.py
- .detect
- Raha
- FeatureBucket
- AutoValidateAlgorithm
- Auto-Validate
- paperclip-issue-update.sh
- CellResult
- Auto-Validate
- open_detect_wheel
- _make_tooltip
- ValidationError
- _FakeDetector
- _fmdv_h_single
- _value_matches
- Detection
- uniqueness_ratio
- Uni-Detect
- FakeConf
- sys
- algorithms/index.md
- CorpusStatsBuilder
- 1. Implement `ErrorDetectionAlgorithm`
- duplicate_value_indices
- Methodology: auto_validate
- SparkUnavailableContext
- _StubDetector
- finite_floats
- `uni_detect`
- `raha`
- Raha
- Registry and results
- _value_matches_groups
- _detector
- test_metrics.py
- TestScopedConf
- pipeline.py
- hierarchy.py
- perturb_numeric_outlier
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- real_world_gov/run_benchmark.py
- RahaConfig
- wiki_subset/generate_report.py
- Performance Baseline — OPE-87
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 99 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 73 edges
5. `FailureCounts` - 56 edges
6. `ValidationError` - 48 edges
7. `UnityCatalogLocation` - 47 edges
8. `build_pattern_index()` - 46 edges
9. `AutoValidateAlgorithm` - 39 edges
10. `CellResult` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Bug Fixes` --references--> `_value_matches()`  [INFERRED]
  RELEASE-NOTES-OPE-162.md → src/open_detect/algorithms/auto_validate/detector.py
- `Phase 1: Core Tooltip Engine (4 weeks)` --references--> `CellResult`  [INFERRED]
  PRD-user-feedback-tooltips.md → src/open_detect/algorithms/base.py
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `3.1 Context` --references--> `AlgorithmResult`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (168 total, 29 thin omitted)

### Community 0 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 1 - "UnknownAlgorithmError"
Cohesion: 0.29
Nodes (6): Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema, UnknownAlgorithmError

### Community 2 - "pandas"
Cohesion: 0.10
Nodes (20): _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), _detect(), _detector(), _make_tiny_corpus() (+12 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "pytest"
Cohesion: 0.05
Nodes (19): Errors, ColumnDataType, ComparisonDirection, _require_min_rows(), CorpusNotFoundError, DataQualityError, InsufficientDataError, UnityCatalogError (+11 more)

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "PRD: Teams Notification Trigger for Scan Context"
Cohesion: 0.07
Nodes (27): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segment(s), 6. Value Proposition(s), 7.1 UX/Prototypes, 7.2 Key Features (+19 more)

### Community 10 - "FailureCounts"
Cohesion: 0.13
Nodes (7): compute(), _score_fd_pair(), FailureCounts, compute(), _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.11
Nodes (17): 1. Summary, 2. Contacts, 4. Objective, 5. Market Segments, 6. Value Propositions, 8. Release, Benefits, Competitive Advantages (+9 more)

### Community 12 - "TeamsNotifier"
Cohesion: 0.06
Nodes (9): Review Findings, TeamsNotificationError, TeamsNotifier, TestBuildMessage, TestCheckRateLimit, TestSend, TestSendSafe, TestSeverityOrdering (+1 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "fmdv_v"
Cohesion: 0.10
Nodes (10): Variants, Recent Changes, _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV (+2 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _date_index(), _date_values(), TestLargeGroups, TestCorpusInputShapes (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.10
Nodes (8): _infer_pattern_to_groups(), check_drift(), _clean_series(), _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.10
Nodes (15): _build_row(), _drop_nulls(), _original_row_ids(), _score_column(), compute(), _positions_of(), _row(), _score() (+7 more)

### Community 18 - "test_algorithms_registry.py"
Cohesion: 0.11
Nodes (11): list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered(), test_register_lazy_is_lazy() (+3 more)

### Community 19 - "perturbation.py"
Cohesion: 0.09
Nodes (9): require_min_size(), _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbSpelling (+1 more)

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (17): _feasible_evidence(), _infeasible_evidence(), _matches_segments(), _conforms(), _conforms_segments(), DriftResult, _append_literal(), _char_class() (+9 more)

### Community 21 - "permissions"
Cohesion: 0.07
Nodes (28): if, permissions, runs-on, steps, types, types, jobs, claude (+20 more)

### Community 22 - "with"
Cohesion: 0.09
Nodes (26): UV_PYTHON, jobs, real-world-gov, wiki-subset, name, on, workflow_dispatch, env (+18 more)

### Community 23 - "update-graph"
Cohesion: 0.08
Nodes (24): concurrency, cancel-in-progress, group, jobs, update-graph, name, on, push (+16 more)

### Community 25 - "with"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "make_evidence_json"
Cohesion: 0.10
Nodes (10): _hash_value(), make_evidence_json(), redact_evidence(), compute(), _score_pair(), compute(), _score_column(), _score_column() (+2 more)

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.11
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 28 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (14): API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, _constant_factory(), _load_entry_points() (+6 more)

### Community 30 - "UniDetectConfig"
Cohesion: 0.15
Nodes (3): UniDetectConfig, config(), TestUniDetectConfig

### Community 31 - "cluster_column"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "warnings"
Cohesion: 0.15
Nodes (3): __getattr__(), __getattr__(), test_old_except_clause_catches_new_error()

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.08
Nodes (12): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestEmptyFrames, TestGaussianOutlierStrategies (+4 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 36 - "algorithms/uni-detect.md"
Cohesion: 0.14
Nodes (11): Benchmarks, How to read them, Latest results, Running them, Getting started, Installation, Installing from source, Pick your extra (+3 more)

### Community 37 - "build_column_features"
Cohesion: 0.14
Nodes (9): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features() (+1 more)

### Community 38 - "build_metadata.py"
Cohesion: 0.09
Nodes (14): _validate_edges(), diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), ConfigurationError, _config() (+6 more)

### Community 39 - "collections_abc"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 40 - "metrics/functional_dependency.py"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 44 - "get_notification_config"
Cohesion: 0.08
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.18
Nodes (8): GroundTruthLabeler, _values_equal(), test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler(), TestGroundTruthLabeler

### Community 47 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 48 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "PatternIndex"
Cohesion: 0.09
Nodes (6): indexable_values(), PatternIndex, _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestEquivalenceToReferenceBuild, TestIndexableValues

### Community 51 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 52 - "spark_session.py"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 53 - "wiki_subset/generate_report.py"
Cohesion: 0.14
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 55 - "fmdv.py"
Cohesion: 0.11
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.10
Nodes (8): build_spark(), main(), _filter_by_column_type(), _require_columns(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates, TestRequireColumns

### Community 60 - "featurization.py"
Cohesion: 0.18
Nodes (8): bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket(), TestFeatureBucketBuilders

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "wiki_subset/run_benchmark.py"
Cohesion: 0.13
Nodes (11): git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), _print_comparison(), run(), run_auto_validate(), _metrics() (+3 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "confusion_metrics"
Cohesion: 0.13
Nodes (11): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+3 more)

### Community 67 - ".batch_score"
Cohesion: 0.12
Nodes (4): CorpusStatsStore, TestBatchScoreOptimization, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "MetricObservation"
Cohesion: 0.29
Nodes (4): Candidate, MetricObservation, TestCandidate, TestMetricObservation

### Community 71 - "CorpusIngestor"
Cohesion: 0.11
Nodes (6): balanced_union(), CorpusIngestor, compute_token_counts(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.09
Nodes (21): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+13 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "labeling.py"
Cohesion: 0.15
Nodes (6): Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, Labeler, _resolve_position(), TestHeuristicLabeler

### Community 79 - "ErrorType"
Cohesion: 0.08
Nodes (12): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, all_specs() (+4 more)

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.17
Nodes (4): _aggregate_scored_rows(), compute(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "_config"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "7.2 Key Features"
Cohesion: 0.10
Nodes (14): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+6 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "test_bench_snapshot.py"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "test_raha_strategies.py"
Cohesion: 0.17
Nodes (11): fd_violation_strategies(), _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column() (+3 more)

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 94 - "get_algorithm_class"
Cohesion: 0.15
Nodes (6): Check it works, get_algorithm(), get_algorithm_class(), test_get_algorithm_constructs_with_args(), test_unknown_algorithm_raises(), TestPluginDiscoveryViaRealDistInfo

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.46
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.10
Nodes (15): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust (+7 more)

### Community 101 - "_segment_dp"
Cohesion: 0.11
Nodes (13): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary (+5 more)

### Community 102 - "7.2 Key Features"
Cohesion: 0.13
Nodes (15): 7.1 UX / Prototypes, 7.2 Key Features, 7.3 Technology, 7.4 Assumptions, 7. Solution, Backend Changes, F1: Pattern-to-Language Translation, F2: Contextual Suggestion Engine (+7 more)

### Community 103 - "score"
Cohesion: 0.12
Nodes (14): Reading the detections, Through the registry, Usage on Databricks, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat (+6 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "test_cache_lifecycle.py"
Cohesion: 0.14
Nodes (3): _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSpark

### Community 110 - "ConfigurationError"
Cohesion: 0.12
Nodes (9): list_tables_matching(), main(), parse_args(), _run(), test_main_installs_logging(), TestMain, TestParseArgs, TestListTablesMatching (+1 more)

### Community 111 - "_check_expected_type"
Cohesion: 0.14
Nodes (10): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status (+2 more)

### Community 112 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 113 - "test_deprecated_shims.py"
Cohesion: 0.21
Nodes (8): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only(), test_module_shims_are_identity_preserving(), test_unknown_exception_attr_raises()

### Community 115 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "uni_detect/core/models.py"
Cohesion: 0.24
Nodes (3): CorpusColumnRecord, CorpusPairRecord, TestCorpusRecords

### Community 118 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 119 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 122 - "Auto-Validate"
Cohesion: 0.17
Nodes (10): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+2 more)

### Community 126 - "CellResult"
Cohesion: 0.11
Nodes (7): open-detect, What is in the box, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 127 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 128 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 129 - "_make_tooltip"
Cohesion: 0.22
Nodes (5): _build_suggestion(), _make_tooltip(), _tooltip_content(), pattern_to_language(), TooltipContent

### Community 131 - "ValidationError"
Cohesion: 0.07
Nodes (18): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, Appendix: Validation Function Reference, _check_columns_present(), ValidationError (+10 more)

### Community 133 - "_fmdv_h_single"
Cohesion: 0.25
Nodes (4): min_conforming(), _fmdv_h_single(), _segment_fmdv_vh(), TestMinConforming

### Community 134 - "_value_matches"
Cohesion: 0.10
Nodes (18): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+10 more)

### Community 137 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 140 - "algorithms/index.md"
Cohesion: 0.20
Nodes (3): Algorithms, Fidelity to the papers, Errors

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.17
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 142 - "1. Implement `ErrorDetectionAlgorithm`"
Cohesion: 0.33
Nodes (6): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm

### Community 144 - "Methodology: auto_validate"
Cohesion: 0.50
Nodes (4): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override

### Community 148 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 149 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 150 - "Raha"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 151 - "Registry and results"
Cohesion: 0.67
Nodes (3): Registry, Registry and results, Result types

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 426 - "pipeline.py"
Cohesion: 0.06
Nodes (12): list_tables(), table_exists(), get_spark(), scoped_conf(), configure_logging(), get_logger(), log_duration(), TestListTables (+4 more)

### Community 530 - "hierarchy.py"
Cohesion: 0.06
Nodes (18): generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize(), _alternatives(), any_pattern() (+10 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.24
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.09
Nodes (14): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), main(), _print_comparison(), _register_table() (+6 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.29
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1430 - "conftest.py"
Cohesion: 0.11
Nodes (13): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect, _cap_driver_memory() (+5 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1173 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **29 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `wiki_subset/run_benchmark.py`, `UnknownAlgorithmError`, `_make_tooltip`, `real_world_gov/run_benchmark.py`, `_fmdv_h_single`, `build_metadata.py`, `_segment_dp`, `fmdv_v`, `InferredPattern`, `PatternIndex`, `auto_validate/detector.py`, `fmdv.py`, `AutoValidateAlgorithm`, `ErrorDetectionAlgorithm`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `pandas` be split into smaller, more focused modules?**
  _Cohesion score 0.09957325746799431 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `_FakeDetector`, `pytest`, `Detection`, `FailureCounts`, `CorpusStatsBuilder`, `_StubDetector`, `conftest.py`, `UnityCatalogLocation`, `ErrorDetectionAlgorithm`, `main`, `build_metadata.py`, `pipeline.py`, `test_build_corpus_statistics.py`, `.build_corpus_statistics`, `featurization.py`, `wiki_subset/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `.batch_score`, `_score_single_column`, `MetricObservation`, `_config`, `test_cache_lifecycle.py`, `ConfigurationError`, `uni_detect/core/models.py`, `.detect`, `FeatureBucket`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._