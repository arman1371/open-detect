# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-16)

## Corpus Check
- 192 files · ~160,643 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3005 nodes · 6604 edges · 163 communities (133 shown, 30 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 834 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c4a856ac`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CorpusStatsBuilder
- dataset_utils.py
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- builder.py
- README.md — Uni-Detect overview
- test_bench_snapshot.py
- FailureCounts
- PRD: User Feedback Tooltips
- CorpusStatsStore
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- FeatureBucket
- ErrorDetectionAlgorithm
- test_auto_validate_fmdv_v.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- TestCorpusStatsSchema
- UnityCatalogLocation
- Completed Work
- _check_expected_type
- UniDetectConfig
- cluster_column
- pytest
- gaussian_outlier_strategies
- main
- test_bench_spark_jobs.py
- list_algorithms
- features.py
- fd_violation_strategies
- InsufficientDataError
- _ensure_sequence_of_str
- real_world_gov benchmark results
- .detect
- test_build_corpus_statistics.py
- log_transform_fits_better
- Benchmark: WIKI subset
- GroundTruthLabeler
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- Registry and results
- PatternIndex
- .detect
- CorpusNotFoundError
- real_world_gov/run_benchmark.py
- fmdv.py
- updates
- Raha
- jobs
- .build_corpus_statistics
- bucket_by_edges
- _coerce_numeric
- build
- uses
- confusion_metrics
- env
- perturb_spelling
- CorpusStatsStore
- dry_run
- _score_single_column
- uni_detect/core/enums.py
- CorpusIngestor
- variables
- KnownIndexLabeler
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
- _check_unknown_kwargs
- spark_session.py
- with
- on
- Contributing
- steps
- argparse
- CallableLabeler
- _segment_dp
- _require_columns
- OpenDetectError
- sonarqube
- require_uni_detect
- infer_column_data_type
- docs
- force
- Appendix: Validation Function Reference
- pipeline.py
- choosing-an-algorithm.md
- select_fd_column_pairs
- .detect
- open-detect
- _ensure_dataframe_is_spark
- test_package_init.py
- real_plugin_path
- `uni_detect`
- `raha`
- Comparing algorithms
- AutoValidateAlgorithm
- _FakeDetector
- paperclip-issue-update.sh
- algorithms/uni-detect.md
- Auto-Validate
- open_detect_wheel
- Concepts
- _check_dataframe_is_spark
- Uni-Detect
- _reject_unknown_kwargs
- TestCorpusStatsSchemaWeightType
- _value_matches
- TestConfigThreshold
- 8. Release
- Uni-Detect
- v0.2.7 (2026-10-18)
- v0.2.8 (2026-11-05)
- _default_classifier_factory
- __getattr__
- _detector
- test_metrics.py
- ScoringJobCounter
- TestScopedConf
- get_logger
- ErrorType
- make_evidence_json
- hierarchy.py
- perturb_numeric_outlier
- perturbation.py
- min_pairwise_edit_distance
- snapshot.py
- json
- _check_unknown_kwargs
- RahaConfig
- wiki_subset/generate_report.py
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
7. `UnityCatalogLocation` - 47 edges
8. `build_pattern_index()` - 46 edges
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

## Communities (163 total, 30 thin omitted)

### Community 0 - "CorpusStatsBuilder"
Cohesion: 0.05
Nodes (21): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), CorpusStatsBuilder, _stats_schema_without_error_type(), _config() (+13 more)

### Community 1 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 2 - "pandas"
Cohesion: 0.10
Nodes (22): _is_null(), _non_null_cells(), _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), _detect() (+14 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "builder.py"
Cohesion: 0.13
Nodes (4): _require_min_rows(), _score_fd_pair(), scoped_conf(), TestScoreFdPair

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 10 - "FailureCounts"
Cohesion: 0.15
Nodes (6): compute(), FailureCounts, compute(), _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "CorpusStatsStore"
Cohesion: 0.17
Nodes (4): CorpusStatsStore, config(), TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.09
Nodes (13): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, 1. Implement `ErrorDetectionAlgorithm`, open-detect, What is in the box, Why a common interface (+5 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (9): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "FeatureBucket"
Cohesion: 0.18
Nodes (6): Candidate, FeatureBucket, MetricObservation, TestCandidate, TestFeatureBucket, TestMetricObservation

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (14): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm(), get_algorithm_class(), _load_entry_points() (+6 more)

### Community 20 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.08
Nodes (11): _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV (+3 more)

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

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 28 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 30 - "UniDetectConfig"
Cohesion: 0.23
Nodes (3): UniDetectConfig, config(), TestUniDetectConfig

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "pytest"
Cohesion: 0.07
Nodes (13): main(), __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim() (+5 more)

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "test_bench_spark_jobs.py"
Cohesion: 0.18
Nodes (8): SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported(), test_scopes_use_distinct_job_groups()

### Community 36 - "list_algorithms"
Cohesion: 0.11
Nodes (12): Check it works, Installation, Installing from source, Pick your extra, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code (+4 more)

### Community 37 - "features.py"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 38 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 39 - "InsufficientDataError"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.21
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.20
Nodes (6): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), TestPluginDiscovery, worker()

### Community 49 - "CHANGELOG"
Cohesion: 0.10
Nodes (20): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+12 more)

### Community 50 - "Registry and results"
Cohesion: 0.67
Nodes (3): Registry, Registry and results, Result types

### Community 51 - "PatternIndex"
Cohesion: 0.07
Nodes (13): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Recent Changes, Test Results, _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh() (+5 more)

### Community 52 - ".detect"
Cohesion: 0.18
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "CorpusNotFoundError"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 54 - "real_world_gov/run_benchmark.py"
Cohesion: 0.18
Nodes (8): git_commit(), _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate(), run_uni_detect()

### Community 55 - "fmdv.py"
Cohesion: 0.12
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Raha"
Cohesion: 0.40
Nodes (5): Configuration, How it works, Install, Raha, Scope

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.20
Nodes (5): build_spark(), main(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "confusion_metrics"
Cohesion: 0.13
Nodes (11): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+3 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "uni_detect/core/enums.py"
Cohesion: 0.08
Nodes (7): ColumnDataType, ComparisonDirection, CorpusColumnRecord, CorpusPairRecord, Detection, TestCorpusRecords, TestDetection

### Community 71 - "CorpusIngestor"
Cohesion: 0.11
Nodes (6): balanced_union(), CorpusIngestor, compute_token_counts(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_auto_validate_index.py"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "raha/detector.py"
Cohesion: 0.11
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.18
Nodes (5): _aggregate_scored_rows(), compute(), compute(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "_config"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "algorithms/index.md"
Cohesion: 0.22
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
Cohesion: 0.14
Nodes (11): _score_column(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+3 more)

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

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
Cohesion: 0.19
Nodes (4): CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "_segment_dp"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "_require_columns"
Cohesion: 0.22
Nodes (3): _filter_by_column_type(), _require_columns(), TestRequireColumns

### Community 103 - "OpenDetectError"
Cohesion: 0.11
Nodes (15): Errors, Errors, CorpusNotFoundError, DataQualityError, InsufficientDataError, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError (+7 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "require_uni_detect"
Cohesion: 0.22
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 106 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "Appendix: Validation Function Reference"
Cohesion: 0.28
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_columns_unique(), TestCheckColumnsUnique

### Community 110 - "pipeline.py"
Cohesion: 0.03
Nodes (22): list_tables(), list_tables_matching(), table_exists(), _validate_edges(), main(), parse_args(), _run(), get_spark() (+14 more)

### Community 111 - "choosing-an-algorithm.md"
Cohesion: 0.18
Nodes (8): Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "real_plugin_path"
Cohesion: 0.22
Nodes (4): real_plugin_path(), test_get_algorithm_constructs_with_args(), test_unknown_algorithm_raises(), _write_distinfo_plugin()

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 120 - "Comparing algorithms"
Cohesion: 0.25
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.06
Nodes (22): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+14 more)

### Community 127 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 128 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 129 - "Concepts"
Cohesion: 0.33
Nodes (4): Concepts, Configuration objects, One contract: `detect()`, The registry

### Community 131 - "Uni-Detect"
Cohesion: 0.29
Nodes (7): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect

### Community 134 - "_value_matches"
Cohesion: 0.07
Nodes (23): Implementation Status, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification (+15 more)

### Community 136 - "8. Release"
Cohesion: 0.40
Nodes (5): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release

### Community 137 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 138 - "v0.2.7 (2026-10-18)"
Cohesion: 0.50
Nodes (4): Bug Fixes, Documentation, Refactoring, v0.2.7 (2026-10-18)

### Community 139 - "v0.2.8 (2026-11-05)"
Cohesion: 0.50
Nodes (4): Documentation, Performance Improvements, Refactoring, v0.2.8 (2026-11-05)

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.31
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "ScoringJobCounter"
Cohesion: 0.10
Nodes (4): ScopeStats, ScoringJobCounter, counting_batch_score(), TestDetectCacheLifecycleSpark

### Community 426 - "get_logger"
Cohesion: 0.12
Nodes (4): get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 433 - "ErrorType"
Cohesion: 0.07
Nodes (12): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, all_specs() (+4 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.22
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), compute(), TestRedactEvidence

### Community 530 - "hierarchy.py"
Cohesion: 0.04
Nodes (33): min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize() (+25 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "perturbation.py"
Cohesion: 0.05
Nodes (25): _score_pair(), drop_nulls(), require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), mad_scores(), MADResult (+17 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "json"
Cohesion: 0.09
Nodes (13): maybe_scope(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+5 more)

### Community 1144 - "_check_unknown_kwargs"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.09
Nodes (17): run_raha(), API reference, main(), ColumnPredictions, _make_classifier(), train_and_predict(), RahaConfig, RahaDetector (+9 more)

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
Cohesion: 0.21
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1105 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **30 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `Concepts`, `json`, `RahaConfig`, `_value_matches`, `pipeline.py`, `InferredPattern`, `hierarchy.py`, `PatternIndex`, `test_auto_validate_fmdv_v.py`, `real_world_gov/run_benchmark.py`, `fmdv.py`, `AutoValidateAlgorithm`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CorpusStatsBuilder` be split into smaller, more focused modules?**
  _Cohesion score 0.050616050616050616 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `CorpusStatsBuilder`, `Uni-Detect`, `RahaConfig`, `builder.py`, `FailureCounts`, `CorpusStatsStore`, `FeatureBucket`, `main`, `ScoringJobCounter`, `test_build_corpus_statistics.py`, `.detect`, `real_world_gov/run_benchmark.py`, `.build_corpus_statistics`, `json`, `CorpusStatsStore`, `_score_single_column`, `uni_detect/core/enums.py`, `_config`, `featurization.py`, `_require_columns`, `OpenDetectError`, `pipeline.py`, `_FakeDetector`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._