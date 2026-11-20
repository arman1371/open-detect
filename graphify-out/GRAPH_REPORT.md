# Graph Report - open-detect  (2026-11-20)

## Corpus Check
- 206 files · ~162,448 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 468 files seen (50%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 3023 nodes · 6620 edges · 148 communities (124 shown, 24 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 852 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9308c4af`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- test_bench_snapshot.py
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
- perturb_uniqueness
- fmdv_v
- permissions
- with
- update-graph
- check_failure_threshold
- with
- _segment_dp
- UnityCatalogLocation
- Completed Work
- ValidationError
- warnings
- .detect
- pytest
- _score_single_column
- main
- ScoringJobCounter
- get_algorithm
- build_column_features
- FailureCountsAccumulatorParam
- metrics/spelling.py
- fd_compliance_ratio
- real_world_gov benchmark results
- test_raha_labeling.py
- test_hygiene.py
- UniDetectConfig
- Benchmark: WIKI subset
- GroundTruthLabeler
- Auto-Validate
- test_algorithms_registry.py
- CHANGELOG
- UniDetectAlgorithm
- index.py
- ErrorDetectionAlgorithm
- Running on Databricks
- _ensure_dataframe_is_spark
- PatternIndex
- updates
- Raha
- jobs
- .build_corpus_statistics
- _ensure_sequence_of_str
- _coerce_numeric
- build
- uses
- confusion_metrics
- env
- perturb_spelling
- CorpusStatsStore
- dry_run
- test_package_init.py
- ErrorType
- CorpusIngestor
- variables
- labeling.py
- PRD: API Validation Framework for open-detect
- dev
- clean_column
- Commit conventions and releases
- HeuristicLabeler
- TestAttempt
- Current Status: BLOCKED
- _aggregate_scored_rows
- UniDetect
- gaussian_outlier_strategies
- test
- hooks
- release.yml
- release
- numpy
- test_exceptions.py
- pypi
- Current Status: BLOCKED
- log_transform_fits_better
- spark_session.py
- with
- on
- Review Complete: OPE-194 (PR #106)
- steps
- argparse
- CallableLabeler
- OPE-133 Review Summary
- finite_floats
- open_detect/exceptions.py
- sonarqube
- Raha
- infer_column_data_type
- docs
- force
- _default_classifier_factory
- TestCorpusStatsSchemaWeightType
- algorithms/uni-detect.md
- select_fd_column_pairs
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_console_scripts.py
- `uni_detect`
- `raha`
- Comparing algorithms
- AutoValidateAlgorithm
- paperclip-issue-update.sh
- API reference
- Uni-Detect
- auto_validate/detector.py
- sys
- CorpusStatsBuilder
- __getattr__
- _detector
- test_metrics.py
- TestScopedConf
- builder.py
- pipeline.py
- get_spec
- patterns.py
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
5. `FailureCounts` - 62 edges
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
- `3.1 Context` --references--> `AlgorithmResult`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (148 total, 24 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.09
Nodes (10): diff_fingerprints(), read_build_config(), verify_build_config(), _config(), FakeConf, FakeSpark, test_diff_fingerprints_reports_missing_fields(), TestLegacyCorpus (+2 more)

### Community 1 - "test_bench_snapshot.py"
Cohesion: 0.20
Nodes (13): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+5 more)

### Community 2 - "pandas"
Cohesion: 0.10
Nodes (21): _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting(), _detect(), _detector() (+13 more)

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
Cohesion: 0.08
Nodes (15): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main() (+7 more)

### Community 10 - "FailureCounts"
Cohesion: 0.18
Nodes (6): compute(), _score_fd_pair(), compute(), FailureCounts, compute(), TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "FeatureBucket"
Cohesion: 0.18
Nodes (6): Candidate, FeatureBucket, MetricObservation, TestCandidate, TestFeatureBucket, TestMetricObservation

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.08
Nodes (16): Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema, Auto-Validate: learn patterns from clean columns, Quickstart, Reading results (+8 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (13): AutoValidateConfig, build_pattern_index(), indexable_values(), TestDefaults, TestValidation, _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCorpusInputShapes (+5 more)

### Community 16 - "InferredPattern"
Cohesion: 0.11
Nodes (7): check_drift(), _clean_series(), _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.17
Nodes (10): _drop_nulls(), _positions_of(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order(), test_evidence_honors_redact_mode() (+2 more)

### Community 18 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "perturb_uniqueness"
Cohesion: 0.14
Nodes (7): duplicate_value_indices(), uniqueness_ratio(), _max_drop(), perturb_uniqueness(), TestDuplicateValueIndices, TestUniquenessRatio, TestPerturbUniqueness

### Community 20 - "fmdv_v"
Cohesion: 0.08
Nodes (10): _coarse_signature(), fmdv_v(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV, TestFmdvVh (+2 more)

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

### Community 26 - "_segment_dp"
Cohesion: 0.12
Nodes (10): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Recent Changes, Test Results, _fmdv_single_segment(), _segment_dp(), _segment_fmdv_v() (+2 more)

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.05
Nodes (15): ensure_schema_exists(), UnityCatalogLocation, _validate_edges(), UnityCatalogError, bucket_by_edges(), bucket_leftness(), _require_columns(), ConfigurationError (+7 more)

### Community 28 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 29 - "ValidationError"
Cohesion: 0.06
Nodes (18): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification, Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_columns_unique() (+10 more)

### Community 31 - ".detect"
Cohesion: 0.10
Nodes (5): cluster_column(), sample_tuple(), _validate_literal_value(), TestClusterColumn, TestSampleTuple

### Community 32 - "pytest"
Cohesion: 0.19
Nodes (11): test_missing_columns_rejected(), test_require_uni_detect_fails_when_undetected(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 34 - "main"
Cohesion: 0.13
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 36 - "get_algorithm"
Cohesion: 0.12
Nodes (13): Check it works, Installation, Installing from source, Pick your extra, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+5 more)

### Community 37 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 39 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 40 - "fd_compliance_ratio"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_hygiene.py"
Cohesion: 0.07
Nodes (11): list_tables(), table_exists(), _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release(), TestListTables, TestTableExists (+3 more)

### Community 44 - "UniDetectConfig"
Cohesion: 0.05
Nodes (16): Configuration, list_tables_matching(), UniDetectConfig, _score_column(), main(), parse_args(), _run(), _FakeDetector (+8 more)

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.35
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 47 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.08
Nodes (15): get_algorithm_class(), list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered() (+7 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.06
Nodes (30): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+22 more)

### Community 50 - "UniDetectAlgorithm"
Cohesion: 0.20
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 51 - "index.py"
Cohesion: 0.07
Nodes (13): _conforms(), DriftResult, _append_literal(), _char_class(), _class_of_token(), _is_numeric(), matches(), matches_tokens() (+5 more)

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.16
Nodes (10): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+2 more)

### Community 53 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 55 - "PatternIndex"
Cohesion: 0.06
Nodes (14): Variants, _clean(), fmdv(), fmdv_h(), min_conforming(), _fmdv_h_single(), fmdv_vh(), _segment_fmdv_vh() (+6 more)

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
Nodes (6): build_spark(), main(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 61 - "_coerce_numeric"
Cohesion: 0.19
Nodes (4): _coerce_numeric(), config(), TestCoerceNumeric, score()

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "confusion_metrics"
Cohesion: 0.14
Nodes (13): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+5 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "perturb_spelling"
Cohesion: 0.20
Nodes (5): perturb_functional_dependency(), perturb_spelling(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbSpelling

### Community 67 - "CorpusStatsStore"
Cohesion: 0.11
Nodes (5): Changes Verified, CorpusStatsStore, TestBatchScoreOptimization, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "ErrorType"
Cohesion: 0.06
Nodes (22): ColumnDataType, ComparisonDirection, ErrorType, CorpusColumnRecord, CorpusPairRecord, Detection, property_key(), write_build_config() (+14 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.12
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "labeling.py"
Cohesion: 0.12
Nodes (14): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+6 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.07
Nodes (26): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+18 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "HeuristicLabeler"
Cohesion: 0.29
Nodes (4): ColumnFeatures, HeuristicLabeler, _resolve_position(), TestHeuristicLabeler

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.17
Nodes (4): _aggregate_scored_rows(), compute(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "UniDetect"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

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

### Community 90 - "test_exceptions.py"
Cohesion: 0.29
Nodes (4): test_all_errors_derive_from_open_detect_error(), test_insufficient_data_error_is_not_a_value_error(), test_open_detect_error_is_catchable_broadly(), test_validation_error_is_also_a_value_error()

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 94 - "spark_session.py"
Cohesion: 0.18
Nodes (5): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "Review Complete: OPE-194 (PR #106)"
Cohesion: 0.40
Nodes (4): Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.18
Nodes (5): Raha: find errors with a few labels, CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.09
Nodes (13): Errors, Errors, CorpusNotFoundError, DataQualityError, InsufficientDataError, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError (+5 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "Raha"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 106 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.09
Nodes (13): Algorithms, Fidelity to the papers, Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance (+5 more)

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

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

### Community 120 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.08
Nodes (11): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm (+3 more)

### Community 127 - "API reference"
Cohesion: 0.12
Nodes (13): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, API reference, Configuration (+5 more)

### Community 131 - "Uni-Detect"
Cohesion: 0.22
Nodes (9): A fully local example, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Reading the detections, Through the registry, Uni-Detect (+1 more)

### Community 134 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (25): Implementation Status, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification (+17 more)

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.12
Nodes (9): CorpusStatsBuilder, _stats_schema_without_error_type(), FailureTracker, scoped_conf(), _config(), _pairs(), _StubDetector, TestCorpusBuilderFailureGate (+1 more)

### Community 205 - "_detector"
Cohesion: 0.13
Nodes (4): _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 426 - "builder.py"
Cohesion: 0.09
Nodes (7): configure_logging(), get_logger(), log_duration(), config(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 433 - "pipeline.py"
Cohesion: 0.07
Nodes (9): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, _filter_by_column_type(), get_spark(), _config() (+1 more)

### Community 458 - "get_spec"
Cohesion: 0.05
Nodes (16): _require_min_rows(), _hash_value(), make_evidence_json(), redact_evidence(), compute(), _score_pair(), _build_row(), _original_row_ids() (+8 more)

### Community 530 - "patterns.py"
Cohesion: 0.06
Nodes (18): generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize(), _alternatives(), any_pattern() (+10 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.19
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.12
Nodes (11): drop_nulls(), require_min_size(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+3 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.08
Nodes (15): main(), ColumnPredictions, _make_classifier(), train_and_predict(), RahaConfig, RahaDetector, _features(), TestClassifierTrainingPath (+7 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.14
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.32
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1129 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `Uni-Detect`, `json`, `FailureCounts`, `FeatureBucket`, `CorpusStatsBuilder`, `_score_single_column`, `main`, `builder.py`, `test_hygiene.py`, `UniDetectConfig`, `pipeline.py`, `UniDetectAlgorithm`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `CorpusStatsStore`, `get_spec`, `UniDetect`, `open_detect/exceptions.py`, `API reference`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.08717948717948718 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `auto_validate/detector.py`, `json`, `CellResult`, `InferredPattern`, `index.py`, `fmdv_v`, `PatternIndex`, `AutoValidateAlgorithm`, `_segment_dp`, `UnityCatalogLocation`, `API reference`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._