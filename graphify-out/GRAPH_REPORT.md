# Graph Report - open-detect  (2026-11-16)

## Corpus Check
- 201 files · ~157,683 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 463 files seen (51%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 2959 nodes · 6497 edges · 171 communities (138 shown, 33 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 836 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `55392f11`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CorpusStatsBuilder
- UnityCatalogLocation
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- fd_compliance_ratio
- README.md — Uni-Detect overview
- Scoring auto_validate
- FailureCounts
- PRD: User Feedback Tooltips
- build_column_features
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- 7.2 Key Features
- raha/detector.py
- index.py
- permissions
- with
- update-graph
- check_failure_threshold
- with
- test_executor_failures.py
- build_corpus_statistics.py
- _check_expected_type
- Appendix: Validation Function Reference
- UniDetectConfig
- .detect
- list_algorithms
- numpy
- main
- pytest
- Benchmark: real_world_gov
- AutoValidateAlgorithm
- Comparing algorithms
- test_cache_lifecycle.py
- infer_column_data_type
- real_world_gov benchmark results
- propagate_labels
- _config
- test_featurization.py
- Benchmark: WIKI subset
- auto_validate/detector.py
- FailureCountsAccumulatorParam
- test_algorithms_registry.py
- CHANGELOG
- Auto-Validate
- PatternIndex
- .detect
- Completed Work
- dataset_utils.py
- fmdv
- updates
- labeling.py
- jobs
- .build_corpus_statistics
- collections_abc
- _coerce_numeric
- build
- uses
- real_world_gov/run_benchmark.py
- env
- perturb_spelling
- CorpusStatsStore
- dry_run
- _score_single_column
- ColumnDataType
- CorpusIngestor
- variables
- matches
- PRD: API Validation Framework for open-detect
- dev
- test_auto_validate_index.py
- Commit conventions and releases
- GroundTruthLabeler
- SparkUnavailableContext
- Current Status: BLOCKED
- test_raha_strategies.py
- UniDetect
- Raha
- test
- hooks
- release.yml
- release
- Running on Databricks
- is_float_like
- pypi
- Current Status: BLOCKED
- algorithms/uni-detect.md
- spark_session.py
- with
- on
- gaussian_outlier_strategies
- steps
- argparse
- CallableLabeler
- OPE-133 Review Summary
- profile.py
- ValidationError
- sonarqube
- TestAttempt
- uni_detect/text_utils.py
- docs
- force
- uni_detect/core/enums.py
- pipeline.py
- docs/index.md
- select_fd_column_pairs
- json
- open-detect
- TestConfigThreshold
- test_package_init.py
- _require_columns
- `uni_detect`
- `raha`
- ConfigurationError
- .index
- _build_index
- paperclip-issue-update.sh
- is_integer_like
- _check_unknown_kwargs
- finite_floats
- FeatureBucket
- Uni-Detect
- RahaDetector
- test_validation.py
- OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)
- Detection
- ._new_failure_tracker
- Uni-Detect
- _validate_literal_value
- _reject_unknown_kwargs
- _counting_value_matches_groups
- OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)
- 8. Release
- __getattr__
- _detector
- test_metrics.py
- ScoringJobCounter
- featurization.py
- TestScopedConf
- _FakeDetector
- ErrorType
- make_evidence_json
- _search_mpd
- hierarchy.py
- test_bench_snapshot.py
- perturb_numeric_outlier
- _ensure_sequence_of_str
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- KnownIndexLabeler
- wiki_subset/run_benchmark.py
- Auto-Validate
- _ensure_dataframe_is_spark
- RahaConfig
- wiki_subset/generate_report.py
- perturb_uniqueness
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 96 edges
3. `UniDetectConfig` - 92 edges
4. `UniDetect` - 70 edges
5. `FailureCounts` - 62 edges
6. `ValidationError` - 48 edges
7. `build_pattern_index()` - 46 edges
8. `UnityCatalogLocation` - 45 edges
9. `AutoValidateAlgorithm` - 39 edges
10. `CellResult` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Overview` --references--> `_value_matches()`  [INFERRED]
  memory/project_ope86_distinct_verdicts.md → src/open_detect/algorithms/auto_validate/detector.py
- `Technical Details` --references--> `_value_matches()`  [INFERRED]
  memory/project_ope86_distinct_verdicts.md → src/open_detect/algorithms/auto_validate/detector.py
- `Code Review State` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Final Fixes Pushed` --references--> `_segment_dp()`  [INFERRED]
  memory/project_ope133_review.md → src/open_detect/algorithms/auto_validate/fmdv_v.py
