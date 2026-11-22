# Graph Report - open-detect  (2026-11-22)

## Corpus Check
- 211 files · ~167,057 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 473 files seen (49%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 3209 nodes · 6966 edges · 184 communities (140 shown, 44 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 845 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `732cad17`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- json
- pipeline.py
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- pytest
- README.md — Uni-Detect overview
- wiki_subset/run_benchmark.py
- FailureCounts
- PRD: User Feedback Tooltips
- FeatureBucket
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- _ensure_dataframe_is_spark
- perturbation.py
- test_auto_validate_fmdv_v.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- PatternIndex
- UnityCatalogLocation
- _check_expected_type
- collections_abc
- notifications/config.py
- .detect
- test_deprecated_shims.py
- _score_single_column
- main
- test_bench_spark_jobs.py
- get_algorithm
- build_column_features
- FailureCountsAccumulatorParam
- metrics/spelling.py
- metrics/functional_dependency.py
- real_world_gov benchmark results
- propagate_labels
- test_build_corpus_statistics.py
- TestListTablesMatching
- `auto_validate`
- GroundTruthLabeler
- Auto-Validate
- test_algorithms_registry.py
- CHANGELOG
- ErrorDetectionAlgorithm
- index.py
- TeamsNotifier
- test_bench_snapshot.py
- UniDetectConfig
- _build_index
- updates
- Raha
- jobs
- .build_corpus_statistics
- _ensure_sequence_of_str
- _coerce_numeric
- build
- uses
- unittest_mock
- env
- main
- .batch_score
- dry_run
- Benchmark: real_world_gov
- featurization.py
- CorpusIngestor
- variables
- ._send_teams_notification_after_detection
- PRD: API Validation Framework for open-detect
- dev
- .send
- Commit conventions and releases
- HeuristicLabeler
- CorpusStatsStore
- Current Status: BLOCKED
- _aggregate_scored_rows
- UniDetect
- numpy
- test
- hooks
- release.yml
- release
- test_raha_strategies.py
- tokenize
- pypi
- Current Status: BLOCKED
- real_world_gov/run_benchmark.py
- registry.py
- with
- on
- Benchmark: WIKI subset
- steps
- finite_floats
- raha/detector.py
- OPE-133 Review Summary
- drop_nulls
- open_detect/exceptions.py
- sonarqube
- infer_column_data_type
- uni_detect/text_utils.py
- docs
- force
- databricks.yml
- .index
- docs/index.md
- select_fd_column_pairs
- ColumnDataType
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_console_scripts.py
- reference/index.md
- .build_fd_stats
- Running on Databricks
- Comparing algorithms
- AutoValidateAlgorithm
- _FakeDetector
- paperclip-issue-update.sh
- SparkUnavailable
- Auto-Validate
- algorithms/uni-detect.md
- OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)
- uniqueness_ratio
- DataQualityError
- Detection
- test_raha_detector.py
- auto_validate/detector.py
- TestPluginDiscoveryViaRealDistInfo
- TestConfigThreshold
- KnownIndexLabeler
- .send_safe
- FakeConf
- comparison.py
- CorpusStatsBuilder
- ScoringJobCounter
- _check_unknown_kwargs
- .detect
- quickstart.py
- TestUniDetectDetect
- Completed Work
- algorithms/index.md
- algorithms/raha.md
- Uni-Detect
- is_integer_like
- ._check_rate_limit
- auto_validate/__init__.py
- test_featurization.py
- ValidationError
- TestSeverityOrdering
- duplicate_value_indices
- _StubDetector
- 5. Market Segment(s)
- test_teams.py
- _stats_schema_without_error_type
- OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)
- TestBuilderWeightOutput
- config
- Scoring auto_validate
- SlidingWindowRateLimiter
- _detector
- test_metrics.py
- scoped_conf
- ErrorType
- make_evidence_json
- hierarchy.py
- perturb_numeric_outlier
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- profile.py
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
6. `TeamsNotifier` - 51 edges
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
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (184 total, 44 thin omitted)

### Community 0 - "json"
Cohesion: 0.10
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "pipeline.py"
Cohesion: 0.08
Nodes (11): list_tables(), list_tables_matching(), table_exists(), _run(), get_spark(), configure_logging(), get_logger(), log_duration() (+3 more)

### Community 2 - "pandas"
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

### Community 7 - "pytest"
Cohesion: 0.08
Nodes (5): TestCorpusStatsSchema, TestCorpusStatsSchemaWeightType, TestListTables, TestTableExists, pair_table()

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.29
Nodes (7): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4)

