# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-14)

## Corpus Check
- 180 files · ~144,206 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 233 file(s) not represented in the graph (top: .csv 227, (none) 2, .properties 1)

## Summary
- 2715 nodes · 6099 edges · 150 communities (121 shown, 29 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 731 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `874aaae8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- tests/algorithms/uni_detect/test_corpus_build_metadata.py
- UniDetectConfig
- test_pipeline.py
- sys
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- TestFunctionalDependency
- README.md — Uni-Detect overview
- .build_index
- FailureCounts
- fd_violation_strategies
- RahaConfig
- fmdv_v
- CellResult
- tests/algorithms/auto_validate/test_auto_validate_index.py
- check_drift
- bucket_by_edges
- infer_column_data_type
- ErrorDetectionAlgorithm
- PatternIndex
- src/open_detect/algorithms/auto_validate/patterns.py
- wiki_subset/generate_report.py
- src/open_detect/algorithms/uni_detect/detectors/spelling.py
- ValidationError
- tests/algorithms/uni_detect/test_hygiene.py
- pytest
- perturbation.py
- _check_expected_type
- ValidationError
- fd_violation_strategies
- .detect
- list_algorithms
- gaussian_outlier_strategies
- main
- test_deprecated_shims.py
- ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py
- _make_tiny_corpus
- score
- test_build_corpus_statistics.py
- algorithms/index.md
- real_world_gov benchmark results
- propagate_labels
- clean_column
- test_featurization.py
- Benchmark: WIKI subset
- Detection
- FailureCountsAccumulatorParam
- list_algorithms
- CHANGELOG
- Auto-Validate
- CellResult
- UniDetectAlgorithm
- uni_detect/core/models.py
- Benchmark: real_world_gov
- fmdv
- argparse
- CallableLabeler
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
- is_integer_like
- ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py
- uniqueness_ratio
- Commit conventions and releases
- _check_columns_unique
- SparkUnavailableContext
- json
- pandas
- UniDetect
- Raha
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- test_corpus_ingestion.py
- ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- Writing your own algorithm
- FailureCountsAccumulatorParam
- Raha
- json
- src/open_detect/algorithms/uni_detect/config.py
- infer_column_data_type
- ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py
- ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- numpy
- tests/algorithms/uni_detect/test_metrics.py
- CallableLabeler
- open_detect/exceptions.py
- src/open_detect/algorithms/auto_validate/drift.py
- ope110-v2/src/open_detect/algorithms/uni_detect/detectors/base.py
- csv
- ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- ErrorType
- pytest
- algorithms/uni-detect.md
- tests/algorithms/uni_detect/test_corpus_ingestion.py
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/numeric_outlier.py
- builder.py
- _require_columns
- _detector
- tests/algorithms/uni_detect/test_metrics.py
- _StubDetector
- SparkJobCounter
- featurization.py
- get_spark
- BaseDetector
- builder.py
- redact_evidence
- InsufficientDataError
- hierarchy.py
- ope74-wt/tests/algorithms/raha/test_raha_labeling.py
- .detect
- perturb_numeric_outlier
- _ensure_sequence_of_str
- outliers.py
- ope85-clean/src/open_detect/algorithms/raha/features.py
- ConfigurationError
- ProfileRunSkippedUniDetect
- snapshot.py
- KnownIndexLabeler
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- .infer_pattern
- _ensure_dataframe_is_spark
- RahaDetector
- wiki_subset/generate_report.py
- uniqueness_ratio
- _raise
- json
- spark_session.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 121 edges
2. `ErrorType` - 95 edges
3. `UniDetectConfig` - 92 edges
4. `UniDetect` - 69 edges
5. `FailureCounts` - 56 edges
6. `build_pattern_index()` - 46 edges
7. `UnityCatalogLocation` - 45 edges
8. `ValidationError` - 42 edges
9. `AutoValidateAlgorithm` - 38 edges
10. `ConfigurationError` - 36 edges

## Surprising Connections (you probably didn't know these)
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `Writing a class` --references--> `Labeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `Operational notes` --references--> `CorpusNotFoundError`  [INFERRED]
  docs/algorithms/uni-detect.md → src/open_detect/algorithms/uni_detect/exceptions.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (150 total, 29 thin omitted)

### Community 0 - "tests/algorithms/uni_detect/test_corpus_build_metadata.py"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.05
Nodes (23): ensure_schema_exists(), UniDetectConfig, UnityCatalogLocation, _drop_nulls(), TestDetectCacheLifecycleSpark, _positions_of(), _row(), _score() (+15 more)

### Community 2 - "test_pipeline.py"
Cohesion: 0.16
Nodes (5): _mock_detector_result(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectWriteDetections

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
Cohesion: 0.20
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 9 - ".build_index"
Cohesion: 0.16
Nodes (8): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (10): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, _raise() (+2 more)

### Community 11 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 12 - "RahaConfig"
Cohesion: 0.08
Nodes (15): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, build_all_features(), build_column_features(), _compact_dtype(), _features() (+7 more)

### Community 13 - "fmdv_v"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 15 - "tests/algorithms/auto_validate/test_auto_validate_index.py"
Cohesion: 0.08
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (9): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.15
Nodes (10): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+2 more)

### Community 20 - "PatternIndex"
Cohesion: 0.06
Nodes (16): _fmdv_h_single(), _fmdv_single_segment(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), generality_weight(), matches(), PatternIndex (+8 more)

### Community 21 - "src/open_detect/algorithms/auto_validate/patterns.py"
Cohesion: 0.07
Nodes (28): if, permissions, runs-on, steps, types, types, jobs, claude (+20 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.09
Nodes (26): UV_PYTHON, jobs, real-world-gov, wiki-subset, name, on, workflow_dispatch, env (+18 more)

### Community 23 - "src/open_detect/algorithms/uni_detect/detectors/spelling.py"
Cohesion: 0.08
Nodes (24): concurrency, cancel-in-progress, group, jobs, update-graph, name, on, push (+16 more)

### Community 24 - "ValidationError"
Cohesion: 0.19
Nodes (4): Configuration, DataQualityError, check_failure_threshold(), TestCheckFailureThreshold

### Community 25 - "tests/algorithms/uni_detect/test_hygiene.py"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "pytest"
Cohesion: 0.06
Nodes (8): list_tables(), list_tables_matching(), table_exists(), configure_logging(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "perturbation.py"
Cohesion: 0.10
Nodes (10): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency (+2 more)

### Community 29 - "ValidationError"
Cohesion: 0.10
Nodes (9): ValidationError, _check_dataframe_is_spark(), _check_unknown_kwargs(), _reject_unknown_kwargs(), _validate_literal_value(), TestCheckDataFrameIsSpark, TestCheckUnknownKwargs, TestRejectUnknownKwargs (+1 more)

### Community 30 - "fd_violation_strategies"
Cohesion: 0.13
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Combine, AlgorithmResult, TestAlgorithmResult

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "list_algorithms"
Cohesion: 0.12
Nodes (11): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+3 more)

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "test_deprecated_shims.py"
Cohesion: 0.10
Nodes (11): __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py"
Cohesion: 0.13
Nodes (12): confusion_metrics(), git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), _print_comparison(), run(), run_auto_validate() (+4 more)

### Community 38 - "score"
Cohesion: 0.20
Nodes (10): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat (+2 more)

### Community 39 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "clean_column"
Cohesion: 0.40
Nodes (5): A fully local example, How it works, Install, Operational notes, Uni-Detect

### Community 44 - "test_featurization.py"
Cohesion: 0.17
Nodes (4): log_transform_fits_better(), token_prevalence(), TestLogFit, TestTokenPrevalence

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 48 - "list_algorithms"
Cohesion: 0.10
Nodes (13): get_algorithm_class(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_builtin_algorithms_are_registered(), test_get_algorithm_constructs_with_args() (+5 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (26): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+18 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 51 - "CellResult"
Cohesion: 0.09
Nodes (10): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _build_index(), TestCoarseSignature, TestFmdvV (+2 more)

### Community 52 - "UniDetectAlgorithm"
Cohesion: 0.19
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "uni_detect/core/models.py"
Cohesion: 0.13
Nodes (7): Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.13
Nodes (12): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+4 more)

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "CallableLabeler"
Cohesion: 0.10
Nodes (9): Who answers the labeling questions?, ColumnFeatures, GroundTruthLabeler, HeuristicLabeler, Labeler, _resolve_position(), _values_equal(), TestGroundTruthLabeler (+1 more)

### Community 58 - "logging"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.26
Nodes (4): build_spark(), main(), TestCorpusBuilderAndDetectors, _write_table()

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
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 65 - "src/open_detect/algorithms/uni_detect/featurization.py"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "concepts.md"
Cohesion: 0.28
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "CorpusStatsStore"
Cohesion: 0.17
Nodes (4): CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "typing"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 71 - "KnownIndexLabeler"
Cohesion: 0.14
Nodes (5): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, TestDetectReturnsEmptyResultWhenNoCandidates, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Detection"
Cohesion: 0.22
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 75 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "uniqueness_ratio"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 81 - "json"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "pandas"
Cohesion: 0.07
Nodes (13): min_conforming(), clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _date_index(), _date_values(), TestLargeGroups (+5 more)

### Community 83 - "UniDetect"
Cohesion: 0.16
Nodes (6): UniDetect, _config(), _mock_spark(), TestUniDetectInit, TestUniDetectRelease, TestUniDetectValidateInputs

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

### Community 90 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 91 - "json"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "src/open_detect/algorithms/uni_detect/config.py"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.12
Nodes (6): is_float_like(), is_mixed_alphanumeric(), tokenize(), TestFloatLike, TestMixedAlphanumeric, TestTokenize

### Community 95 - "ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "numpy"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 98 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 100 - "CallableLabeler"
Cohesion: 0.17
Nodes (10): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, TestCallableLabeler (+2 more)

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.12
Nodes (12): The registry, Errors, InsufficientDataError, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved() (+4 more)

### Community 104 - "src/open_detect/algorithms/auto_validate/drift.py"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "ope110-v2/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 107 - "csv"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "ErrorType"
Cohesion: 0.11
Nodes (10): ComparisonDirection, ErrorType, parse_args(), all_specs(), ErrorTypeSpec, get_spec(), TestParseArgs, TestScoreFdPair (+2 more)

### Community 110 - "pytest"
Cohesion: 0.15
Nodes (5): get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.20
Nodes (6): open-detect, What is in the box, Why a common interface, Registry, Registry and results, Result types

### Community 112 - "tests/algorithms/uni_detect/test_corpus_ingestion.py"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 116 - "builder.py"
Cohesion: 0.14
Nodes (5): UnityCatalogError, __getattr__(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.20
Nodes (5): _brute_force_mpd(), _random_words(), _single_edit(), TestDropNulls, TestSpellingBlocking

### Community 268 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 297 - "SparkJobCounter"
Cohesion: 0.10
Nodes (17): ScopeStats, SparkJobCounter, Blockers, Completed Work, Key Changes, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress (+9 more)

### Community 339 - "featurization.py"
Cohesion: 0.13
Nodes (12): ColumnDataType, _score_pair(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket() (+4 more)

### Community 376 - "get_spark"
Cohesion: 0.08
Nodes (4): get_spark(), TestGetSparkExtended, TestScopedConf, TestGetSpark

### Community 426 - "BaseDetector"
Cohesion: 0.07
Nodes (7): BaseDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, _FakeDetector, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 433 - "builder.py"
Cohesion: 0.10
Nodes (7): _require_min_rows(), make_evidence_json(), FunctionalDependencyDetector, _build_row(), _original_row_ids(), FailureTracker, scoped_conf()

### Community 458 - "redact_evidence"
Cohesion: 0.27
Nodes (3): _hash_value(), redact_evidence(), TestRedactEvidence

### Community 527 - "InsufficientDataError"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "hierarchy.py"
Cohesion: 0.06
Nodes (19): _append_literal(), _char_class(), _class_of_token(), generalize(), _is_numeric(), _iter_runs(), matches_tokens(), _parse() (+11 more)

### Community 537 - "ope74-wt/tests/algorithms/raha/test_raha_labeling.py"
Cohesion: 0.18
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 635 - ".detect"
Cohesion: 0.20
Nodes (6): _check_columns_present(), _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+1 more)

### Community 699 - "ope85-clean/src/open_detect/algorithms/raha/features.py"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 711 - "ConfigurationError"
Cohesion: 0.15
Nodes (10): Concepts, Configuration objects, Errors, One contract: `detect()`, _validate_edges(), main(), _run(), ConfigurationError (+2 more)

### Community 783 - "snapshot.py"
Cohesion: 0.21
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.14
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, Scoring raha, The corpus (`data/corpus/`) (+5 more)

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.08
Nodes (16): maybe_scope(), require_uni_detect(), UniDetectProfile, dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames() (+8 more)

### Community 880 - "AutoValidateAlgorithm"
Cohesion: 0.19
Nodes (3): AutoValidateAlgorithm, segment(), TestAutoValidateDetector

### Community 1123 - ".infer_pattern"
Cohesion: 0.22
Nodes (9): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+1 more)

### Community 1156 - "RahaDetector"
Cohesion: 0.19
Nodes (7): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.15
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 1252 - "_raise"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "json"
Cohesion: 0.29
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 1430 - "spark_session.py"
Cohesion: 0.10
Nodes (9): spark_session(), SparkUnavailable, candidates(), main(), select(), _delta_jars(), _download(), spark() (+1 more)

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `catalog.list_tables_matching`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 954 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **29 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `tests/algorithms/auto_validate/test_auto_validate_index.py` to `.build_index`, `check_drift`, `PatternIndex`, `list_algorithms`, `ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py`, `_make_tiny_corpus`, `CellResult`, `fmdv`, `real_world_gov/run_benchmark.py`, `ConfigurationError`, `pandas`, `.test_all_variants_infer_something`, `.test_score_computed_as_1_minus_fpr`, `.test_columns_subset`, `.test_empty_dataframe`, `.test_infeasible_column_no_flags`, `AutoValidateAlgorithm`, `.test_evidence_keys`, `.detect`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 35 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 35 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `catalog.list_tables_matching`, `ErrorType enum (Definition 1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `tests/algorithms/uni_detect/test_corpus_build_metadata.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10801393728222997 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `tests/algorithms/uni_detect/test_corpus_build_metadata.py`, `UniDetectConfig`, `test_pipeline.py`, `FailureCounts`, `_StubDetector`, `ErrorDetectionAlgorithm`, `pytest`, `list_algorithms`, `main`, `ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py`, `test_build_corpus_statistics.py`, `BaseDetector`, `clean_column`, `Detection`, `builder.py`, `UniDetectAlgorithm`, `uni_detect/core/models.py`, `.build_corpus_statistics`, `real_world_gov/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `CorpusStatsStore`, `_score_single_column`, `FeatureBucket`, `ConfigurationError`, `KnownIndexLabeler`, `featurization.py`, `UniDetect`, `builder.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 63 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._