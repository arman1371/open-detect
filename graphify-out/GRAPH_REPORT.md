# Graph Report - bd7b3e13-0c9e-4465-82cd-8ea9c7959798  (2026-11-11)

## Corpus Check
- 178 files · ~141,105 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 227, (none) 2, .properties 1)

## Summary
- 2594 nodes · 5828 edges · 147 communities (123 shown, 24 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 689 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `64c074a6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- tests/algorithms/uni_detect/test_corpus_build_metadata.py
- UniDetectConfig
- ErrorDetectionAlgorithm
- sys
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- TestFunctionalDependency
- fmdv_v
- UnityCatalogLocation
- FailureCounts
- test_spelling_detector.py
- RahaDetector
- fmdv_v
- warnings
- tests/algorithms/auto_validate/test_auto_validate_index.py
- check_drift
- .detect
- test_ope86_distinct_verdicts.py
- ConfigurationError
- hierarchy.py
- src/open_detect/algorithms/auto_validate/patterns.py
- wiki_subset/generate_report.py
- src/open_detect/algorithms/uni_detect/detectors/spelling.py
- ValidationError
- tests/algorithms/uni_detect/test_hygiene.py
- _run
- tests/algorithms/uni_detect/test_perturbation.py
- check_failure_threshold
- real_world_gov/run_benchmark.py
- fd_violation_strategies
- .detect
- GroundTruthLabeler
- tests/algorithms/raha/test_raha_strategies.py
- main
- pytest
- ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py
- AutoValidateAlgorithm
- UnknownAlgorithmError
- real_world_gov/generate_report.py
- KnownIndexLabeler
- real_world_gov benchmark results
- re
- clean_column
- ErrorType
- Benchmark: WIKI subset
- pandas
- UniDetectAlgorithm
- list_algorithms
- CHANGELOG
- fresh_registry
- CellResult
- spark_session
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
- docs/index.md
- tests/algorithms/uni_detect/test_corpus_edge_cases.py
- typing
- RahaConfig
- perturb_spelling
- KnownIndexLabeler
- src/open_detect/algorithms/uni_detect/detectors/base.py
- Detection
- open_detect/__init__.py
- ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py
- uniqueness_ratio
- Commit conventions and releases
- algorithms/raha.md
- featurization.py
- json
- auto_validate/detector.py
- test_pipeline.py
- TestConfigThreshold
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- `uni_detect`
- ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py
- Writing your own algorithm
- FailureCountsAccumulatorParam
- `raha`
- json
- src/open_detect/algorithms/uni_detect/config.py
- infer_column_data_type
- _score_single_column
- ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py
- ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- tokenize
- tests/algorithms/uni_detect/test_metrics.py
- open_detect_wheel
- argparse
- paperclip-issue-update.sh
- ope89-wt/benchmarks/real_world_gov/run_benchmark.py
- test_algorithms_registry.py
- src/open_detect/algorithms/auto_validate/drift.py
- FeatureBucket
- ope110-v2/src/open_detect/algorithms/uni_detect/detectors/base.py
- csv
- ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py
- get_spec
- pytest
- algorithms/uni-detect.md
- tests/algorithms/uni_detect/test_corpus_ingestion.py
- .build_index
- ope89-wt/src/open_detect/algorithms/uni_detect/detectors/numeric_outlier.py
- argparse
- builder.py
- .__init__
- RahaDetector
- main
- TestAttempt
- test_console_scripts.py
- reference/index.md
- algorithms/index.md
- OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)
- Auto-Validate
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- Running on Databricks
- is_integer_like
- Raha
- diff_fingerprints
- test_corpus_ingestion.py
- Installation
- tests/algorithms/uni_detect/test_metrics.py
- test_executor_failures.py
- test_bench_spark_jobs.py
- redact_evidence
- InsufficientDataError
- TestMatching
- ope74-wt/tests/algorithms/raha/test_raha_labeling.py
- perturbation.py
- ope138-verify/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py
- ope85-clean/src/open_detect/algorithms/raha/features.py
- .infer_pattern
- _raise

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 123 edges
2. `ErrorType` - 86 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 46 edges
6. `AutoValidateAlgorithm` - 41 edges
7. `UnityCatalogLocation` - 39 edges
8. `UniDetect` - 39 edges
9. `RahaConfig` - 36 edges
10. `ConfigurationError` - 36 edges

## Surprising Connections (you probably didn't know these)
- `Technical Details` --references--> `_value_matches()`  [INFERRED]
  memory/project_ope86_distinct_verdicts.md → src/open_detect/algorithms/auto_validate/detector.py
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `The simplest labeler: a function` --references--> `CallableLabeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (147 total, 24 thin omitted)

### Community 0 - "tests/algorithms/uni_detect/test_corpus_build_metadata.py"
Cohesion: 0.15
Nodes (10): property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, TestLegacyCorpus, TestMismatch (+2 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.18
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 2 - "ErrorDetectionAlgorithm"
Cohesion: 0.15
Nodes (10): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+2 more)

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
Cohesion: 0.18
Nodes (5): InsufficientDataError, fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 8 - "fmdv_v"
Cohesion: 0.07
Nodes (14): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _build_index(), _date_index(), _date_values() (+6 more)

### Community 9 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (12): compute(), _score_fd_pair(), compute(), _score_pair(), compute(), _score_column(), compute(), _score_column() (+4 more)

### Community 11 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 12 - "RahaDetector"
Cohesion: 0.11
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 13 - "fmdv_v"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "warnings"
Cohesion: 0.11
Nodes (10): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 15 - "tests/algorithms/auto_validate/test_auto_validate_index.py"
Cohesion: 0.07
Nodes (13): AutoValidateConfig, _infeasible_evidence(), _segment_dp(), build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve() (+5 more)

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (9): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - ".detect"
Cohesion: 0.20
Nodes (8): Changes Made, Overview, _distinct_value_verdicts(), _feasible_evidence(), _is_null(), _non_null_cells(), _value_matches(), _value_text()

### Community 18 - "test_ope86_distinct_verdicts.py"
Cohesion: 0.19
Nodes (9): main(), _detect_dirty(), _make_tiny_corpus(), test_all_nan_column(), test_empty_dataframe(), test_identical_to_per_cell_baseline(), test_nan_and_empty_string_distinct_verdicts(), test_single_value_column() (+1 more)

### Community 19 - "ConfigurationError"
Cohesion: 0.12
Nodes (11): Errors, _validate_edges(), ConfigurationError, IndexNotBuiltError, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error() (+3 more)

### Community 20 - "hierarchy.py"
Cohesion: 0.06
Nodes (23): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+15 more)

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
Nodes (10): _check_columns_present(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _ensure_dataframe_is_spark(), _ensure_sequence_of_str() (+2 more)

### Community 25 - "tests/algorithms/uni_detect/test_hygiene.py"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "_run"
Cohesion: 0.08
Nodes (12): list_tables(), list_tables_matching(), table_exists(), parse_args(), _run(), get_spark(), TestParseArgs, TestListTables (+4 more)

### Community 27 - "tests/algorithms/uni_detect/test_perturbation.py"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "check_failure_threshold"
Cohesion: 0.19
Nodes (4): Configuration, DataQualityError, check_failure_threshold(), TestCheckFailureThreshold

### Community 29 - "real_world_gov/run_benchmark.py"
Cohesion: 0.08
Nodes (16): ProfileRunSkippedUniDetect, require_uni_detect(), git_commit(), dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames() (+8 more)

### Community 30 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "GroundTruthLabeler"
Cohesion: 0.21
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 33 - "tests/algorithms/raha/test_raha_strategies.py"
Cohesion: 0.08
Nodes (19): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), _assert_same(), _naive_fd() (+11 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.09
Nodes (11): __getattr__(), __getattr__(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py"
Cohesion: 0.08
Nodes (14): confusion_metrics(), maybe_scope(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "UnknownAlgorithmError"
Cohesion: 0.12
Nodes (15): Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema (+7 more)

### Community 39 - "real_world_gov/generate_report.py"
Cohesion: 0.21
Nodes (10): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+2 more)

### Community 40 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "re"
Cohesion: 0.15
Nodes (9): A fully local example, How it works, Install, Operational notes, Uni-Detect, _delta_jars(), _download(), spark() (+1 more)

### Community 43 - "clean_column"
Cohesion: 0.13
Nodes (7): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), _reference_iter_corpus_columns(), TestCleanColumn, TestIndexableValues

### Community 44 - "ErrorType"
Cohesion: 0.15
Nodes (8): ErrorType, BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "pandas"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 47 - "UniDetectAlgorithm"
Cohesion: 0.19
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 48 - "list_algorithms"
Cohesion: 0.11
Nodes (13): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+5 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (26): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+18 more)

