# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-23)

## Corpus Check
- 201 files · ~166,424 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3171 nodes · 6926 edges · 176 communities (137 shown, 39 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 887 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9d4997eb`
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
- uni_detect/config.py
- _segment_dp
- notifications/config.py
- FailureCounts
- README.md — Uni-Detect overview
- build_column_features
- new_cluster
- CellResult
- AutoValidateConfig
- check_drift
- test_spelling_detector.py
- pandas
- ErrorDetectionAlgorithm
- auto_validate/detector.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- _segment_dp
- perturbation.py
- ConfigurationError
- _ensure_sequence_of_str
- AlgorithmResult
- .detect
- __getattr__
- numpy
- main
- pytest
- TestUniDetectDetect
- AutoValidateAlgorithm
- _check_unknown_kwargs
- _check_expected_type
- algorithms/index.md
- real_world_gov benchmark results
- _FakeDetector
- CorpusStatsBuilder
- ErrorType
- `auto_validate`
- _value_matches
- FailureCountsAccumulatorParam
- fresh_registry
- CHANGELOG
- builder.py
- propagate_labels
- SlidingWindowRateLimiter
- _FakeDetector
- UniDetectConfig
- index.py
- updates
- algorithms/index.md
- jobs
- UniDetect
- argparse
- _coerce_numeric
- build
- uses
- list_algorithms
- env
- docs/index.md
- CorpusStatsStore
- dry_run
- _score_single_column
- FeatureBucket
- CorpusIngestor
- variables
- Auto-Validate
- PRD: API Validation Framework for open-detect
- dev
- index.py
- dataset_utils.py
- .send
- TeamsNotifier
- Current Status: BLOCKED
- _reference_build_pattern_index
- UniDetect
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- test
- OPE-89: Fix Spark Cache Lifecycle in Uni-Detect
- release.yml
- release
- real_world_gov/generate_report.py
- HeuristicLabeler
- pypi
- Current Status: BLOCKED
- tokenize
- real_world_gov/run_benchmark.py
- with
- on
- .build_index
- steps
- score
- labeling.py
- _segment_dp
- builder.py
- ConfigurationError
- sonarqube
- perturb_numeric_outlier
- infer_column_data_type
- docs
- force
- get_spec
- test_logging_utils.py
- algorithms.md
- .detect
- sys
- open-detect
- argparse
- test_package_init.py
- _require_columns
- `uni_detect`
- `raha`
- test_teams.py
- _aggregate_scored_rows
- _make_tiny_corpus
- paperclip-issue-update.sh
- bucket_by_edges
- .send_safe
- ValidationError
- FeatureBucket
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- select_fd_column_pairs
- perturb_spelling
- infer_column_data_type
- _ensure_dataframe_is_spark
- argparse
- Appendix: Validation Function Reference
- .detect
- test_build_corpus_statistics.py
- is_mixed_alphanumeric
- _check_dataframe_is_spark
- Changes Verified
- reference/index.md
- is_float_like
- is_integer_like
- ._check_rate_limit
- _reject_unknown_kwargs
- _StubDetector
- TestSeverityOrdering
- OPE-86 / PR #96 — Copilot Review Fixes
- config
- __getattr__
- _detector
- _random_words
- SparkJobCounter
- featurization.py
- scoped_conf
- pipeline.py
- metrics/spelling.py
- auto_validate/detector.py
- test_bench_snapshot.py
- finite_floats
- outliers.py
- min_pairwise_edit_distance
- InsufficientDataError
- snapshot.py
- Labeler
- real_world_gov/run_benchmark.py
- Auto-Validate
- RahaDetector
- wiki_subset/generate_report.py
- uniqueness_ratio
- Performance Baseline — OPE-87
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 97 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 70 edges
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

## Communities (176 total, 39 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.10
Nodes (10): diff_fingerprints(), read_build_config(), verify_build_config(), _config(), FakeConf, FakeSpark, test_diff_fingerprints_reports_missing_fields(), TestLegacyCorpus (+2 more)

### Community 1 - "builder.py"
Cohesion: 0.10
Nodes (10): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestDetectCacheLifecycleSpark, test_build_row_maps_row_ids_via_original_positions(), TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation (+2 more)

### Community 2 - "detectors/spelling.py"
Cohesion: 0.11
Nodes (19): _city_column(), _count_detect_calls(), _counting_value_matches_groups(), counting(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference() (+11 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "uni_detect/config.py"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 8 - "_segment_dp"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "notifications/config.py"
Cohesion: 0.07
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (11): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, compute() (+3 more)

### Community 11 - "README.md — Uni-Detect overview"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "build_column_features"
Cohesion: 0.07
Nodes (18): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, build_all_features(), build_column_features(), _compact_dtype() (+10 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.10
Nodes (7): open-detect, What is in the box, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "AutoValidateConfig"
Cohesion: 0.10
Nodes (8): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "check_drift"
Cohesion: 0.10
Nodes (8): _infer_pattern_to_groups(), check_drift(), _clean_series(), _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.10
Nodes (16): _hash_value(), make_evidence_json(), redact_evidence(), _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row() (+8 more)

### Community 18 - "pandas"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.15
Nodes (12): ErrorDetectionAlgorithm, TooltipContent, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm() (+4 more)

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (21): Variants, _build_suggestion(), _make_tooltip(), _matches_segments(), _tooltip_content(), _conforms(), _conforms_segments(), _clean() (+13 more)

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

### Community 26 - "_segment_dp"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "perturbation.py"
Cohesion: 0.15
Nodes (8): _score_pair(), _score_column(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 30 - "AlgorithmResult"
Cohesion: 0.14
Nodes (3): UniDetectConfig, config(), TestUniDetectConfig

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "numpy"
Cohesion: 0.06
Nodes (23): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), _assert_same() (+15 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.07
Nodes (12): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 36 - "TestUniDetectDetect"
Cohesion: 0.10
Nodes (12): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Which 5 datasets, and why (+4 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.14
Nodes (6): Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm, segment(), TestAutoValidateDetector

### Community 38 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 39 - "_check_expected_type"
Cohesion: 0.10
Nodes (5): get_spark(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSparkExtended, TestGetSpark

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "CorpusStatsBuilder"
Cohesion: 0.16
Nodes (7): CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 45 - "`auto_validate`"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "_value_matches"
Cohesion: 0.13
Nodes (15): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+7 more)

### Community 48 - "fresh_registry"
Cohesion: 0.11
Nodes (12): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy() (+4 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.05
Nodes (36): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+28 more)

### Community 50 - "builder.py"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 51 - "propagate_labels"
Cohesion: 0.09
Nodes (9): fmdv_v(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV, TestFmdvVh, TestLargeGroups (+1 more)

### Community 52 - "SlidingWindowRateLimiter"
Cohesion: 0.13
Nodes (3): SlidingWindowRateLimiter, TestEdgeCases, TestSlidingWindowRateLimiter

### Community 54 - "UniDetectConfig"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 55 - "index.py"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "algorithms/index.md"
Cohesion: 0.18
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, ColumnFeatures, HeuristicLabeler, _resolve_position() (+1 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.17
Nodes (6): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "argparse"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "list_algorithms"
Cohesion: 0.11
Nodes (12): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+4 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "docs/index.md"
Cohesion: 0.23
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "CorpusStatsStore"
Cohesion: 0.12
Nodes (4): CorpusStatsStore, TestBatchScoreOptimization, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "FeatureBucket"
Cohesion: 0.10
Nodes (11): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, TestCandidate (+3 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.13
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "index.py"
Cohesion: 0.08
Nodes (13): DriftResult, _append_literal(), _char_class(), _class_of_token(), _is_numeric(), matches_tokens(), _parse(), _part_matches() (+5 more)

### Community 77 - "dataset_utils.py"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 79 - "TeamsNotifier"
Cohesion: 0.16
Nodes (3): TeamsNotifier, TestBuildAdaptiveCard, TestTeamsNotifierInit

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_reference_build_pattern_index"
Cohesion: 0.12
Nodes (7): clean_column(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild

### Community 83 - "UniDetect"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.40
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "OPE-89: Fix Spark Cache Lifecycle in Uni-Detect"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "real_world_gov/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 90 - "HeuristicLabeler"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tokenize"
Cohesion: 0.19
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 94 - "real_world_gov/run_benchmark.py"
Cohesion: 0.11
Nodes (13): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, _build_config(), main(), _print_comparison() (+5 more)

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - ".build_index"
Cohesion: 0.13
Nodes (8): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "score"
Cohesion: 0.12
Nodes (16): Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema (+8 more)

### Community 100 - "labeling.py"
Cohesion: 0.08
Nodes (14): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, GroundTruthLabeler (+6 more)

### Community 101 - "_segment_dp"
Cohesion: 0.12
Nodes (12): Recent Changes, Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps (+4 more)

### Community 102 - "builder.py"
Cohesion: 0.06
Nodes (7): build_spark(), main(), property_key(), write_build_config(), TestCorpusStatsSchema, TestCorpusStatsSchemaWeightType, TestWiring

### Community 103 - "ConfigurationError"
Cohesion: 0.08
Nodes (17): Errors, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, _validate_edges(), CorpusNotFoundError (+9 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (4): _score_column(), perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 106 - "infer_column_data_type"
Cohesion: 0.33
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_spec"
Cohesion: 0.10
Nodes (6): all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 110 - "test_logging_utils.py"
Cohesion: 0.09
Nodes (9): _build_token_stats_impl(), _compute_token_counts_batch(), _count_tables_batch(), configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger (+1 more)

### Community 111 - "algorithms.md"
Cohesion: 0.50
Nodes (3): Registry, Registry and results, Result types

### Community 112 - ".detect"
Cohesion: 0.18
Nodes (6): _distinct_value_verdicts_groups(), _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches_groups()

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "_require_columns"
Cohesion: 0.22
Nodes (3): _filter_by_column_type(), _require_columns(), TestRequireColumns

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 121 - "_aggregate_scored_rows"
Cohesion: 0.18
Nodes (3): _aggregate_scored_rows(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 126 - "bucket_by_edges"
Cohesion: 0.19
Nodes (4): bucket_by_edges(), bucket_leftness(), bucket_token_prevalence(), TestBucketing

### Community 128 - "ValidationError"
Cohesion: 0.19
Nodes (8): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, ValidationError, _validate_literal_value(), TestValidateLiteralValue

### Community 130 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 131 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 132 - "perturb_spelling"
Cohesion: 0.29
Nodes (3): _score_column(), perturb_spelling(), TestPerturbSpelling

### Community 135 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 136 - "Appendix: Validation Function Reference"
Cohesion: 0.28
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_columns_unique(), TestCheckColumnsUnique

### Community 137 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 138 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 141 - "Changes Verified"
Cohesion: 0.33
Nodes (5): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results

### Community 149 - "OPE-86 / PR #96 — Copilot Review Fixes"
Cohesion: 0.40
Nodes (4): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "_random_words"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "SparkJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "featurization.py"
Cohesion: 0.24
Nodes (7): bucket_row_count(), bucket_token_length(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket(), TestFeatureBucketBuilders

### Community 433 - "pipeline.py"
Cohesion: 0.10
Nodes (8): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, _spark_available()

### Community 527 - "metrics/spelling.py"
Cohesion: 0.18
Nodes (8): drop_nulls(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance(), TestDropNulls

### Community 530 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (19): generality_weight(), generalize(), _iter_runs(), Token, tokenize(), _alternatives(), any_pattern(), _best_first_patterns() (+11 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 686 - "outliers.py"
Cohesion: 0.15
Nodes (9): require_min_size(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+1 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.16
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 711 - "InsufficientDataError"
Cohesion: 0.15
Nodes (8): _require_min_rows(), InsufficientDataError, main(), parse_args(), _run(), test_main_installs_logging(), TestMain, TestParseArgs

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "Labeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.09
Nodes (12): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main() (+4 more)

### Community 1123 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1156 - "RahaDetector"
Cohesion: 0.19
Nodes (7): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 1219 - "uniqueness_ratio"
Cohesion: 0.19
Nodes (4): duplicate_value_indices(), uniqueness_ratio(), TestDuplicateValueIndices, TestUniquenessRatio

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1430 - "conftest.py"
Cohesion: 0.10
Nodes (15): A fully local example, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect, Installation, Installing from source (+7 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1166 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **39 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ValidationError` connect `ValidationError` to `uni_detect/config.py`, `Appendix: Validation Function Reference`, `_check_dataframe_is_spark`, `metrics/spelling.py`, `AutoValidateConfig`, `_reject_unknown_kwargs`, `auto_validate/detector.py`, `OPE-86 / PR #96 — Copilot Review Fixes`, `ConfigurationError`, `_ensure_sequence_of_str`, `pytest`, `_check_unknown_kwargs`, `pipeline.py`, `UniDetect`, `min_pairwise_edit_distance`, `_score_single_column`, `FeatureBucket`, `PRD: API Validation Framework for open-detect`, `index.py`, `_reference_build_pattern_index`, `UniDetect`, `builder.py`, `ConfigurationError`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.09672830725462304 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `pipeline.py` to `verify_build_config`, `FeatureBucket`, `builder.py`, `.detect`, `FailureCounts`, `test_build_corpus_statistics.py`, `ErrorDetectionAlgorithm`, `_StubDetector`, `conftest.py`, `main`, `_check_expected_type`, `CorpusStatsBuilder`, `_FakeDetector`, `UniDetect`, `list_algorithms`, `real_world_gov/run_benchmark.py`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `InsufficientDataError`, `featurization.py`, `UniDetect`, `real_world_gov/run_benchmark.py`, `builder.py`, `get_spec`, `_require_columns`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._