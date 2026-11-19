# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-19)

## Corpus Check
- 198 files · ~166,015 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3154 nodes · 6840 edges · 168 communities (131 shown, 37 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 878 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `98ab6a3a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_bench_snapshot.py
- Benchmark: real_world_gov
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- README.md — Uni-Detect overview
- PRD: Teams Notification Trigger for Scan Context
- FailureCounts
- PRD: User Feedback Tooltips
- TeamsNotifier
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- ErrorDetectionAlgorithm
- perturbation.py
- auto_validate/detector.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- RahaDetector
- ScoringJobCounter
- Completed Work
- _ensure_sequence_of_str
- UniDetectConfig
- cluster_column
- pytest
- gaussian_outlier_strategies
- main
- ScoringJobCounter
- Benchmarks
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
- fmdv_v
- test_algorithms_registry.py
- CHANGELOG
- reference/index.md
- PatternIndex
- ErrorDetectionAlgorithm
- wiki_subset/generate_report.py
- unittest_mock
- fmdv.py
- updates
- Raha
- jobs
- ErrorType
- featurization.py
- _coerce_numeric
- build
- uses
- real_world_gov/run_benchmark.py
- env
- perturb_spelling
- .batch_score
- dry_run
- _score_single_column
- ErrorType
- CorpusIngestor
- variables
- dataset_utils.py
- PRD: API Validation Framework for open-detect
- dev
- clean_column
- Commit conventions and releases
- labeling.py
- .detect
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
- uni_detect/text_utils.py
- spark_session.py
- with
- on
- FailureCountsAccumulatorParam
- steps
- argparse
- CallableLabeler
- _segment_dp
- ConfigurationError
- score
- sonarqube
- require_uni_detect
- tokenize
- docs
- force
- get_algorithm
- pipeline.py
- _check_expected_type
- bucket_by_edges
- _ensure_dataframe_is_spark
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_console_scripts.py
- _check_unknown_kwargs
- FeatureBucket
- Raha
- infer_column_data_type
- AutoValidateAlgorithm
- Auto-Validate
- paperclip-issue-update.sh
- docs/index.md
- Auto-Validate
- open_detect_wheel
- _make_tooltip
- Appendix: Validation Function Reference
- ValidationError
- _FakeDetector
- is_mixed_alphanumeric
- _value_matches
- _check_dataframe_is_spark
- uniqueness_ratio
- Uni-Detect
- TestPluginDiscoveryViaRealDistInfo
- sys
- algorithms/index.md
- CorpusStatsBuilder
- is_float_like
- _validate_literal_value
- _reject_unknown_kwargs
- SparkUnavailableContext
- _StubDetector
- finite_floats
- `uni_detect`
- `raha`
- TestCorpusStatsSchema
- TestCorpusStatsSchemaWeightType
- _detector
- test_metrics.py
- TestScopedConf
- get_logger
- ErrorType
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
4. `UniDetect` - 71 edges
5. `FailureCounts` - 56 edges
6. `ValidationError` - 48 edges
7. `UnityCatalogLocation` - 47 edges
8. `build_pattern_index()` - 46 edges
9. `AutoValidateAlgorithm` - 39 edges
10. `CellResult` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Bug Fixes` --references--> `_value_matches()`  [INFERRED]
  RELEASE-NOTES-OPE-162.md → src/open_detect/algorithms/auto_validate/detector.py
- `Code Review State` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Final Fixes Pushed` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Phase 1: Core Tooltip Engine (4 weeks)` --references--> `CellResult`  [INFERRED]
  PRD-user-feedback-tooltips.md → src/open_detect/algorithms/base.py
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (168 total, 37 thin omitted)

### Community 0 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 1 - "Benchmark: real_world_gov"
Cohesion: 0.20
Nodes (10): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Reading the results, Running the benchmark (+2 more)

### Community 2 - "pandas"
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

### Community 9 - "PRD: Teams Notification Trigger for Scan Context"
Cohesion: 0.07
Nodes (27): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segment(s), 6. Value Proposition(s), 7.1 UX/Prototypes, 7.2 Key Features (+19 more)

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (11): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, compute() (+3 more)

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "TeamsNotifier"
Cohesion: 0.06
Nodes (8): TeamsNotificationError, TeamsNotifier, TestBuildMessage, TestCheckRateLimit, TestSend, TestSendSafe, TestSeverityOrdering, TestTeamsNotifierInit

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.09
Nodes (8): Combine, open-detect, What is in the box, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.10
Nodes (8): _infer_pattern_to_groups(), check_drift(), _clean_series(), _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.09
Nodes (17): _hash_value(), make_evidence_json(), redact_evidence(), _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row() (+9 more)

### Community 18 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (15): The registry, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm_class(), _load_entry_points() (+7 more)

### Community 19 - "perturbation.py"
Cohesion: 0.12
Nodes (9): _score_column(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency (+1 more)

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (22): _matches_segments(), _conforms(), _conforms_segments(), DriftResult, _fmdv_h_single(), _fmdv_single_segment(), _append_literal(), _char_class() (+14 more)

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

### Community 26 - "RahaDetector"
Cohesion: 0.27
Nodes (6): RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 28 - "Completed Work"
Cohesion: 0.25
Nodes (7): Blockers, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 30 - "UniDetectConfig"
Cohesion: 0.10
Nodes (9): UniDetectConfig, UnityCatalogLocation, config(), TestRedactEvidence, TestUniDetectConfig, TestUnityCatalogLocation, config(), config() (+1 more)

### Community 31 - "cluster_column"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "pytest"
Cohesion: 0.07
Nodes (19): __getattr__(), __getattr__(), OpenDetectError, pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim() (+11 more)

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.08
Nodes (12): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestEmptyFrames, TestGaussianOutlierStrategies (+4 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.09
Nodes (10): ScopeStats, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop() (+2 more)

### Community 36 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 37 - "build_column_features"
Cohesion: 0.11
Nodes (12): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features() (+4 more)

### Community 38 - "build_metadata.py"
Cohesion: 0.08
Nodes (13): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeConf, FakeSpark (+5 more)

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
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 47 - "fmdv_v"
Cohesion: 0.08
Nodes (13): min_conforming(), _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), _date_index(), _date_values(), TestCoarseSignature (+5 more)

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.11
Nodes (11): list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered(), TestPluginDiscovery (+3 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "reference/index.md"
Cohesion: 0.23
Nodes (3): Registry, Registry and results, Result types

### Community 51 - "PatternIndex"
Cohesion: 0.07
Nodes (13): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Recent Changes, Test Results, _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh() (+5 more)

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.19
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 55 - "fmdv.py"
Cohesion: 0.12
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Raha"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "ErrorType"
Cohesion: 0.08
Nodes (16): Methodology: uni_detect -- mapping real dirty data onto its four error types, build_spark(), main(), Completed Work, ErrorType, parse_args(), _run(), _build_teams_affected_summary() (+8 more)

### Community 60 - "featurization.py"
Cohesion: 0.16
Nodes (10): _score_pair(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+2 more)

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "real_world_gov/run_benchmark.py"
Cohesion: 0.11
Nodes (14): confusion_metrics(), Methodology: raha, _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate() (+6 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 67 - ".batch_score"
Cohesion: 0.09
Nodes (10): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, CorpusStatsStore, CorpusNotFoundError, TestBatchScoreOptimization (+2 more)

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.19
Nodes (5): _require_min_rows(), _score_single_column(), InsufficientDataError, TestScoreFdPair, TestScoreSingleColumn

### Community 70 - "ErrorType"
Cohesion: 0.07
Nodes (14): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, __getattr__() (+6 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.08
Nodes (9): balanced_union(), CorpusIngestor, compute_token_counts(), select_fd_column_pairs(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment, TestSelectFdColumnPairs (+1 more)

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

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
Cohesion: 0.12
Nodes (11): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, ColumnFeatures, HeuristicLabeler (+3 more)

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
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

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

### Community 94 - "spark_session.py"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

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
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.15
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "_segment_dp"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "ConfigurationError"
Cohesion: 0.12
Nodes (7): _validate_edges(), main(), _require_columns(), ConfigurationError, test_main_installs_logging(), TestMain, TestRequireColumns

### Community 103 - "score"
Cohesion: 0.12
Nodes (16): Reading the output, Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, Errors, One contract: `detect()` (+8 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "require_uni_detect"
Cohesion: 0.33
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 106 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_algorithm"
Cohesion: 0.15
Nodes (10): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+2 more)

### Community 110 - "pipeline.py"
Cohesion: 0.11
Nodes (10): ensure_schema_exists(), list_tables(), list_tables_matching(), table_exists(), UnityCatalogError, TestEnsureSchemaExists, TestListTables, TestListTablesMatching (+2 more)

### Community 112 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 115 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 116 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 117 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 119 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.06
Nodes (18): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, Inspecting a pattern, Usage, AutoValidateAlgorithm, _distinct_value_verdicts_groups() (+10 more)

### Community 122 - "Auto-Validate"
Cohesion: 0.22
Nodes (7): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly, Errors

### Community 126 - "docs/index.md"
Cohesion: 0.18
Nodes (7): Getting started, Installation, Installing from source, Pick your extra, At a glance, Choosing an algorithm, Rules of thumb

### Community 127 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 128 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 129 - "_make_tooltip"
Cohesion: 0.22
Nodes (5): _build_suggestion(), _make_tooltip(), _tooltip_content(), pattern_to_language(), TooltipContent

### Community 130 - "Appendix: Validation Function Reference"
Cohesion: 0.28
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_columns_unique(), TestCheckColumnsUnique

### Community 131 - "ValidationError"
Cohesion: 0.29
Nodes (6): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, ValidationError

### Community 134 - "_value_matches"
Cohesion: 0.21
Nodes (10): Implementation Status, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification (+2 more)

### Community 137 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.17
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 148 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 149 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.20
Nodes (5): _brute_force_mpd(), _random_words(), _single_edit(), TestDropNulls, TestSpellingBlocking

### Community 426 - "get_logger"
Cohesion: 0.09
Nodes (8): _send_teams_notification(), get_spark(), configure_logging(), get_logger(), TestGetSparkExtended, TestGetSpark, TestConfigureLogging, TestGetLogger

### Community 433 - "ErrorType"
Cohesion: 0.07
Nodes (11): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, all_specs(), ErrorTypeSpec (+3 more)

### Community 530 - "hierarchy.py"
Cohesion: 0.07
Nodes (13): generalize(), _iter_runs(), Token, token_count(), tokenize(), _alternatives(), iter_patterns(), _ordered_alternatives() (+5 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.20
Nodes (4): _score_column(), perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), require_min_size(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+2 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.21
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.10
Nodes (10): maybe_scope(), UniDetectProfile, git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1430 - "conftest.py"
Cohesion: 0.12
Nodes (12): A fully local example, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect, _cap_driver_memory(), _delta_jars() (+4 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1174 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **37 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `_make_tooltip`, `ConfigurationError`, `score`, `get_algorithm`, `fmdv_v`, `InferredPattern`, `PatternIndex`, `auto_validate/detector.py`, `fmdv.py`, `AutoValidateAlgorithm`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `pandas` be split into smaller, more focused modules?**
  _Cohesion score 0.09581646423751687 - nodes in this community are weakly interconnected._
- **Why does `ValidationError` connect `ValidationError` to `Appendix: Validation Function Reference`, `builder.py`, `_check_dataframe_is_spark`, `_validate_literal_value`, `_reject_unknown_kwargs`, `AutoValidateConfig`, `auto_validate/detector.py`, `_ensure_sequence_of_str`, `pytest`, `collections_abc`, `metrics/functional_dependency.py`, `get_logger`, `outliers.py`, `ErrorType`, `PatternIndex`, `ErrorType`, `min_pairwise_edit_distance`, `_score_single_column`, `ErrorType`, `PRD: API Validation Framework for open-detect`, `clean_column`, `_config`, `spark_session.py`, `_check_expected_type`, `_check_unknown_kwargs`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Are the 66 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 66 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._