### Community 50 - "fresh_registry"
Cohesion: 0.20
Nodes (6): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), TestPluginDiscovery, worker()

### Community 51 - "CellResult"
Cohesion: 0.11
Nodes (6): Combine, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 52 - "spark_session"
Cohesion: 0.14
Nodes (8): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 53 - "src/open_detect/algorithms/uni_detect/core/models.py"
Cohesion: 0.13
Nodes (9): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords (+1 more)

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.20
Nodes (9): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Source (+1 more)

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "CallableLabeler"
Cohesion: 0.18
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 58 - "logging"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.18
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 60 - "itertools"
Cohesion: 0.19
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

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

### Community 66 - "docs/index.md"
Cohesion: 0.24
Nodes (5): At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 67 - "tests/algorithms/uni_detect/test_corpus_edge_cases.py"
Cohesion: 0.16
Nodes (4): CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "typing"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "RahaConfig"
Cohesion: 0.10
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 71 - "KnownIndexLabeler"
Cohesion: 0.14
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 74 - "open_detect/__init__.py"
Cohesion: 0.17
Nodes (4): __getattr__(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 75 - "ope-73/src/open_detect/algorithms/uni_detect/detectors/functional_dependency.py"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "algorithms/raha.md"
Cohesion: 0.33
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 79 - "featurization.py"
Cohesion: 0.09
Nodes (13): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+5 more)

