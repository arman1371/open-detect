# Graph Report - open-detect  (2026-11-23)

## Corpus Check
- 211 files · ~166,424 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 473 files seen (49%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 3185 nodes · 6880 edges · 158 communities (133 shown, 25 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 827 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0dd44d26`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UnityCatalogLocation
- test_ope86_distinct_verdicts.py
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- README.md — Uni-Detect overview
- wiki_subset/run_benchmark.py
- FailureCounts
- PRD: User Feedback Tooltips
- build_column_features
- new_cluster
- CellResult
- AutoValidateConfig
- check_drift
- test_spelling_detector.py
- notifications/config.py
- UniDetectAlgorithm
- fmdv_v
- permissions
- with
- update-graph
- check_failure_threshold
- with
- _run
- ErrorDetectionAlgorithm
- CorpusStatsBuilder
- ValidationError
- UniDetectConfig
- .detect
- __getattr__
- gaussian_outlier_strategies
- main
- pytest
- Benchmark: real_world_gov
- AutoValidateAlgorithm
- SlidingWindowRateLimiter
- test_cache_lifecycle.py
- Commit conventions and releases
- real_world_gov benchmark results
- propagate_labels
- Uni-Detect
- log_transform_fits_better
- `auto_validate`
- _value_matches
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- Auto-Validate
- _date_index
- .send
- get_spec
- TeamsNotifier
- fmdv
- updates
- labeling.py
- jobs
- .build_corpus_statistics
- databricks.yml
- _coerce_numeric
- build
- uses
- TestUniDetectDetect
- env
- concepts.md
- _aggregate_scored_rows
- dry_run
- _score_single_column
- ColumnDataType
- CorpusIngestor
- variables
- Uni-Detect
- PRD: API Validation Framework for open-detect
- dev
- auto_validate/detector.py
- PatternIndex
- GroundTruthLabeler
- TestDetectCacheLifecycleSpark
- Current Status: BLOCKED
- clean_column
- UniDetect
- Raha
- test
- Completed Work
- release.yml
- release
- Running on Databricks
- Raha
- pypi
- Current Status: BLOCKED
- infer_column_data_type
- spark_session.py
- with
- on
- numpy
- steps
- pandas
- Labeler
- OPE-133 Review Summary
- test_batch_score_optimization.py
- builder.py
- sonarqube
- wiki_subset/generate_report.py
- algorithms/uni-detect.md
- docs
- force
- perturb_spelling
- pipeline.py
- docs/index.md
- test_teams.py
- sys
- open-detect
- Benchmark: WIKI subset
- test_package_init.py
- ConfigurationError
- hooks
- fd_violation_strategies
- .send_safe
- _count_detect_calls
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- paperclip-issue-update.sh
- select_fd_column_pairs
- test_logging_utils.py
- list_algorithms
- test_build_corpus_statistics.py
- ProfileRunSkippedUniDetect
- TestPluginDiscoveryViaRealDistInfo
- Comparing algorithms
- ._check_rate_limit
- _StubDetector
- TestSeverityOrdering
- Concepts
- _default_classifier_factory
- _detector
- ScoringJobCounter
- bucket_by_edges
- scoped_conf
- ErrorType
- make_evidence_json
- patterns.py
- test_bench_snapshot.py
- perturb_numeric_outlier
- outliers.py
- test_metrics.py
- snapshot.py
- KnownIndexLabeler
- real_world_gov/run_benchmark.py
- Auto-Validate
- RahaConfig
- real_world_gov/generate_report.py
- Performance Baseline — OPE-87
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 97 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 70 edges
5. `FailureCounts` - 62 edges
6. `ValidationError` - 48 edges
7. `TeamsNotifier` - 48 edges
8. `UnityCatalogLocation` - 47 edges
9. `build_pattern_index()` - 46 edges
10. `AutoValidateAlgorithm` - 39 edges

## Surprising Connections (you probably didn't know these)
- `Bug Fixes` --references--> `_value_matches()`  [INFERRED]
  RELEASE-NOTES-OPE-162.md → src/open_detect/algorithms/auto_validate/detector.py
- `Code Review State` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Final Fixes Pushed` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Phase 1: Core Tooltip Engine (4 weeks)` --references--> `CellResult`  [INFERRED]
  PRD-user-feedback-tooltips.md → src/open_detect/algorithms/base.py
- `3.1 Context` --references--> `AlgorithmResult`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (158 total, 25 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.08
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeConf, FakeSpark (+4 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config(), config(), test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 2 - "test_ope86_distinct_verdicts.py"
Cohesion: 0.17
Nodes (12): _city_column(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference(), test_empty_dataframe(), test_feasible_column_empty_string_is_error_cell(), test_identical_to_per_cell_baseline() (+4 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.09
Nodes (11): fd_compliance_ratio(), minority_violation_rows(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices (+3 more)

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.29
Nodes (7): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4)

### Community 9 - "wiki_subset/run_benchmark.py"
Cohesion: 0.07
Nodes (11): maybe_scope(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+3 more)

### Community 10 - "FailureCounts"
Cohesion: 0.13
Nodes (7): compute(), _score_fd_pair(), FailureCounts, compute(), _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.08
Nodes (15): Reading the detections, Through the registry, Usage on Databricks, Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog (+7 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.05
Nodes (15): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _build_index(), TestFmdvV, TestFmdvVh, TestSegmentDp (+7 more)

### Community 16 - "check_drift"
Cohesion: 0.10
Nodes (7): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "notifications/config.py"
Cohesion: 0.07
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 19 - "UniDetectAlgorithm"
Cohesion: 0.24
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 20 - "fmdv_v"
Cohesion: 0.10
Nodes (14): Variants, Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Recent Changes, Test Results, _coarse_signature(), fmdv_v() (+6 more)

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

### Community 26 - "_run"
Cohesion: 0.11
Nodes (10): list_tables(), list_tables_matching(), table_exists(), parse_args(), _run(), TestParseArgs, TestListTables, TestListTablesMatching (+2 more)

### Community 27 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (17): API reference, ErrorDetectionAlgorithm, TooltipContent, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, _constant_factory() (+9 more)

### Community 28 - "CorpusStatsBuilder"
Cohesion: 0.16
Nodes (7): CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 29 - "ValidationError"
Cohesion: 0.06
Nodes (17): Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _ensure_sequence_of_str() (+9 more)

### Community 30 - "UniDetectConfig"
Cohesion: 0.05
Nodes (11): UniDetectConfig, CorpusStatsStore, _FakeDetector, config(), TestBatchScoreOptimization, TestRedactEvidence, TestUniDetectConfig, config() (+3 more)

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
Cohesion: 0.09
Nodes (12): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 36 - "Benchmark: real_world_gov"
Cohesion: 0.12
Nodes (15): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+7 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.07
Nodes (7): AutoValidateAlgorithm, _distinct_value_verdicts_groups(), _infer_pattern_to_groups(), _non_null_cells(), _value_matches_groups(), _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "SlidingWindowRateLimiter"
Cohesion: 0.13
Nodes (3): SlidingWindowRateLimiter, TestEdgeCases, TestSlidingWindowRateLimiter

### Community 39 - "test_cache_lifecycle.py"
Cohesion: 0.12
Nodes (5): get_spark(), _config(), _spark_available(), TestGetSparkExtended, TestGetSpark

### Community 40 - "Commit conventions and releases"
Cohesion: 0.14
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "Uni-Detect"
Cohesion: 0.29
Nodes (7): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect

### Community 45 - "`auto_validate`"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 46 - "_value_matches"
Cohesion: 0.08
Nodes (19): Implementation Status, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification (+11 more)

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.12
Nodes (9): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_get_algorithm_constructs_with_args(), TestPluginDiscovery, worker() (+1 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.05
Nodes (36): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+28 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.20
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 51 - "_date_index"
Cohesion: 0.40
Nodes (3): _date_index(), _date_values(), TestLargeGroups

### Community 53 - "get_spec"
Cohesion: 0.11
Nodes (6): all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 54 - "TeamsNotifier"
Cohesion: 0.16
Nodes (3): TeamsNotifier, TestBuildAdaptiveCard, TestTeamsNotifierInit

### Community 55 - "fmdv"
Cohesion: 0.11
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "labeling.py"
Cohesion: 0.20
Nodes (4): ColumnFeatures, HeuristicLabeler, _resolve_position(), TestHeuristicLabeler

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.15
Nodes (6): build_spark(), main(), _filter_by_column_type(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "databricks.yml"
Cohesion: 0.22
Nodes (8): artifacts, open_detect_wheel, bundle, name, build, path, type, UniDetect pipeline facade

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "TestUniDetectDetect"
Cohesion: 0.24
Nodes (3): _mock_detector_result(), _mock_spark_context(), TestUniDetectDetect

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "concepts.md"
Cohesion: 0.28
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "_aggregate_scored_rows"
Cohesion: 0.12
Nodes (8): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results, _aggregate_scored_rows(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.24
Nodes (3): _score_single_column(), TestScoreSingleColumn, score()

### Community 70 - "ColumnDataType"
Cohesion: 0.08
Nodes (13): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation (+5 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.13
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.04
Nodes (40): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+32 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (18): _matches_segments(), _conforms(), _conforms_segments(), InferredPattern, min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), _append_literal() (+10 more)

### Community 77 - "PatternIndex"
Cohesion: 0.11
Nodes (5): indexable_values(), PatternIndex, _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestIndexableValues

### Community 78 - "GroundTruthLabeler"
Cohesion: 0.35
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "UniDetect"
Cohesion: 0.14
Nodes (8): UniDetect, _config(), _mock_spark(), TestUniDetectBuildCorpusStatistics, TestUniDetectInit, TestUniDetectRelease, TestUniDetectValidateInputs, TestUniDetectWriteDetections

### Community 84 - "Raha"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

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

### Community 94 - "spark_session.py"
Cohesion: 0.10
Nodes (12): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, candidates(), main(), select() (+4 more)

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "numpy"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "pandas"
Cohesion: 0.13
Nodes (6): main(), _build_token_stats_impl(), _compute_token_counts_batch(), _count_tables_batch(), test_empty_dataframe_returns_no_cells(), test_missing_columns_rejected()

### Community 100 - "Labeler"
Cohesion: 0.12
Nodes (11): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, Labeler (+3 more)

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 103 - "builder.py"
Cohesion: 0.09
Nodes (15): Errors, Errors, _require_min_rows(), CorpusNotFoundError, DataQualityError, InsufficientDataError, IndexNotBuiltError, OpenDetectError (+7 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "wiki_subset/generate_report.py"
Cohesion: 0.27
Nodes (11): _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart(), render_markdown() (+3 more)

### Community 106 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "perturb_spelling"
Cohesion: 0.12
Nodes (6): compute(), _score_pair(), _score_column(), compute(), perturb_spelling(), TestPerturbSpelling

### Community 110 - "pipeline.py"
Cohesion: 0.08
Nodes (4): configure_logging(), get_logger(), log_duration(), TestLogDuration

### Community 111 - "docs/index.md"
Cohesion: 0.19
Nodes (5): Algorithms, Fidelity to the papers, Registry, Registry and results, Result types

### Community 115 - "Benchmark: WIKI subset"
Cohesion: 0.14
Nodes (14): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Expected weakness: read Auto-Validate's low recall honestly, Layout, Reading the results without JSON, Running the benchmark, Scoring auto_validate (+6 more)

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "ConfigurationError"
Cohesion: 0.12
Nodes (8): _validate_edges(), main(), _require_columns(), ConfigurationError, test_main_installs_logging(), TestMain, TestWiring, TestRequireColumns

### Community 118 - "hooks"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

### Community 119 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 121 - "_count_detect_calls"
Cohesion: 0.16
Nodes (7): _count_detect_calls(), _counting_value_matches_groups(), counting(), test_stubbed_pattern_matches_real_inference(), test_verdict_cache_invoked_exactly_once_per_distinct(), test_verdict_cache_reduces_value_matches_calls(), _two_distinct_frame()

### Community 122 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 126 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 128 - "list_algorithms"
Cohesion: 0.25
Nodes (8): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, list_algorithms()

### Community 129 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 130 - "ProfileRunSkippedUniDetect"
Cohesion: 0.33
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 132 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 136 - "Concepts"
Cohesion: 0.40
Nodes (5): Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema

### Community 205 - "_detector"
Cohesion: 0.13
Nodes (4): _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 297 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 433 - "ErrorType"
Cohesion: 0.08
Nodes (17): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, _score_column(), UniquenessDetector, FailureTracker (+9 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.23
Nodes (5): _hash_value(), make_evidence_json(), redact_evidence(), compute(), TestRedactEvidence

### Community 530 - "patterns.py"
Cohesion: 0.05
Nodes (19): _char_class(), _class_of_token(), generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize() (+11 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.20
Nodes (13): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+5 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.13
Nodes (7): compute(), _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.09
Nodes (13): drop_nulls(), require_min_size(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+5 more)

### Community 699 - "test_metrics.py"
Cohesion: 0.09
Nodes (13): _blocking_keys(), _closest_pair(), differing_token_lengths(), min_pairwise_edit_distance(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance() (+5 more)

### Community 783 - "snapshot.py"
Cohesion: 0.13
Nodes (12): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot() (+4 more)

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.39
Nodes (3): KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 1123 - "Auto-Validate"
Cohesion: 0.22
Nodes (9): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+1 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (9): ColumnPredictions, _make_classifier(), train_and_predict(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases, TestDeterminismAndSeeding (+1 more)

### Community 1218 - "real_world_gov/generate_report.py"
Cohesion: 0.21
Nodes (10): comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name() (+2 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1430 - "conftest.py"
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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1200 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UniDetectConfig` connect `UniDetectConfig` to `verify_build_config`, `test_build_corpus_statistics.py`, `UnityCatalogLocation`, `Concepts`, `wiki_subset/run_benchmark.py`, `FailureCounts`, `test_spelling_detector.py`, `UniDetectAlgorithm`, `_run`, `ErrorDetectionAlgorithm`, `CorpusStatsBuilder`, `main`, `Benchmark: real_world_gov`, `test_cache_lifecycle.py`, `ScoringJobCounter`, `Uni-Detect`, `CHANGELOG`, `ErrorType`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `_score_single_column`, `TestDetectCacheLifecycleSpark`, `UniDetect`, `builder.py`, `perturb_spelling`, `pipeline.py`, `ConfigurationError`, `perturb_numeric_outlier`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.08484848484848485 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `Concepts`, `wiki_subset/run_benchmark.py`, `auto_validate/detector.py`, `PatternIndex`, `_value_matches`, `check_drift`, `_date_index`, `fmdv_v`, `ConfigurationError`, `fmdv`, `ErrorDetectionAlgorithm`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._