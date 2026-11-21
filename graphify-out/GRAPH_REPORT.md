# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-21)

## Corpus Check
- 200 files · ~166,307 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3191 nodes · 6952 edges · 194 communities (139 shown, 55 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 916 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `06d42373`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AlgorithmResult
- pipeline.py
- test_ope86_distinct_verdicts.py
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- builder.py
- README.md — Uni-Detect overview
- run_raha
- FailureCounts
- PRD: User Feedback Tooltips
- FeatureBucket
- new_cluster
- AlgorithmResult
- AutoValidateConfig
- check_drift
- test_spelling_detector.py
- CellResult
- perturb_spelling
- test_auto_validate_fmdv_v.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- PatternIndex
- UniDetectConfig
- _reference_build_pattern_index
- ValidationError
- get_notification_config
- .detect
- pytest
- _score_single_column
- main
- ScoringJobCounter
- get_algorithm_class
- build_column_features
- FailureCountsAccumulatorParam
- _search_mpd
- fd_compliance_ratio
- real_world_gov benchmark results
- propagate_labels
- algorithms/index.md
- test_catalog.py
- `auto_validate`
- labeling.py
- Auto-Validate
- Benchmark: WIKI subset
- CHANGELOG
- ErrorDetectionAlgorithm
- index.py
- TestEdgeCases
- test_bench_snapshot.py
- uni_detect/text_utils.py
- index.py
- updates
- Raha
- jobs
- corpus_tables_by_category
- ErrorType
- _coerce_numeric
- build
- uses
- OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)
- env
- numpy
- CorpusStatsStore
- dry_run
- confusion_metrics
- ErrorType
- CorpusIngestor
- variables
- ._send_teams_notification_after_detection
- PRD: API Validation Framework for open-detect
- dev
- patch
- Commit conventions and releases
- HeuristicLabeler
- test_metrics.py
- Current Status: BLOCKED
- Review Complete: OPE-194 (PR #106)
- UniDetect
- numpy
- test
- hooks
- release.yml
- release
- TestConfigureLogging
- list_algorithms
- pypi
- Current Status: BLOCKED
- validation.py
- TeamsNotifier
- with
- on
- Appendix: Validation Function Reference
- steps
- argparse
- labeling.py
- _segment_dp
- ConfigurationError
- score
- sonarqube
- CellResult
- infer_column_data_type
- docs
- force
- Completed Work
- get_spec
- algorithms/uni-detect.md
- get_algorithm
- ErrorType
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_package_init.py
- Appendix: Validation Function Reference
- test_algorithms_registry.py
- _make_classifier
- score
- AutoValidateAlgorithm
- Benchmarks
- paperclip-issue-update.sh
- UniDetectProfile
- is_mixed_alphanumeric
- _FakeDetector
- 7.2 Key Features
- 8. Release
- ValidationError
- parse_args
- _check_columns_unique
- auto_validate/detector.py
- ScoringJobCounter
- drop_nulls
- KnownIndexLabeler
- TeamsNotificationError
- sys
- tokenize
- CorpusStatsBuilder
- ._build_affected_summary
- _check_unknown_kwargs
- .detect
- ._new_failure_tracker
- TestUniDetectDetect
- OPE-89: Fix Spark Cache Lifecycle in Uni-Detect
- test_teams.py
- _make_classifier
- _row
- TestAttempt
- .test_release_calls_detector_release
- auto_validate/metrics.py
- log_transform_fits_better
- _check_dataframe_is_spark
- FakeConf
- is_integer_like
- _check_columns_unique
- _reject_unknown_kwargs
- TestSeverityOrdering
- open_detect_wheel
- OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)
- parse_args
- duplicate_value_indices
- TestMatching
- Scoring auto_validate
- diff_fingerprints
- _stats_schema_without_error_type
- all_specs
- log_duration
- TestScoreFdPair
- _detector
- _random_words
- validation.py
- test_logging_utils.py
- collections_abc
- detectors/base.py
- hierarchy.py
- perturb_numeric_outlier
- collections_abc
- min_pairwise_edit_distance
- snapshot.py
- wiki_subset/run_benchmark.py
- RahaConfig
- wiki_subset/generate_report.py
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- spark_session.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 101 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 85 edges
5. `FailureCounts` - 56 edges
6. `TeamsNotifier` - 56 edges
7. `ValidationError` - 48 edges
8. `UnityCatalogLocation` - 47 edges
9. `build_pattern_index()` - 46 edges
10. `AutoValidateAlgorithm` - 39 edges

