# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-22)

## Corpus Check
- 191 files · ~155,974 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 2930 nodes · 6433 edges · 149 communities (124 shown, 25 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 810 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `eaea4ba6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AlgorithmResult
- builder.py
- detectors/spelling.py
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- uni_detect/config.py
- _segment_dp
- json
- FailureCounts
- README.md — Uni-Detect overview
- build_column_features
- new_cluster
- CellResult
- AutoValidateConfig
- check_drift
- RahaConfig
- pandas
- ErrorDetectionAlgorithm
- warnings
- permissions
- with
- update-graph
- check_failure_threshold
- with
- _segment_dp
- perturbation.py
- ConfigurationError
- ValidationError
- AlgorithmResult
- .detect
- open_detect/__init__.py
- _score_single_column
- main
- pytest
- TestUniDetectDetect
- build_all_features
- _check_unknown_kwargs
- _check_expected_type
- algorithms/index.md
- real_world_gov benchmark results
- _FakeDetector
- _make_tooltip
- ErrorType
- `auto_validate`
- auto_validate/detector.py
- FailureCountsAccumulatorParam
- fresh_registry
- CHANGELOG
- builder.py
- propagate_labels
- require_min_size
- ErrorType
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
- TestUniDetectDetect
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
- .send
- dataset_utils.py
- Uni-Detect
- _reject_unknown_kwargs
- Current Status: BLOCKED
- _reference_build_pattern_index
- test_pipeline.py
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- test
- OPE-89: Fix Spark Cache Lifecycle in Uni-Detect
- release.yml
- release
- fd_violation_strategies
- HeuristicLabeler
- pypi
- Current Status: BLOCKED
- infer_column_data_type
- perturb_spelling
- with
- on
- `raha`
- steps
- .test_release_calls_detector_release
- CallableLabeler
- duplicate_value_indices
- builder.py
- InsufficientDataError
- sonarqube
- open-detect
- infer_column_data_type
- docs
- force
- get_spec
- test_logging_utils.py
- algorithms/uni-detect.md
- sys
- open-detect
- argparse
- test_console_scripts.py
- _require_columns
- `uni_detect`
- `raha`
- duplicate_value_indices
- paperclip-issue-update.sh
- _detector
- _random_words
- SparkJobCounter
- log_transform_fits_better
- scoped_conf
- pipeline.py
- detectors/base.py
- metrics/spelling.py
- auto_validate/detector.py
- test_bench_snapshot.py
- finite_floats
- outliers.py
- min_pairwise_edit_distance
- main
- snapshot.py
- Labeler
- real_world_gov/run_benchmark.py
- Auto-Validate
- RahaConfig
- wiki_subset/generate_report.py
- uniqueness_ratio
- Performance Baseline — OPE-87
- profile.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 95 edges
3. `UniDetectConfig` - 92 edges
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

## Communities (149 total, 25 thin omitted)

### Community 0 - "AlgorithmResult"
Cohesion: 0.05
Nodes (21): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), CorpusStatsBuilder, _stats_schema_without_error_type(), _config() (+13 more)

### Community 1 - "builder.py"
Cohesion: 0.10
Nodes (9): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config() (+1 more)

### Community 2 - "detectors/spelling.py"
Cohesion: 0.10
Nodes (21): _infer_pattern_to_groups(), _is_null(), _city_column(), _count_detect_calls(), _counting_value_matches_groups(), counting(), _detect(), _detector() (+13 more)

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

### Community 9 - "json"
Cohesion: 0.16
Nodes (10): _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_auto_validate(), run_raha() (+2 more)

### Community 10 - "FailureCounts"
Cohesion: 0.19
Nodes (6): compute(), _score_fd_pair(), compute(), FailureCounts, compute(), TestPerElementFunctions

### Community 11 - "README.md — Uni-Detect overview"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "build_column_features"
Cohesion: 0.08
Nodes (11): _default_classifier_factory(), build_all_features(), build_column_features(), _compact_dtype(), histogram_outlier_strategies(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary() (+3 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.06
Nodes (24): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs (+16 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "RahaConfig"
Cohesion: 0.06
Nodes (20): _build_row(), _drop_nulls(), _original_row_ids(), perturb_numeric_outlier(), perturb_spelling(), _positions_of(), _row(), _score() (+12 more)

### Community 18 - "pandas"
Cohesion: 0.10
Nodes (14): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+6 more)

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.12
Nodes (10): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), register_algorithm(), decorator(), UniDetectAlgorithm, _config() (+2 more)

### Community 20 - "warnings"
Cohesion: 0.07
Nodes (14): Variants, Recent Changes, min_conforming(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_v(), fmdv_vh() (+6 more)

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
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "perturbation.py"
Cohesion: 0.17
Nodes (6): _score_pair(), _score_column(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome

### Community 29 - "ValidationError"
Cohesion: 0.08
Nodes (13): Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _ensure_sequence_of_str(), _reject_unknown_kwargs(), _validate_literal_value() (+5 more)

### Community 30 - "AlgorithmResult"
Cohesion: 0.18
Nodes (4): UniDetectConfig, _run(), TestUniDetectConfig, config()

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "open_detect/__init__.py"
Cohesion: 0.20
Nodes (3): __getattr__(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 33 - "_score_single_column"
Cohesion: 0.10
Nodes (9): _factorize_column(), gaussian_outlier_strategies(), _is_float_like(), pattern_character_strategies(), TestEmptyFrames, TestGaussianOutlierStrategies, TestNullSentinel, TestPatternCharacterStrategies (+1 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.09
Nodes (11): __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "TestUniDetectDetect"
Cohesion: 0.10
Nodes (16): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+8 more)

### Community 37 - "build_all_features"
Cohesion: 0.08
Nodes (11): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm (+3 more)

### Community 38 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 39 - "_check_expected_type"
Cohesion: 0.10
Nodes (7): get_spark(), _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release(), TestGetSparkExtended, TestGetSpark

### Community 40 - "algorithms/index.md"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "_make_tooltip"
Cohesion: 0.25
Nodes (7): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, DataQualityError

### Community 45 - "`auto_validate`"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (26): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+18 more)

### Community 48 - "fresh_registry"
Cohesion: 0.06
Nodes (26): Check it works, Installation, Installing from source, Pick your extra, _constant_factory(), get_algorithm(), get_algorithm_class(), list_algorithms() (+18 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "builder.py"
Cohesion: 0.20
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 51 - "propagate_labels"
Cohesion: 0.14
Nodes (7): _build_index(), _date_index(), _date_values(), TestFmdvV, TestFmdvVh, TestLargeGroups, _time_corpus()

### Community 53 - "ErrorType"
Cohesion: 0.10
Nodes (7): ColumnDataType, ComparisonDirection, ErrorType, all_specs(), ErrorTypeSpec, _FakeDetector, TestAllSpecs

### Community 54 - "UniDetectConfig"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 55 - "index.py"
Cohesion: 0.11
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "algorithms/index.md"
Cohesion: 0.23
Nodes (4): ColumnFeatures, HeuristicLabeler, _resolve_position(), TestHeuristicLabeler

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.17
Nodes (8): build_spark(), main(), Completed Work, __getattr__(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "argparse"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "TestUniDetectDetect"
Cohesion: 0.24
Nodes (3): _mock_detector_result(), _mock_spark_context(), TestUniDetectDetect

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "docs/index.md"
Cohesion: 0.28
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "CorpusStatsStore"
Cohesion: 0.16
Nodes (4): CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 70 - "FeatureBucket"
Cohesion: 0.10
Nodes (11): Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, TestCandidate, TestCorpusRecords (+3 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.10
Nodes (7): CorpusIngestor, select_fd_column_pairs(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment, TestSelectFdColumnPairs, by_name()

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.09
Nodes (21): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+13 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - ".send"
Cohesion: 0.20
Nodes (4): matches(), fpr_column(), impurity(), TestMatching

### Community 77 - "dataset_utils.py"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "Uni-Detect"
Cohesion: 0.27
Nodes (4): GroundTruthLabeler, _values_equal(), normalize_to_str(), TestGroundTruthLabeler

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_reference_build_pattern_index"
Cohesion: 0.10
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 83 - "test_pipeline.py"
Cohesion: 0.16
Nodes (6): _config(), _mock_spark(), TestUniDetectBuildCorpusStatistics, TestUniDetectInit, TestUniDetectValidateInputs, TestUniDetectWriteDetections

### Community 84 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.22
Nodes (6): Algorithms, Fidelity to the papers, Configuration, Detector, Labelers, Raha

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

### Community 89 - "fd_violation_strategies"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - "HeuristicLabeler"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 94 - "perturb_spelling"
Cohesion: 0.13
Nodes (9): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution (+1 more)

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "`raha`"
Cohesion: 0.17
Nodes (11): fd_violation_strategies(), _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column() (+3 more)

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 100 - "CallableLabeler"
Cohesion: 0.15
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "duplicate_value_indices"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "builder.py"
Cohesion: 0.09
Nodes (5): _require_min_rows(), __getattr__(), TestScoreFdPair, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 103 - "InsufficientDataError"
Cohesion: 0.12
Nodes (16): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Errors, InsufficientDataError, IndexNotBuiltError (+8 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "infer_column_data_type"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 110 - "test_logging_utils.py"
Cohesion: 0.08
Nodes (8): parse_args(), configure_logging(), get_logger(), log_duration(), TestParseArgs, TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.25
Nodes (3): Registry, Registry and results, Result types

### Community 116 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 117 - "_require_columns"
Cohesion: 0.21
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "_random_words"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "SparkJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "log_transform_fits_better"
Cohesion: 0.09
Nodes (13): _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket() (+5 more)

### Community 433 - "pipeline.py"
Cohesion: 0.08
Nodes (6): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 458 - "detectors/base.py"
Cohesion: 0.22
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), compute(), TestRedactEvidence

### Community 527 - "metrics/spelling.py"
Cohesion: 0.24
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "auto_validate/detector.py"
Cohesion: 0.05
Nodes (25): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+17 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 686 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 711 - "main"
Cohesion: 0.36
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 783 - "snapshot.py"
Cohesion: 0.15
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "Labeler"
Cohesion: 0.11
Nodes (14): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+6 more)

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.09
Nodes (13): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), main(), _print_comparison(), _register_table() (+5 more)

### Community 1123 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1156 - "RahaConfig"
Cohesion: 0.09
Nodes (16): API reference, main(), ColumnPredictions, _make_classifier(), train_and_predict(), RahaConfig, RahaDetector, _features() (+8 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.10
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1430 - "profile.py"
Cohesion: 0.14
Nodes (7): candidates(), main(), select(), _delta_jars(), _download(), spark(), uc_location()

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1064 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Benchmark: real_world_gov` connect `TestUniDetectDetect` to `_segment_dp`, `UniDetectConfig`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `AlgorithmResult` be split into smaller, more focused modules?**
  _Cohesion score 0.05369369369369369 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `AlgorithmResult`, `builder.py`, `RahaConfig`, `json`, `FailureCounts`, `ErrorDetectionAlgorithm`, `AlgorithmResult`, `open_detect/__init__.py`, `main`, `_check_expected_type`, `_make_tooltip`, `pipeline.py`, `UniDetect`, `TestUniDetectDetect`, `real_world_gov/run_benchmark.py`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `main`, `log_transform_fits_better`, `test_pipeline.py`, `.test_release_calls_detector_release`, `builder.py`, `get_spec`, `test_logging_utils.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 63 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._