### Community 9 - "wiki_subset/run_benchmark.py"
Cohesion: 0.10
Nodes (10): git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_auto_validate() (+2 more)

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
Cohesion: 0.08
Nodes (15): Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema (+7 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.13
Nodes (5): check_drift(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "_ensure_dataframe_is_spark"
Cohesion: 0.10
Nodes (14): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+6 more)

### Community 19 - "perturbation.py"
Cohesion: 0.09
Nodes (11): _score_pair(), _score_column(), _score_column(), _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome (+3 more)

### Community 20 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.12
Nodes (8): _build_index(), _date_index(), _date_values(), TestFmdvV, TestFmdvVh, TestLargeGroups, TestMinConforming, _time_corpus()

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

### Community 26 - "PatternIndex"
Cohesion: 0.07
Nodes (17): Variants, Recent Changes, _clean(), fmdv(), fmdv_h(), min_conforming(), _coarse_signature(), _fmdv_h_single() (+9 more)

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.12
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config()

### Community 30 - "notifications/config.py"
Cohesion: 0.07
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "test_deprecated_shims.py"
Cohesion: 0.08
Nodes (12): main(), __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 33 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "test_bench_spark_jobs.py"
Cohesion: 0.10
Nodes (10): ScopeStats, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop() (+2 more)

### Community 36 - "get_algorithm"
Cohesion: 0.13
Nodes (14): Check it works, Installation, Installing from source, Pick your extra, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+6 more)

### Community 37 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 39 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 40 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 45 - "`auto_validate`"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.21
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 47 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.11
Nodes (11): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_register_lazy_is_lazy(), test_unknown_algorithm_raises() (+3 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.05
Nodes (36): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+28 more)

### Community 50 - "ErrorDetectionAlgorithm"
Cohesion: 0.13
Nodes (8): API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, UniDetectAlgorithm, __getattr__()

### Community 51 - "index.py"
Cohesion: 0.09
Nodes (8): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestIndexableValues

### Community 52 - "TeamsNotifier"
Cohesion: 0.16
Nodes (3): TeamsNotifier, TestBuildAdaptiveCard, TestTeamsNotifierInit

### Community 53 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 54 - "UniDetectConfig"
Cohesion: 0.21
Nodes (3): UniDetectConfig, config(), TestUniDetectConfig

### Community 55 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.16
Nodes (5): _require_columns(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates, TestRequireColumns

### Community 61 - "_coerce_numeric"
Cohesion: 0.19
Nodes (4): _coerce_numeric(), config(), TestCoerceNumeric, score()

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "unittest_mock"
Cohesion: 0.11
Nodes (4): _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSparkExtended, TestGetSpark

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "main"
Cohesion: 0.18
Nodes (5): main(), parse_args(), test_main_installs_logging(), TestMain, TestParseArgs

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "Benchmark: real_world_gov"
Cohesion: 0.12
Nodes (15): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+7 more)

### Community 70 - "featurization.py"
Cohesion: 0.12
Nodes (11): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.12
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.11
Nodes (18): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+10 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "HeuristicLabeler"
Cohesion: 0.18
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, ColumnFeatures, HeuristicLabeler, _resolve_position() (+1 more)

### Community 79 - "CorpusStatsStore"
Cohesion: 0.19
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.15
Nodes (7): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results, _aggregate_scored_rows(), TestAggregateScoredRows

### Community 83 - "UniDetect"
Cohesion: 0.10
Nodes (9): UniDetect, _config(), _mock_spark(), TestBuildAffectedSummary, TestUniDetectBuildCorpusStatistics, TestUniDetectInit, TestUniDetectRelease, TestUniDetectValidateInputs (+1 more)

### Community 84 - "numpy"
Cohesion: 0.07
Nodes (15): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestEmptyFrames (+7 more)

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

### Community 89 - "test_raha_strategies.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 90 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 94 - "registry.py"
Cohesion: 0.24
Nodes (6): _constant_factory(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), test_register_lazy_overrides_existing_name()

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "Benchmark: WIKI subset"
Cohesion: 0.20
Nodes (10): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, Scoring raha, The corpus (`data/corpus/`) (+2 more)

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "finite_floats"
Cohesion: 0.24
Nodes (4): compute(), _score_column(), finite_floats(), TestFiniteFloats