### Community 81 - "json"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (16): _matches_segments(), _clean(), fmdv(), fmdv_h(), min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), _segment_fmdv_v() (+8 more)

### Community 83 - "test_pipeline.py"
Cohesion: 0.15
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 85 - "ope89-wt/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 87 - "ope104-wt/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "Writing your own algorithm"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 90 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 91 - "json"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "src/open_detect/algorithms/uni_detect/config.py"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.12
Nodes (6): infer_column_data_type(), is_float_like(), is_mixed_alphanumeric(), TestDataTypeInference, TestFloatLike, TestMixedAlphanumeric

### Community 94 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 95 - "ope71-wt/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "ope110-v2/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 98 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 102 - "ope89-wt/benchmarks/real_world_gov/run_benchmark.py"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 103 - "test_algorithms_registry.py"
Cohesion: 0.18
Nodes (5): real_plugin_path(), test_builtin_algorithms_are_registered(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy(), _write_distinfo_plugin()

### Community 104 - "src/open_detect/algorithms/auto_validate/drift.py"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "ope110-v2/src/open_detect/algorithms/uni_detect/detectors/base.py"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 107 - "csv"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "ope83-verify/tests/algorithms/auto_validate/test_auto_validate_fmdv_v.py"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "get_spec"
Cohesion: 0.10
Nodes (6): all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.24
Nodes (4): Getting started, Registry, Registry and results, Result types

### Community 112 - "tests/algorithms/uni_detect/test_corpus_ingestion.py"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 113 - ".build_index"
Cohesion: 0.15
Nodes (9): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+1 more)

### Community 115 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 116 - "builder.py"
Cohesion: 0.09
Nodes (7): _require_min_rows(), configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 118 - "RahaDetector"
Cohesion: 0.27
Nodes (6): RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 119 - "main"
Cohesion: 0.36
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 121 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 124 - "OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)"
Cohesion: 0.33
Nodes (5): Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Related, Technical Details, Verification

### Community 125 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 127 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.40
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 128 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 131 - "Raha"
Cohesion: 0.40
Nodes (5): Configuration, How it works, Install, Raha, Scope

### Community 134 - "Installation"
Cohesion: 0.67
Nodes (3): Installation, Installing from source, Pick your extra

### Community 251 - "tests/algorithms/uni_detect/test_metrics.py"
Cohesion: 0.24
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "test_bench_spark_jobs.py"
Cohesion: 0.15
Nodes (9): ScopeStats, SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported() (+1 more)

### Community 458 - "redact_evidence"
Cohesion: 0.24
Nodes (3): _hash_value(), redact_evidence(), TestRedactEvidence

### Community 527 - "InsufficientDataError"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 537 - "ope74-wt/tests/algorithms/raha/test_raha_labeling.py"
Cohesion: 0.18
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 639 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 667 - "ope138-verify/src/open_detect/algorithms/uni_detect/jobs/build_corpus_statistics.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 699 - "ope85-clean/src/open_detect/algorithms/raha/features.py"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 1123 - ".infer_pattern"
Cohesion: 0.14
Nodes (10): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+2 more)

### Community 1252 - "_raise"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 913 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `tests/algorithms/auto_validate/test_auto_validate_index.py` to `.infer_pattern`, `ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py`, `AutoValidateAlgorithm`, `UnknownAlgorithmError`, `fmdv_v`, `list_algorithms`, `.detect`, `auto_validate/detector.py`, `ConfigurationError`, `check_drift`, `.build_index`, `test_ope86_distinct_verdicts.py`, `fmdv`, `real_world_gov/run_benchmark.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 37 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 37 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `tests/algorithms/uni_detect/test_corpus_build_metadata.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14838709677419354 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `tests/algorithms/uni_detect/test_corpus_build_metadata.py`, `ErrorDetectionAlgorithm`, `FailureCounts`, `test_executor_failures.py`, `_run`, `real_world_gov/run_benchmark.py`, `main`, `ope-73/src/open_detect/algorithms/uni_detect/detectors/uniqueness.py`, `re`, `UniDetectAlgorithm`, `list_algorithms`, `src/open_detect/algorithms/uni_detect/core/models.py`, `UniDetect`, `real_world_gov/run_benchmark.py`, `tests/algorithms/uni_detect/test_corpus_edge_cases.py`, `Detection`, `open_detect/__init__.py`, `featurization.py`, `_score_single_column`, `FeatureBucket`, `get_spec`, `pytest`, `builder.py`, `main`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._