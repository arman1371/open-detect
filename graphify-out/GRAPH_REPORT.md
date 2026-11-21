# Graph Report - open-detect  (2026-11-21)

## Corpus Check
- 210 files · ~166,313 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 472 files seen (50%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 3189 nodes · 6982 edges · 173 communities (134 shown, 39 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 913 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a76fd9da`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- pipeline.py
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- TestCorpusStatsSchema
- README.md — Uni-Detect overview
- json
- FailureCounts
- PRD: User Feedback Tooltips
- FeatureBucket
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- 7.2 Key Features
- perturbation.py
- fmdv_v
- permissions
- with
- update-graph
- check_failure_threshold
- with
- PatternIndex
- UnityCatalogLocation
- _check_expected_type
- ValidationError
- get_notification_config
- .detect
- pytest
- _score_single_column
- main
- ScoringJobCounter
- list_algorithms
- build_column_features
- FailureCountsAccumulatorParam
- metrics/spelling.py
- InsufficientDataError
- real_world_gov benchmark results
- propagate_labels
- test_build_corpus_statistics.py
- list_tables_matching
- Benchmark: WIKI subset
- RahaDetector
- Auto-Validate
- test_algorithms_registry.py
- CHANGELOG
- ErrorDetectionAlgorithm
- test_auto_validate_index.py
- TeamsNotifier
- test_bench_snapshot.py
- UniDetectConfig
- fmdv
- updates
- Raha
- jobs
- UniDetect
- _ensure_sequence_of_str
- _coerce_numeric
- build
- uses
- warnings
- env
- _run
- CorpusStatsStore
- dry_run
- confusion_metrics
- featurization.py
- CorpusIngestor
- variables
- ._send_teams_notification_after_detection
- PRD: API Validation Framework for open-detect
- dev
- .send
- Commit conventions and releases
- HeuristicLabeler
- _value_matches_groups
- Current Status: BLOCKED
- _aggregate_scored_rows
- _config
- gaussian_outlier_strategies
- test
- hooks
- release.yml
- release
- numpy
- auto_validate/detector.py
- pypi
- Current Status: BLOCKED
- dataset_utils.py
- ._build_message
- with
- on
- _ensure_dataframe_is_spark
- steps
- argparse
- CallableLabeler
- OPE-133 Review Summary
- ConfigurationError
- OpenDetectError
- sonarqube
- perturb_spelling
- infer_column_data_type
- docs
- force
- test_package_init.py
- .index
- algorithms/uni-detect.md
- select_fd_column_pairs
- uni_detect/core/enums.py
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_console_scripts.py
- `uni_detect`
- `raha`
- Running on Databricks
- Comparing algorithms
- AutoValidateAlgorithm
- _validate_literal_value
- paperclip-issue-update.sh
- OPE-86 / PR #96 — Copilot Review Fixes
- get_algorithm
- Quickstart
- TestCorpusStatsSchemaWeightType
- uniqueness_ratio
- Uni-Detect
- config
- _value_matches
- TestDetectCacheLifecycleSpark
- TestConfigThreshold
- KnownIndexLabeler
- patch
- sys
- CorpusStatsBuilder
- _check_unknown_kwargs
- .detect
- TestUniDetectDetect
- OPE-89: Fix Spark Cache Lifecycle in Uni-Detect
- .test_release_calls_detector_release
- matches
- log_transform_fits_better
- _check_dataframe_is_spark
- Appendix: Validation Function Reference
- _reject_unknown_kwargs
- test_teams.py
- OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)
- parse_args
- Scoring auto_validate
- TestEdgeCases
- test_cache_lifecycle.py
- test_metrics.py
- scoped_conf
- TestConfigureLogging
- ErrorType
- make_evidence_json
- hierarchy.py
- perturb_numeric_outlier
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- real_world_gov/run_benchmark.py
- RahaConfig
- wiki_subset/generate_report.py
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 101 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 85 edges
5. `FailureCounts` - 62 edges
6. `TeamsNotifier` - 56 edges
7. `ValidationError` - 48 edges
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
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (173 total, 39 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.10
Nodes (10): diff_fingerprints(), read_build_config(), verify_build_config(), _config(), FakeConf, FakeSpark, test_diff_fingerprints_reports_missing_fields(), TestLegacyCorpus (+2 more)

### Community 1 - "pipeline.py"
Cohesion: 0.06
Nodes (6): FailureTracker, configure_logging(), get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 2 - "pandas"
Cohesion: 0.13
Nodes (17): _city_column(), _count_detect_calls(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference(), test_empty_dataframe(), test_feasible_column_empty_string_is_error_cell() (+9 more)

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
Cohesion: 0.13
Nodes (15): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, artifacts, open_detect_wheel, bundle, name, build (+7 more)

### Community 9 - "json"
Cohesion: 0.09
Nodes (16): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets() (+8 more)

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (8): compute(), _score_fd_pair(), compute(), FailureCounts, compute(), _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.09
Nodes (11): Concepts, Configuration objects, One contract: `detect()`, The shared result schema, open-detect, What is in the box, Why a common interface, AlgorithmResult (+3 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.14
Nodes (12): _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions() (+4 more)

### Community 18 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 20 - "fmdv_v"
Cohesion: 0.07
Nodes (13): min_conforming(), _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), _date_index(), _date_values(), TestCoarseSignature (+5 more)

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
Cohesion: 0.08
Nodes (11): Recent Changes, _fmdv_h_single(), _fmdv_single_segment(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), generality_weight(), PatternIndex (+3 more)

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.16
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config()

### Community 29 - "ValidationError"
Cohesion: 0.29
Nodes (6): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, ValidationError

### Community 30 - "get_notification_config"
Cohesion: 0.07
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "pytest"
Cohesion: 0.19
Nodes (11): test_missing_columns_rejected(), test_require_uni_detect_fails_when_undetected(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 34 - "main"
Cohesion: 0.16
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 36 - "list_algorithms"
Cohesion: 0.10
Nodes (13): Check it works, Installation, Installing from source, Pick your extra, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+5 more)

### Community 37 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 39 - "metrics/spelling.py"
Cohesion: 0.15
Nodes (8): drop_nulls(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance(), TestDropNulls

### Community 40 - "InsufficientDataError"
Cohesion: 0.18
Nodes (5): InsufficientDataError, fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 44 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "RahaDetector"
Cohesion: 0.09
Nodes (15): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), main(), RahaDetector, GroundTruthLabeler, Labeler (+7 more)

### Community 47 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.11
Nodes (12): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered(), test_register_lazy_is_lazy() (+4 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.06
Nodes (34): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+26 more)

### Community 50 - "ErrorDetectionAlgorithm"
Cohesion: 0.09
Nodes (16): 5.1 Primary Segment, 5.2 Secondary Segment, 5.3 Constraints, 5. Market Segment(s), ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect() (+8 more)

### Community 51 - "test_auto_validate_index.py"
Cohesion: 0.10
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 52 - "TeamsNotifier"
Cohesion: 0.12
Nodes (3): TeamsNotifier, TestCheckRateLimit, TestTeamsNotifierInit

### Community 53 - "test_bench_snapshot.py"
Cohesion: 0.20
Nodes (13): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+5 more)

### Community 54 - "UniDetectConfig"
Cohesion: 0.15
Nodes (4): UniDetectConfig, config(), TestUniDetectConfig, config()

### Community 55 - "fmdv"
Cohesion: 0.11
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.13
Nodes (10): build_spark(), main(), Completed Work, UniDetect, __getattr__(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table() (+2 more)

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "_run"
Cohesion: 0.27
Nodes (4): main(), _run(), test_main_installs_logging(), TestMain

### Community 67 - "CorpusStatsStore"
Cohesion: 0.10
Nodes (6): CorpusStatsStore, CorpusNotFoundError, TestBatchScoreOptimization, TestWiring, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "confusion_metrics"
Cohesion: 0.12
Nodes (14): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+6 more)

### Community 70 - "featurization.py"
Cohesion: 0.07
Nodes (15): _score_pair(), _score_column(), _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length() (+7 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.12
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.15
Nodes (12): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+4 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "HeuristicLabeler"
Cohesion: 0.26
Nodes (7): Benchmarks, How to read them, Latest results, Running them, ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 79 - "_value_matches_groups"
Cohesion: 0.25
Nodes (5): _value_matches_groups(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting()

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.11
Nodes (9): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results, _aggregate_scored_rows(), compute(), TestAggregateScoredRows (+1 more)

### Community 83 - "_config"
Cohesion: 0.12
Nodes (6): _config(), _mock_spark(), TestBuildAffectedSummary, TestUniDetectInit, TestUniDetectValidateInputs, TestUniDetectWriteDetections

### Community 84 - "gaussian_outlier_strategies"
Cohesion: 0.08
Nodes (12): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestEmptyFrames, TestGaussianOutlierStrategies (+4 more)

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

### Community 89 - "numpy"
Cohesion: 0.17
Nodes (11): fd_violation_strategies(), _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column() (+3 more)

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

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
Cohesion: 0.13
Nodes (10): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, TestCallableLabeler (+2 more)

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 103 - "OpenDetectError"
Cohesion: 0.14
Nodes (11): Errors, The registry, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error() (+3 more)

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

### Community 110 - ".index"
Cohesion: 0.33
Nodes (4): Inspecting a pattern, Reading the output, Usage, segment()

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.12
Nodes (9): Algorithms, Fidelity to the papers, Getting started, At a glance, Choosing an algorithm, Rules of thumb, Registry, Registry and results (+1 more)

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 113 - "uni_detect/core/enums.py"
Cohesion: 0.09
Nodes (11): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, TestCandidate (+3 more)

### Community 115 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 116 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 117 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 118 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 119 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 120 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 126 - "OPE-86 / PR #96 — Copilot Review Fixes"
Cohesion: 0.40
Nodes (4): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 127 - "get_algorithm"
Cohesion: 0.07
Nodes (21): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, Errors, API reference (+13 more)

### Community 128 - "Quickstart"
Cohesion: 0.40
Nodes (5): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog

### Community 131 - "Uni-Detect"
Cohesion: 0.20
Nodes (10): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Reading the detections, Through the registry (+2 more)

### Community 134 - "_value_matches"
Cohesion: 0.08
Nodes (20): Implementation Status, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification (+12 more)

### Community 137 - "KnownIndexLabeler"
Cohesion: 0.39
Nodes (3): KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.15
Nodes (7): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate, TestDetectorFailureGate

### Community 143 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 144 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 147 - "OPE-89: Fix Spark Cache Lifecycle in Uni-Detect"
Cohesion: 0.25
Nodes (7): Blockers, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 153 - "matches"
Cohesion: 0.17
Nodes (5): matches(), fpr_column(), impurity(), matching_pattern(), TestMatching

### Community 158 - "Appendix: Validation Function Reference"
Cohesion: 0.28
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_columns_unique(), TestCheckColumnsUnique

### Community 162 - "OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)"
Cohesion: 0.40
Nodes (4): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results

### Community 166 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 205 - "test_cache_lifecycle.py"
Cohesion: 0.09
Nodes (7): _config(), _detector(), _FakeDetector, _spark_available(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 376 - "scoped_conf"
Cohesion: 0.09
Nodes (5): get_spark(), scoped_conf(), TestGetSparkExtended, TestScopedConf, TestGetSpark

### Community 433 - "ErrorType"
Cohesion: 0.07
Nodes (19): ErrorType, property_key(), write_build_config(), _require_min_rows(), BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector (+11 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.12
Nodes (8): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), _build_row(), compute(), TestRedactEvidence

### Community 530 - "hierarchy.py"
Cohesion: 0.06
Nodes (21): _append_literal(), _char_class(), _class_of_token(), generalize(), _is_numeric(), _iter_runs(), matches_tokens(), _parse() (+13 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.10
Nodes (12): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), main(), _print_comparison(), _register_table() (+4 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 1430 - "conftest.py"
Cohesion: 0.16
Nodes (6): _cap_driver_memory(), _delta_jars(), _download(), _host_memory_bytes(), spark(), uc_location()

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1194 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **39 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UniDetect` connect `UniDetect` to `pipeline.py`, `TestDetectCacheLifecycleSpark`, `json`, `CorpusStatsBuilder`, `TestUniDetectDetect`, `.test_release_calls_detector_release`, `ValidationError`, `main`, `test_build_corpus_statistics.py`, `Benchmark: WIKI subset`, `ErrorType`, `ErrorDetectionAlgorithm`, `TeamsNotifier`, `UniDetectConfig`, `_run`, `real_world_gov/run_benchmark.py`, `CorpusIngestor`, `._send_teams_notification_after_detection`, `_config`, `test_package_init.py`, `uni_detect/core/enums.py`, `get_algorithm`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.09672830725462304 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `PatternIndex`, `ConfigurationError`, `_value_matches`, `json`, `CellResult`, `InferredPattern`, `test_auto_validate_index.py`, `fmdv_v`, `fmdv`, `AutoValidateAlgorithm`, `auto_validate/detector.py`, `get_algorithm`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 67 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._