- `Phase 1: Core Tooltip Engine (4 weeks)` --references--> `CellResult`  [INFERRED]
  PRD-user-feedback-tooltips.md → src/open_detect/algorithms/base.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (171 total, 33 thin omitted)

### Community 0 - "CorpusStatsBuilder"
Cohesion: 0.06
Nodes (19): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), CorpusStatsBuilder, _stats_schema_without_error_type(), _config() (+11 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.13
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), score(), config()

### Community 2 - "pandas"
Cohesion: 0.13
Nodes (17): _city_column(), _count_detect_calls(), _detect(), _detector(), _make_tiny_corpus(), _per_cell_reference(), test_empty_dataframe(), test_feasible_column_empty_string_is_error_cell() (+9 more)

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
Cohesion: 0.13
Nodes (8): _score_pair(), fd_compliance_ratio(), FDResult, minority_violation_rows(), perturb_functional_dependency(), PerturbationOutcome, TestFunctionalDependency, TestPerturbFunctionalDependency

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.13
Nodes (15): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, artifacts, open_detect_wheel, bundle, name, build (+7 more)

### Community 9 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 10 - "FailureCounts"
Cohesion: 0.20
Nodes (5): compute(), compute(), _score_fd_pair(), FailureCounts, TestPerElementFunctions

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.05
Nodes (36): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+28 more)

### Community 12 - "build_column_features"
Cohesion: 0.19
Nodes (7): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.10
Nodes (7): Through the registry, The shared result schema, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestFmdvV, TestSegmentDp, solve(), TestCorpusInputShapes (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.16
Nodes (11): _drop_nulls(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id(), test_drop_nulls_returns_original_positions(), test_duplicates_map_every_occurrence_in_ascending_order() (+3 more)

### Community 18 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "raha/detector.py"
Cohesion: 0.11
Nodes (12): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+4 more)

### Community 20 - "index.py"
Cohesion: 0.12
Nodes (5): min_conforming(), _date_index(), _date_values(), TestLargeGroups, TestMinConforming

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

### Community 27 - "build_corpus_statistics.py"
Cohesion: 0.08
Nodes (13): list_tables(), list_tables_matching(), table_exists(), main(), parse_args(), _run(), test_main_installs_logging(), TestMain (+5 more)

### Community 29 - "Appendix: Validation Function Reference"
Cohesion: 0.22
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_dataframe_is_spark(), TestCheckDataFrameIsSpark

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "list_algorithms"
Cohesion: 0.10
Nodes (15): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+7 more)

