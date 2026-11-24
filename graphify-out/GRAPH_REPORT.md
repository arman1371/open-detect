# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-24)

## Corpus Check
- 201 files · ~168,378 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3236 nodes · 7074 edges · 192 communities (146 shown, 46 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 910 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a0b175e0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- builder.py
- detectors/spelling.py
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- json
- _segment_dp
- wiki_subset/run_benchmark.py
- FailureCounts
- README.md — Uni-Detect overview
- .batch_score
- new_cluster
- CellResult
- build_pattern_index
- check_drift
- test_spelling_detector.py
- pandas
- ErrorDetectionAlgorithm
- fmdv_v
- permissions
- with
- update-graph
- check_failure_threshold
- with
- list_tables
- perturbation.py
- .detect
- _check_expected_type
- UniDetectConfig
- .detect
- ScoringJobCounter
- numpy
- main
- pytest
- pipeline.py
- AutoValidateAlgorithm
- real_world_gov/generate_report.py
- get_logger
- Contributing
- real_world_gov benchmark results
- _FakeDetector
- _value_matches
- _build_index
- `auto_validate`
- _value_matches
- FailureCountsAccumulatorParam
- .detect
- CHANGELOG
- builder.py
- list_algorithms
- UniDetectAlgorithm
- InsufficientDataError
- UniDetectConfig
- index.py
- updates
- algorithms/index.md
- jobs
- ErrorType
- test_bench_spark_jobs.py
- _coerce_numeric
- build
- uses
- dataset_utils.py
- env
- choosing-an-algorithm.md
- CorpusStatsStore
- dry_run
- _score_single_column
- FeatureBucket
- CorpusIngestor
- variables
- _row
- PRD: API Validation Framework for open-detect
- dev
- index.py
- PatternIndex
- RahaDetector
- infer_column_data_type
- Current Status: BLOCKED
- test_auto_validate_index.py
- _config
- CorpusStatsStore
- test
- _check_expected_type
- release.yml
- release
- argparse
- .batch_score
- pypi
- Current Status: BLOCKED
- tokenize
- select_datasets.py
- with
- on
- TestBatchScoreOptimization
- steps
- RahaDetector
- labeling.py
- perturb_numeric_outlier
- TestCorpusStatsSchema
- OpenDetectError
- sonarqube
- Contributing
- Installation
- docs
- force
- profile.py
- catalog.py
- .detect
- sys
- open-detect
- Scoring auto_validate
- reference/index.md
- ConfigurationError
- `uni_detect`
- Commit conventions and releases
- Benchmarks
- _value_matches_groups
- Choosing an algorithm
- paperclip-issue-update.sh
- bucket_by_edges
- get_logger
- _search_mpd
- TestAttempt
- Auto-Validate
- test_algorithms_registry.py
- score
- infer_column_data_type
- _StubDetector
- TestSeverityOrdering
- _filter_by_column_type
- test_metrics.py
- algorithms/index.md
- 7.2 Key Features
- _check_unknown_kwargs
- FeatureBucket
- uniqueness_ratio
- _ensure_sequence_of_str
- Appendix: Validation Function Reference
- _ensure_dataframe_is_spark
- TestUniDetectBaselineDiff
- ValidationError
- _FakeDetector
- 1. Implement `ErrorDetectionAlgorithm`
- Detection
- _date_index
- _check_dataframe_is_spark
- FakeConf
- is_integer_like
- _validate_literal_value
- _reject_unknown_kwargs
- TestConfigThreshold
- `uni_detect`
- `raha`
- OPE-86 / PR #96 — Copilot Review Fixes
- open_detect_wheel
- Raha
- finite_floats
- v0.2.8 (2026-11-05)
- Raha
- ComparisonDirection
- 5. Market Segment(s)
- diff_fingerprints
- TestUniDetectCacheLifecycle
- Registry and results
- TestCorpusStatsSchemaWeightType
- _NoCandidatesDetector
- _detector
- featurization.py
- scoped_conf
- detectors/base.py
- make_evidence_json
- auto_validate/detector.py
- test_bench_snapshot.py
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- KnownIndexLabeler
- real_world_gov/run_benchmark.py
- RahaDetector
- wiki_subset/generate_report.py
- Performance Baseline — OPE-87
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 102 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 86 edges
5. `FailureCounts` - 56 edges
6. `ValidationError` - 48 edges
7. `TeamsNotifier` - 48 edges
8. `UnityCatalogLocation` - 47 edges
9. `build_pattern_index()` - 46 edges
10. `AutoValidateAlgorithm` - 39 edges

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

## Communities (192 total, 46 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.14
Nodes (10): property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, TestLegacyCorpus, TestMismatch (+2 more)

### Community 1 - "builder.py"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 2 - "detectors/spelling.py"
Cohesion: 0.12
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

### Community 7 - "json"
Cohesion: 0.08
Nodes (13): _score_pair(), _score_column(), _score_column(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness() (+5 more)

### Community 8 - "_segment_dp"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "wiki_subset/run_benchmark.py"
Cohesion: 0.09
Nodes (16): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets() (+8 more)

### Community 10 - "FailureCounts"
Cohesion: 0.18
Nodes (7): compute(), _score_fd_pair(), compute(), compute(), compute(), FailureCounts, TestPerElementFunctions

### Community 11 - "README.md — Uni-Detect overview"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - ".batch_score"
Cohesion: 0.13
Nodes (9): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features() (+1 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.10
Nodes (7): open-detect, What is in the box, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "build_pattern_index"
Cohesion: 0.08
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "pandas"
Cohesion: 0.07
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 20 - "fmdv_v"
Cohesion: 0.10
Nodes (10): Variants, Recent Changes, _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV (+2 more)

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

### Community 26 - "list_tables"
Cohesion: 0.08
Nodes (13): list_tables(), list_tables_matching(), table_exists(), main(), parse_args(), _run(), test_main_installs_logging(), TestMain (+5 more)

### Community 27 - "perturbation.py"
Cohesion: 0.11
Nodes (13): ErrorDetectionAlgorithm, TooltipContent, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm() (+5 more)

### Community 28 - ".detect"
Cohesion: 0.19
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 30 - "UniDetectConfig"
Cohesion: 0.14
Nodes (4): UniDetectConfig, config(), TestUniDetectConfig, config()

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "ScoringJobCounter"
Cohesion: 0.10
Nodes (4): ScopeStats, ScoringJobCounter, counting_batch_score(), TestDetectCacheLifecycleSpark

### Community 33 - "numpy"
Cohesion: 0.08
Nodes (19): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), _assert_same(), _naive_fd() (+11 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.09
Nodes (12): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 36 - "pipeline.py"
Cohesion: 0.13
Nodes (13): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results (+5 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "real_world_gov/generate_report.py"
Cohesion: 0.13
Nodes (3): SlidingWindowRateLimiter, TestEdgeCases, TestSlidingWindowRateLimiter

### Community 39 - "get_logger"
Cohesion: 0.20
Nodes (3): get_spark(), TestGetSparkExtended, TestGetSpark

### Community 40 - "Contributing"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "_value_matches"
Cohesion: 0.14
Nodes (14): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+6 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "_value_matches"
Cohesion: 0.11
Nodes (12): _build_suggestion(), _distinct_value_verdicts_groups(), _feasible_evidence(), _infeasible_evidence(), _infer_pattern_to_groups(), _is_null(), _make_tooltip(), _non_null_cells() (+4 more)

### Community 48 - ".detect"
Cohesion: 0.09
Nodes (6): Completed Work, _mock_detector_result(), _mock_spark_context(), TestUniDetectColumnTypeRouting, TestUniDetectSharedIngestionOnce, TestUniDetectSingleScanIngestion

### Community 49 - "CHANGELOG"
Cohesion: 0.06
Nodes (32): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+24 more)

### Community 50 - "builder.py"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 51 - "list_algorithms"
Cohesion: 0.16
Nodes (8): list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), test_builtin_algorithms_are_registered(), TestPluginDiscovery, worker()

### Community 53 - "InsufficientDataError"
Cohesion: 0.11
Nodes (8): _require_min_rows(), InsufficientDataError, require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), TestScoreFdPair, TestFunctionalDependency

### Community 54 - "UniDetectConfig"
Cohesion: 0.16
Nodes (3): TeamsNotifier, TestBuildAdaptiveCard, TestTeamsNotifierInit

### Community 55 - "index.py"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "algorithms/index.md"
Cohesion: 0.11
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "ErrorType"
Cohesion: 0.11
Nodes (14): API reference, build_spark(), main(), ErrorType, UniDetect, _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path() (+6 more)

### Community 60 - "test_bench_spark_jobs.py"
Cohesion: 0.18
Nodes (8): SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported(), test_scopes_use_distinct_job_groups()

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "choosing-an-algorithm.md"
Cohesion: 0.18
Nodes (8): Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "CorpusStatsStore"
Cohesion: 0.17
Nodes (4): _aggregate_scored_rows(), compute(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "FeatureBucket"
Cohesion: 0.12
Nodes (9): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, __getattr__(), TestCandidate, TestCorpusRecords (+1 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.10
Nodes (6): balanced_union(), CorpusIngestor, log_duration(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "_row"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.15
Nodes (12): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+4 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "index.py"
Cohesion: 0.08
Nodes (14): _append_literal(), _is_numeric(), matches(), matches_tokens(), _parse(), _part_matches(), token_count(), indexable_values() (+6 more)

### Community 77 - "PatternIndex"
Cohesion: 0.07
Nodes (16): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary (+8 more)

### Community 78 - "RahaDetector"
Cohesion: 0.21
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 79 - "infer_column_data_type"
Cohesion: 0.18
Nodes (4): infer_column_data_type(), is_mixed_alphanumeric(), TestDataTypeInference, TestMixedAlphanumeric

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "test_auto_validate_index.py"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "_config"
Cohesion: 0.11
Nodes (6): _config(), _mock_spark(), TestUniDetectDetect, TestUniDetectInit, TestUniDetectRelease, TestUniDetectValidateInputs

### Community 84 - "CorpusStatsStore"
Cohesion: 0.22
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "_check_expected_type"
Cohesion: 0.25
Nodes (7): Blockers, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "argparse"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - ".batch_score"
Cohesion: 0.21
Nodes (5): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tokenize"
Cohesion: 0.13
Nodes (7): compute_token_counts(), token_prevalence(), is_float_like(), tokenize(), TestTokenPrevalence, TestFloatLike, TestTokenize

### Community 94 - "select_datasets.py"
Cohesion: 0.46
Nodes (3): candidates(), main(), select()

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "RahaDetector"
Cohesion: 0.31
Nodes (5): RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 100 - "labeling.py"
Cohesion: 0.19
Nodes (4): CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "perturb_numeric_outlier"
Cohesion: 0.24
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 103 - "OpenDetectError"
Cohesion: 0.14
Nodes (11): Operational notes, Errors, CorpusNotFoundError, IndexNotBuiltError, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error() (+3 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "Contributing"
Cohesion: 0.18
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 106 - "Installation"
Cohesion: 0.50
Nodes (4): Check it works, Installation, Installing from source, Pick your extra

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "profile.py"
Cohesion: 0.22
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 115 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 116 - "reference/index.md"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 118 - "`uni_detect`"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

### Community 119 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 121 - "_value_matches_groups"
Cohesion: 0.29
Nodes (4): _matches_segments(), _value_matches_groups(), _counting_value_matches_groups(), counting()

### Community 122 - "Choosing an algorithm"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 126 - "bucket_by_edges"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 127 - "get_logger"
Cohesion: 0.12
Nodes (5): configure_logging(), get_logger(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 128 - "_search_mpd"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 130 - "Auto-Validate"
Cohesion: 0.17
Nodes (10): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+2 more)

### Community 131 - "test_algorithms_registry.py"
Cohesion: 0.10
Nodes (9): get_algorithm(), get_algorithm_class(), test_registered_under_raha(), real_plugin_path(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy(), test_unknown_algorithm_raises(), TestPluginDiscoveryViaRealDistInfo (+1 more)

### Community 132 - "score"
Cohesion: 0.12
Nodes (16): Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema (+8 more)

### Community 134 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 137 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 138 - "algorithms/index.md"
Cohesion: 0.20
Nodes (3): Algorithms, Fidelity to the papers, Errors

### Community 139 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 140 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 144 - "Appendix: Validation Function Reference"
Cohesion: 0.28
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_columns_unique(), TestCheckColumnsUnique

### Community 147 - "ValidationError"
Cohesion: 0.29
Nodes (6): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, ValidationError

### Community 149 - "1. Implement `ErrorDetectionAlgorithm`"
Cohesion: 0.33
Nodes (6): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm

### Community 151 - "_date_index"
Cohesion: 0.40
Nodes (3): _date_index(), _date_values(), TestLargeGroups

### Community 158 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 159 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 160 - "OPE-86 / PR #96 — Copilot Review Fixes"
Cohesion: 0.40
Nodes (4): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 161 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 162 - "Raha"
Cohesion: 0.40
Nodes (5): Configuration, How it works, Install, Raha, Scope

### Community 164 - "v0.2.8 (2026-11-05)"
Cohesion: 0.50
Nodes (4): Documentation, Performance Improvements, Refactoring, v0.2.8 (2026-11-05)

### Community 165 - "Raha"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 167 - "5. Market Segment(s)"
Cohesion: 0.50
Nodes (4): 5.1 Primary Segment, 5.2 Secondary Segment, 5.3 Constraints, 5. Market Segment(s)

### Community 171 - "Registry and results"
Cohesion: 0.67
Nodes (3): Registry, Registry and results, Result types

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 339 - "featurization.py"
Cohesion: 0.12
Nodes (11): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 433 - "detectors/base.py"
Cohesion: 0.06
Nodes (11): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, all_specs(), ErrorTypeSpec (+3 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.22
Nodes (6): _hash_value(), make_evidence_json(), redact_evidence(), compute(), _score_column(), TestRedactEvidence

### Community 530 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (19): _char_class(), _class_of_token(), generality_weight(), generalize(), _iter_runs(), Token, tokenize(), _alternatives() (+11 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 686 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.21
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.09
Nodes (12): confusion_metrics(), maybe_scope(), UniDetectProfile, Methodology: raha, _build_config(), main(), _print_comparison(), _register_table() (+4 more)

### Community 1156 - "RahaDetector"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1430 - "conftest.py"
Cohesion: 0.13
Nodes (11): A fully local example, Corpus Statistics Schema (OPE-92), How it works, Install, Uni-Detect, _cap_driver_memory(), _delta_jars(), _download() (+3 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1203 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **46 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `_StubDetector`, `_filter_by_column_type`, `wiki_subset/run_benchmark.py`, `FailureCounts`, `FeatureBucket`, `ErrorDetectionAlgorithm`, `_FakeDetector`, `conftest.py`, `Detection`, `list_tables`, `perturbation.py`, `.detect`, `ScoringJobCounter`, `main`, `ComparisonDirection`, `TestUniDetectCacheLifecycle`, `_NoCandidatesDetector`, `.detect`, `detectors/base.py`, `InsufficientDataError`, `real_world_gov/run_benchmark.py`, `_score_single_column`, `FeatureBucket`, `featurization.py`, `CorpusStatsStore`, `_config`, `.batch_score`, `TestBatchScoreOptimization`, `catalog.py`, `get_logger`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.14112903225806453 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `build_pattern_index` to `real_world_gov/run_benchmark.py`, `score`, `AutoValidateAlgorithm`, `wiki_subset/run_benchmark.py`, `index.py`, `PatternIndex`, `_value_matches`, `check_drift`, `fmdv_v`, `ConfigurationError`, `index.py`, `_date_index`, `ErrorType`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 70 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._