# Graph Report - open-detect  (2026-11-14)

## Corpus Check
- 199 files · ~152,869 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 461 files seen (51%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2871 nodes · 6310 edges · 161 communities (129 shown, 32 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 803 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `54785482`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- test_spelling_detector.py
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- pandas
- auto_validate/detector.py
- test_raha_strategies.py
- FailureCounts
- PRD: API Validation Framework for open-detect
- infer_column_data_type
- new_cluster
- spark_session
- AutoValidateConfig
- InferredPattern
- RahaConfig
- .detect
- ErrorDetectionAlgorithm
- hooks
- permissions
- with
- update-graph
- check_failure_threshold
- with
- test_catalog.py
- perturb_numeric_outlier
- ConfigurationError
- _check_expected_type
- CellResult
- cluster_column
- list_algorithms
- numpy
- main
- test_deprecated_shims.py
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- Comparing algorithms
- 7.2 Key Features
- GroundTruthLabeler
- real_world_gov benchmark results
- TestUniDetectDetect
- Uni-Detect
- featurization.py
- Benchmark: WIKI subset
- _check_unknown_kwargs
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- _ensure_sequence_of_str
- test_auto_validate_fmdv_v.py
- algorithm.py
- ErrorType
- run_raha
- _build_index
- updates
- labeling.py
- jobs
- UniDetect
- README.md — Uni-Detect overview
- _coerce_numeric
- build
- uses
- CorpusStatsBuilder
- env
- docs/index.md
- CorpusStatsStore
- dry_run
- _score_single_column
- FeatureBucket
- CorpusIngestor
- variables
- Auto-Validate
- OPE-133 Review Summary
- dev
- test_package_init.py
- Commit conventions and releases
- TestDetectCacheLifecycleSpark
- UnityCatalogLocation
- Current Status: BLOCKED
- index.py
- test_pipeline.py
- Detection
- test
- _check_dataframe_is_spark
- release.yml
- release
- Running on Databricks
- algorithms/raha.md
- pypi
- Current Status: BLOCKED
- uni_detect/text_utils.py
- TestConfigThreshold
- with
- on
- FakeConf
- steps
- algorithms/index.md
- CallableLabeler
- Uni-Detect
- sys
- pytest
- sonarqube
- _reject_unknown_kwargs
- algorithms/uni-detect.md
- docs
- force
- get_spec
- ValidationError
- reference/index.md
- select_fd_column_pairs
- `uni_detect`
- `raha`
- argparse
- Raha
- _require_columns
- 8. Release
- _value_matches_groups
- paperclip-issue-update.sh
- corpus_tables_by_category
- open-detect
- _detector
- _StubDetector
- SparkJobCounter
- patterns_of
- _score_column
- tokenize
- scoped_conf
- _FakeDetector
- collections_abc
- redact_evidence
- hierarchy.py
- test_bench_snapshot.py
- UnknownAlgorithmError
- _value_matches
- _validate_literal_value
- perturbation.py
- test_metrics.py
- main
- parse_args
- profile.py
- snapshot.py
- KnownIndexLabeler
- real_world_gov/run_benchmark.py
- .index
- Appendix: Validation Function Reference
- dataset_utils.py
- Auto-Validate
- _ensure_dataframe_is_spark
- wiki_subset/generate_report.py
- auto_validate/metrics.py
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- conftest.py
- Summary
- all_specs

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 121 edges
2. `UniDetectConfig` - 91 edges
3. `ErrorType` - 91 edges
4. `UniDetect` - 62 edges
5. `FailureCounts` - 56 edges
6. `ValidationError` - 48 edges
7. `build_pattern_index()` - 46 edges
8. `UnityCatalogLocation` - 44 edges
9. `AutoValidateAlgorithm` - 39 edges
10. `RahaConfig` - 36 edges

## Surprising Connections (you probably didn't know these)
- `Code Review State` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Final Fixes Pushed` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `3.1 Context` --references--> `AlgorithmResult`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `5.2 Secondary Segment` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (161 total, 32 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.13
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.17
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "pandas"
Cohesion: 0.12
Nodes (18): _is_null(), _city_column(), _count_detect_calls(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference(), test_empty_dataframe() (+10 more)

### Community 8 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (17): Variants, Recent Changes, _clean(), fmdv(), fmdv_h(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+9 more)

### Community 9 - "test_raha_strategies.py"
Cohesion: 0.20
Nodes (10): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestPatternCharacterStrategies (+2 more)

### Community 10 - "FailureCounts"
Cohesion: 0.15
Nodes (7): compute(), compute(), _score_fd_pair(), FailureCounts, _raise(), TestAttempt, TestPerElementFunctions

### Community 11 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 12 - "infer_column_data_type"
Cohesion: 0.18
Nodes (4): infer_column_data_type(), is_mixed_alphanumeric(), TestDataTypeInference, TestMixedAlphanumeric

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "spark_session"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 15 - "AutoValidateConfig"
Cohesion: 0.06
Nodes (12): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestFmdvV, TestSegmentDp, solve(), TestCorpusInputShapes (+4 more)

### Community 16 - "InferredPattern"
Cohesion: 0.08
Nodes (12): _infer_pattern_to_groups(), _matches_segments(), check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed() (+4 more)

### Community 17 - "RahaConfig"
Cohesion: 0.08
Nodes (17): main(), ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, RahaDetector, _features() (+9 more)

### Community 18 - ".detect"
Cohesion: 0.12
Nodes (7): build_all_features(), propagate_labels(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestPropagateLabels

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.17
Nodes (9): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+1 more)

### Community 20 - "hooks"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

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

### Community 26 - "test_catalog.py"
Cohesion: 0.15
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.07
Nodes (16): compute(), _score_pair(), _score_column(), _score_column(), compute(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency() (+8 more)

### Community 30 - "CellResult"
Cohesion: 0.09
Nodes (11): Through the registry, Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Why a common interface, AlgorithmResult (+3 more)

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "list_algorithms"
Cohesion: 0.11
Nodes (13): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+5 more)

### Community 33 - "numpy"
Cohesion: 0.07
Nodes (16): build_column_features(), _compact_dtype(), _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str() (+8 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "test_deprecated_shims.py"
Cohesion: 0.09
Nodes (11): __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.15
Nodes (10): git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_auto_validate() (+2 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 39 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 40 - "GroundTruthLabeler"
Cohesion: 0.35
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "TestUniDetectDetect"
Cohesion: 0.20
Nodes (3): _mock_detector_result(), _mock_spark_context(), TestUniDetectDetect

### Community 43 - "Uni-Detect"
Cohesion: 0.29
Nodes (7): A fully local example, Configuration, How it works, Install, Reading the detections, Uni-Detect, Usage on Databricks

### Community 44 - "featurization.py"
Cohesion: 0.09
Nodes (13): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+5 more)

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.11
Nodes (12): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy() (+4 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (26): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+18 more)

### Community 51 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.09
Nodes (9): min_conforming(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvVh, TestLargeGroups, TestMinConforming (+1 more)

### Community 52 - "algorithm.py"
Cohesion: 0.18
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "ErrorType"
Cohesion: 0.11
Nodes (12): ColumnDataType, ComparisonDirection, ErrorType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, ErrorTypeSpec (+4 more)

### Community 54 - "run_raha"
Cohesion: 0.10
Nodes (16): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+8 more)

### Community 55 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "labeling.py"
Cohesion: 0.11
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.23
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.13
Nodes (15): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, artifacts, open_detect_wheel, bundle, name, build (+7 more)

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 67 - "CorpusStatsStore"
Cohesion: 0.13
Nodes (6): Operational notes, Practical advice, CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 74 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.13
Nodes (9): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), score() (+1 more)

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "index.py"
Cohesion: 0.09
Nodes (8): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestIndexableValues

### Community 83 - "test_pipeline.py"
Cohesion: 0.17
Nodes (6): _config(), _mock_spark(), TestUniDetectBuildCorpusStatistics, TestUniDetectInit, TestUniDetectValidateInputs, TestUniDetectWriteDetections

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "Running on Databricks"
Cohesion: 0.40
Nodes (4): Job arguments, Jobs, Notebooks, Running on Databricks

### Community 90 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "uni_detect/text_utils.py"
Cohesion: 0.19
Nodes (4): is_float_like(), is_integer_like(), TestFloatLike, TestIntegerLike

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 100 - "CallableLabeler"
Cohesion: 0.19
Nodes (4): CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 101 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 103 - "pytest"
Cohesion: 0.06
Nodes (13): Errors, IndexNotBuiltError, OpenDetectError, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSparkExtended, TestGetSpark, test_all_errors_derive_from_open_detect_error() (+5 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_spec"
Cohesion: 0.13
Nodes (5): _require_min_rows(), compute(), get_spec(), TestScoreFdPair, TestGetSpec

### Community 110 - "ValidationError"
Cohesion: 0.06
Nodes (9): _run(), get_spark(), ValidationError, configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger (+1 more)

### Community 111 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 113 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 114 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 115 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 116 - "Raha"
Cohesion: 0.40
Nodes (5): Configuration, How it works, Install, Raha, Scope

### Community 118 - "8. Release"
Cohesion: 0.40
Nodes (5): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release

### Community 119 - "_value_matches_groups"
Cohesion: 0.40
Nodes (3): _value_matches_groups(), _counting_value_matches_groups(), counting()

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 268 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 297 - "SparkJobCounter"
Cohesion: 0.05
Nodes (19): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, Blockers, Completed Work, Key Changes, Next Steps (+11 more)

### Community 299 - "patterns_of"
Cohesion: 0.19
Nodes (3): patterns_of(), TestMatching, TestPatternsOf

### Community 339 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 433 - "collections_abc"
Cohesion: 0.09
Nodes (7): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 458 - "redact_evidence"
Cohesion: 0.27
Nodes (3): _hash_value(), redact_evidence(), TestRedactEvidence

### Community 530 - "hierarchy.py"
Cohesion: 0.07
Nodes (21): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+13 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 560 - "UnknownAlgorithmError"
Cohesion: 0.29
Nodes (6): Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema, UnknownAlgorithmError

### Community 635 - "_value_matches"
Cohesion: 0.09
Nodes (19): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+11 more)

### Community 686 - "perturbation.py"
Cohesion: 0.05
Nodes (26): _as_json_list(), InsufficientDataError, drop_nulls(), require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), finite_floats() (+18 more)

### Community 699 - "test_metrics.py"
Cohesion: 0.09
Nodes (9): differing_token_lengths(), min_pairwise_edit_distance(), perturb_spelling(), _brute_force_mpd(), _random_words(), _single_edit(), TestSpelling, TestSpellingBlocking (+1 more)

### Community 711 - "main"
Cohesion: 0.29
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 779 - "profile.py"
Cohesion: 0.22
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 783 - "snapshot.py"
Cohesion: 0.17
Nodes (7): diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.16
Nodes (11): Expected weakness: read Auto-Validate's low recall honestly, Layout, Scoring auto_validate, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), The `m` override, Timing (+3 more)

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.14
Nodes (10): maybe_scope(), UniDetectProfile, _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate() (+2 more)

### Community 880 - ".index"
Cohesion: 0.33
Nodes (4): Inspecting a pattern, Reading the output, Usage, segment()

### Community 901 - "Appendix: Validation Function Reference"
Cohesion: 0.28
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_columns_unique(), TestCheckColumnsUnique

### Community 1118 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 1123 - "Auto-Validate"
Cohesion: 0.22
Nodes (7): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly, Errors

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
Cohesion: 0.20
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `catalog.list_tables_matching`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1043 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **32 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `list_algorithms`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `AutoValidateAlgorithm`, `auto_validate/detector.py`, `UnknownAlgorithmError`, `InferredPattern`, `index.py`, `test_auto_validate_fmdv_v.py`, `_build_index`, `_value_matches`, `ConfigurationError`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 35 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 35 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `catalog.list_tables_matching`, `ErrorType enum (Definition 1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.13012477718360071 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `all_specs`, `FailureCounts`, `_StubDetector`, `list_algorithms`, `main`, `wiki_subset/run_benchmark.py`, `_FakeDetector`, `Uni-Detect`, `featurization.py`, `TestUniDetectDetect`, `collections_abc`, `algorithm.py`, `UniDetect`, `CorpusStatsBuilder`, `real_world_gov/run_benchmark.py`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `main`, `TestDetectCacheLifecycleSpark`, `parse_args`, `Detection`, `test_pipeline.py`, `pytest`, `get_spec`, `ValidationError`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Are the 41 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 41 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._