### Community 33 - "numpy"
Cohesion: 0.09
Nodes (10): _compact_dtype(), _factorize_column(), fd_violation_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies (+2 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "pytest"
Cohesion: 0.10
Nodes (12): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 36 - "Benchmark: real_world_gov"
Cohesion: 0.18
Nodes (11): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha, Reading the results (+3 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 39 - "test_cache_lifecycle.py"
Cohesion: 0.12
Nodes (3): get_spark(), TestGetSparkExtended, TestGetSpark

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "_config"
Cohesion: 0.29
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 44 - "test_featurization.py"
Cohesion: 0.17
Nodes (4): log_transform_fits_better(), token_prevalence(), TestLogFit, TestTokenPrevalence

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "auto_validate/detector.py"
Cohesion: 0.09
Nodes (18): Implementation Status, Changes Made, _build_suggestion(), _distinct_value_verdicts(), _distinct_value_verdicts_groups(), _feasible_evidence(), _infeasible_evidence(), _infer_pattern_to_groups() (+10 more)

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.11
Nodes (10): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy(), TestPluginDiscovery (+2 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.15
Nodes (9): Registry, Registry and results, Result types, Auto-Validate, Configuration, Detector, Drift, Pattern index (+1 more)

### Community 51 - "PatternIndex"
Cohesion: 0.11
Nodes (11): Recent Changes, _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_v(), fmdv_vh(), _segment_dp(), _segment_fmdv_v() (+3 more)

### Community 52 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 54 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 55 - "fmdv"
Cohesion: 0.09
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "labeling.py"
Cohesion: 0.12
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.14
Nodes (8): Methodology: uni_detect -- mapping real dirty data onto its four error types, build_spark(), main(), config(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "real_world_gov/run_benchmark.py"
Cohesion: 0.14
Nodes (11): confusion_metrics(), _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate(), run_raha() (+3 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 66 - "perturb_spelling"
Cohesion: 0.29
Nodes (3): _score_column(), perturb_spelling(), TestPerturbSpelling

### Community 67 - "CorpusStatsStore"
Cohesion: 0.13
Nodes (4): CorpusStatsStore, config(), TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 70 - "ColumnDataType"
Cohesion: 0.14
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 71 - "CorpusIngestor"
Cohesion: 0.11
Nodes (6): balanced_union(), CorpusIngestor, compute_token_counts(), TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "matches"
Cohesion: 0.17
Nodes (5): matches(), fpr_column(), impurity(), matching_pattern(), TestMatching

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "test_auto_validate_index.py"
Cohesion: 0.11
Nodes (8): clean_column(), indexable_values(), _is_null(), _reference_build_pattern_index(), _reference_iter_corpus_columns(), TestCleanColumn, TestEquivalenceToReferenceBuild, TestIndexableValues

### Community 77 - "Commit conventions and releases"
Cohesion: 0.14
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "GroundTruthLabeler"
Cohesion: 0.17
Nodes (4): main(), GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "test_raha_strategies.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 83 - "UniDetect"
Cohesion: 0.10
Nodes (11): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+3 more)

### Community 84 - "Raha"
Cohesion: 0.17
Nodes (9): Configuration, How it works, Install, Raha, Scope, Configuration, Detector, Labelers (+1 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "hooks"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "algorithms/uni-detect.md"
Cohesion: 0.17
Nodes (9): Algorithms, Fidelity to the papers, Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source (+1 more)

### Community 94 - "spark_session.py"
Cohesion: 0.13
Nodes (9): _cap_driver_memory(), git_commit(), _host_memory_bytes(), spark_session(), SparkUnavailable, Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution (+1 more)

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 97 - "gaussian_outlier_strategies"
Cohesion: 0.12
Nodes (6): gaussian_outlier_strategies(), _is_float_like(), TestEmptyFrames, TestGaussianOutlierStrategies, TestNullSentinel, TestRowWeightedNumericGate

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.18
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "OPE-133 Review Summary"
Cohesion: 0.22
Nodes (8): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary

### Community 102 - "profile.py"
Cohesion: 0.20
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 103 - "ValidationError"
Cohesion: 0.08
Nodes (16): Errors, Errors, _iter_corpus_columns(), CorpusNotFoundError, DataQualityError, UnityCatalogError, IndexNotBuiltError, OpenDetectError (+8 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 106 - "uni_detect/text_utils.py"
Cohesion: 0.13
Nodes (4): is_mixed_alphanumeric(), tokenize(), TestMixedAlphanumeric, TestTokenize

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 109 - "uni_detect/core/enums.py"
Cohesion: 0.12
Nodes (8): ComparisonDirection, _require_min_rows(), all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 110 - "pipeline.py"
Cohesion: 0.08
Nodes (8): FailureTracker, scoped_conf(), configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 111 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 113 - "json"
Cohesion: 0.12
Nodes (3): main(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "_require_columns"
Cohesion: 0.22
Nodes (3): _filter_by_column_type(), _require_columns(), TestRequireColumns

### Community 118 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 119 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 120 - "ConfigurationError"
Cohesion: 0.18
Nodes (6): Concepts, Configuration objects, One contract: `detect()`, The registry, _validate_edges(), ConfigurationError

### Community 121 - ".index"
Cohesion: 0.33
Nodes (4): Inspecting a pattern, Reading the output, Usage, segment()

### Community 122 - "_build_index"
Cohesion: 0.24
Nodes (3): _build_index(), TestFmdvVh, _time_corpus()

### Community 128 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 129 - "finite_floats"
Cohesion: 0.32
Nodes (3): compute(), finite_floats(), TestFiniteFloats

### Community 131 - "Uni-Detect"
Cohesion: 0.25
Nodes (8): A fully local example, Configuration, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks

### Community 132 - "RahaDetector"
Cohesion: 0.36
Nodes (5): RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 134 - "OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)"
Cohesion: 0.29
Nodes (6): Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part), Overview, Related, Technical Details, Verification

### Community 137 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 140 - "_counting_value_matches_groups"
Cohesion: 0.33
Nodes (4): _counting_value_matches(), counting(), _counting_value_matches_groups(), counting()

### Community 141 - "OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)"
Cohesion: 0.40
Nodes (4): Code Review State, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results

### Community 142 - "8. Release"
Cohesion: 0.40
Nodes (5): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 297 - "ScoringJobCounter"
Cohesion: 0.08
Nodes (11): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, _FakeContext, _FakeTracker, _spark(), test_counts_jobs_and_distinct_stages_per_scope() (+3 more)

### Community 339 - "featurization.py"
Cohesion: 0.12
Nodes (11): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 433 - "ErrorType"
Cohesion: 0.09
Nodes (9): ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, _build_row(), _original_row_ids(), SpellingDetector, UniquenessDetector (+1 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.18
Nodes (6): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), TestRedactEvidence

### Community 527 - "_search_mpd"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 530 - "hierarchy.py"
Cohesion: 0.05
Nodes (24): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches_tokens() (+16 more)

### Community 537 - "test_bench_snapshot.py"
Cohesion: 0.19
Nodes (14): _frame(), _row(), test_added_and_removed_candidates_are_reported(), test_empty_detections_roundtrip(), test_flag_and_list_changes_are_exact(), test_identical_snapshots_match(), test_lr_ratio_beyond_tolerance_differs(), test_lr_ratio_within_tolerance_matches() (+6 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (4): _score_column(), perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.13
Nodes (10): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 831 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 835 - "wiki_subset/run_benchmark.py"
Cohesion: 0.10
Nodes (11): maybe_scope(), UniDetectProfile, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+3 more)

### Community 1123 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 1156 - "RahaConfig"
Cohesion: 0.11
Nodes (10): ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases (+2 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 1219 - "perturb_uniqueness"
Cohesion: 0.13
Nodes (8): _score_column(), duplicate_value_indices(), uniqueness_ratio(), _max_drop(), perturb_uniqueness(), TestDuplicateValueIndices, TestUniquenessRatio, TestPerturbUniqueness

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 1430 - "conftest.py"
Cohesion: 0.20
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1096 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `list_algorithms`, `AutoValidateAlgorithm`, `test_auto_validate_index.py`, `auto_validate/detector.py`, `InferredPattern`, `PatternIndex`, `index.py`, `fmdv`, `ConfigurationError`, `_build_index`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CorpusStatsBuilder` be split into smaller, more focused modules?**
  _Cohesion score 0.06010230179028133 - nodes in this community are weakly interconnected._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `CorpusStatsBuilder`, `UnityCatalogLocation`, `Uni-Detect`, `fd_compliance_ratio`, `FailureCounts`, `test_spelling_detector.py`, `raha/detector.py`, `build_corpus_statistics.py`, `list_algorithms`, `main`, `_FakeDetector`, `_config`, `CHANGELOG`, `ErrorType`, `.detect`, `.build_corpus_statistics`, `collections_abc`, `real_world_gov/run_benchmark.py`, `perturb_spelling`, `wiki_subset/run_benchmark.py`, `CorpusStatsStore`, `_score_single_column`, `perturb_uniqueness`, `_detector`, `UniDetect`, `ValidationError`, `pipeline.py`, `json`, `TestConfigThreshold`, `ConfigurationError`, `perturb_numeric_outlier`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 64 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 64 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._