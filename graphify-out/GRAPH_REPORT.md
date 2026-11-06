# Graph Report - open-detect  (2026-11-06)

## Corpus Check
- 181 files · ~137,244 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 227, (none) 2, .properties 1)
- WARNING: 232 of 439 files seen (53%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2507 nodes · 5629 edges · 128 communities (110 shown, 18 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 687 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `011b59df`
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
- InsufficientDataError
- auto_validate/detector.py
- algorithms/index.md
- FailureCounts
- fd_violation_strategies
- RahaDetector
- new_cluster
- outliers.py
- AutoValidateConfig
- InferredPattern
- KnownIndexLabeler
- RahaConfig
- ErrorDetectionAlgorithm
- patterns.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- pipeline.py
- perturb_numeric_outlier
- ConfigurationError
- real_world_gov/run_benchmark.py
- AlgorithmResult
- .detect
- list_algorithms
- gaussian_outlier_strategies
- main
- pytest
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- numeric_outlier.py
- numpy
- Uni-Detect
- real_world_gov benchmark results
- spark_session.py
- CellResult
- featurization.py
- `auto_validate`
- open_detect_wheel
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- builder.py
- fmdv_v
- .detect
- FeatureBucket
- confusion_metrics
- PatternIndex
- updates
- CallableLabeler
- jobs
- UniDetect
- README.md — Uni-Detect overview
- _coerce_numeric
- build
- uses
- CorpusStatsBuilder
- env
- concepts.md
- CorpusStatsStore
- dry_run
- _score_single_column
- CorpusIngestor
- variables
- Auto-Validate
- TestAttempt
- dev
- test_console_scripts.py
- Commit conventions and releases
- Raha
- UnityCatalogLocation
- Current Status: BLOCKED
- _reference_build_pattern_index
- wiki_subset/generate_report.py
- test
- BaseDetector
- release.yml
- release
- Running on Databricks
- Raha
- pypi
- Current Status: BLOCKED
- infer_column_data_type
- test_failures.py
- with
- on
- steps
- perturb_spelling
- propagate_labels
- test_corpus_build_metadata.py
- Uni-Detect
- open_detect/exceptions.py
- sonarqube
- algorithms/uni-detect.md
- docs
- force
- ErrorType
- docs/index.md
- select_fd_column_pairs
- open-detect
- config
- _default_classifier_factory
- __getattr__
- test_metrics.py
- _StubDetector
- SparkJobCounter
- make_evidence_json
- metrics/spelling.py
- pandas
- test_bench_snapshot.py
- perturbation.py
- snapshot.py
- min_pairwise_edit_distance
- main
- Auto-Validate
- Performance Baseline — OPE-87
- uniqueness_ratio

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 121 edges
2. `ErrorType` - 85 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 46 edges
6. `UnityCatalogLocation` - 39 edges
7. `AutoValidateAlgorithm` - 38 edges
8. `UniDetect` - 38 edges
9. `ConfigurationError` - 36 edges
10. `RahaConfig` - 34 edges

## Surprising Connections (you probably didn't know these)
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `Writing a class` --references--> `Labeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (128 total, 18 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (11): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+3 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.15
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.18
Nodes (10): _drop_nulls(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order() (+2 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "InsufficientDataError"
Cohesion: 0.18
Nodes (5): InsufficientDataError, fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 8 - "auto_validate/detector.py"
Cohesion: 0.17
Nodes (5): _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 10 - "FailureCounts"
Cohesion: 0.17
Nodes (9): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, compute() (+1 more)

### Community 11 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 12 - "RahaDetector"
Cohesion: 0.07
Nodes (20): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, main(), RahaDetector, ColumnFeatures (+12 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (14): AutoValidateConfig, _segment_dp(), segment(), _segment_fmdv_v(), _segment_fmdv_vh(), build_pattern_index(), TestDefaults, TestValidation (+6 more)

### Community 16 - "InferredPattern"
Cohesion: 0.10
Nodes (8): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "KnownIndexLabeler"
Cohesion: 0.14
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, Scoring raha, The corpus (`data/corpus/`) (+5 more)

### Community 18 - "RahaConfig"
Cohesion: 0.09
Nodes (14): ColumnPredictions, train_and_predict(), RahaConfig, build_all_features(), build_column_features(), _compact_dtype(), _features(), TestClassifierTrainingPath (+6 more)

### Community 19 - "ErrorDetectionAlgorithm"
Cohesion: 0.13
Nodes (13): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm_class(), _load_entry_points(), register_algorithm() (+5 more)

### Community 20 - "patterns.py"
Cohesion: 0.07
Nodes (14): generality_weight(), generalize(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns() (+6 more)

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

### Community 26 - "pipeline.py"
Cohesion: 0.08
Nodes (9): list_tables(), list_tables_matching(), table_exists(), _run(), get_spark(), TestListTables, TestListTablesMatching, fake_sql() (+1 more)

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.16
Nodes (8): Concepts, Configuration objects, One contract: `detect()`, The registry, _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 29 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (13): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), _print_comparison() (+5 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "list_algorithms"
Cohesion: 0.09
Nodes (14): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+6 more)

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.09
Nodes (11): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+3 more)

### Community 34 - "main"
Cohesion: 0.16
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.12
Nodes (11): __getattr__(), config(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.09
Nodes (14): maybe_scope(), ProfileRunSkippedUniDetect, require_uni_detect(), UniDetectProfile, git_commit(), main(), _build_config(), _load_corpus_tables() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.08
Nodes (10): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing, Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm (+2 more)

### Community 38 - "numeric_outlier.py"
Cohesion: 0.14
Nodes (4): _score_column(), build_outlier_bucket(), log_transform_fits_better(), TestLogFit

### Community 39 - "numpy"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 40 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "spark_session.py"
Cohesion: 0.10
Nodes (9): spark_session(), SparkUnavailable, candidates(), main(), select(), _delta_jars(), _download(), spark() (+1 more)

### Community 43 - "CellResult"
Cohesion: 0.15
Nodes (7): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, CellResult, TestCellResultEvidence, score()

### Community 44 - "featurization.py"
Cohesion: 0.09
Nodes (12): _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket() (+4 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.11
Nodes (17): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (cell-level) (+9 more)

### Community 46 - "open_detect_wheel"
Cohesion: 0.40
Nodes (5): artifacts, open_detect_wheel, build, path, type

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (9): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_unknown_algorithm_raises(), TestPluginDiscovery, worker() (+1 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.08
Nodes (24): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+16 more)

### Community 50 - "builder.py"
Cohesion: 0.10
Nodes (5): FailureTracker, get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 51 - "fmdv_v"
Cohesion: 0.08
Nodes (13): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _build_index(), _date_index(), _date_values() (+5 more)

### Community 52 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "FeatureBucket"
Cohesion: 0.08
Nodes (13): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, __getattr__() (+5 more)

### Community 54 - "confusion_metrics"
Cohesion: 0.09
Nodes (16): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+8 more)

### Community 55 - "PatternIndex"
Cohesion: 0.06
Nodes (13): _clean(), fmdv(), fmdv_h(), min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), PatternIndex, sorted_patterns() (+5 more)

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "CallableLabeler"
Cohesion: 0.13
Nodes (10): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, TestCallableLabeler (+2 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.20
Nodes (7): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates, _write_table()

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.20
Nodes (10): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, bundle, name, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching (+2 more)

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "concepts.md"
Cohesion: 0.15
Nodes (10): Getting started, At a glance, Choosing an algorithm, Rules of thumb, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs (+2 more)

### Community 67 - "CorpusStatsStore"
Cohesion: 0.20
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 71 - "CorpusIngestor"
Cohesion: 0.17
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Auto-Validate"
Cohesion: 0.22
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_console_scripts.py"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "Raha"
Cohesion: 0.50
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.15
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, test_evidence_honors_redact_mode(), TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_reference_build_pattern_index"
Cohesion: 0.12
Nodes (7): clean_column(), _is_null(), _iter_corpus_columns(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "BaseDetector"
Cohesion: 0.10
Nodes (6): BaseDetector, FunctionalDependencyDetector, _score_pair(), NumericOutlierDetector, SpellingDetector, UniquenessDetector

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "Running on Databricks"
Cohesion: 0.40
Nodes (4): Job arguments, Jobs, Notebooks, Running on Databricks

### Community 90 - "Raha"
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

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 101 - "test_corpus_build_metadata.py"
Cohesion: 0.13
Nodes (4): TestWiring, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSpark

### Community 102 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.08
Nodes (17): Errors, Practical advice, Errors, CorpusNotFoundError, DataQualityError, IndexNotBuiltError, OpenDetectError, UnknownAlgorithmError (+9 more)

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

### Community 109 - "ErrorType"
Cohesion: 0.12
Nodes (9): ComparisonDirection, ErrorType, _require_min_rows(), all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs (+1 more)

### Community 111 - "docs/index.md"
Cohesion: 0.20
Nodes (6): open-detect, What is in the box, Why a common interface, Registry, Registry and results, Result types

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 118 - "config"
Cohesion: 0.40
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "SparkJobCounter"
Cohesion: 0.16
Nodes (9): ScopeStats, SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported() (+1 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.19
Nodes (6): _hash_value(), make_evidence_json(), redact_evidence(), _build_row(), _original_row_ids(), TestRedactEvidence

### Community 527 - "metrics/spelling.py"
Cohesion: 0.15
Nodes (8): drop_nulls(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance(), TestDropNulls

### Community 530 - "pandas"
Cohesion: 0.07
Nodes (17): _conforms(), _append_literal(), _char_class(), _class_of_token(), _is_numeric(), _iter_runs(), matches(), matches_tokens() (+9 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.18
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 639 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 667 - "snapshot.py"
Cohesion: 0.21
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 711 - "main"
Cohesion: 0.12
Nodes (7): main(), parse_args(), configure_logging(), test_main_installs_logging(), TestMain, TestParseArgs, TestConfigureLogging

### Community 1123 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 886 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `list_algorithms`, `AutoValidateAlgorithm`, `auto_validate/detector.py`, `InferredPattern`, `pandas`, `fmdv_v`, `_reference_build_pattern_index`, `confusion_metrics`, `PatternIndex`, `ConfigurationError`, `real_world_gov/run_benchmark.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 35 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 35 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11411411411411411 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `FailureCounts`, `_StubDetector`, `ErrorDetectionAlgorithm`, `pipeline.py`, `real_world_gov/run_benchmark.py`, `list_algorithms`, `main`, `wiki_subset/run_benchmark.py`, `numeric_outlier.py`, `Uni-Detect`, `featurization.py`, `builder.py`, `.detect`, `FeatureBucket`, `UniDetect`, `CorpusStatsBuilder`, `CorpusStatsStore`, `_score_single_column`, `main`, `BaseDetector`, `test_corpus_build_metadata.py`, `open_detect/exceptions.py`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._