# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-16)

## Corpus Check
- 192 files · ~160,079 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3000 nodes · 6588 edges · 162 communities (130 shown, 32 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 832 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7b07d831`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- write_build_config
- UnityCatalogLocation
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- fd_compliance_ratio
- README.md — Uni-Detect overview
- .build_index
- FailureCounts
- PRD: User Feedback Tooltips
- build_column_features
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- 7.2 Key Features
- ErrorDetectionAlgorithm
- test_auto_validate_fmdv_v.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- builder.py
- _run
- _check_expected_type
- ValidationError
- UniDetectConfig
- cluster_column
- get_algorithm
- numpy
- main
- pytest
- CorpusStatsBuilder
- .detect
- Labeler
- log_duration
- CellResult
- real_world_gov benchmark results
- verify_build_config
- test_build_corpus_statistics.py
- log_transform_fits_better
- Benchmark: WIKI subset
- _make_tooltip
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- Auto-Validate
- fmdv_v
- .detect
- choosing-an-algorithm.md
- algorithms/index.md
- fmdv.py
- updates
- HeuristicLabeler
- jobs
- .build_corpus_statistics
- main
- _coerce_numeric
- build
- uses
- run_raha
- env
- perturb_spelling
- CorpusStatsStore
- dry_run
- _score_single_column
- FeatureBucket
- CorpusIngestor
- variables
- patterns_of
- PRD: API Validation Framework for open-detect
- dev
- test_auto_validate_index.py
- Commit conventions and releases
- RahaDetector
- test_cache_lifecycle.py
- Current Status: BLOCKED
- _aggregate_scored_rows
- _config
- algorithms/index.md
- test
- test_bench_snapshot.py
- release.yml
- release
- CorpusNotFoundError
- bucket_by_edges
- pypi
- Current Status: BLOCKED
- tokenize
- spark_session.py
- with
- on
- get_algorithm
- steps
- argparse
- CallableLabeler
- _segment_dp
- get_algorithm_class
- OpenDetectError
- sonarqube
- _make_classifier
- infer_column_data_type
- docs
- force
- uni_detect/core/enums.py
- pipeline.py
- algorithms/uni-detect.md
- select_fd_column_pairs
- sys
- open-detect
- TestConfigThreshold
- test_console_scripts.py
- test_algorithms_registry.py
- `uni_detect`
- `raha`
- Concepts
- AutoValidateAlgorithm
- TestDetectCacheLifecycleSpark
- paperclip-issue-update.sh
- algorithms/index.md
- Auto-Validate
- open_detect_wheel
- config
- config
- _value_matches
- ._new_failure_tracker
- Uni-Detect
- __getattr__
- _detector
- test_metrics.py
- ScoringJobCounter
- featurization.py
- .detect
- _FakeDetector
- ErrorType
- detectors/base.py
- hierarchy.py
- perturb_numeric_outlier
- _ensure_sequence_of_str
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- labeling.py
- json
- Auto-Validate
- _check_unknown_kwargs
- RahaConfig
- wiki_subset/generate_report.py
- builder.py
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 97 edges
3. `UniDetectConfig` - 93 edges
4. `UniDetect` - 70 edges
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

## Communities (162 total, 32 thin omitted)

### Community 0 - "write_build_config"
Cohesion: 0.09
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeConf, FakeSpark (+4 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.15
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 2 - "pandas"
Cohesion: 0.06
Nodes (37): _is_null(), _non_null_cells(), _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting() (+29 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "fd_compliance_ratio"
Cohesion: 0.16
Nodes (6): InsufficientDataError, require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - ".build_index"
Cohesion: 0.20
Nodes (8): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (11): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, compute() (+3 more)

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "InferredPattern"
Cohesion: 0.08
Nodes (12): _infer_pattern_to_groups(), _matches_segments(), check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed() (+4 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.10
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "7.2 Key Features"
Cohesion: 0.25
Nodes (8): 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific), 7.2 Key Features

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.14
Nodes (10): 5.1 Primary Segment, 5.2 Secondary Segment, 5.3 Constraints, 5. Market Segment(s), ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect() (+2 more)

### Community 20 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.11
Nodes (9): min_conforming(), _build_index(), _date_index(), _date_values(), TestFmdvV, TestFmdvVh, TestLargeGroups, TestMinConforming (+1 more)

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

### Community 26 - "builder.py"
Cohesion: 0.12
Nodes (3): TestCorpusStatsSchema, TestCorpusStatsSchemaWeightType, TestScoreFdPair

### Community 27 - "_run"
Cohesion: 0.15
Nodes (8): list_tables(), list_tables_matching(), table_exists(), _run(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 29 - "ValidationError"
Cohesion: 0.08
Nodes (16): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, Appendix: Validation Function Reference, _check_columns_present(), ValidationError (+8 more)

### Community 31 - "cluster_column"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "get_algorithm"
Cohesion: 0.13
Nodes (9): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, list_algorithms(), test_builtin_algorithms_are_registered() (+1 more)

### Community 33 - "numpy"
Cohesion: 0.06
Nodes (23): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), _assert_same() (+15 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.08
Nodes (12): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 36 - "CorpusStatsBuilder"
Cohesion: 0.17
Nodes (7): CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 38 - "Labeler"
Cohesion: 0.18
Nodes (11): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs (+3 more)

### Community 39 - "log_duration"
Cohesion: 0.14
Nodes (3): balanced_union(), log_duration(), TestLogDuration

### Community 40 - "CellResult"
Cohesion: 0.18
Nodes (5): open-detect, What is in the box, Why a common interface, CellResult, TestCellResultEvidence

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "_make_tooltip"
Cohesion: 0.15
Nodes (7): _build_suggestion(), _feasible_evidence(), _infeasible_evidence(), _make_tooltip(), _tooltip_content(), pattern_to_language(), TooltipContent

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.20
Nodes (6): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), TestPluginDiscovery, worker()

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 51 - "fmdv_v"
Cohesion: 0.08
Nodes (14): Recent Changes, _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_v(), fmdv_vh(), _segment_dp(), _segment_fmdv_v() (+6 more)

### Community 52 - ".detect"
Cohesion: 0.16
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "choosing-an-algorithm.md"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 54 - "algorithms/index.md"
Cohesion: 0.13
Nodes (13): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+5 more)

### Community 55 - "fmdv.py"
Cohesion: 0.08
Nodes (9): Variants, _clean(), fmdv(), fmdv_h(), sorted_patterns(), _build_index(), TestFmdvBasic, TestFmdvH (+1 more)

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "HeuristicLabeler"
Cohesion: 0.18
Nodes (11): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions? (+3 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.14
Nodes (7): build_spark(), main(), _filter_by_column_type(), _require_columns(), TestCorpusBuilderAndDetectors, _write_table(), TestRequireColumns

### Community 60 - "main"
Cohesion: 0.18
Nodes (5): main(), parse_args(), test_main_installs_logging(), TestMain, TestParseArgs

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
Cohesion: 0.11
Nodes (4): CorpusStatsStore, TestBatchScoreOptimization, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "FeatureBucket"
Cohesion: 0.13
Nodes (9): Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, TestCandidate, TestCorpusRecords, TestDetection (+1 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.11
Nodes (6): CorpusIngestor, compute_token_counts(), TestCorpusIngestorSkipsBadInputs, TestDetectReturnsEmptyResultWhenNoCandidates, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "patterns_of"
Cohesion: 0.19
Nodes (3): patterns_of(), TestMatching, TestPatternsOf

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.11
Nodes (17): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+9 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_auto_validate_index.py"
Cohesion: 0.08
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "RahaDetector"
Cohesion: 0.25
Nodes (4): GroundTruthLabeler, _resolve_position(), _values_equal(), TestGroundTruthLabeler

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.22
Nodes (3): _aggregate_scored_rows(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "_config"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "algorithms/index.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

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

### Community 89 - "CorpusNotFoundError"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tokenize"
Cohesion: 0.33
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 94 - "spark_session.py"
Cohesion: 0.13
Nodes (9): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution (+1 more)

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "get_algorithm"
Cohesion: 0.20
Nodes (7): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.13
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "_segment_dp"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "get_algorithm_class"
Cohesion: 0.24
Nodes (7): _constant_factory(), get_algorithm_class(), _load_entry_points(), register_lazy(), test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name(), test_unknown_algorithm_raises()

### Community 103 - "OpenDetectError"
Cohesion: 0.09
Nodes (16): Errors, Errors, _validate_edges(), CorpusNotFoundError, DataQualityError, UnityCatalogError, ConfigurationError, IndexNotBuiltError (+8 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "_make_classifier"
Cohesion: 0.32
Nodes (3): _make_classifier(), TestDeterminismAndSeeding, factory()

### Community 106 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "uni_detect/core/enums.py"
Cohesion: 0.14
Nodes (3): ColumnDataType, ComparisonDirection, TestWiring

### Community 110 - "pipeline.py"
Cohesion: 0.06
Nodes (8): get_spark(), scoped_conf(), configure_logging(), get_logger(), TestGetSparkExtended, TestGetSpark, TestConfigureLogging, TestGetLogger

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.23
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "test_console_scripts.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 120 - "Concepts"
Cohesion: 0.50
Nodes (4): Concepts, Configuration objects, One contract: `detect()`, The registry

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.17
Nodes (6): Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm, segment(), TestAutoValidateDetector

### Community 127 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 128 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 134 - "_value_matches"
Cohesion: 0.09
Nodes (17): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+9 more)

### Community 137 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "featurization.py"
Cohesion: 0.10
Nodes (14): FeatureBucket, _score_pair(), _score_column(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence() (+6 more)

### Community 433 - "ErrorType"
Cohesion: 0.09
Nodes (14): ErrorType, _require_min_rows(), BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector (+6 more)

### Community 458 - "detectors/base.py"
Cohesion: 0.17
Nodes (5): _hash_value(), redact_evidence(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestRedactEvidence

### Community 530 - "hierarchy.py"
Cohesion: 0.06
Nodes (22): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+14 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.11
Nodes (9): _blocking_keys(), _closest_pair(), differing_token_lengths(), min_pairwise_edit_distance(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance() (+1 more)

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "labeling.py"
Cohesion: 0.12
Nodes (14): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+6 more)

### Community 835 - "json"
Cohesion: 0.08
Nodes (12): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main() (+4 more)

### Community 1123 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1144 - "_check_unknown_kwargs"
Cohesion: 0.12
Nodes (8): 7.1 Architecture Overview, 7.3 Technology, 7.4 Assumptions, 7. Solution, _check_unknown_kwargs(), _ensure_dataframe_is_spark(), TestCheckUnknownKwargs, TestEnsureDataFrameIsSpark

### Community 1156 - "RahaConfig"
Cohesion: 0.08
Nodes (15): run_raha(), API reference, main(), ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, RahaDetector (+7 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 1219 - "builder.py"
Cohesion: 0.10
Nodes (10): duplicate_value_indices(), uniqueness_ratio(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestUniquenessRatio (+2 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 1430 - "conftest.py"
Cohesion: 0.12
Nodes (11): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect, _delta_jars() (+3 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1101 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **32 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `run_raha`, `.test_all_variants_infer_something`, `RahaConfig`, `.detect`, `_value_matches`, `OpenDetectError`, `.build_index`, `test_auto_validate_index.py`, `_make_tooltip`, `InferredPattern`, `fmdv_v`, `test_auto_validate_fmdv_v.py`, `algorithms/index.md`, `fmdv.py`, `Concepts`, `AutoValidateAlgorithm`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `write_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.09080841638981174 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `write_build_config`, `RahaConfig`, `._new_failure_tracker`, `FailureCounts`, `conftest.py`, `builder.py`, `_run`, `main`, `CorpusStatsBuilder`, `_FakeDetector`, `test_build_corpus_statistics.py`, `.detect`, `algorithms/index.md`, `.build_corpus_statistics`, `main`, `json`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `CorpusIngestor`, `detectors/base.py`, `featurization.py`, `_config`, `OpenDetectError`, `uni_detect/core/enums.py`, `pipeline.py`, `TestDetectCacheLifecycleSpark`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._