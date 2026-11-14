# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-14)

## Corpus Check
- 191 files · ~155,929 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 2930 nodes · 6439 edges · 156 communities (131 shown, 25 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 789 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `54ffc29e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- tests/algorithms/uni_detect/test_corpus_build_metadata.py
- UnityCatalogLocation
- pandas
- sys
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- TestFunctionalDependency
- README.md — Uni-Detect overview
- Scoring auto_validate
- FailureCounts
- PRD: User Feedback Tooltips
- RahaConfig
- fmdv_v
- CellResult
- tests/algorithms/auto_validate/test_auto_validate_index.py
- check_drift
- test_spelling_detector.py
- _check_unknown_kwargs
- ErrorDetectionAlgorithm
- PatternIndex
- src/open_detect/algorithms/auto_validate/patterns.py
- wiki_subset/generate_report.py
- src/open_detect/algorithms/uni_detect/detectors/spelling.py
- ValidationError
- tests/algorithms/uni_detect/test_hygiene.py
- list_tables_matching
- test_perturbation.py
- _check_expected_type
- ValidationError
- UniDetectConfig
- .detect
- list_algorithms
- gaussian_outlier_strategies
- main
- pytest
- run_raha
- AutoValidateAlgorithm
- score
- test_hygiene.py
- Contributing
- real_world_gov benchmark results
- propagate_labels
- clean_column
- log_transform_fits_better
- Benchmark: WIKI subset
- _value_matches
- FailureCountsAccumulatorParam
- list_algorithms
- CHANGELOG
- Auto-Validate
- test_auto_validate_fmdv_v.py
- UniDetectAlgorithm
- uni_detect/core/enums.py
- dataset_utils.py
- fmdv
- argparse
- labeling.py
- logging
- .build_corpus_statistics
- itertools
- _coerce_numeric
- ope89-wt/benchmarks/real_world_gov/run_benchmark.py
- functools
- real_world_gov/run_benchmark.py
- src/open_detect/algorithms/uni_detect/featurization.py
- concepts.md
- CorpusStatsStore
- typing
- _score_single_column
- FeatureBucket
- KnownIndexLabeler
- src/open_detect/algorithms/uni_detect/detectors/base.py
- Detection
- PRD: API Validation Framework for open-detect
- ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py
- matches
- Commit conventions and releases
- GroundTruthLabeler
- SparkUnavailableContext
- json
- test_auto_validate_index.py
- UniDetect
- algorithms/index.md
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- test_corpus_ingestion.py
- ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- Writing your own algorithm
- FailureCountsAccumulatorParam
- Raha
- json
- src/open_detect/algorithms/uni_detect/config.py
- infer_column_data_type
- spark_session.py
- ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py
- ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- numpy
- tests/algorithms/uni_detect/test_metrics.py
- argparse
- CallableLabeler
- OPE-133 Review Summary
- test_corpus_builder_helpers.py
- open_detect/exceptions.py
- src/open_detect/algorithms/auto_validate/drift.py
- TestAttempt
- Benchmarks
- csv
- ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- get_spec
- pipeline.py
- algorithms/uni-detect.md
- tests/algorithms/uni_detect/test_corpus_ingestion.py
- sys
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/numeric_outlier.py
- TestConfigThreshold
- builder.py
- ConfigurationError
- `uni_detect`
- `raha`
- parse_args
- duplicate_value_indices
- paperclip-issue-update.sh
- _detector
- tests/algorithms/uni_detect/test_metrics.py
- SparkJobCounter
- builder.py
- get_spark
- _FakeDetector
- ErrorType
- redact_evidence
- InsufficientDataError
- hierarchy.py
- ope74-wt/tests/algorithms/raha/test_raha_labeling.py
- auto_validate/detector.py
- perturb_numeric_outlier
- _ensure_sequence_of_str
- outliers.py
- ope85-clean/src/open_detect/algorithms/raha/features.py
- main
- snapshot.py
- KnownIndexLabeler
- json
- .infer_pattern
- _ensure_dataframe_is_spark
- RahaConfig
- wiki_subset/generate_report.py
- drop_nulls
- _raise
- json
- conftest.py
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

## Communities (156 total, 25 thin omitted)

### Community 0 - "tests/algorithms/uni_detect/test_corpus_build_metadata.py"
Cohesion: 0.05
Nodes (21): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), CorpusStatsBuilder, _stats_schema_without_error_type(), _config() (+13 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.10
Nodes (9): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config() (+1 more)

### Community 2 - "pandas"
Cohesion: 0.11
Nodes (19): _city_column(), _count_detect_calls(), _counting_value_matches_groups(), counting(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference() (+11 more)

### Community 3 - "sys"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "TestFunctionalDependency"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 10 - "FailureCounts"
Cohesion: 0.19
Nodes (6): compute(), _score_fd_pair(), compute(), FailureCounts, compute(), TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "RahaConfig"
Cohesion: 0.08
Nodes (11): _default_classifier_factory(), build_all_features(), build_column_features(), _compact_dtype(), histogram_outlier_strategies(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary() (+3 more)

### Community 13 - "fmdv_v"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.10
Nodes (7): open-detect, What is in the box, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "tests/algorithms/auto_validate/test_auto_validate_index.py"
Cohesion: 0.07
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.10
Nodes (15): _build_row(), _drop_nulls(), _original_row_ids(), perturb_spelling(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions() (+7 more)

### Community 18 - "_check_unknown_kwargs"
Cohesion: 0.09
Nodes (19): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling (+11 more)

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.15
Nodes (10): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+2 more)

### Community 20 - "PatternIndex"
Cohesion: 0.07
Nodes (14): Variants, Recent Changes, min_conforming(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_v(), fmdv_vh() (+6 more)

### Community 21 - "src/open_detect/algorithms/auto_validate/patterns.py"
Cohesion: 0.07
Nodes (28): if, permissions, runs-on, steps, types, types, jobs, claude (+20 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.09
Nodes (26): UV_PYTHON, jobs, real-world-gov, wiki-subset, name, on, workflow_dispatch, env (+18 more)

### Community 23 - "src/open_detect/algorithms/uni_detect/detectors/spelling.py"
Cohesion: 0.08
Nodes (24): concurrency, cancel-in-progress, group, jobs, update-graph, name, on, push (+16 more)

### Community 25 - "tests/algorithms/uni_detect/test_hygiene.py"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 28 - "_check_expected_type"
Cohesion: 0.14
Nodes (10): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status (+2 more)

### Community 29 - "ValidationError"
Cohesion: 0.08
Nodes (18): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification, 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP) (+10 more)

### Community 30 - "UniDetectConfig"
Cohesion: 0.22
Nodes (3): UniDetectConfig, _run(), TestUniDetectConfig

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "list_algorithms"
Cohesion: 0.09
Nodes (16): Check it works, Installation, Installing from source, Pick your extra, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+8 more)

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.10
Nodes (9): _factorize_column(), gaussian_outlier_strategies(), _is_float_like(), pattern_character_strategies(), TestEmptyFrames, TestGaussianOutlierStrategies, TestNullSentinel, TestPatternCharacterStrategies (+1 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.07
Nodes (11): __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "run_raha"
Cohesion: 0.10
Nodes (16): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+8 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "score"
Cohesion: 0.18
Nodes (11): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs (+3 more)

### Community 39 - "test_hygiene.py"
Cohesion: 0.11
Nodes (6): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 40 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "clean_column"
Cohesion: 0.25
Nodes (7): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, DataQualityError

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "_value_matches"
Cohesion: 0.13
Nodes (14): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+6 more)

### Community 48 - "list_algorithms"
Cohesion: 0.11
Nodes (11): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_register_lazy_is_lazy(), test_unknown_algorithm_raises() (+3 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.20
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 51 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.14
Nodes (7): _build_index(), _date_index(), _date_values(), TestFmdvV, TestFmdvVh, TestLargeGroups, _time_corpus()

### Community 52 - "UniDetectAlgorithm"
Cohesion: 0.24
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "uni_detect/core/enums.py"
Cohesion: 0.09
Nodes (5): ColumnDataType, ComparisonDirection, CorpusColumnRecord, CorpusPairRecord, TestCorpusRecords

### Community 54 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 55 - "fmdv"
Cohesion: 0.11
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "labeling.py"
Cohesion: 0.23
Nodes (4): ColumnFeatures, HeuristicLabeler, _resolve_position(), TestHeuristicLabeler

### Community 58 - "logging"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.14
Nodes (6): build_spark(), main(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "itertools"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 62 - "ope89-wt/benchmarks/real_world_gov/run_benchmark.py"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, type-check, env (+4 more)

### Community 63 - "functools"
Cohesion: 0.23
Nodes (12): steps, steps, lint, runs-on, steps, timeout-minutes, steps, name (+4 more)

### Community 64 - "real_world_gov/run_benchmark.py"
Cohesion: 0.20
Nodes (9): git_commit(), _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate(), run_raha() (+1 more)

### Community 65 - "src/open_detect/algorithms/uni_detect/featurization.py"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "concepts.md"
Cohesion: 0.28
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "CorpusStatsStore"
Cohesion: 0.14
Nodes (4): CorpusStatsStore, config(), TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "typing"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 70 - "FeatureBucket"
Cohesion: 0.12
Nodes (8): Candidate, Detection, FeatureBucket, MetricObservation, TestCandidate, TestDetection, TestFeatureBucket, TestMetricObservation

### Community 71 - "KnownIndexLabeler"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Detection"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 75 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "matches"
Cohesion: 0.20
Nodes (4): matches(), fpr_column(), impurity(), TestMatching

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "GroundTruthLabeler"
Cohesion: 0.27
Nodes (4): GroundTruthLabeler, _values_equal(), normalize_to_str(), TestGroundTruthLabeler

### Community 81 - "json"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "test_auto_validate_index.py"
Cohesion: 0.10
Nodes (9): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild (+1 more)

### Community 83 - "UniDetect"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "algorithms/index.md"
Cohesion: 0.22
Nodes (6): Algorithms, Fidelity to the papers, Configuration, Detector, Labelers, Raha

### Community 85 - "ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 87 - "ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "Writing your own algorithm"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "FailureCountsAccumulatorParam"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 91 - "json"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "src/open_detect/algorithms/uni_detect/config.py"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 94 - "spark_session.py"
Cohesion: 0.23
Nodes (4): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable

### Community 95 - "ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "numpy"
Cohesion: 0.17
Nodes (11): fd_violation_strategies(), _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column() (+3 more)

### Community 98 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.15
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.10
Nodes (18): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Errors, CorpusNotFoundError, InsufficientDataError (+10 more)

### Community 104 - "src/open_detect/algorithms/auto_validate/drift.py"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 107 - "csv"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_spec"
Cohesion: 0.12
Nodes (5): all_specs(), ErrorTypeSpec, get_spec(), TestAllSpecs, TestGetSpec

### Community 110 - "pipeline.py"
Cohesion: 0.07
Nodes (9): get_spark(), configure_logging(), get_logger(), log_duration(), TestGetSparkExtended, TestGetSpark, TestConfigureLogging, TestGetLogger (+1 more)

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.25
Nodes (3): Registry, Registry and results, Result types

### Community 112 - "tests/algorithms/uni_detect/test_corpus_ingestion.py"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "builder.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "ConfigurationError"
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

### Community 251 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "SparkJobCounter"
Cohesion: 0.09
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "builder.py"
Cohesion: 0.07
Nodes (20): _require_min_rows(), _score_pair(), _score_column(), _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count() (+12 more)

### Community 433 - "ErrorType"
Cohesion: 0.11
Nodes (7): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 458 - "redact_evidence"
Cohesion: 0.22
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), compute(), TestRedactEvidence

### Community 527 - "InsufficientDataError"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "hierarchy.py"
Cohesion: 0.05
Nodes (25): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+17 more)

### Community 537 - "ope74-wt/tests/algorithms/raha/test_raha_labeling.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 635 - "auto_validate/detector.py"
Cohesion: 0.10
Nodes (14): _build_suggestion(), _distinct_value_verdicts_groups(), _feasible_evidence(), _infeasible_evidence(), _infer_pattern_to_groups(), _is_null(), _make_tooltip(), _matches_segments() (+6 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 699 - "ope85-clean/src/open_detect/algorithms/raha/features.py"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 711 - "main"
Cohesion: 0.36
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.11
Nodes (14): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+6 more)

### Community 835 - "json"
Cohesion: 0.07
Nodes (14): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main() (+6 more)

### Community 1123 - ".infer_pattern"
Cohesion: 0.17
Nodes (10): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+2 more)

### Community 1144 - "_ensure_dataframe_is_spark"
Cohesion: 0.13
Nodes (4): _check_dataframe_is_spark(), _ensure_dataframe_is_spark(), TestCheckDataFrameIsSpark, TestEnsureDataFrameIsSpark

### Community 1156 - "RahaConfig"
Cohesion: 0.09
Nodes (16): API reference, main(), ColumnPredictions, _make_classifier(), train_and_predict(), RahaConfig, RahaDetector, _features() (+8 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.14
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 1219 - "drop_nulls"
Cohesion: 0.16
Nodes (4): drop_nulls(), uniqueness_ratio(), TestDropNulls, TestUniquenessRatio

### Community 1252 - "_raise"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "json"
Cohesion: 0.32
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1064 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Benchmark: real_world_gov` connect `run_raha` to `README.md — Uni-Detect overview`, `dataset_utils.py`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `tests/algorithms/uni_detect/test_corpus_build_metadata.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05369369369369369 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `tests/algorithms/uni_detect/test_corpus_build_metadata.py`, `UnityCatalogLocation`, `RahaConfig`, `FailureCounts`, `UniDetectConfig`, `main`, `test_hygiene.py`, `_FakeDetector`, `clean_column`, `UniDetectAlgorithm`, `uni_detect/core/enums.py`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `json`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `main`, `builder.py`, `UniDetect`, `test_corpus_builder_helpers.py`, `open_detect/exceptions.py`, `get_spec`, `pipeline.py`, `parse_args`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 63 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._