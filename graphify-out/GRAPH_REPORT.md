# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-15)

## Corpus Check
- 191 files · ~156,778 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)

## Summary
- 2936 nodes · 6466 edges · 162 communities (125 shown, 37 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 794 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ffdbe705`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- json
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
- build_column_features
- fmdv_v
- CellResult
- tests/algorithms/auto_validate/test_auto_validate_index.py
- check_drift
- test_spelling_detector.py
- _check_unknown_kwargs
- ErrorDetectionAlgorithm
- auto_validate/detector.py
- src/open_detect/algorithms/auto_validate/patterns.py
- wiki_subset/generate_report.py
- src/open_detect/algorithms/uni_detect/detectors/spelling.py
- ValidationError
- tests/algorithms/uni_detect/test_hygiene.py
- CorpusStatsBuilder
- _segment_dp
- _check_expected_type
- ValidationError
- UniDetectConfig
- .detect
- list_algorithms
- numpy
- main
- pytest
- run_raha
- AutoValidateAlgorithm
- score
- test_hygiene.py
- infer_column_data_type
- real_world_gov benchmark results
- propagate_labels
- test_build_corpus_statistics.py
- log_transform_fits_better
- Benchmark: WIKI subset
- _value_matches
- FailureCountsAccumulatorParam
- list_algorithms
- CHANGELOG
- API reference
- fmdv_v
- UniDetect
- OPE-89: Fix Spark Cache Lifecycle in Uni-Detect
- dataset_utils.py
- fmdv
- argparse
- raha/detector.py
- logging
- .build_corpus_statistics
- itertools
- _coerce_numeric
- ope89-wt/benchmarks/real_world_gov/run_benchmark.py
- functools
- real_world_gov/run_benchmark.py
- src/open_detect/algorithms/uni_detect/featurization.py
- perturb_spelling
- CorpusStatsStore
- typing
- _score_single_column
- FeatureBucket
- CorpusIngestor
- src/open_detect/algorithms/uni_detect/detectors/base.py
- .test_release_calls_detector_release
- PRD: API Validation Framework for open-detect
- ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py
- matches
- Commit conventions and releases
- GroundTruthLabeler
- SparkUnavailableContext
- json
- clean_column
- _config
- Raha
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- Appendix: Validation Function Reference
- ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- Writing your own algorithm
- FailureCountsAccumulatorParam
- is_float_like
- json
- src/open_detect/algorithms/uni_detect/config.py
- tokenize
- spark_session.py
- ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py
- ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- fd_violation_strategies
- tests/algorithms/uni_detect/test_metrics.py
- argparse
- .label_tuple
- OPE-133 Review Summary
- .test_release_calls_detector_release
- open_detect/exceptions.py
- src/open_detect/algorithms/auto_validate/drift.py
- TestAttempt
- is_mixed_alphanumeric
- csv
- ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- get_spec
- pipeline.py
- algorithms/uni-detect.md
- Detection
- sys
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/numeric_outlier.py
- TestConfigThreshold
- builder.py
- _require_columns
- `uni_detect`
- `raha`
- FakeConf
- .index
- 1. Implement `ErrorDetectionAlgorithm`
- paperclip-issue-update.sh
- is_integer_like
- OPE-86 / PR #96 — Copilot Review Fixes
- finite_floats
- corpus_tables_by_category
- config
- _infer_pattern_to_groups
- _detector
- tests/algorithms/uni_detect/test_metrics.py
- SparkJobCounter
- bucket_by_edges
- get_spark
- _FakeDetector
- ErrorType
- redact_evidence
- metrics/spelling.py
- hierarchy.py
- ope74-wt/tests/algorithms/raha/test_raha_labeling.py
- _make_tooltip
- perturb_numeric_outlier
- _ensure_sequence_of_str
- outliers.py
- ope85-clean/src/open_detect/algorithms/raha/features.py
- snapshot.py
- KnownIndexLabeler
- json
- Auto-Validate
- _ensure_dataframe_is_spark
- RahaConfig
- wiki_subset/generate_report.py
- perturbation.py
- _raise
- json
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

## Communities (162 total, 37 thin omitted)

### Community 0 - "json"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.11
Nodes (7): UnityCatalogLocation, TestDetectCacheLifecycleSpark, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 2 - "pandas"
Cohesion: 0.12
Nodes (18): _is_null(), _city_column(), _count_detect_calls(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference(), test_empty_dataframe() (+10 more)

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
Cohesion: 0.19
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

### Community 12 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 13 - "fmdv_v"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.10
Nodes (7): Reading the detections, Through the registry, Usage on Databricks, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "tests/algorithms/auto_validate/test_auto_validate_index.py"
Cohesion: 0.10
Nodes (8): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "_check_unknown_kwargs"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.13
Nodes (13): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm_class(), _load_entry_points(), register_algorithm() (+5 more)

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (9): min_conforming(), _fmdv_h_single(), _segment_fmdv_vh(), PatternIndex, pattern_to_language(), _date_index(), _date_values(), TestLargeGroups (+1 more)

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

### Community 26 - "CorpusStatsBuilder"
Cohesion: 0.13
Nodes (8): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), _StubDetector, TestCorpusBuilderFailureGate, TestDetectorFailureGate

### Community 27 - "_segment_dp"
Cohesion: 0.19
Nodes (5): _fmdv_single_segment(), _segment_dp(), _segment_fmdv_v(), TestSegmentDp, solve()

### Community 29 - "ValidationError"
Cohesion: 0.09
Nodes (13): Appendix: Validation Function Reference, _check_columns_present(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_unknown_kwargs(), _reject_unknown_kwargs(), _validate_literal_value() (+5 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "list_algorithms"
Cohesion: 0.12
Nodes (8): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args(), TestPluginDiscoveryViaRealDistInfo

### Community 33 - "numpy"
Cohesion: 0.08
Nodes (19): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), _assert_same(), _naive_fd() (+11 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.08
Nodes (11): __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "run_raha"
Cohesion: 0.15
Nodes (13): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types (+5 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "score"
Cohesion: 0.11
Nodes (19): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Concepts (+11 more)

### Community 39 - "test_hygiene.py"
Cohesion: 0.13
Nodes (3): _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSparkExtended

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "_value_matches"
Cohesion: 0.08
Nodes (20): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+12 more)

### Community 48 - "list_algorithms"
Cohesion: 0.12
Nodes (10): list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered(), TestPluginDiscovery (+2 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "API reference"
Cohesion: 0.12
Nodes (13): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, API reference, Configuration (+5 more)

### Community 51 - "fmdv_v"
Cohesion: 0.10
Nodes (10): Variants, Recent Changes, _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV (+2 more)

### Community 52 - "UniDetect"
Cohesion: 0.24
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "OPE-89: Fix Spark Cache Lifecycle in Uni-Detect"
Cohesion: 0.25
Nodes (7): Blockers, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 54 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 55 - "fmdv"
Cohesion: 0.09
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "raha/detector.py"
Cohesion: 0.14
Nodes (12): Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, ColumnFeatures (+4 more)

### Community 58 - "logging"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.15
Nodes (9): build_spark(), main(), Completed Work, _filter_by_column_type(), UniDetect, __getattr__(), TestCorpusBuilderAndDetectors, _write_table() (+1 more)

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
Cohesion: 0.11
Nodes (12): confusion_metrics(), _build_config(), _print_comparison(), _register_table(), run(), run_auto_validate(), run_raha(), run_uni_detect() (+4 more)

### Community 65 - "src/open_detect/algorithms/uni_detect/featurization.py"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 67 - "CorpusStatsStore"
Cohesion: 0.12
Nodes (5): CorpusStatsStore, CorpusNotFoundError, DataQualityError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "typing"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 70 - "FeatureBucket"
Cohesion: 0.08
Nodes (13): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation (+5 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.18
Nodes (4): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 72 - "src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.07
Nodes (26): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+18 more)

### Community 75 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "matches"
Cohesion: 0.10
Nodes (9): matches(), indexable_values(), fpr_column(), impurity(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestEquivalenceToReferenceBuild, TestIndexableValues (+1 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "GroundTruthLabeler"
Cohesion: 0.21
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 81 - "json"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "_config"
Cohesion: 0.11
Nodes (9): _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit, TestUniDetectValidateInputs (+1 more)

### Community 84 - "Raha"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

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

### Community 91 - "json"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "src/open_detect/algorithms/uni_detect/config.py"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 94 - "spark_session.py"
Cohesion: 0.22
Nodes (4): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable

### Community 95 - "ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 98 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - ".label_tuple"
Cohesion: 0.19
Nodes (4): CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.06
Nodes (20): Errors, Errors, _validate_edges(), _require_min_rows(), InsufficientDataError, main(), parse_args(), ConfigurationError (+12 more)

### Community 104 - "src/open_detect/algorithms/auto_validate/drift.py"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

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
Cohesion: 0.05
Nodes (18): ensure_schema_exists(), list_tables(), list_tables_matching(), table_exists(), UnityCatalogError, _run(), get_spark(), configure_logging() (+10 more)

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.08
Nodes (16): Algorithms, Fidelity to the papers, Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance (+8 more)

### Community 112 - "Detection"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "builder.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 121 - ".index"
Cohesion: 0.33
Nodes (4): Inspecting a pattern, Reading the output, Usage, segment()

### Community 122 - "1. Implement `ErrorDetectionAlgorithm`"
Cohesion: 0.33
Nodes (6): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm

### Community 128 - "OPE-86 / PR #96 — Copilot Review Fixes"
Cohesion: 0.40
Nodes (4): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "SparkJobCounter"
Cohesion: 0.09
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 433 - "ErrorType"
Cohesion: 0.07
Nodes (19): ErrorType, BaseDetector, FunctionalDependencyDetector, _score_pair(), NumericOutlierDetector, _score_column(), _score_column(), SpellingDetector (+11 more)

### Community 458 - "redact_evidence"
Cohesion: 0.22
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), compute(), TestRedactEvidence

### Community 527 - "metrics/spelling.py"
Cohesion: 0.14
Nodes (9): drop_nulls(), require_min_size(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance() (+1 more)

### Community 530 - "hierarchy.py"
Cohesion: 0.05
Nodes (25): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+17 more)

### Community 537 - "ope74-wt/tests/algorithms/raha/test_raha_labeling.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 635 - "_make_tooltip"
Cohesion: 0.15
Nodes (7): _build_suggestion(), _feasible_evidence(), _infeasible_evidence(), _make_tooltip(), _non_null_cells(), _tooltip_content(), TooltipContent

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.19
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.16
Nodes (7): mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 699 - "ope85-clean/src/open_detect/algorithms/raha/features.py"
Cohesion: 0.16
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 835 - "json"
Cohesion: 0.08
Nodes (14): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, git_commit(), main(), _build_config(), _load_corpus_tables() (+6 more)

### Community 1123 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1156 - "RahaConfig"
Cohesion: 0.08
Nodes (16): main(), ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, RahaDetector, _features() (+8 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.14
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 1219 - "perturbation.py"
Cohesion: 0.11
Nodes (10): duplicate_value_indices(), uniqueness_ratio(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestUniquenessRatio (+2 more)

### Community 1252 - "_raise"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "json"
Cohesion: 0.32
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 1430 - "conftest.py"
Cohesion: 0.13
Nodes (10): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, _delta_jars(), _download() (+2 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1067 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **37 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `tests/algorithms/auto_validate/test_auto_validate_index.py` to `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `score`, `open_detect/exceptions.py`, `_segment_dp`, `matches`, `check_drift`, `API reference`, `fmdv_v`, `auto_validate/detector.py`, `fmdv`, `_make_tooltip`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `json` be split into smaller, more focused modules?**
  _Cohesion score 0.11033681765389082 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `json`, `UnityCatalogLocation`, `FailureCounts`, `conftest.py`, `CorpusStatsBuilder`, `main`, `test_hygiene.py`, `_FakeDetector`, `test_build_corpus_statistics.py`, `API reference`, `UniDetect`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `json`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `.test_release_calls_detector_release`, `_config`, `.test_release_calls_detector_release`, `open_detect/exceptions.py`, `get_spec`, `pipeline.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 64 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 64 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._