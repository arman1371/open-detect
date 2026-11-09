# Graph Report - open-detect  (2026-11-09)

## Corpus Check
- 182 files · ~138,812 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 227, (none) 2, .properties 1)
- WARNING: 232 of 440 files seen (53%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2545 nodes · 5716 edges · 139 communities (115 shown, 24 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 685 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b031e3dd`
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
- _value_matches
- algorithms/index.md
- FailureCounts
- fd_violation_strategies
- RahaConfig
- new_cluster
- outliers.py
- AutoValidateConfig
- InferredPattern
- KnownIndexLabeler
- features.py
- raha/detector.py
- hierarchy.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- list_tables_matching
- perturb_numeric_outlier
- ConfigurationError
- real_world_gov/run_benchmark.py
- pandas
- sample_tuple
- Writing your own algorithm
- raha/strategies.py
- main
- pytest
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- log_transform_fits_better
- numpy
- Uni-Detect
- real_world_gov benchmark results
- conftest.py
- CellResult
- uni_detect/core/enums.py
- Benchmark: WIKI subset
- PatternIndex
- FailureCountsAccumulatorParam
- registry.py
- CHANGELOG
- builder.py
- fmdv_v
- dataset_utils.py
- FeatureBucket
- Benchmark: real_world_gov
- fmdv
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
- docs/index.md
- log_duration
- dry_run
- _score_single_column
- gaussian_outlier_strategies
- CorpusIngestor
- variables
- Auto-Validate
- TestAttempt
- dev
- test_console_scripts.py
- Commit conventions and releases
- algorithms/raha.md
- ensure_schema_exists
- Current Status: BLOCKED
- clean_column
- wiki_subset/generate_report.py
- warnings
- test
- collections_abc
- release.yml
- release
- Running on Databricks
- Raha
- pypi
- Current Status: BLOCKED
- infer_column_data_type
- TestConfigThreshold
- with
- on
- profile.py
- steps
- perturb_spelling
- labeling.py
- test_hygiene.py
- Uni-Detect
- test_exceptions.py
- sonarqube
- argparse
- Benchmarks
- docs
- force
- ErrorType
- test_package_init.py
- algorithms/uni-detect.md
- select_fd_column_pairs
- open-detect
- cluster_column
- .index
- Comparing algorithms
- test_corpus_and_detectors.py
- _date_index
- `uni_detect`
- `raha`
- run_raha
- TestNullSentinel
- test_metrics.py
- test_executor_failures.py
- SparkJobCounter
- redact_evidence
- metrics/spelling.py
- auto_validate/detector.py
- test_bench_snapshot.py
- perturbation.py
- json
- min_pairwise_edit_distance
- TestConfigureLogging
- Auto-Validate
- Performance Baseline — OPE-87
- uniqueness_ratio

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 121 edges
2. `ErrorType` - 85 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 46 edges
6. `AutoValidateAlgorithm` - 39 edges
7. `UnityCatalogLocation` - 39 edges
8. `UniDetect` - 38 edges
9. `ConfigurationError` - 36 edges
10. `CellResult` - 34 edges

## Surprising Connections (you probably didn't know these)
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `The simplest labeler: a function` --references--> `CallableLabeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `As a plugin package (no changes to `open-detect`)` --references--> `list_algorithms()`  [INFERRED]
  docs/guides/writing-an-algorithm.md → src/open_detect/algorithms/registry.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (139 total, 24 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (11): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+3 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.12
Nodes (8): UniDetectConfig, UnityCatalogLocation, _run(), TestRedactEvidence, TestUniDetectConfig, TestUnityCatalogLocation, config(), config()

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.16
Nodes (11): _drop_nulls(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order() (+3 more)

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
Cohesion: 0.12
Nodes (7): InsufficientDataError, require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), ValidationError, TestFunctionalDependency

### Community 8 - "_value_matches"
Cohesion: 0.15
Nodes (6): _feasible_evidence(), _infeasible_evidence(), _non_null_cells(), _value_matches(), _counting_value_matches(), counting()

### Community 10 - "FailureCounts"
Cohesion: 0.18
Nodes (7): compute(), compute(), _score_fd_pair(), compute(), FailureCounts, compute(), TestPerElementFunctions

### Community 11 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 12 - "RahaConfig"
Cohesion: 0.14
Nodes (11): API reference, main(), RahaConfig, RahaDetector, GroundTruthLabeler, _values_equal(), test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler() (+3 more)

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (9): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - "KnownIndexLabeler"
Cohesion: 0.16
Nodes (11): Expected weakness: read Auto-Validate's low recall honestly, Layout, Scoring auto_validate, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), The `m` override, Timing (+3 more)

### Community 18 - "features.py"
Cohesion: 0.07
Nodes (15): ColumnPredictions, train_and_predict(), _default_classifier_factory(), build_all_features(), build_column_features(), ColumnFeatures, _compact_dtype(), _features() (+7 more)

### Community 19 - "raha/detector.py"
Cohesion: 0.11
Nodes (9): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), UniDetectAlgorithm, __getattr__(), _config(), _row() (+1 more)

### Community 20 - "hierarchy.py"
Cohesion: 0.05
Nodes (27): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches() (+19 more)

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

### Community 26 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.13
Nodes (7): _validate_edges(), main(), _require_columns(), ConfigurationError, test_main_installs_logging(), TestMain, TestRequireColumns

### Community 29 - "real_world_gov/run_benchmark.py"
Cohesion: 0.10
Nodes (14): confusion_metrics(), git_commit(), spark_session(), SparkUnavailable, _build_config(), main(), _print_comparison(), _register_table() (+6 more)

### Community 30 - "pandas"
Cohesion: 0.12
Nodes (18): _is_null(), _city_column(), _count_detect_calls(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference(), test_empty_dataframe() (+10 more)

### Community 32 - "Writing your own algorithm"
Cohesion: 0.33
Nodes (6): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm

### Community 33 - "raha/strategies.py"
Cohesion: 0.16
Nodes (6): _factorize_column(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestHistogramOutlierStrategies, TestPatternCharacterStrategies

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.19
Nodes (11): test_missing_columns_rejected(), test_require_uni_detect_fails_when_undetected(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only() (+3 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.12
Nodes (10): maybe_scope(), require_uni_detect(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 39 - "numpy"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 40 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.21
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "CellResult"
Cohesion: 0.07
Nodes (18): Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The shared result schema, Auto-Validate: learn patterns from clean columns (+10 more)

### Community 44 - "uni_detect/core/enums.py"
Cohesion: 0.10
Nodes (12): ColumnDataType, bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+4 more)

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "PatternIndex"
Cohesion: 0.12
Nodes (6): _fmdv_h_single(), _fmdv_single_segment(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), PatternIndex

### Community 48 - "registry.py"
Cohesion: 0.05
Nodes (29): The registry, Check it works, Installation, Installing from source, Pick your extra, _constant_factory(), get_algorithm(), get_algorithm_class() (+21 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (26): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+18 more)

### Community 50 - "builder.py"
Cohesion: 0.06
Nodes (11): Errors, CorpusNotFoundError, DataQualityError, UnityCatalogError, get_spark(), IndexNotBuiltError, OpenDetectError, configure_logging() (+3 more)

### Community 51 - "fmdv_v"
Cohesion: 0.09
Nodes (10): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _build_index(), TestCoarseSignature, TestFmdvV (+2 more)

### Community 52 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 53 - "FeatureBucket"
Cohesion: 0.09
Nodes (11): Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, TestCandidate, TestCorpusRecords (+3 more)

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.18
Nodes (11): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha, Reading the results (+3 more)

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "CallableLabeler"
Cohesion: 0.19
Nodes (4): CallableLabeler, TestCallableLabeler, fn(), test_callable_labeler_still_accepts_position_argument()

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - "UniDetect"
Cohesion: 0.16
Nodes (7): build_spark(), main(), UniDetect, __getattr__(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

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
Cohesion: 0.21
Nodes (5): Getting started, At a glance, Choosing an algorithm, Rules of thumb, Errors

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "_score_single_column"
Cohesion: 0.20
Nodes (4): _score_single_column(), config(), TestScoreSingleColumn, score()

### Community 70 - "gaussian_outlier_strategies"
Cohesion: 0.23
Nodes (4): gaussian_outlier_strategies(), _is_float_like(), TestGaussianOutlierStrategies, TestRowWeightedNumericGate

### Community 71 - "CorpusIngestor"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "Auto-Validate"
Cohesion: 0.33
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

### Community 78 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "collections_abc"
Cohesion: 0.08
Nodes (15): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, compute(), _score_pair(), NumericOutlierDetector, compute(), _score_column() (+7 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 90 - "Raha"
Cohesion: 0.40
Nodes (5): Configuration, How it works, Install, Raha, Scope

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

### Community 100 - "labeling.py"
Cohesion: 0.08
Nodes (16): Reading the output, Usage, Who answers the labeling questions?, Raha: find errors with a few labels, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+8 more)

### Community 101 - "test_hygiene.py"
Cohesion: 0.11
Nodes (5): parse_args(), TestParseArgs, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestGetSpark

### Community 102 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 103 - "test_exceptions.py"
Cohesion: 0.22
Nodes (6): test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error(), test_open_detect_error_is_catchable_broadly(), test_relocated_exceptions_importable_from_every_path(), test_validation_error_is_also_a_value_error()

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 106 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "ErrorType"
Cohesion: 0.08
Nodes (12): ComparisonDirection, ErrorType, _require_min_rows(), CorpusStatsStore, all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair (+4 more)

### Community 110 - "test_package_init.py"
Cohesion: 0.22
Nodes (3): test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 111 - "algorithms/uni-detect.md"
Cohesion: 0.24
Nodes (3): Registry, Registry and results, Result types

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 116 - ".index"
Cohesion: 0.33
Nodes (4): Inspecting a pattern, Reading the output, Usage, segment()

### Community 117 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 118 - "test_corpus_and_detectors.py"
Cohesion: 0.33
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 119 - "_date_index"
Cohesion: 0.40
Nodes (3): _date_index(), _date_values(), TestLargeGroups

### Community 120 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 121 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 251 - "test_metrics.py"
Cohesion: 0.24
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "SparkJobCounter"
Cohesion: 0.15
Nodes (9): ScopeStats, SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope(), test_disabled_counter_is_a_noop(), test_evicted_jobs_are_reported() (+1 more)

### Community 458 - "redact_evidence"
Cohesion: 0.24
Nodes (3): _hash_value(), redact_evidence(), TestRedactEvidence

### Community 527 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (8): min_conforming(), indexable_values(), fpr_column(), impurity(), TestMinConforming, _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestIndexableValues

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.22
Nodes (13): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+5 more)

### Community 639 - "perturbation.py"
Cohesion: 0.12
Nodes (9): _score_column(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency (+1 more)

### Community 667 - "json"
Cohesion: 0.16
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 1123 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 907 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UniDetectConfig` connect `UniDetectConfig` to `verify_build_config`, `test_spelling_detector.py`, `FailureCounts`, `RahaConfig`, `raha/detector.py`, `ConfigurationError`, `real_world_gov/run_benchmark.py`, `main`, `wiki_subset/run_benchmark.py`, `Uni-Detect`, `CellResult`, `CHANGELOG`, `builder.py`, `UniDetect`, `CorpusStatsBuilder`, `_score_single_column`, `collections_abc`, `TestConfigThreshold`, `test_hygiene.py`, `ErrorType`, `test_corpus_and_detectors.py`, `perturbation.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 35 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 35 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11261261261261261 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `AutoValidateAlgorithm`, `_value_matches`, `CellResult`, `RahaConfig`, `PatternIndex`, `InferredPattern`, `auto_validate/detector.py`, `fmdv_v`, `_date_index`, `fmdv`, `ConfigurationError`, `real_world_gov/run_benchmark.py`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._