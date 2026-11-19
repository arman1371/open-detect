# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-18)

## Corpus Check
- 193 files · ~161,403 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 3019 nodes · 6620 edges · 165 communities (139 shown, 26 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 835 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2c5c2c75`
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
- config
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- FeatureBucket
- perturbation.py
- test_auto_validate_fmdv_v.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- get_spec
- UnityCatalogLocation
- Completed Work
- ValidationError
- UniDetectConfig
- cluster_column
- pytest
- raha/strategies.py
- main
- ScoringJobCounter
- algorithms/uni-detect.md
- features.py
- fd_violation_strategies
- collections_abc
- metrics/functional_dependency.py
- real_world_gov benchmark results
- .detect
- test_build_corpus_statistics.py
- main
- `auto_validate`
- GroundTruthLabeler
- .infer_pattern
- registry.py
- CHANGELOG
- reference/index.md
- auto_validate/detector.py
- ErrorDetectionAlgorithm
- CorpusNotFoundError
- matches
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
- ColumnDataType
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
- pattern_character_strategies
- test
- test_bench_snapshot.py
- release.yml
- release
- test_raha_strategies.py
- featurization.py
- pypi
- Current Status: BLOCKED
- RahaDetector
- spark_session.py
- with
- on
- gaussian_outlier_strategies
- steps
- argparse
- CallableLabeler
- _segment_dp
- _require_columns
- OpenDetectError
- sonarqube
- require_uni_detect
- uni_detect/text_utils.py
- docs
- force
- tokenize
- pipeline.py
- docs/index.md
- select_fd_column_pairs
- Benchmark: WIKI subset
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_console_scripts.py
- infer_column_data_type
- TestUniDetectDetect
- _build_row
- Comparing algorithms
- AutoValidateAlgorithm
- _FakeDetector
- paperclip-issue-update.sh
- algorithms/index.md
- Auto-Validate
- open_detect_wheel
- _make_tooltip
- _value_matches_groups
- Uni-Detect
- _fmdv_h_single
- Detection
- _value_matches
- TestConfigThreshold
- uniqueness_ratio
- Uni-Detect
- _StubDetector
- sys
- is_float_like
- CorpusStatsBuilder
- __getattr__
- Methodology: auto_validate
- Scoring auto_validate
- _NoCandidatesDetector
- _detector
- test_metrics.py
- TestScopedConf
- get_logger
- BaseDetector
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

## Communities (165 total, 26 thin omitted)

### Community 0 - "CorpusStatsBuilder"
Cohesion: 0.08
Nodes (13): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeConf, FakeSpark (+5 more)

### Community 1 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 2 - "pandas"
Cohesion: 0.12
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

### Community 7 - "builder.py"
Cohesion: 0.07
Nodes (5): _validate_edges(), _require_min_rows(), ConfigurationError, TestCorpusStatsSchema, TestCorpusStatsSchemaWeightType

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.29
Nodes (7): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4)

### Community 9 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 10 - "FailureCounts"
Cohesion: 0.11
Nodes (8): compute(), _score_fd_pair(), FailureCounts, FailureCountsAccumulatorParam, _raise(), TestAttempt, TestFailureCounts, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.08
Nodes (16): Through the registry, The shared result schema, Combine, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code (+8 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "InferredPattern"
Cohesion: 0.08
Nodes (12): _infer_pattern_to_groups(), _matches_segments(), check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed() (+4 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.16
Nodes (11): _drop_nulls(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order() (+3 more)

### Community 19 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 20 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.14
Nodes (7): _build_index(), _date_index(), _date_values(), TestFmdvV, TestFmdvVh, TestLargeGroups, _time_corpus()

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

### Community 26 - "get_spec"
Cohesion: 0.17
Nodes (6): all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.11
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 28 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 29 - "ValidationError"
Cohesion: 0.06
Nodes (17): Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _ensure_sequence_of_str() (+9 more)

### Community 30 - "UniDetectConfig"
Cohesion: 0.20
Nodes (3): UniDetectConfig, config(), TestUniDetectConfig

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "pytest"
Cohesion: 0.07
Nodes (14): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+6 more)

### Community 33 - "raha/strategies.py"
Cohesion: 0.21
Nodes (4): _factorize_column(), histogram_outlier_strategies(), normalize_to_str(), TestHistogramOutlierStrategies

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 36 - "algorithms/uni-detect.md"
Cohesion: 0.20
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 37 - "features.py"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 38 - "fd_violation_strategies"
Cohesion: 0.27
Nodes (3): fd_violation_strategies(), TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 39 - "collections_abc"
Cohesion: 0.19
Nodes (7): require_min_size(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 40 - "metrics/functional_dependency.py"
Cohesion: 0.19
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.27
Nodes (5): ErrorType, _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 44 - "main"
Cohesion: 0.18
Nodes (5): main(), parse_args(), test_main_installs_logging(), TestMain, TestParseArgs

### Community 45 - "`auto_validate`"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.21
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 47 - ".infer_pattern"
Cohesion: 0.18
Nodes (10): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+2 more)

### Community 48 - "registry.py"
Cohesion: 0.06
Nodes (23): Check it works, API reference, _constant_factory(), get_algorithm(), get_algorithm_class(), list_algorithms(), _load_entry_points(), register_lazy() (+15 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 51 - "auto_validate/detector.py"
Cohesion: 0.09
Nodes (10): Recent Changes, _clean(), _coarse_signature(), fmdv_v(), fmdv_vh(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh() (+2 more)

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (11): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), register_algorithm(), decorator(), UniDetectAlgorithm, __getattr__() (+3 more)

### Community 53 - "CorpusNotFoundError"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 54 - "matches"
Cohesion: 0.20
Nodes (4): matches(), fpr_column(), impurity(), TestMatching

### Community 55 - "fmdv.py"
Cohesion: 0.10
Nodes (7): Variants, fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Raha"
Cohesion: 0.17
Nodes (9): Configuration, How it works, Install, Raha, Scope, Configuration, Detector, Labelers (+1 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.15
Nodes (6): build_spark(), main(), _filter_by_column_type(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

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
Cohesion: 0.08
Nodes (15): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+7 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 67 - "CorpusStatsStore"
Cohesion: 0.12
Nodes (4): CorpusStatsStore, TestBatchScoreOptimization, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "ColumnDataType"
Cohesion: 0.12
Nodes (9): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords (+1 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.11
Nodes (6): balanced_union(), CorpusIngestor, compute_token_counts(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "KnownIndexLabeler"
Cohesion: 0.39
Nodes (3): KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.04
Nodes (40): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+32 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_auto_validate_index.py"
Cohesion: 0.10
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "raha/detector.py"
Cohesion: 0.10
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.20
Nodes (4): _aggregate_scored_rows(), compute(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "_config"
Cohesion: 0.14
Nodes (8): UniDetect, _config(), _mock_spark(), TestUniDetectBuildCorpusStatistics, TestUniDetectInit, TestUniDetectRelease, TestUniDetectValidateInputs, TestUniDetectWriteDetections

### Community 84 - "pattern_character_strategies"
Cohesion: 0.17
Nodes (4): pattern_character_strategies(), TestEmptyFrames, TestNullSentinel, TestPatternCharacterStrategies

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
Nodes (10): bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket(), log_transform_fits_better() (+2 more)

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "RahaDetector"
Cohesion: 0.21
Nodes (6): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 94 - "spark_session.py"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "gaussian_outlier_strategies"
Cohesion: 0.23
Nodes (4): gaussian_outlier_strategies(), _is_float_like(), TestGaussianOutlierStrategies, TestRowWeightedNumericGate

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.18
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "_segment_dp"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 103 - "OpenDetectError"
Cohesion: 0.10
Nodes (15): Errors, Errors, CorpusNotFoundError, DataQualityError, InsufficientDataError, UnityCatalogError, IndexNotBuiltError, OpenDetectError (+7 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "require_uni_detect"
Cohesion: 0.33
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 106 - "uni_detect/text_utils.py"
Cohesion: 0.15
Nodes (4): is_integer_like(), is_mixed_alphanumeric(), TestIntegerLike, TestMixedAlphanumeric

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 110 - "pipeline.py"
Cohesion: 0.08
Nodes (11): list_tables(), list_tables_matching(), table_exists(), _run(), get_spark(), configure_logging(), TestListTables, TestListTablesMatching (+3 more)

### Community 111 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 113 - "Benchmark: WIKI subset"
Cohesion: 0.20
Nodes (10): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, Scoring raha, The corpus (`data/corpus/`) (+2 more)

### Community 115 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 116 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 118 - "TestUniDetectDetect"
Cohesion: 0.24
Nodes (3): _mock_detector_result(), _mock_spark_context(), TestUniDetectDetect

### Community 119 - "_build_row"
Cohesion: 0.22
Nodes (4): _build_row(), _original_row_ids(), _score_column(), compute()

### Community 120 - "Comparing algorithms"
Cohesion: 0.40
Nodes (5): Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 127 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 128 - "open_detect_wheel"
Cohesion: 0.22
Nodes (8): artifacts, open_detect_wheel, bundle, name, build, path, type, UniDetect pipeline facade

### Community 129 - "_make_tooltip"
Cohesion: 0.29
Nodes (4): _build_suggestion(), _make_tooltip(), _tooltip_content(), TooltipContent

### Community 130 - "_value_matches_groups"
Cohesion: 0.25
Nodes (5): _value_matches_groups(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting()

### Community 131 - "Uni-Detect"
Cohesion: 0.22
Nodes (9): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Reading the detections, Uni-Detect (+1 more)

### Community 132 - "_fmdv_h_single"
Cohesion: 0.33
Nodes (3): min_conforming(), _fmdv_h_single(), TestMinConforming

### Community 134 - "_value_matches"
Cohesion: 0.09
Nodes (19): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+11 more)

### Community 137 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 138 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.14
Nodes (7): CorpusStatsBuilder, _stats_schema_without_error_type(), FailureTracker, TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 143 - "Methodology: auto_validate"
Cohesion: 0.50
Nodes (4): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override

### Community 144 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 376 - "TestScopedConf"
Cohesion: 0.11
Nodes (3): scoped_conf(), TestGetSparkExtended, TestScopedConf

### Community 426 - "get_logger"
Cohesion: 0.15
Nodes (5): get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 433 - "BaseDetector"
Cohesion: 0.12
Nodes (5): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector

### Community 458 - "make_evidence_json"
Cohesion: 0.10
Nodes (9): _hash_value(), make_evidence_json(), redact_evidence(), compute(), _score_pair(), compute(), _score_column(), compute() (+1 more)

### Community 530 - "hierarchy.py"
Cohesion: 0.05
Nodes (27): _fmdv_single_segment(), _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs() (+19 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.16
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.09
Nodes (18): maybe_scope(), UniDetectProfile, git_commit(), _build_config(), main(), _print_comparison(), _register_table(), run() (+10 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.09
Nodes (14): Concepts, Configuration objects, One contract: `detect()`, The registry, ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory() (+6 more)

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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1114 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `confusion_metrics`, `_make_tooltip`, `real_world_gov/run_benchmark.py`, `RahaConfig`, `_fmdv_h_single`, `_value_matches`, `builder.py`, `test_auto_validate_index.py`, `registry.py`, `InferredPattern`, `hierarchy.py`, `auto_validate/detector.py`, `test_auto_validate_fmdv_v.py`, `fmdv.py`, `AutoValidateAlgorithm`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CorpusStatsBuilder` be split into smaller, more focused modules?**
  _Cohesion score 0.08309178743961353 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `test_build_corpus_statistics.py` to `CorpusStatsBuilder`, `Uni-Detect`, `Detection`, `builder.py`, `FailureCounts`, `_StubDetector`, `CorpusStatsBuilder`, `_NoCandidatesDetector`, `FeatureBucket`, `get_spec`, `UnityCatalogLocation`, `main`, `main`, `registry.py`, `BaseDetector`, `ErrorDetectionAlgorithm`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `CorpusStatsStore`, `_score_single_column`, `ColumnDataType`, `_config`, `featurization.py`, `OpenDetectError`, `pipeline.py`, `TestUniDetectDetect`, `_FakeDetector`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._