### Community 100 - "raha/detector.py"
Cohesion: 0.11
Nodes (11): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, Labeler (+3 more)

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.07
Nodes (19): Errors, Errors, _validate_edges(), CorpusNotFoundError, InsufficientDataError, UnityCatalogError, ConfigurationError, IndexNotBuiltError (+11 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "uni_detect/text_utils.py"
Cohesion: 0.15
Nodes (4): is_float_like(), is_mixed_alphanumeric(), TestFloatLike, TestMixedAlphanumeric

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "databricks.yml"
Cohesion: 0.22
Nodes (8): artifacts, open_detect_wheel, bundle, name, build, path, type, UniDetect pipeline facade

### Community 110 - ".index"
Cohesion: 0.33
Nodes (4): Inspecting a pattern, Reading the output, Usage, segment()

### Community 111 - "docs/index.md"
Cohesion: 0.22
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 113 - "ColumnDataType"
Cohesion: 0.14
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 115 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 116 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 117 - "reference/index.md"
Cohesion: 0.25
Nodes (3): Registry, Registry and results, Result types

### Community 118 - ".build_fd_stats"
Cohesion: 0.46
Nodes (3): _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 119 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 120 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.09
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 126 - "SparkUnavailable"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 127 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 128 - "algorithms/uni-detect.md"
Cohesion: 0.33
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 129 - "OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)"
Cohesion: 0.29
Nodes (6): Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification

### Community 131 - "DataQualityError"
Cohesion: 0.22
Nodes (8): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect, DataQualityError

### Community 134 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (19): Implementation Status, Changes Made, _build_suggestion(), _check_columns_present(), _distinct_value_verdicts(), _distinct_value_verdicts_groups(), _feasible_evidence(), _infeasible_evidence() (+11 more)

### Community 137 - "KnownIndexLabeler"
Cohesion: 0.39
Nodes (3): KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 143 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 144 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 147 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 149 - "algorithms/raha.md"
Cohesion: 0.33
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 150 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 153 - "auto_validate/__init__.py"
Cohesion: 0.10
Nodes (10): _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), matches(), fpr_column(), impurity() (+2 more)

### Community 155 - "ValidationError"
Cohesion: 0.10
Nodes (9): ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _reject_unknown_kwargs(), _validate_literal_value(), TestCheckColumnsUnique, TestCheckDataFrameIsSpark, TestRejectUnknownKwargs (+1 more)

### Community 159 - "5. Market Segment(s)"
Cohesion: 0.50
Nodes (4): 5.1 Primary Segment, 5.2 Secondary Segment, 5.3 Constraints, 5. Market Segment(s)

### Community 162 - "OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)"
Cohesion: 0.40
Nodes (4): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results

### Community 166 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 174 - "SlidingWindowRateLimiter"
Cohesion: 0.13
Nodes (3): SlidingWindowRateLimiter, TestEdgeCases, TestSlidingWindowRateLimiter

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 433 - "ErrorType"
Cohesion: 0.08
Nodes (15): ComparisonDirection, ErrorType, _require_min_rows(), BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector (+7 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.16
Nodes (6): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), TestRedactEvidence

### Community 530 - "hierarchy.py"
Cohesion: 0.06
Nodes (23): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+15 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.24
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (11): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal() (+3 more)

### Community 835 - "profile.py"
Cohesion: 0.09
Nodes (5): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, test_require_uni_detect_fails_when_undetected()

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.27
Nodes (11): _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart(), render_markdown() (+3 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.32
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 1430 - "conftest.py"
Cohesion: 0.13
Nodes (9): candidates(), main(), select(), _cap_driver_memory(), _delta_jars(), _download(), _host_memory_bytes(), spark() (+1 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1212 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **44 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `auto_validate/__init__.py`, `auto_validate/detector.py`, `open_detect/exceptions.py`, `wiki_subset/run_benchmark.py`, `CellResult`, `InferredPattern`, `ErrorDetectionAlgorithm`, `index.py`, `test_auto_validate_fmdv_v.py`, `_build_index`, `AutoValidateAlgorithm`, `PatternIndex`, `real_world_gov/run_benchmark.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `json` be split into smaller, more focused modules?**
  _Cohesion score 0.10359408033826638 - nodes in this community are weakly interconnected._
- **Why does `UniDetect` connect `UniDetect` to `pipeline.py`, `wiki_subset/run_benchmark.py`, `CorpusStatsBuilder`, `quickstart.py`, `TestUniDetectDetect`, `Completed Work`, `UnityCatalogLocation`, `ValidationError`, `main`, `test_build_corpus_statistics.py`, `ErrorType`, `ErrorDetectionAlgorithm`, `TeamsNotifier`, `UniDetectConfig`, `.build_corpus_statistics`, `CorpusIngestor`, `._send_teams_notification_after_detection`, `real_world_gov/run_benchmark.py`, `Benchmark: WIKI subset`, `open_detect/exceptions.py`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 67 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._