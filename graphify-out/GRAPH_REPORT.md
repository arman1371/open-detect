# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-16)

## Corpus Check
- 191 files · ~157,224 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 2939 nodes · 6463 edges · 156 communities (121 shown, 35 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 815 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f6a4998d`
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
- matches
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
- PatternIndex
- permissions
- with
- update-graph
- check_failure_threshold
- with
- CorpusStatsBuilder
- test_raha_strategies.py
- _check_expected_type
- _check_dataframe_is_spark
- UniDetectConfig
- cluster_column
- get_algorithm
- numpy
- main
- pytest
- Benchmark: real_world_gov
- AutoValidateAlgorithm
- Labeler
- pipeline.py
- infer_column_data_type
- real_world_gov benchmark results
- verify_build_config
- test_build_corpus_statistics.py
- log_transform_fits_better
- Benchmark: WIKI subset
- auto_validate/detector.py
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
- labeling.py
- jobs
- .build_corpus_statistics
- open_detect_wheel
- _coerce_numeric
- build
- uses
- real_world_gov/run_benchmark.py
- env
- perturb_spelling
- CorpusStatsStore
- dry_run
- _score_single_column
- FeatureBucket
- CorpusIngestor
- variables
- uniqueness_ratio
- PRD: API Validation Framework for open-detect
- dev
- test_auto_validate_index.py
- Commit conventions and releases
- RahaDetector
- test_cache_lifecycle.py
- Current Status: BLOCKED
- TestPluginDiscoveryViaRealDistInfo
- _config
- algorithms/index.md
- test
- test_bench_snapshot.py
- release.yml
- release
- CorpusNotFoundError
- is_float_like
- pypi
- Current Status: BLOCKED
- tokenize
- spark_session.py
- with
- on
- Uni-Detect
- steps
- argparse
- CallableLabeler
- _segment_dp
- _check_columns_unique
- OpenDetectError
- sonarqube
- _StubDetector
- dataset_utils.py
- docs
- force
- get_spec
- logging_utils.py
- algorithms/uni-detect.md
- select_fd_column_pairs
- sys
- open-detect
- TestConfigThreshold
- test_console_scripts.py
- ConfigurationError
- `uni_detect`
- `raha`
- KnownIndexLabeler
- duplicate_value_indices
- score
- paperclip-issue-update.sh
- is_integer_like
- diff_fingerprints
- finite_floats
- __getattr__
- _detector
- test_metrics.py
- ScoringJobCounter
- featurization.py
- .detect
- _FakeDetector
- ErrorType
- detectors/base.py
- _search_mpd
- hierarchy.py
- perturb_numeric_outlier
- _ensure_sequence_of_str
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- json
- TestEnsureDataFrameIsSpark
- RahaConfig
- wiki_subset/generate_report.py
- builder.py
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 96 edges
3. `UniDetectConfig` - 92 edges
4. `UniDetect` - 70 edges
5. `FailureCounts` - 56 edges
6. `ValidationError` - 48 edges
7. `build_pattern_index()` - 46 edges
8. `UnityCatalogLocation` - 45 edges
9. `AutoValidateAlgorithm` - 39 edges
10. `CellResult` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Phase 1: Core Tooltip Engine (4 weeks)` --references--> `CellResult`  [INFERRED]
  PRD-user-feedback-tooltips.md → src/open_detect/algorithms/base.py
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `3.1 Context` --references--> `AlgorithmResult`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (156 total, 35 thin omitted)

### Community 0 - "write_build_config"
Cohesion: 0.15
Nodes (6): property_key(), read_build_config(), write_build_config(), FakeSpark, TestRoundTrip, TestWiring

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.16
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config()

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

### Community 7 - "fd_compliance_ratio"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "matches"
Cohesion: 0.17
Nodes (5): matches(), fpr_column(), impurity(), matching_pattern(), TestMatching

### Community 10 - "FailureCounts"
Cohesion: 0.14
Nodes (8): compute(), compute(), _score_fd_pair(), FailureCounts, compute(), _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.09
Nodes (6): Combine, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (13): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _date_index(), _date_values(), TestLargeGroups, TestSegmentDp (+5 more)

### Community 16 - "InferredPattern"
Cohesion: 0.07
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.16
Nodes (11): _drop_nulls(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order() (+3 more)

### Community 18 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.10
Nodes (17): 5.1 Primary Segment, 5.2 Secondary Segment, 5.3 Constraints, 5. Market Segment(s), ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect() (+9 more)

### Community 20 - "PatternIndex"
Cohesion: 0.08
Nodes (9): _fmdv_h_single(), _fmdv_single_segment(), _segment_fmdv_v(), _segment_fmdv_vh(), PatternIndex, any_pattern(), patterns_of(), sorted_patterns() (+1 more)

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

### Community 26 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 27 - "test_raha_strategies.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 28 - "_check_expected_type"
Cohesion: 0.14
Nodes (10): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status (+2 more)

### Community 29 - "_check_dataframe_is_spark"
Cohesion: 0.09
Nodes (12): Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_dataframe_is_spark(), _check_unknown_kwargs(), _ensure_dataframe_is_spark(), _reject_unknown_kwargs(), _validate_literal_value() (+4 more)

### Community 30 - "UniDetectConfig"
Cohesion: 0.17
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "get_algorithm"
Cohesion: 0.18
Nodes (8): Check it works, Installation, Installing from source, Pick your extra, API reference, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 33 - "numpy"
Cohesion: 0.07
Nodes (15): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestEmptyFrames (+7 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.09
Nodes (11): __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "Benchmark: real_world_gov"
Cohesion: 0.13
Nodes (12): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+4 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.06
Nodes (22): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+14 more)

### Community 38 - "Labeler"
Cohesion: 0.09
Nodes (19): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Configuration, How it works, Install, Raha (+11 more)

### Community 39 - "pipeline.py"
Cohesion: 0.08
Nodes (4): list_tables(), table_exists(), TestListTables, TestTableExists

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "verify_build_config"
Cohesion: 0.34
Nodes (4): verify_build_config(), _config(), TestLegacyCorpus, TestMismatch

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (21): Implementation Status, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification (+13 more)

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.11
Nodes (12): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered(), test_register_lazy_is_lazy() (+4 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 51 - "fmdv_v"
Cohesion: 0.09
Nodes (10): min_conforming(), _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV, TestFmdvVh (+2 more)

### Community 52 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "choosing-an-algorithm.md"
Cohesion: 0.18
Nodes (8): Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 55 - "fmdv.py"
Cohesion: 0.10
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "labeling.py"
Cohesion: 0.14
Nodes (6): ColumnFeatures, HeuristicLabeler, propagate_labels(), _resolve_position(), TestHeuristicLabeler, TestPropagateLabels

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.15
Nodes (6): build_spark(), main(), _filter_by_column_type(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "real_world_gov/run_benchmark.py"
Cohesion: 0.11
Nodes (14): confusion_metrics(), git_commit(), dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main() (+6 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 67 - "CorpusStatsStore"
Cohesion: 0.17
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "FeatureBucket"
Cohesion: 0.18
Nodes (6): Candidate, FeatureBucket, MetricObservation, TestCandidate, TestFeatureBucket, TestMetricObservation

### Community 71 - "CorpusIngestor"
Cohesion: 0.18
Nodes (4): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.09
Nodes (22): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+14 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_auto_validate_index.py"
Cohesion: 0.10
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "RahaDetector"
Cohesion: 0.35
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 83 - "_config"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "algorithms/index.md"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "CorpusNotFoundError"
Cohesion: 0.22
Nodes (7): Operational notes, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, CorpusNotFoundError

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 94 - "spark_session.py"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.15
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "_segment_dp"
Cohesion: 0.12
Nodes (14): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Recent Changes, Test Results, Code Review State, Completed Actions, Current PR State (+6 more)

### Community 103 - "OpenDetectError"
Cohesion: 0.12
Nodes (15): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Errors, IndexNotBuiltError, OpenDetectError (+7 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_spec"
Cohesion: 0.07
Nodes (13): compute(), _score_pair(), compute(), _score_column(), _build_row(), _original_row_ids(), _score_column(), compute() (+5 more)

### Community 110 - "logging_utils.py"
Cohesion: 0.05
Nodes (18): list_tables_matching(), main(), parse_args(), _run(), get_spark(), configure_logging(), get_logger(), log_duration() (+10 more)

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.19
Nodes (5): open-detect, What is in the box, Registry, Registry and results, Result types

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "test_console_scripts.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 122 - "score"
Cohesion: 0.11
Nodes (17): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat (+9 more)

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "ScoringJobCounter"
Cohesion: 0.07
Nodes (12): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, TestDetectCacheLifecycleSpark, _FakeContext, _FakeTracker, _spark() (+4 more)

### Community 339 - "featurization.py"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 433 - "ErrorType"
Cohesion: 0.06
Nodes (24): ColumnDataType, ComparisonDirection, ErrorType, CorpusColumnRecord, CorpusPairRecord, Detection, BaseDetector, FunctionalDependencyDetector (+16 more)

### Community 458 - "detectors/base.py"
Cohesion: 0.15
Nodes (6): _hash_value(), make_evidence_json(), redact_evidence(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestRedactEvidence

### Community 527 - "_search_mpd"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "hierarchy.py"
Cohesion: 0.07
Nodes (20): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+12 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.24
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), FDResult, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "json"
Cohesion: 0.08
Nodes (16): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main() (+8 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.08
Nodes (16): main(), ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, RahaDetector, _features() (+8 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.14
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 1219 - "builder.py"
Cohesion: 0.06
Nodes (10): _require_min_rows(), InsufficientDataError, FailureTracker, require_min_size(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome (+2 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.29
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 1430 - "conftest.py"
Cohesion: 0.15
Nodes (8): A fully local example, How it works, Install, Uni-Detect, _delta_jars(), _download(), spark(), uc_location()

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1068 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **35 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `get_algorithm`, `json`, `AutoValidateAlgorithm`, `_segment_dp`, `OpenDetectError`, `test_auto_validate_index.py`, `auto_validate/detector.py`, `InferredPattern`, `fmdv_v`, `PatternIndex`, `ConfigurationError`, `fmdv.py`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `pandas` be split into smaller, more focused modules?**
  _Cohesion score 0.055905220288781934 - nodes in this community are weakly interconnected._
- **Why does `UniDetect` connect `_config` to `__getattr__`, `ErrorDetectionAlgorithm`, `CorpusStatsBuilder`, `_check_expected_type`, `_check_dataframe_is_spark`, `UniDetectConfig`, `get_algorithm`, `main`, `pipeline.py`, `ScoringJobCounter`, `test_build_corpus_statistics.py`, `Benchmark: WIKI subset`, `ErrorType`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `json`, `CorpusIngestor`, `logging_utils.py`, `test_console_scripts.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 64 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 64 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._