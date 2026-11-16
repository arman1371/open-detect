# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-16)

## Corpus Check
- 192 files · ~160,458 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3004 nodes · 6601 edges · 159 communities (125 shown, 34 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 833 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `607a506b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- dataset_utils.py
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- fd_compliance_ratio
- README.md — Uni-Detect overview
- RahaDetector
- FailureCounts
- PRD: User Feedback Tooltips
- CorpusStatsStore
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- pattern_character_strategies
- ErrorDetectionAlgorithm
- test_auto_validate_fmdv_v.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- TestCorpusStatsSchema
- catalog.py
- Completed Work
- ValidationError
- UniDetectConfig
- cluster_column
- warnings
- raha/strategies.py
- main
- pytest
- CorpusStatsBuilder
- gaussian_outlier_strategies
- fd_violation_strategies
- InsufficientDataError
- _ensure_sequence_of_str
- real_world_gov benchmark results
- .detect
- test_build_corpus_statistics.py
- log_transform_fits_better
- Benchmark: WIKI subset
- cluster_column
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- docs/index.md
- fmdv_v
- .detect
- CorpusNotFoundError
- algorithms/index.md
- fmdv.py
- updates
- HeuristicLabeler
- jobs
- .build_corpus_statistics
- test_package_init.py
- _coerce_numeric
- build
- uses
- Benchmark: real_world_gov
- env
- perturb_spelling
- CorpusStatsStore
- dry_run
- _score_single_column
- ErrorType
- CorpusIngestor
- variables
- TestMatching
- PRD: API Validation Framework for open-detect
- dev
- test_auto_validate_index.py
- Commit conventions and releases
- raha/detector.py
- test_cache_lifecycle.py
- Current Status: BLOCKED
- _aggregate_scored_rows
- _config
- algorithms/index.md
- test
- test_bench_snapshot.py
- release.yml
- release
- test_raha_strategies.py
- featurization.py
- pypi
- Current Status: BLOCKED
- tokenize
- spark_session.py
- with
- on
- Contributing
- steps
- argparse
- CallableLabeler
- _segment_dp
- FakeConf
- OpenDetectError
- sonarqube
- require_uni_detect
- infer_column_data_type
- docs
- force
- open_detect/exceptions.py
- pipeline.py
- algorithms/uni-detect.md
- select_fd_column_pairs
- uniqueness_ratio
- open-detect
- sys
- test_console_scripts.py
- real_plugin_path
- `uni_detect`
- `raha`
- AutoValidateAlgorithm
- duplicate_value_indices
- paperclip-issue-update.sh
- algorithms/index.md
- Auto-Validate
- open_detect_wheel
- Concepts
- test_corpus_ingestion.py
- Choosing an algorithm
- TestCorpusStatsSchemaWeightType
- _value_matches
- _StubDetector
- Uni-Detect
- _detector
- test_metrics.py
- ScoringJobCounter
- TestScopedConf
- BaseDetector
- builder.py
- detectors/base.py
- hierarchy.py
- perturb_numeric_outlier
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- json
- Auto-Validate
- _check_unknown_kwargs
- RahaConfig
- wiki_subset/generate_report.py
- test_perturbation.py
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 97 edges
3. `UniDetectConfig` - 95 edges
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

## Communities (159 total, 34 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.18
Nodes (6): verify_build_config(), _config(), FakeSpark, TestLegacyCorpus, TestMismatch, TestWiring

### Community 1 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 2 - "pandas"
Cohesion: 0.06
Nodes (39): _is_null(), _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting(), _detect() (+31 more)

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
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "RahaDetector"
Cohesion: 0.20
Nodes (6): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 10 - "FailureCounts"
Cohesion: 0.13
Nodes (7): compute(), _score_fd_pair(), FailureCounts, compute(), _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "CorpusStatsStore"
Cohesion: 0.22
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.07
Nodes (18): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs (+10 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.06
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.10
Nodes (7): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "pattern_character_strategies"
Cohesion: 0.17
Nodes (4): pattern_character_strategies(), TestEmptyFrames, TestNullSentinel, TestPatternCharacterStrategies

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.08
Nodes (19): API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm(), get_algorithm_class() (+11 more)

### Community 20 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.10
Nodes (9): _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV, TestFmdvVh, TestLargeGroups, TestMinConforming (+1 more)

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

### Community 27 - "catalog.py"
Cohesion: 0.14
Nodes (7): ensure_schema_exists(), list_tables(), table_exists(), UnityCatalogError, TestEnsureSchemaExists, TestListTables, TestTableExists

### Community 28 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 29 - "ValidationError"
Cohesion: 0.07
Nodes (15): Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _reject_unknown_kwargs() (+7 more)

### Community 30 - "UniDetectConfig"
Cohesion: 0.07
Nodes (14): UniDetectConfig, UnityCatalogLocation, _validate_edges(), _require_columns(), ConfigurationError, config(), TestRedactEvidence, TestUniDetectConfig (+6 more)

### Community 32 - "warnings"
Cohesion: 0.15
Nodes (3): __getattr__(), __getattr__(), test_old_except_clause_catches_new_error()

### Community 33 - "raha/strategies.py"
Cohesion: 0.19
Nodes (4): _factorize_column(), histogram_outlier_strategies(), normalize_to_str(), TestHistogramOutlierStrategies

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.27
Nodes (8): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only(), test_module_shims_are_identity_preserving(), test_unknown_exception_attr_raises()

### Community 36 - "CorpusStatsBuilder"
Cohesion: 0.17
Nodes (7): CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 37 - "gaussian_outlier_strategies"
Cohesion: 0.23
Nodes (4): gaussian_outlier_strategies(), _is_float_like(), TestGaussianOutlierStrategies, TestRowWeightedNumericGate

### Community 38 - "fd_violation_strategies"
Cohesion: 0.27
Nodes (3): fd_violation_strategies(), TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 39 - "InsufficientDataError"
Cohesion: 0.17
Nodes (8): drop_nulls(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance(), TestDropNulls

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.10
Nodes (16): Check it works, Installation, Installing from source, Pick your extra, 2. Register it, As a plugin package (no changes to `open-detect`), In your own code, list_algorithms() (+8 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "docs/index.md"
Cohesion: 0.25
Nodes (6): open-detect, What is in the box, Why a common interface, Registry, Registry and results, Result types

### Community 51 - "fmdv_v"
Cohesion: 0.05
Nodes (26): Variants, Recent Changes, _infer_pattern_to_groups(), _conforms(), _conforms_segments(), _clean(), fmdv(), fmdv_h() (+18 more)

### Community 52 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "CorpusNotFoundError"
Cohesion: 0.25
Nodes (6): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, CorpusNotFoundError

### Community 54 - "algorithms/index.md"
Cohesion: 0.13
Nodes (11): confusion_metrics(), _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate(), run_raha() (+3 more)

### Community 55 - "fmdv.py"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

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
Cohesion: 0.13
Nodes (9): Methodology: uni_detect -- mapping real dirty data onto its four error types, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, config(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors (+1 more)

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "Benchmark: real_world_gov"
Cohesion: 0.18
Nodes (11): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha, Reading the results (+3 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "ErrorType"
Cohesion: 0.05
Nodes (23): ColumnDataType, ComparisonDirection, ErrorType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation (+15 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.10
Nodes (7): balanced_union(), CorpusIngestor, compute_token_counts(), TestCorpusIngestorSkipsBadInputs, TestDetectReturnsEmptyResultWhenNoCandidates, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.07
Nodes (26): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+18 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_auto_validate_index.py"
Cohesion: 0.13
Nodes (7): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_iter_corpus_columns(), TestCleanColumn, TestIndexableValues

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "raha/detector.py"
Cohesion: 0.10
Nodes (15): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+7 more)

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.22
Nodes (3): _aggregate_scored_rows(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "_config"
Cohesion: 0.09
Nodes (13): __getattr__(), UniDetect, __getattr__(), _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics (+5 more)

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

### Community 89 - "test_raha_strategies.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 90 - "featurization.py"
Cohesion: 0.07
Nodes (16): FeatureBucket, bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+8 more)

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tokenize"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 94 - "spark_session.py"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

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

### Community 103 - "OpenDetectError"
Cohesion: 0.15
Nodes (11): Errors, Errors, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error() (+3 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "require_uni_detect"
Cohesion: 0.20
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 106 - "infer_column_data_type"
Cohesion: 0.09
Nodes (9): infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), TestDataTypeInference, TestFloatLike, TestIntegerLike, TestMixedAlphanumeric (+1 more)

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "open_detect/exceptions.py"
Cohesion: 0.10
Nodes (9): _as_json_list(), build_spark(), main(), diff_fingerprints(), property_key(), read_build_config(), write_build_config(), test_diff_fingerprints_reports_missing_fields() (+1 more)

### Community 110 - "pipeline.py"
Cohesion: 0.05
Nodes (19): list_tables_matching(), main(), parse_args(), _run(), get_spark(), scoped_conf(), configure_logging(), get_logger() (+11 more)

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.08
Nodes (9): Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm, _distinct_value_verdicts_groups(), _non_null_cells(), _value_matches_groups(), _make_tiny_corpus() (+1 more)

### Community 127 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 128 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 129 - "Concepts"
Cohesion: 0.50
Nodes (4): Concepts, Configuration objects, One contract: `detect()`, The registry

### Community 132 - "Choosing an algorithm"
Cohesion: 0.67
Nodes (3): At a glance, Choosing an algorithm, Rules of thumb

### Community 134 - "_value_matches"
Cohesion: 0.07
Nodes (23): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+15 more)

### Community 137 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 205 - "_detector"
Cohesion: 0.13
Nodes (4): _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.20
Nodes (5): _brute_force_mpd(), _random_words(), _single_edit(), TestFiniteFloats, TestSpellingBlocking

### Community 297 - "ScoringJobCounter"
Cohesion: 0.07
Nodes (12): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, TestDetectCacheLifecycleSpark, _FakeContext, _FakeTracker, _spark() (+4 more)

### Community 426 - "BaseDetector"
Cohesion: 0.06
Nodes (10): BaseDetector, FunctionalDependencyDetector, compute(), _score_column(), SpellingDetector, compute(), UniquenessDetector, compute() (+2 more)

### Community 433 - "builder.py"
Cohesion: 0.07
Nodes (9): _score_pair(), _score_column(), InsufficientDataError, require_min_size(), finite_floats(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness() (+1 more)

### Community 458 - "detectors/base.py"
Cohesion: 0.11
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), _config(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestRedactEvidence

### Community 530 - "hierarchy.py"
Cohesion: 0.06
Nodes (23): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+15 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.24
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.15
Nodes (8): FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.17
Nodes (7): diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "json"
Cohesion: 0.12
Nodes (12): maybe_scope(), UniDetectProfile, git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+4 more)

### Community 1123 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1144 - "_check_unknown_kwargs"
Cohesion: 0.10
Nodes (14): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+6 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.07
Nodes (18): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, build_all_features(), build_column_features(), _compact_dtype() (+10 more)

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
Cohesion: 0.14
Nodes (10): A fully local example, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect, _delta_jars(), _download() (+2 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1104 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **34 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `Concepts`, `json`, `_value_matches`, `InferredPattern`, `ErrorDetectionAlgorithm`, `fmdv_v`, `test_auto_validate_fmdv_v.py`, `algorithms/index.md`, `fmdv.py`, `AutoValidateAlgorithm`, `UniDetectConfig`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `pandas` be split into smaller, more focused modules?**
  _Cohesion score 0.057902973395931145 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `_StubDetector`, `FailureCounts`, `CorpusStatsStore`, `ErrorDetectionAlgorithm`, `conftest.py`, `main`, `CorpusStatsBuilder`, `ScoringJobCounter`, `BaseDetector`, `test_build_corpus_statistics.py`, `builder.py`, `.detect`, `algorithms/index.md`, `.build_corpus_statistics`, `json`, `CorpusStatsStore`, `_score_single_column`, `CorpusIngestor`, `detectors/base.py`, `_config`, `featurization.py`, `open_detect/exceptions.py`, `pipeline.py`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._