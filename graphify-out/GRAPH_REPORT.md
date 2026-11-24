# Graph Report - open-detect  (2026-11-24)

## Corpus Check
- 211 files · ~168,300 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 473 files seen (49%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 3236 nodes · 7016 edges · 176 communities (138 shown, 38 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 850 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `32cbb237`
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
- pandas
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- notifications/config.py
- .detect
- test_auto_validate_fmdv_v.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- InsufficientDataError
- raha/detector.py
- CorpusStatsBuilder
- _check_expected_type
- UniDetectConfig
- cluster_column
- ScoringJobCounter
- raha/strategies.py
- ErrorType
- test_deprecated_shims.py
- Benchmark: real_world_gov
- AutoValidateAlgorithm
- SlidingWindowRateLimiter
- unittest_mock
- Commit conventions and releases
- real_world_gov benchmark results
- propagate_labels
- _value_matches
- log_transform_fits_better
- `auto_validate`
- auto_validate/detector.py
- FailureCountsAccumulatorParam
- numpy
- CHANGELOG
- Auto-Validate
- get_spec
- .send
- fd_compliance_ratio
- TeamsNotifier
- fmdv
- updates
- HeuristicLabeler
- jobs
- .detect
- spark_session.py
- _coerce_numeric
- build
- uses
- charts.py
- env
- choosing-an-algorithm.md
- _aggregate_scored_rows
- dry_run
- _score_single_column
- open_detect/__init__.py
- CorpusIngestor
- databricks.yml
- Uni-Detect
- PRD: API Validation Framework for open-detect
- dev
- matches
- PatternIndex
- GroundTruthLabeler
- infer_column_data_type
- Current Status: BLOCKED
- test_auto_validate_index.py
- UniDetect
- gaussian_outlier_strategies
- test
- OPE-89: Fix Spark Cache Lifecycle in Uni-Detect
- release.yml
- release
- CorpusNotFoundError
- perturb_spelling
- pypi
- Current Status: BLOCKED
- tokenize
- argparse
- with
- on
- CorpusStatsStore
- steps
- test_raha_detector.py
- CallableLabeler
- concepts.md
- TestCorpusStatsSchema
- pytest
- sonarqube
- wiki_subset/generate_report.py
- Installation
- docs
- force
- OPE-133 Review Summary
- builder.py
- algorithms/uni-detect.md
- test_teams.py
- sys
- open-detect
- Scoring auto_validate
- test_package_init.py
- ConfigurationError
- hooks
- fd_violation_strategies
- .send_safe
- _value_matches_groups
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- paperclip-issue-update.sh
- select_fd_column_pairs
- test_logging_utils.py
- Benchmark: WIKI subset
- Auto-Validate
- test_algorithms_registry.py
- UnknownAlgorithmError
- ._check_rate_limit
- _StubDetector
- TestSeverityOrdering
- _filter_by_column_type
- _random_words
- algorithms/index.md
- 7.2 Key Features
- _check_unknown_kwargs
- FeatureBucket
- .index
- _ensure_sequence_of_str
- _check_columns_unique
- .detect
- TestUniDetectBaselineDiff
- ValidationError
- _FakeDetector
- _build_row
- Detection
- v0.2.7 (2026-10-18)
- _check_dataframe_is_spark
- FakeConf
- is_integer_like
- Appendix: Validation Function Reference
- _reject_unknown_kwargs
- _spark_available
- _detector
- featurization.py
- scoped_conf
- BaseDetector
- make_evidence_json
- patterns.py
- test_bench_snapshot.py
- test_metrics.py
- min_pairwise_edit_distance
- snapshot.py
- KnownIndexLabeler
- real_world_gov/run_benchmark.py
- RahaConfig
- real_world_gov/generate_report.py
- Performance Baseline — OPE-87
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 102 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 86 edges
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

## Communities (176 total, 38 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.12
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.10
Nodes (9): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config() (+1 more)

### Community 2 - "test_ope86_distinct_verdicts.py"
Cohesion: 0.11
Nodes (18): _is_null(), _city_column(), _count_detect_calls(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference(), test_empty_dataframe() (+10 more)

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
Cohesion: 0.06
Nodes (17): _as_json_list(), _score_pair(), _score_column(), _score_column(), finite_floats(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency() (+9 more)

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.29
Nodes (7): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4)

### Community 9 - "wiki_subset/run_benchmark.py"
Cohesion: 0.07
Nodes (11): maybe_scope(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+3 more)

### Community 10 - "FailureCounts"
Cohesion: 0.14
Nodes (6): compute(), _score_fd_pair(), FailureCounts, _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "pandas"
Cohesion: 0.12
Nodes (9): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features() (+1 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.08
Nodes (15): Reading the detections, Through the registry, Usage on Databricks, Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog (+7 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestFmdvV, TestSegmentDp, solve(), TestCorpusInputShapes (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.14
Nodes (12): _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions() (+4 more)

### Community 18 - "notifications/config.py"
Cohesion: 0.07
Nodes (10): get_notification_config(), get_rate_limit(), get_severity_threshold(), get_teams_enabled(), get_teams_webhook_url(), TestGetNotificationConfig, TestGetRateLimit, TestGetSeverityThreshold (+2 more)

### Community 19 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 20 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.12
Nodes (7): _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvVh, TestLargeGroups, _time_corpus()

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

### Community 26 - "InsufficientDataError"
Cohesion: 0.08
Nodes (15): list_tables(), list_tables_matching(), table_exists(), InsufficientDataError, main(), parse_args(), _run(), configure_logging() (+7 more)

### Community 27 - "raha/detector.py"
Cohesion: 0.08
Nodes (22): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference, ErrorDetectionAlgorithm (+14 more)

### Community 28 - "CorpusStatsBuilder"
Cohesion: 0.19
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 30 - "UniDetectConfig"
Cohesion: 0.12
Nodes (4): UniDetectConfig, config(), TestUniDetectConfig, config()

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "ScoringJobCounter"
Cohesion: 0.09
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 33 - "raha/strategies.py"
Cohesion: 0.13
Nodes (7): _factorize_column(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestHistogramOutlierStrategies, TestNullSentinel, TestPatternCharacterStrategies

### Community 34 - "ErrorType"
Cohesion: 0.09
Nodes (12): ErrorType, main(), parse_args(), _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release(), TestUniDetectCacheLifecycle (+4 more)

### Community 35 - "test_deprecated_shims.py"
Cohesion: 0.10
Nodes (11): __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "Benchmark: real_world_gov"
Cohesion: 0.12
Nodes (15): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+7 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "SlidingWindowRateLimiter"
Cohesion: 0.13
Nodes (3): SlidingWindowRateLimiter, TestEdgeCases, TestSlidingWindowRateLimiter

### Community 39 - "unittest_mock"
Cohesion: 0.11
Nodes (5): get_spark(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSparkExtended, TestGetSpark

### Community 40 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "_value_matches"
Cohesion: 0.11
Nodes (16): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+8 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 46 - "auto_validate/detector.py"
Cohesion: 0.10
Nodes (9): _build_suggestion(), _feasible_evidence(), _infeasible_evidence(), _infer_pattern_to_groups(), _make_tooltip(), _non_null_cells(), _tooltip_content(), pattern_to_language() (+1 more)

### Community 48 - "numpy"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 49 - "CHANGELOG"
Cohesion: 0.06
Nodes (32): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+24 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.15
Nodes (10): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, Configuration, Detector (+2 more)

### Community 51 - "get_spec"
Cohesion: 0.17
Nodes (7): _require_min_rows(), all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 53 - "fd_compliance_ratio"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 54 - "TeamsNotifier"
Cohesion: 0.16
Nodes (3): TeamsNotifier, TestBuildAdaptiveCard, TestTeamsNotifierInit

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "HeuristicLabeler"
Cohesion: 0.11
Nodes (18): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions? (+10 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".detect"
Cohesion: 0.16
Nodes (6): build_spark(), main(), Completed Work, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "spark_session.py"
Cohesion: 0.19
Nodes (5): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "charts.py"
Cohesion: 0.20
Nodes (5): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown()

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "choosing-an-algorithm.md"
Cohesion: 0.18
Nodes (8): Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "_aggregate_scored_rows"
Cohesion: 0.12
Nodes (8): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results, _aggregate_scored_rows(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.18
Nodes (5): compute(), _score_single_column(), config(), TestScoreSingleColumn, score()

### Community 70 - "open_detect/__init__.py"
Cohesion: 0.12
Nodes (9): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, __getattr__(), TestCandidate, TestCorpusRecords (+1 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.10
Nodes (6): balanced_union(), CorpusIngestor, log_duration(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "databricks.yml"
Cohesion: 0.11
Nodes (18): artifacts, open_detect_wheel, bundle, name, default, description, default, description (+10 more)

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "matches"
Cohesion: 0.17
Nodes (5): matches(), fpr_column(), impurity(), matching_pattern(), TestMatching

### Community 77 - "PatternIndex"
Cohesion: 0.07
Nodes (16): Variants, Recent Changes, _clean(), fmdv_h(), min_conforming(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+8 more)

### Community 78 - "GroundTruthLabeler"
Cohesion: 0.25
Nodes (4): GroundTruthLabeler, _resolve_position(), _values_equal(), TestGroundTruthLabeler

### Community 79 - "infer_column_data_type"
Cohesion: 0.18
Nodes (4): infer_column_data_type(), is_mixed_alphanumeric(), TestDataTypeInference, TestMixedAlphanumeric

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "test_auto_validate_index.py"
Cohesion: 0.10
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 83 - "UniDetect"
Cohesion: 0.07
Nodes (14): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectColumnTypeRouting, TestUniDetectDetect (+6 more)

### Community 84 - "gaussian_outlier_strategies"
Cohesion: 0.23
Nodes (4): gaussian_outlier_strategies(), _is_float_like(), TestGaussianOutlierStrategies, TestRowWeightedNumericGate

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "OPE-89: Fix Spark Cache Lifecycle in Uni-Detect"
Cohesion: 0.25
Nodes (7): Blockers, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "CorpusNotFoundError"
Cohesion: 0.13
Nodes (13): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Uni-Detect, Job arguments (+5 more)

### Community 90 - "perturb_spelling"
Cohesion: 0.29
Nodes (3): _score_column(), perturb_spelling(), TestPerturbSpelling

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tokenize"
Cohesion: 0.13
Nodes (7): compute_token_counts(), token_prevalence(), is_float_like(), tokenize(), TestTokenPrevalence, TestFloatLike, TestTokenize

### Community 94 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "CorpusStatsStore"
Cohesion: 0.11
Nodes (5): ComparisonDirection, CorpusStatsStore, TestBatchScoreOptimization, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 100 - "CallableLabeler"
Cohesion: 0.19
Nodes (4): CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "concepts.md"
Cohesion: 0.25
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 103 - "pytest"
Cohesion: 0.09
Nodes (11): Errors, DataQualityError, IndexNotBuiltError, OpenDetectError, pair_table(), test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error() (+3 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "wiki_subset/generate_report.py"
Cohesion: 0.27
Nodes (11): _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart(), render_markdown() (+3 more)

### Community 106 - "Installation"
Cohesion: 0.50
Nodes (4): Check it works, Installation, Installing from source, Pick your extra

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 110 - "builder.py"
Cohesion: 0.06
Nodes (3): FailureTracker, get_logger(), TestCorpusStatsSchemaWeightType

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 115 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 118 - "hooks"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

### Community 119 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 121 - "_value_matches_groups"
Cohesion: 0.29
Nodes (4): _matches_segments(), _value_matches_groups(), _counting_value_matches_groups(), counting()

### Community 122 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 126 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 127 - "test_logging_utils.py"
Cohesion: 0.15
Nodes (3): TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 129 - "Benchmark: WIKI subset"
Cohesion: 0.33
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 130 - "Auto-Validate"
Cohesion: 0.22
Nodes (7): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly, Errors

### Community 131 - "test_algorithms_registry.py"
Cohesion: 0.08
Nodes (14): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy() (+6 more)

### Community 132 - "UnknownAlgorithmError"
Cohesion: 0.29
Nodes (6): Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema, UnknownAlgorithmError

### Community 134 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 137 - "_random_words"
Cohesion: 0.31
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 139 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 140 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 142 - ".index"
Cohesion: 0.33
Nodes (4): Inspecting a pattern, Reading the output, Usage, segment()

### Community 147 - "ValidationError"
Cohesion: 0.17
Nodes (10): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification, 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP) (+2 more)

### Community 151 - "v0.2.7 (2026-10-18)"
Cohesion: 0.50
Nodes (4): Bug Fixes, Documentation, Refactoring, v0.2.7 (2026-10-18)

### Community 155 - "Appendix: Validation Function Reference"
Cohesion: 0.29
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _validate_literal_value(), TestValidateLiteralValue

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 339 - "featurization.py"
Cohesion: 0.12
Nodes (11): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 433 - "BaseDetector"
Cohesion: 0.24
Nodes (5): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector

### Community 458 - "make_evidence_json"
Cohesion: 0.14
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), compute(), TestRedactEvidence

### Community 530 - "patterns.py"
Cohesion: 0.06
Nodes (23): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+15 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.13
Nodes (17): ProfileRunSkippedUniDetect, require_uni_detect(), _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match() (+9 more)

### Community 686 - "test_metrics.py"
Cohesion: 0.07
Nodes (18): drop_nulls(), require_min_size(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+10 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.15
Nodes (4): differing_token_lengths(), min_pairwise_edit_distance(), try_min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.26
Nodes (7): diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.11
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 1218 - "real_world_gov/generate_report.py"
Cohesion: 0.32
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1225 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `UnknownAlgorithmError`, `AutoValidateAlgorithm`, `wiki_subset/run_benchmark.py`, `PatternIndex`, `auto_validate/detector.py`, `InferredPattern`, `test_auto_validate_index.py`, `test_auto_validate_fmdv_v.py`, `ConfigurationError`, `fmdv`, `raha/detector.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11904761904761904 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `UnityCatalogLocation`, `_StubDetector`, `_filter_by_column_type`, `wiki_subset/run_benchmark.py`, `FailureCounts`, `FeatureBucket`, `.detect`, `_FakeDetector`, `Detection`, `InsufficientDataError`, `raha/detector.py`, `CorpusStatsBuilder`, `unittest_mock`, `BaseDetector`, `get_spec`, `.detect`, `real_world_gov/run_benchmark.py`, `_score_single_column`, `open_detect/__init__.py`, `featurization.py`, `UniDetect`, `CorpusNotFoundError`, `CorpusStatsStore`, `builder.py`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 70 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._