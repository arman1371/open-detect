# Graph Report - open-detect  (2026-11-20)

## Corpus Check
- 206 files · ~162,492 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 468 files seen (50%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 3025 nodes · 6622 edges · 160 communities (135 shown, 25 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 852 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `def94f1a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- builder.py
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- TestCorpusStatsSchema
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
- fmdv_v
- permissions
- with
- update-graph
- check_failure_threshold
- with
- PatternIndex
- UnityCatalogLocation
- _check_expected_type
- ValidationError
- warnings
- .detect
- test_deprecated_shims.py
- InsufficientDataError
- main
- ScoringJobCounter
- list_algorithms
- build_column_features
- FailureCountsAccumulatorParam
- metrics/spelling.py
- metrics/functional_dependency.py
- real_world_gov benchmark results
- test_raha_labeling.py
- test_build_corpus_statistics.py
- _run
- Benchmark: WIKI subset
- GroundTruthLabeler
- Auto-Validate
- test_algorithms_registry.py
- CHANGELOG
- raha/detector.py
- matches
- registry.py
- Running on Databricks
- UniDetectConfig
- fmdv
- updates
- Raha
- jobs
- .build_corpus_statistics
- _ensure_sequence_of_str
- _coerce_numeric
- build
- uses
- _value_matches
- env
- perturb_spelling
- .batch_score
- dry_run
- test_package_init.py
- featurization.py
- CorpusIngestor
- variables
- AutoValidateAlgorithm
- PRD: API Validation Framework for open-detect
- dev
- clean_column
- Commit conventions and releases
- labeling.py
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
- run_detection.py
- pypi
- Current Status: BLOCKED
- dataset_utils.py
- spark_session.py
- with
- on
- RahaDetector
- steps
- argparse
- CallableLabeler
- OPE-133 Review Summary
- ConfigurationError
- OpenDetectError
- sonarqube
- Raha
- infer_column_data_type
- docs
- force
- profile.py
- TestCorpusStatsSchemaWeightType
- docs/index.md
- select_fd_column_pairs
- uni_detect/core/models.py
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_console_scripts.py
- `uni_detect`
- `raha`
- MetricObservation
- Comparing algorithms
- .detect
- algorithms/uni-detect.md
- paperclip-issue-update.sh
- concepts.md
- reference/index.md
- _FakeDetector
- Detection
- uniqueness_ratio
- Uni-Detect
- _StubDetector
- algorithms/index.md
- auto_validate/detector.py
- Auto-Validate
- TestConfigThreshold
- 5. Market Segment(s)
- sys
- CorpusStatsBuilder
- __getattr__
- _detector
- test_metrics.py
- scoped_conf
- build_corpus_statistics.py
- ErrorType
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

## Communities (160 total, 25 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.08
Nodes (13): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeConf, FakeSpark (+5 more)

### Community 1 - "builder.py"
Cohesion: 0.08
Nodes (3): _spark_available(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 2 - "pandas"
Cohesion: 0.06
Nodes (40): _is_null(), _non_null_cells(), _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting() (+32 more)

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

### Community 9 - "wiki_subset/run_benchmark.py"
Cohesion: 0.07
Nodes (25): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+17 more)

### Community 10 - "FailureCounts"
Cohesion: 0.14
Nodes (6): compute(), _score_fd_pair(), FailureCounts, _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.09
Nodes (11): Through the registry, Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Why a common interface, AlgorithmResult (+3 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.14
Nodes (12): _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions() (+4 more)

### Community 18 - "_ensure_dataframe_is_spark"
Cohesion: 0.10
Nodes (14): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+6 more)

### Community 19 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 20 - "fmdv_v"
Cohesion: 0.11
Nodes (8): _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV, TestFmdvVh, _time_corpus()

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
Cohesion: 0.20
Nodes (3): DataQualityError, check_failure_threshold(), TestCheckFailureThreshold

### Community 25 - "with"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "PatternIndex"
Cohesion: 0.11
Nodes (7): Recent Changes, _fmdv_h_single(), _fmdv_single_segment(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), PatternIndex

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.11
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config()

### Community 28 - "_check_expected_type"
Cohesion: 0.14
Nodes (10): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status (+2 more)

### Community 29 - "ValidationError"
Cohesion: 0.07
Nodes (18): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, Appendix: Validation Function Reference, _check_columns_present(), ValidationError (+10 more)

### Community 30 - "warnings"
Cohesion: 0.15
Nodes (3): __getattr__(), __getattr__(), test_old_except_clause_catches_new_error()

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "test_deprecated_shims.py"
Cohesion: 0.21
Nodes (8): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only(), test_module_shims_are_identity_preserving(), test_unknown_exception_attr_raises()

### Community 33 - "InsufficientDataError"
Cohesion: 0.14
Nodes (7): _require_min_rows(), _score_single_column(), InsufficientDataError, config(), TestScoreFdPair, TestScoreSingleColumn, score()

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 36 - "list_algorithms"
Cohesion: 0.10
Nodes (13): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+5 more)

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
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 44 - "_run"
Cohesion: 0.08
Nodes (13): list_tables(), list_tables_matching(), table_exists(), main(), parse_args(), _run(), test_main_installs_logging(), TestMain (+5 more)

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 47 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (9): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_get_algorithm_constructs_with_args(), TestPluginDiscovery, worker() (+1 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.06
Nodes (32): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+24 more)

### Community 50 - "raha/detector.py"
Cohesion: 0.11
Nodes (10): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), register_algorithm(), UniDetectAlgorithm, __getattr__(), _config() (+2 more)

### Community 51 - "matches"
Cohesion: 0.10
Nodes (9): matches(), indexable_values(), fpr_column(), impurity(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestEquivalenceToReferenceBuild, TestIndexableValues (+1 more)

### Community 52 - "registry.py"
Cohesion: 0.20
Nodes (8): _constant_factory(), get_algorithm_class(), _load_entry_points(), decorator(), register_lazy(), test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name(), test_unknown_algorithm_raises()

### Community 53 - "Running on Databricks"
Cohesion: 0.40
Nodes (4): Job arguments, Jobs, Notebooks, Running on Databricks

### Community 54 - "UniDetectConfig"
Cohesion: 0.16
Nodes (4): UniDetectConfig, config(), TestUniDetectConfig, config()

### Community 55 - "fmdv"
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
Cohesion: 0.13
Nodes (6): build_spark(), main(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "_value_matches"
Cohesion: 0.10
Nodes (16): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+8 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "featurization.py"
Cohesion: 0.06
Nodes (19): ColumnDataType, _score_pair(), _score_column(), _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count() (+11 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.12
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "AutoValidateAlgorithm"
Cohesion: 0.16
Nodes (6): Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm, segment(), TestAutoValidateDetector

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.11
Nodes (17): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+9 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "labeling.py"
Cohesion: 0.11
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 79 - "CorpusStatsStore"
Cohesion: 0.15
Nodes (6): Operational notes, Practical advice, CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.11
Nodes (9): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results, _aggregate_scored_rows(), compute(), TestAggregateScoredRows (+1 more)

### Community 83 - "UniDetect"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "numpy"
Cohesion: 0.07
Nodes (14): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), pattern_character_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls (+6 more)

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

### Community 90 - "run_detection.py"
Cohesion: 0.14
Nodes (3): get_spark(), TestGetSparkExtended, TestGetSpark

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 94 - "spark_session.py"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "RahaDetector"
Cohesion: 0.19
Nodes (7): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.19
Nodes (4): CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 103 - "OpenDetectError"
Cohesion: 0.11
Nodes (16): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, The shared result schema, Errors, IndexNotBuiltError (+8 more)

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

### Community 109 - "profile.py"
Cohesion: 0.20
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 111 - "docs/index.md"
Cohesion: 0.22
Nodes (5): open-detect, What is in the box, Registry, Registry and results, Result types

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 113 - "uni_detect/core/models.py"
Cohesion: 0.24
Nodes (3): CorpusColumnRecord, CorpusPairRecord, TestCorpusRecords

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

### Community 119 - "MetricObservation"
Cohesion: 0.29
Nodes (4): Candidate, MetricObservation, TestCandidate, TestMetricObservation

### Community 120 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 121 - ".detect"
Cohesion: 0.11
Nodes (5): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, _make_tiny_corpus()

### Community 122 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 126 - "concepts.md"
Cohesion: 0.28
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 127 - "reference/index.md"
Cohesion: 0.22
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 131 - "Uni-Detect"
Cohesion: 0.25
Nodes (8): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Reading the detections, Uni-Detect, Usage on Databricks

### Community 132 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 134 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (15): _build_suggestion(), _feasible_evidence(), _infeasible_evidence(), _infer_pattern_to_groups(), _make_tooltip(), _matches_segments(), _tooltip_content(), _value_matches_groups() (+7 more)

### Community 135 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 137 - "5. Market Segment(s)"
Cohesion: 0.50
Nodes (4): 5.1 Primary Segment, 5.2 Secondary Segment, 5.3 Constraints, 5. Market Segment(s)

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.19
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 426 - "build_corpus_statistics.py"
Cohesion: 0.09
Nodes (7): configure_logging(), get_logger(), log_duration(), pair_table(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 433 - "ErrorType"
Cohesion: 0.09
Nodes (13): ComparisonDirection, ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker (+5 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.11
Nodes (9): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), _build_row(), compute(), compute() (+1 more)

### Community 530 - "hierarchy.py"
Cohesion: 0.05
Nodes (25): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+17 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (12): maybe_scope(), UniDetectProfile, git_commit(), _build_config(), main(), _print_comparison(), _register_table(), run() (+4 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1130 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `builder.py`, `Detection`, `Uni-Detect`, `_FakeDetector`, `_StubDetector`, `wiki_subset/run_benchmark.py`, `FailureCounts`, `FeatureBucket`, `CorpusStatsBuilder`, `UnityCatalogLocation`, `InsufficientDataError`, `main`, `list_algorithms`, `build_corpus_statistics.py`, `test_build_corpus_statistics.py`, `_run`, `raha/detector.py`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `.batch_score`, `featurization.py`, `CorpusStatsStore`, `UniDetect`, `run_detection.py`, `uni_detect/core/models.py`, `MetricObservation`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.08309178743961353 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `_value_matches`, `real_world_gov/run_benchmark.py`, `list_algorithms`, `auto_validate/detector.py`, `OpenDetectError`, `ConfigurationError`, `wiki_subset/run_benchmark.py`, `AutoValidateAlgorithm`, `.test_all_variants_infer_something`, `InferredPattern`, `matches`, `fmdv_v`, `fmdv`, `.detect`, `PatternIndex`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._