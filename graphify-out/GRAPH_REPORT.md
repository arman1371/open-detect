# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-10)

## Corpus Check
- 176 files · ~139,801 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 227, (none) 2, .properties 1)

## Summary
- 2571 nodes · 5784 edges · 143 communities (118 shown, 25 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 677 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ef2a4ffb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- tests/algorithms/uni_detect/test_corpus_build_metadata.py
- UniDetectConfig
- PatternIndex
- sys
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- TestFunctionalDependency
- fmdv_v.py
- PatternIndex
- FailureCounts
- list_algorithms
- RahaDetector
- fmdv_v
- warnings
- tests/algorithms/auto_validate/test_auto_validate_index.py
- check_drift
- _is_null
- numpy
- ConfigurationError
- ope83-verify/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py
- src/open_detect/algorithms/auto_validate/patterns.py
- wiki_subset/generate_report.py
- src/open_detect/algorithms/uni_detect/detectors/spelling.py
- ValidationError
- tests/algorithms/uni_detect/test_hygiene.py
- ErrorType
- tests/algorithms/uni_detect/test_perturbation.py
- check_failure_threshold
- dataset_utils.py
- AlgorithmResult
- .detect
- GroundTruthLabeler
- tests/algorithms/raha/test_raha_strategies.py
- main
- pytest
- ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py
- TestAutoValidateDetector
- score
- ope76-wt/src/open_detect/algorithms/auto_validate/patterns.py
- ope74-wt/src/open_detect/exceptions.py
- real_world_gov benchmark results
- re
- Uni-Detect
- featurization.py
- `auto_validate`
- pandas
- tokenize
- test_algorithms_registry.py
- CHANGELOG
- pipeline.py
- CellResult
- ErrorDetectionAlgorithm
- src/open_detect/algorithms/uni_detect/core/models.py
- Benchmark: real_world_gov
- fmdv
- argparse
- CallableLabeler
- logging
- UniDetect
- itertools
- _coerce_numeric
- ope89-wt/benchmarks/real_world_gov/run_benchmark.py
- functools
- real_world_gov/run_benchmark.py
- src/open_detect/algorithms/uni_detect/featurization.py
- docs/algorithms/index.md
- tests/algorithms/uni_detect/test_corpus_edge_cases.py
- typing
- RahaConfig
- wiki_subset/generate_report.py
- KnownIndexLabeler
- src/open_detect/algorithms/uni_detect/detectors/base.py
- Detection
- ErrorType
- ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py
- ope85-clean/src/open_detect/algorithms/auto_validate/patterns.py
- Commit conventions and releases
- algorithms/raha.md
- bucket_by_edges
- json
- auto_validate/detector.py
- test_pipeline.py
- test_package_init.py
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- test_corpus_builder_helpers.py
- ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- Writing your own algorithm
- FailureCountsAccumulatorParam
- .detect
- json
- src/open_detect/algorithms/uni_detect/config.py
- tests/test_text_utils.py
- _score_single_column
- ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py
- ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- profile.py
- tests/algorithms/uni_detect/test_metrics.py
- get_algorithm
- argparse
- paperclip-issue-update.sh
- ope89-wt/benchmarks/real_world_gov/run_benchmark.py
- get_algorithm_class
- src/open_detect/algorithms/auto_validate/drift.py
- wiki_subset/run_benchmark.py
- ope110-v2/src/open_detect/algorithms/uni_detect/detectors/base.py
- csv
- ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- BaseDetector
- logging_utils.py
- algorithms/uni-detect.md
- tests/algorithms/uni_detect/test_corpus_ingestion.py
- infer_column_data_type
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/numeric_outlier.py
- config
- common/__init__.py
- .__init__
- test_featurization.py
- TestAttempt
- __getattr__
- Raha
- __getattr__
- Benchmark: WIKI subset
- Auto-Validate
- is_integer_like
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- Running on Databricks
- tests/algorithms/uni_detect/test_metrics.py
- test_executor_failures.py
- test_bench_spark_jobs.py
- make_evidence_json
- InsufficientDataError
- matches
- ope74-wt/tests/algorithms/raha/test_raha_labeling.py
- perturbation.py
- ope138-verify/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py
- ope85-clean/src/open_detect/algorithms/raha/features.py
- get_logger
- Auto-Validate
- _raise

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 120 edges
2. `ErrorType` - 86 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 46 edges
6. `UnityCatalogLocation` - 39 edges
7. `UniDetect` - 39 edges
8. `AutoValidateAlgorithm` - 38 edges
9. `RahaConfig` - 36 edges
10. `ConfigurationError` - 36 edges

## Surprising Connections (you probably didn't know these)
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `The simplest labeler: a function` --references--> `CallableLabeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (143 total, 25 thin omitted)

### Community 0 - "tests/algorithms/uni_detect/test_corpus_build_metadata.py"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.06
Nodes (20): UniDetectConfig, UnityCatalogLocation, _drop_nulls(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+12 more)

### Community 2 - "PatternIndex"
Cohesion: 0.09
Nodes (7): _fmdv_h_single(), _fmdv_single_segment(), PatternIndex, any_pattern(), patterns_of(), sorted_patterns(), TestPatternsOf

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
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 8 - "fmdv_v.py"
Cohesion: 0.14
Nodes (9): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh() (+1 more)

### Community 10 - "FailureCounts"
Cohesion: 0.17
Nodes (9): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, compute() (+1 more)

### Community 11 - "list_algorithms"
Cohesion: 0.13
Nodes (9): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, list_algorithms(), test_builtin_algorithms_are_registered() (+1 more)

### Community 12 - "RahaDetector"
Cohesion: 0.12
Nodes (12): Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, ColumnFeatures (+4 more)

### Community 13 - "fmdv_v"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "warnings"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "tests/algorithms/auto_validate/test_auto_validate_index.py"
Cohesion: 0.06
Nodes (15): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _build_index(), TestFmdvV, TestFmdvVh, TestSegmentDp (+7 more)

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (9): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - "_is_null"
Cohesion: 0.17
Nodes (7): _distinct_value_verdicts(), _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches(), _value_text()

### Community 18 - "numpy"
Cohesion: 0.14
Nodes (3): ColumnPredictions, _default_classifier_factory(), _compact_dtype()

### Community 19 - "ConfigurationError"
Cohesion: 0.08
Nodes (21): Unreleased, Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Practical advice, Errors (+13 more)

### Community 20 - "ope83-verify/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py"
Cohesion: 0.07
Nodes (20): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+12 more)

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
Cohesion: 0.13
Nodes (10): _iter_corpus_columns(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _ensure_dataframe_is_spark(), _ensure_sequence_of_str() (+2 more)

### Community 25 - "tests/algorithms/uni_detect/test_hygiene.py"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "ErrorType"
Cohesion: 0.11
Nodes (10): ensure_schema_exists(), list_tables(), list_tables_matching(), table_exists(), UnityCatalogError, TestEnsureSchemaExists, TestListTables, TestListTablesMatching (+2 more)

### Community 27 - "tests/algorithms/uni_detect/test_perturbation.py"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 29 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 30 - "AlgorithmResult"
Cohesion: 0.19
Nodes (3): Combine, AlgorithmResult, TestAlgorithmResult

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "GroundTruthLabeler"
Cohesion: 0.16
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 33 - "tests/algorithms/raha/test_raha_strategies.py"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 34 - "main"
Cohesion: 0.16
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.20
Nodes (10): test_missing_columns_rejected(), test_require_uni_detect_fails_when_undetected(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+2 more)

### Community 36 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py"
Cohesion: 0.09
Nodes (14): confusion_metrics(), maybe_scope(), spark_session(), SparkUnavailable, _build_config(), _register_table(), run(), run_auto_validate() (+6 more)

### Community 37 - "TestAutoValidateDetector"
Cohesion: 0.06
Nodes (24): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+16 more)

### Community 38 - "score"
Cohesion: 0.18
Nodes (11): Reading the output, Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Comparing algorithms, Find the cells they agree on, Mixed inputs (+3 more)

### Community 39 - "ope76-wt/src/open_detect/algorithms/auto_validate/patterns.py"
Cohesion: 0.14
Nodes (12): fd_violation_strategies(), _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column() (+4 more)

### Community 40 - "ope74-wt/src/open_detect/exceptions.py"
Cohesion: 0.17
Nodes (3): __getattr__(), __getattr__(), test_old_except_clause_catches_new_error()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "re"
Cohesion: 0.15
Nodes (5): main(), _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect

### Community 44 - "featurization.py"
Cohesion: 0.14
Nodes (11): _score_pair(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+3 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 46 - "pandas"
Cohesion: 0.11
Nodes (12): main(), build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype (+4 more)

### Community 47 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (8): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), TestPluginDiscovery, worker(), _write_distinfo_plugin()

### Community 49 - "CHANGELOG"
Cohesion: 0.08
Nodes (23): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+15 more)

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.18
Nodes (7): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), register_algorithm(), decorator(), UniDetectAlgorithm

### Community 53 - "src/open_detect/algorithms/uni_detect/core/models.py"
Cohesion: 0.14
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.29
Nodes (7): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Which 5 datasets, and why

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "CallableLabeler"
Cohesion: 0.21
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn()

### Community 58 - "logging"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.17
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "itertools"
Cohesion: 0.29
Nodes (7): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4)

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

### Community 66 - "docs/algorithms/index.md"
Cohesion: 0.20
Nodes (7): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box, Why a common interface

### Community 67 - "tests/algorithms/uni_detect/test_corpus_edge_cases.py"
Cohesion: 0.17
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "typing"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "RahaConfig"
Cohesion: 0.12
Nodes (13): _make_classifier(), train_and_predict(), RahaConfig, RahaDetector, _features(), TestClassifierTrainingPath, TestDegenerateCases, TestDeterminismAndSeeding (+5 more)

### Community 71 - "KnownIndexLabeler"
Cohesion: 0.18
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 72 - "src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.11
Nodes (18): artifacts, open_detect_wheel, bundle, name, default, description, default, description (+10 more)

### Community 74 - "ErrorType"
Cohesion: 0.14
Nodes (5): ComparisonDirection, ErrorType, all_specs(), ErrorTypeSpec, TestAllSpecs

### Community 75 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "ope85-clean/src/open_detect/algorithms/auto_validate/patterns.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 79 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 81 - "json"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (12): min_conforming(), clean_column(), indexable_values(), _is_null(), _date_index(), _date_values(), TestLargeGroups, TestMinConforming (+4 more)

### Community 83 - "test_pipeline.py"
Cohesion: 0.18
Nodes (14): grouped_bar_chart(), comparison_charts(), comparison_table_markdown(), _print_comparison(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct() (+6 more)

### Community 84 - "test_package_init.py"
Cohesion: 0.32
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 85 - "ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 87 - "ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "Writing your own algorithm"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 90 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 91 - "json"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "src/open_detect/algorithms/uni_detect/config.py"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "tests/test_text_utils.py"
Cohesion: 0.17
Nodes (4): is_float_like(), is_mixed_alphanumeric(), TestFloatLike, TestMixedAlphanumeric

### Community 94 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 95 - "ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 98 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "get_algorithm"
Cohesion: 0.20
Nodes (7): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 102 - "ope89-wt/benchmarks/real_world_gov/run_benchmark.py"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 103 - "get_algorithm_class"
Cohesion: 0.24
Nodes (7): _constant_factory(), get_algorithm_class(), _load_entry_points(), register_lazy(), test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name(), test_unknown_algorithm_raises()

### Community 104 - "src/open_detect/algorithms/auto_validate/drift.py"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "wiki_subset/run_benchmark.py"
Cohesion: 0.12
Nodes (12): require_uni_detect(), UniDetectProfile, git_commit(), main(), main(), _build_config(), _load_corpus_tables(), _load_targets() (+4 more)

### Community 106 - "ope110-v2/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.33
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 107 - "csv"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "BaseDetector"
Cohesion: 0.09
Nodes (7): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, get_spec(), TestGetSpec

### Community 110 - "logging_utils.py"
Cohesion: 0.09
Nodes (8): _require_min_rows(), FailureTracker, configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.25
Nodes (4): Registry, Registry and results, Result types, API reference

### Community 112 - "tests/algorithms/uni_detect/test_corpus_ingestion.py"
Cohesion: 0.16
Nodes (5): select_fd_column_pairs(), pair_table(), TestIngestColumnPairsNullAlignment, TestSelectFdColumnPairs, by_name()

### Community 115 - "config"
Cohesion: 0.21
Nodes (5): _cap_driver_memory(), _host_memory_bytes(), candidates(), main(), select()

### Community 116 - "common/__init__.py"
Cohesion: 0.22
Nodes (3): test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 122 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 124 - "Benchmark: WIKI subset"
Cohesion: 0.33
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 125 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 127 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.40
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 128 - "Running on Databricks"
Cohesion: 0.40
Nodes (4): Job arguments, Jobs, Notebooks, Running on Databricks

### Community 251 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.24
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "test_bench_spark_jobs.py"
Cohesion: 0.15
Nodes (9): ScopeStats, SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported() (+1 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.12
Nodes (8): _hash_value(), make_evidence_json(), redact_evidence(), _build_row(), _original_row_ids(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestRedactEvidence

### Community 527 - "InsufficientDataError"
Cohesion: 0.12
Nodes (10): InsufficientDataError, require_min_size(), FDResult, _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result() (+2 more)

### Community 530 - "matches"
Cohesion: 0.17
Nodes (5): matches(), fpr_column(), impurity(), matching_pattern(), TestMatching

### Community 537 - "ope74-wt/tests/algorithms/raha/test_raha_labeling.py"
Cohesion: 0.22
Nodes (13): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+5 more)

### Community 639 - "perturbation.py"
Cohesion: 0.10
Nodes (10): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency (+2 more)

### Community 667 - "ope138-verify/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py"
Cohesion: 0.16
Nodes (10): _nice_ceiling(), _rounded_top_rect(), _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main() (+2 more)

### Community 699 - "ope85-clean/src/open_detect/algorithms/raha/features.py"
Cohesion: 0.15
Nodes (4): differing_token_lengths(), min_pairwise_edit_distance(), try_min_pairwise_edit_distance(), TestSpelling

### Community 711 - "get_logger"
Cohesion: 0.17
Nodes (6): main(), parse_args(), _run(), test_main_installs_logging(), TestMain, TestParseArgs

### Community 1123 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1252 - "_raise"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 901 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `tests/algorithms/auto_validate/test_auto_validate_index.py` to `PatternIndex`, `ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py`, `TestAutoValidateDetector`, `fmdv_v.py`, `algorithms/uni-detect.md`, `check_drift`, `_is_null`, `auto_validate/detector.py`, `ConfigurationError`, `fmdv`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 37 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 37 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `tests/algorithms/uni_detect/test_corpus_build_metadata.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11025641025641025 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `tests/algorithms/uni_detect/test_corpus_build_metadata.py`, `FailureCounts`, `test_executor_failures.py`, `ConfigurationError`, `main`, `ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py`, `Uni-Detect`, `featurization.py`, `pipeline.py`, `ErrorDetectionAlgorithm`, `src/open_detect/algorithms/uni_detect/core/models.py`, `UniDetect`, `real_world_gov/run_benchmark.py`, `tests/algorithms/uni_detect/test_corpus_edge_cases.py`, `wiki_subset/generate_report.py`, `get_logger`, `Detection`, `make_evidence_json`, `test_corpus_builder_helpers.py`, `.detect`, `_score_single_column`, `wiki_subset/run_benchmark.py`, `BaseDetector`, `logging_utils.py`, `algorithms/uni-detect.md`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._