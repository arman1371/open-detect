# Graph Report - open-detect  (2026-11-16)

## Corpus Check
- 191 files · ~159,233 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 2995 nodes · 6611 edges · 165 communities (131 shown, 34 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 817 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `55392f11`
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
- build_corpus_statistics.py
- PatternIndex
- auto_validate/detector.py
- FailureCounts
- fd_violation_strategies
- README.md — Uni-Detect overview
- new_cluster
- test_raha_strategies.py
- AutoValidateConfig
- InferredPattern
- RahaConfig
- build_column_features
- raha/detector.py
- TestUniDetectDetect
- permissions
- with
- update-graph
- matches
- with
- ErrorType
- auto_validate/detector.py
- _mock_spark_context
- warnings
- CellResult
- .detect
- registry.py
- histogram_outlier_strategies
- main
- pytest
- Methodology: auto_validate
- AutoValidateAlgorithm
- Comparing algorithms
- get_spark
- logging_utils.py
- real_world_gov benchmark results
- get_spec
- Detection
- featurization.py
- Benchmark: WIKI subset
- real_plugin_path
- TestUniDetectBaselineDiff
- test_algorithms_registry.py
- CHANGELOG
- ProfileRunSkippedUniDetect
- _build_index
- _config
- MetricObservation
- real_world_gov/run_benchmark.py
- _build_index
- updates
- HeuristicLabeler
- jobs
- UniDetect
- open_detect_wheel
- _value_matches_groups
- build
- uses
- run_raha
- env
- FakeConf
- CorpusStatsStore
- dry_run
- Uni-Detect
- uni_detect/core/models.py
- CorpusIngestor
- variables
- numpy
- PRD: API Validation Framework for open-detect
- dev
- test_console_scripts.py
- Commit conventions and releases
- GroundTruthLabeler
- `uni_detect`
- Current Status: BLOCKED
- _reference_build_pattern_index
- UniDetect
- Raha
- test
- `raha`
- release.yml
- release
- Running on Databricks
- test_raha_strategies.py
- pypi
- Current Status: BLOCKED
- infer_column_data_type
- TestConfigThreshold
- with
- on
- _infer_type_from_sample
- steps
- test_pipeline.py
- CallableLabeler
- test_hygiene.py
- 5. Market Segment(s)
- open_detect/exceptions.py
- sonarqube
- labeling.py
- gaussian_outlier_strategies
- docs
- force
- warnings
- pipeline.py
- docs/index.md
- select_fd_column_pairs
- sys
- open-detect
- TestConfigThreshold
- test_package_init.py
- _require_columns
- `uni_detect`
- `raha`
- algorithms/uni-detect.md
- Auto-Validate
- TestUniDetectOutlierVsSpellingRouting
- paperclip-issue-update.sh
- concepts.md
- algorithms/index.md
- test_console_scripts.py
- uniqueness_ratio
- TestDetectCacheLifecycleSpark
- config
- _StubDetector
- Auto-Validate
- real_plugin_path
- .test_shared_columns_df_unpersisted_at_end
- Quickstart
- 5. Market Segment(s)
- _resolve_position
- _detector
- test_metrics.py
- SparkJobCounter
- featurization.py
- scoped_conf
- ErrorType
- make_evidence_json
- pandas
- test_bench_snapshot.py
- _is_null
- perturb_numeric_outlier
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- KnownIndexLabeler
- json
- TestEnsureDataFrameIsSpark
- RahaConfig
- wiki_subset/generate_report.py
- perturbation.py
- Performance Baseline — OPE-87
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 100 edges
3. `UniDetectConfig` - 92 edges
4. `UniDetect` - 83 edges
5. `FailureCounts` - 56 edges
6. `ValidationError` - 48 edges
7. `build_pattern_index()` - 46 edges
8. `UnityCatalogLocation` - 45 edges
9. `AutoValidateAlgorithm` - 39 edges
10. `CellResult` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Code Review State` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Final Fixes Pushed` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Phase 1: Core Tooltip Engine (4 weeks)` --references--> `CellResult`  [INFERRED]
  PRD-user-feedback-tooltips.md → src/open_detect/algorithms/base.py
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `3.1 Context` --references--> `AlgorithmResult`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (165 total, 34 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.09
Nodes (11): diff_fingerprints(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeConf, FakeSpark, test_diff_fingerprints_reports_missing_fields() (+3 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.15
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.09
Nodes (22): main(), _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting(), _detect() (+14 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "build_corpus_statistics.py"
Cohesion: 0.12
Nodes (9): list_tables_matching(), main(), parse_args(), _run(), test_main_installs_logging(), TestMain, TestParseArgs, TestListTablesMatching (+1 more)

### Community 8 - "PatternIndex"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "auto_validate/detector.py"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (10): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, _raise() (+2 more)

### Community 11 - "fd_violation_strategies"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (7): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "test_raha_strategies.py"
Cohesion: 0.09
Nodes (11): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, 1. Implement `ErrorDetectionAlgorithm`, API reference, AlgorithmResult, CellResult (+3 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "RahaConfig"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "build_column_features"
Cohesion: 0.25
Nodes (8): 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific), 7.2 Key Features

### Community 19 - "raha/detector.py"
Cohesion: 0.13
Nodes (11): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, UniDetectAlgorithm, __getattr__(), test_empty_dataframe_returns_no_cells() (+3 more)

### Community 20 - "TestUniDetectDetect"
Cohesion: 0.08
Nodes (12): min_conforming(), _append_literal(), _char_class(), _class_of_token(), _is_numeric(), matches_tokens(), _parse(), _part_matches() (+4 more)

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

### Community 26 - "ErrorType"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 27 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (15): Recent Changes, _infer_pattern_to_groups(), _matches_segments(), _value_matches_groups(), _clean(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+7 more)

### Community 28 - "_mock_spark_context"
Cohesion: 0.13
Nodes (4): _mock_detector_result(), _mock_spark_context(), TestUniDetectColumnTypeRouting, TestUniDetectDetect

### Community 29 - "warnings"
Cohesion: 0.06
Nodes (18): Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _ensure_sequence_of_str() (+10 more)

### Community 31 - ".detect"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "registry.py"
Cohesion: 0.08
Nodes (21): Check it works, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, _constant_factory(), get_algorithm() (+13 more)

### Community 33 - "histogram_outlier_strategies"
Cohesion: 0.13
Nodes (7): _factorize_column(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestHistogramOutlierStrategies, TestNullSentinel, TestPatternCharacterStrategies

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.28
Nodes (8): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_module_shims_are_identity_preserving(), test_old_except_clause_catches_new_error(), test_unknown_exception_attr_raises()

### Community 36 - "Methodology: auto_validate"
Cohesion: 0.50
Nodes (4): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "Comparing algorithms"
Cohesion: 0.25
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 39 - "get_spark"
Cohesion: 0.28
Nodes (3): get_spark(), TestGetSparkExtended, TestGetSpark

### Community 40 - "logging_utils.py"
Cohesion: 0.13
Nodes (6): configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "Detection"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "real_plugin_path"
Cohesion: 0.11
Nodes (16): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+8 more)

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.20
Nodes (6): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), TestPluginDiscovery, worker()

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "ProfileRunSkippedUniDetect"
Cohesion: 0.22
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 51 - "_build_index"
Cohesion: 0.22
Nodes (4): _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 52 - "_config"
Cohesion: 0.53
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "MetricObservation"
Cohesion: 0.25
Nodes (7): Blockers, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 54 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 55 - "_build_index"
Cohesion: 0.13
Nodes (7): Variants, fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "HeuristicLabeler"
Cohesion: 0.29
Nodes (6): Reading the output, Usage, Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.22
Nodes (5): main(), Completed Work, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "run_raha"
Cohesion: 0.08
Nodes (15): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+7 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 67 - "CorpusStatsStore"
Cohesion: 0.10
Nodes (6): property_key(), CorpusStatsStore, _FakeDetector, TestWiring, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "Uni-Detect"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 70 - "uni_detect/core/models.py"
Cohesion: 0.08
Nodes (12): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, _filter_by_column_type() (+4 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.10
Nodes (6): balanced_union(), CorpusIngestor, compute_token_counts(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.09
Nodes (22): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+14 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_console_scripts.py"
Cohesion: 0.12
Nodes (8): matches(), indexable_values(), fpr_column(), impurity(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestIndexableValues, TestMatching

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_reference_build_pattern_index"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "UniDetect"
Cohesion: 0.12
Nodes (8): UniDetect, _config(), _mock_spark(), TestUniDetectInit, TestUniDetectRelease, TestUniDetectSingleScanIngestion, TestUniDetectValidateInputs, TestUniDetectWriteDetections

### Community 84 - "Raha"
Cohesion: 0.18
Nodes (9): Configuration, How it works, Install, Raha, Scope, Configuration, Detector, Labelers (+1 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - "test_raha_strategies.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 94 - "TestConfigThreshold"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "_infer_type_from_sample"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "test_pipeline.py"
Cohesion: 0.14
Nodes (4): TestUniDetectBaselineDiff, TestUniDetectBuildCorpusStatistics, TestUniDetectScanCount, TestUniDetectSharedIngestionOnce

### Community 100 - "CallableLabeler"
Cohesion: 0.27
Nodes (5): The simplest labeler: a function, CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "test_hygiene.py"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.07
Nodes (22): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Errors, _validate_edges(), CorpusNotFoundError (+14 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "labeling.py"
Cohesion: 0.18
Nodes (7): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, Writing a class, Labeler, _values_equal()

### Community 106 - "gaussian_outlier_strategies"
Cohesion: 0.23
Nodes (4): gaussian_outlier_strategies(), _is_float_like(), TestGaussianOutlierStrategies, TestRowWeightedNumericGate

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 110 - "pipeline.py"
Cohesion: 0.07
Nodes (4): list_tables(), table_exists(), TestListTables, TestTableExists

### Community 111 - "docs/index.md"
Cohesion: 0.22
Nodes (6): open-detect, What is in the box, Why a common interface, Registry, Registry and results, Result types

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "test_package_init.py"
Cohesion: 0.22
Nodes (3): test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 120 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 121 - "Auto-Validate"
Cohesion: 0.17
Nodes (10): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+2 more)

### Community 126 - "concepts.md"
Cohesion: 0.28
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 128 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 132 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 133 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 136 - "Quickstart"
Cohesion: 0.40
Nodes (5): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog

### Community 138 - "5. Market Segment(s)"
Cohesion: 0.50
Nodes (4): 5.1 Primary Segment, 5.2 Secondary Segment, 5.3 Constraints, 5. Market Segment(s)

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.24
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "SparkJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "featurization.py"
Cohesion: 0.07
Nodes (17): FeatureBucket, _score_pair(), _score_column(), _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count() (+9 more)

### Community 433 - "ErrorType"
Cohesion: 0.08
Nodes (12): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, all_specs() (+4 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.19
Nodes (6): _hash_value(), make_evidence_json(), redact_evidence(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestRedactEvidence

### Community 530 - "pandas"
Cohesion: 0.06
Nodes (19): generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize(), _alternatives(), any_pattern() (+11 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 635 - "_is_null"
Cohesion: 0.14
Nodes (8): _build_suggestion(), _feasible_evidence(), _infeasible_evidence(), _is_null(), _make_tooltip(), _non_null_cells(), _tooltip_content(), TooltipContent

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.11
Nodes (9): _blocking_keys(), _closest_pair(), differing_token_lengths(), min_pairwise_edit_distance(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance() (+1 more)

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 835 - "json"
Cohesion: 0.09
Nodes (14): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, git_commit(), _build_config(), _load_corpus_tables(), _load_targets() (+6 more)

### Community 1144 - "TestEnsureDataFrameIsSpark"
Cohesion: 0.17
Nodes (6): 7.1 Architecture Overview, 7.3 Technology, 7.4 Assumptions, 7. Solution, _ensure_dataframe_is_spark(), TestEnsureDataFrameIsSpark

### Community 1156 - "RahaConfig"
Cohesion: 0.14
Nodes (9): ColumnPredictions, _make_classifier(), train_and_predict(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases, TestDeterminismAndSeeding (+1 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.10
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 1219 - "perturbation.py"
Cohesion: 0.09
Nodes (11): fd_compliance_ratio(), minority_violation_rows(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices (+3 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1430 - "conftest.py"
Cohesion: 0.11
Nodes (13): candidates(), main(), select(), A fully local example, Configuration, How it works, Install, Operational notes (+5 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1096 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **34 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `run_raha`, `AutoValidateAlgorithm`, `open_detect/exceptions.py`, `_is_null`, `test_console_scripts.py`, `test_raha_strategies.py`, `InferredPattern`, `_build_index`, `TestUniDetectDetect`, `real_world_gov/run_benchmark.py`, `_build_index`, `auto_validate/detector.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.09268292682926829 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `TestDetectCacheLifecycleSpark`, `_StubDetector`, `build_corpus_statistics.py`, `.test_shared_columns_df_unpersisted_at_end`, `FailureCounts`, `test_raha_strategies.py`, `raha/detector.py`, `conftest.py`, `ErrorType`, `_mock_spark_context`, `main`, `Detection`, `real_world_gov/run_benchmark.py`, `UniDetect`, `json`, `CorpusStatsStore`, `Uni-Detect`, `uni_detect/core/models.py`, `make_evidence_json`, `featurization.py`, `UniDetect`, `test_pipeline.py`, `5. Market Segment(s)`, `open_detect/exceptions.py`, `pipeline.py`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Are the 68 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 68 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._