## Surprising Connections (you probably didn't know these)
- `Overview` --references--> `_value_matches()`  [INFERRED]
  memory/project_ope86_distinct_verdicts.md → src/open_detect/algorithms/auto_validate/detector.py
- `Technical Details` --references--> `_value_matches()`  [INFERRED]
  memory/project_ope86_distinct_verdicts.md → src/open_detect/algorithms/auto_validate/detector.py
- `Bug Fixes` --references--> `_value_matches()`  [INFERRED]
  RELEASE-NOTES-OPE-162.md → src/open_detect/algorithms/auto_validate/detector.py
- `Code Review State` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Final Fixes Pushed` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (194 total, 55 thin omitted)

### Community 0 - "AlgorithmResult"
Cohesion: 0.14
Nodes (10): property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, TestLegacyCorpus, TestMismatch (+2 more)

### Community 1 - "pipeline.py"
Cohesion: 0.11
Nodes (3): get_spark(), configure_logging(), get_logger()

### Community 2 - "test_ope86_distinct_verdicts.py"
Cohesion: 0.10
Nodes (21): _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting(), _detect(), _detector() (+13 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "run_raha"
Cohesion: 0.13
Nodes (11): _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_auto_validate(), _metrics() (+3 more)

### Community 10 - "FailureCounts"
Cohesion: 0.19
Nodes (6): compute(), _score_fd_pair(), compute(), compute(), FailureCounts, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "AlgorithmResult"
Cohesion: 0.17
Nodes (3): Combine, AlgorithmResult, TestAlgorithmResult

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestFmdvV, TestSegmentDp, solve(), TestCorpusInputShapes (+3 more)

### Community 16 - "check_drift"
Cohesion: 0.08
Nodes (9): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.19
Nodes (9): _drop_nulls(), _original_row_ids(), _positions_of(), _score(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order(), test_leading_nulls_map_to_original_positions() (+1 more)

### Community 18 - "CellResult"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "perturb_spelling"
Cohesion: 0.10
Nodes (11): _score_pair(), _score_column(), _score_column(), _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome (+3 more)

### Community 20 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.11
Nodes (8): _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvVh, TestLargeGroups, TestMinConforming, _time_corpus()

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
Cohesion: 0.20
Nodes (3): DataQualityError, check_failure_threshold(), TestCheckFailureThreshold

### Community 25 - "with"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "PatternIndex"
Cohesion: 0.07
Nodes (19): Variants, Recent Changes, _clean(), fmdv(), fmdv_h(), InferredPattern, min_conforming(), _coarse_signature() (+11 more)

### Community 27 - "UniDetectConfig"
Cohesion: 0.12
Nodes (11): API reference, ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, _config(), TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation (+3 more)

### Community 29 - "ValidationError"
Cohesion: 0.17
Nodes (10): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification, 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP) (+2 more)

### Community 30 - "get_notification_config"
Cohesion: 0.07
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "pytest"
Cohesion: 0.08
Nodes (12): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.10
Nodes (10): ScopeStats, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop() (+2 more)

### Community 36 - "get_algorithm_class"
Cohesion: 0.10
Nodes (11): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), get_algorithm_class(), test_registered_under_raha(), test_get_algorithm_constructs_with_args() (+3 more)

### Community 37 - "build_column_features"
Cohesion: 0.19
Nodes (7): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 39 - "_search_mpd"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 40 - "fd_compliance_ratio"
Cohesion: 0.18
Nodes (5): InsufficientDataError, fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "algorithms/index.md"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 44 - "test_catalog.py"
Cohesion: 0.15
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 45 - "`auto_validate`"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 47 - "Auto-Validate"
Cohesion: 0.17
Nodes (10): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+2 more)

### Community 48 - "Benchmark: WIKI subset"
Cohesion: 0.12
Nodes (10): list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered(), TestPluginDiscovery (+2 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.06
Nodes (34): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+26 more)

### Community 50 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (12): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+4 more)

### Community 51 - "index.py"
Cohesion: 0.07
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 53 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 54 - "uni_detect/text_utils.py"
Cohesion: 0.17
Nodes (4): UniDetectConfig, config(), TestUniDetectConfig, config()

### Community 55 - "index.py"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Raha"
Cohesion: 0.18
Nodes (9): Configuration, How it works, Install, Raha, Scope, Configuration, Detector, Labelers (+1 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "corpus_tables_by_category"
Cohesion: 0.21
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)"
Cohesion: 0.29
Nodes (6): Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "numpy"
Cohesion: 0.13
Nodes (3): ColumnPredictions, _default_classifier_factory(), _compact_dtype()

### Community 67 - "CorpusStatsStore"
Cohesion: 0.07
Nodes (15): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results, Job arguments, Jobs, Notebooks (+7 more)

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "confusion_metrics"
Cohesion: 0.11
Nodes (15): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+7 more)

### Community 70 - "ErrorType"
Cohesion: 0.11
Nodes (12): _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+4 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.12
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "HeuristicLabeler"
Cohesion: 0.10
Nodes (15): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+7 more)

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "Review Complete: OPE-194 (PR #106)"
Cohesion: 0.17
Nodes (4): _aggregate_scored_rows(), compute(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "UniDetect"
Cohesion: 0.17
Nodes (6): _config(), _mock_spark(), TestUniDetectBuildCorpusStatistics, TestUniDetectInit, TestUniDetectValidateInputs, TestUniDetectWriteDetections

### Community 84 - "numpy"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "hooks"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "TestConfigureLogging"
Cohesion: 0.14
Nodes (12): fd_violation_strategies(), _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column() (+4 more)

### Community 90 - "list_algorithms"
Cohesion: 0.10
Nodes (3): _spark_available(), TestGetSparkExtended, TestGetSpark

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "validation.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 94 - "TeamsNotifier"
Cohesion: 0.18
Nodes (3): TeamsNotifier, TestBuildMessage, TestCheckRateLimit

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "Appendix: Validation Function Reference"
Cohesion: 0.15
Nodes (5): Appendix: Validation Function Reference, _ensure_dataframe_is_spark(), _validate_literal_value(), TestEnsureDataFrameIsSpark, TestValidateLiteralValue

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "labeling.py"
Cohesion: 0.18
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "_segment_dp"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "ConfigurationError"
Cohesion: 0.13
Nodes (8): _validate_edges(), main(), _run(), _require_columns(), ConfigurationError, test_main_installs_logging(), TestMain, TestRequireColumns

### Community 103 - "score"
Cohesion: 0.12
Nodes (14): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError (+6 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "infer_column_data_type"
Cohesion: 0.11
Nodes (6): infer_column_data_type(), is_float_like(), is_mixed_alphanumeric(), TestDataTypeInference, TestFloatLike, TestMixedAlphanumeric

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "Completed Work"
Cohesion: 0.33
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 110 - "get_spec"
Cohesion: 0.19
Nodes (3): _require_min_rows(), get_spec(), TestGetSpec

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.14
Nodes (10): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box, Why a common interface, Registry (+2 more)

### Community 112 - "get_algorithm"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 113 - "ErrorType"
Cohesion: 0.11
Nodes (11): ColumnDataType, ComparisonDirection, ErrorType, CorpusColumnRecord, CorpusPairRecord, NumericOutlierDetector, SpellingDetector, _filter_by_column_type() (+3 more)

### Community 115 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "Appendix: Validation Function Reference"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 118 - "test_algorithms_registry.py"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 119 - "_make_classifier"
Cohesion: 0.29
Nodes (4): Candidate, MetricObservation, TestCandidate, TestMetricObservation

### Community 120 - "score"
Cohesion: 0.12
Nodes (16): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat (+8 more)

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 122 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 127 - "is_mixed_alphanumeric"
Cohesion: 0.13
Nodes (12): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, Configuration, Enumerations (+4 more)

### Community 131 - "ValidationError"
Cohesion: 0.29
Nodes (7): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect

### Community 133 - "_check_columns_unique"
Cohesion: 0.22
Nodes (3): Algorithms, Fidelity to the papers, Errors

### Community 134 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (19): Implementation Status, Changes Made, _build_suggestion(), _check_columns_present(), _distinct_value_verdicts(), _distinct_value_verdicts_groups(), _feasible_evidence(), _infeasible_evidence() (+11 more)

### Community 137 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 140 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (5): CorpusStatsBuilder, FailureTracker, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 143 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 144 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 145 - "._new_failure_tracker"
Cohesion: 0.20
Nodes (3): compute(), compute(), compute()

### Community 147 - "OPE-89: Fix Spark Cache Lifecycle in Uni-Detect"
Cohesion: 0.25
Nodes (7): Blockers, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 149 - "_make_classifier"
Cohesion: 0.32
Nodes (3): _make_classifier(), TestDeterminismAndSeeding, factory()

### Community 150 - "_row"
Cohesion: 0.25
Nodes (4): _build_row(), _row(), test_build_row_maps_row_ids_via_original_positions(), test_evidence_honors_redact_mode()

### Community 161 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 162 - "OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)"
Cohesion: 0.40
Nodes (4): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results

### Community 166 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 205 - "_detector"
Cohesion: 0.13
Nodes (4): _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "_random_words"
Cohesion: 0.31
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 426 - "test_logging_utils.py"
Cohesion: 0.15
Nodes (3): TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 433 - "collections_abc"
Cohesion: 0.10
Nodes (4): Completed Work, BaseDetector, FunctionalDependencyDetector, UniquenessDetector

### Community 458 - "detectors/base.py"
Cohesion: 0.13
Nodes (5): _hash_value(), make_evidence_json(), redact_evidence(), _NoCandidatesDetector, TestRedactEvidence

### Community 530 - "hierarchy.py"
Cohesion: 0.06
Nodes (23): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+15 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "collections_abc"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "wiki_subset/run_benchmark.py"
Cohesion: 0.11
Nodes (13): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, _build_config(), main(), _print_comparison() (+5 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.13
Nodes (11): main(), train_and_predict(), RahaConfig, RahaDetector, _features(), TestClassifierTrainingPath, TestDegenerateCases, test_empty_dataframe_returns_no_cells() (+3 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 1430 - "spark_session.py"
Cohesion: 0.17
Nodes (6): _cap_driver_memory(), _delta_jars(), _download(), _host_memory_bytes(), spark(), uc_location()

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1183 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **55 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `AlgorithmResult`, `pipeline.py`, `7.2 Key Features`, `ValidationError`, `_FakeDetector`, `parse_args`, `builder.py`, `ScoringJobCounter`, `run_raha`, `FailureCounts`, `FeatureBucket`, `CorpusStatsBuilder`, `._build_affected_summary`, `.detect`, `TestUniDetectDetect`, `.test_release_calls_detector_release`, `UniDetectConfig`, `_score_single_column`, `main`, `parse_args`, `all_specs`, `algorithms/index.md`, `TestScoreFdPair`, `collections_abc`, `ErrorDetectionAlgorithm`, `corpus_tables_by_category`, `wiki_subset/run_benchmark.py`, `CorpusStatsStore`, `ErrorType`, `._send_teams_notification_after_detection`, `detectors/base.py`, `UniDetect`, `ConfigurationError`, `get_spec`, `_make_classifier`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `AlgorithmResult` be split into smaller, more focused modules?**
  _Cohesion score 0.14112903225806453 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `wiki_subset/run_benchmark.py`, `ConfigurationError`, `score`, `auto_validate/detector.py`, `run_raha`, `check_drift`, `index.py`, `test_auto_validate_fmdv_v.py`, `index.py`, `AutoValidateAlgorithm`, `PatternIndex`, `UniDetectConfig`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 67 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._