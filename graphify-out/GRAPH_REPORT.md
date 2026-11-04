# Graph Report - ope74-wt  (2026-11-04)

## Corpus Check
- 165 files · ~133,704 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 226, (none) 3, .properties 1)

## Summary
- 2061 nodes · 5001 edges · 124 communities (92 shown, 32 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 619 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a61806dc`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- algorithms/__init__.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- InsufficientDataError
- PatternIndex
- labeling.py
- FailureCounts
- real_world_gov/generate_report.py
- CorpusStatsBuilder
- fmdv_v
- outliers.py
- AutoValidateConfig
- InferredPattern
- RahaConfig
- main
- CorpusIngestor
- tokenize
- patterns.py
- wiki_subset/generate_report.py
- ._new_failure_tracker
- test_metrics.py
- test_hygiene.py
- list_tables_matching
- require_min_size
- ConfigurationError
- UniDetect
- AlgorithmResult
- .detect
- raha/strategies.py
- pandas
- min_pairwise_edit_distance
- dataset_utils.py
- AutoValidateAlgorithm
- HeuristicLabeler
- bucket_by_edges
- ._new_failure_tracker
- real_world_gov benchmark results
- conftest.py
- test_algorithms_registry.py
- bucket_by_edges
- `auto_validate`
- wiki_subset/run_benchmark.py
- fd_compliance_ratio
- builder.py
- CHANGELOG
- clean_column
- propagate_labels
- UniDetectAlgorithm
- reference/index.md
- drop_nulls
- fmdv
- argparse
- perturbation.py
- build_corpus_statistics.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- algorithms/index.md
- pytest
- select_fd_column_pairs
- featurization.py
- .detect
- config
- builder.py
- docs/index.md
- Benchmark: real_world_gov
- models.py
- ErrorType
- Uni-Detect
- Raha
- Auto-Validate
- ColumnDataType
- Commit conventions and releases
- collections_abc
- UnityCatalogLocation
- algorithms/uni-detect.md
- _date_index
- `raha`
- auto_validate/detector.py
- min_conforming
- TestMatching
- open-detect
- list_algorithms
- min_pairwise_edit_distance
- Raha
- confusion_metrics
- Current Status: BLOCKED
- uni_detect/text_utils.py
- TestConfigThreshold
- `auto_validate`
- test_auto_validate_fmdv_v.py
- algorithms.md
- test_metrics.py
- metrics/spelling.py
- patterns_of
- .detect
- hierarchy.py
- OpenDetectError
- matches
- _segment_dp
- sorted_patterns
- perturb_spelling
- get_spec
- logging_utils.py
- _require_columns
- test_corpus_and_detectors.py
- generalize
- uniqueness_ratio
- reference/index.md
- UnknownAlgorithmError
- is_float_like
- real_plugin_path
- parse_args
- _StubDetector
- __getattr__

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 115 edges
2. `UniDetectConfig` - 84 edges
3. `ErrorType` - 83 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 45 edges
6. `UnityCatalogLocation` - 39 edges
7. `UniDetect` - 39 edges
8. `ConfigurationError` - 36 edges
9. `AutoValidateAlgorithm` - 35 edges
10. `RahaConfig` - 34 edges

## Surprising Connections (you probably didn't know these)
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/open_detect/algorithms/uni_detect/pipeline.py
- `Reading the output` --references--> `score()`  [INFERRED]
  docs/algorithms/auto-validate.md → tests/algorithms/uni_detect/test_corpus_builder_helpers.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (124 total, 32 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.05
Nodes (22): Operational notes, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, diff_fingerprints(), property_key() (+14 more)

### Community 2 - "algorithms/__init__.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.13
Nodes (10): git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "InsufficientDataError"
Cohesion: 0.18
Nodes (5): InsufficientDataError, fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 8 - "PatternIndex"
Cohesion: 0.09
Nodes (10): min_conforming(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_vh(), _infer_cmp(), _segment_fmdv_v(), _segment_fmdv_vh() (+2 more)

### Community 9 - "labeling.py"
Cohesion: 0.08
Nodes (17): Scoring raha, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, ColumnFeatures (+9 more)

### Community 10 - "FailureCounts"
Cohesion: 0.19
Nodes (5): compute(), compute(), _score_fd_pair(), FailureCounts, TestPerElementFunctions

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 12 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (7): CorpusStatsBuilder, _stats_schema_without_error_type(), FailureTracker, TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 13 - "fmdv_v"
Cohesion: 0.15
Nodes (5): fmdv_v(), _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 14 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.10
Nodes (8): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "InferredPattern"
Cohesion: 0.11
Nodes (7): check_drift(), _clean_series(), _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.10
Nodes (13): API reference, ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, RahaDetector, _features(), TestClassifierTrainingPath (+5 more)

### Community 18 - "main"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 19 - "CorpusIngestor"
Cohesion: 0.15
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 20 - "tokenize"
Cohesion: 0.16
Nodes (6): _iter_runs(), token_count(), tokenize(), indexable_values(), TestIndexableValues, TestTokenize

### Community 21 - "patterns.py"
Cohesion: 0.14
Nodes (7): generality_weight(), Token, _alternatives(), _best_first_patterns(), common_patterns(), iter_patterns(), _ordered_alternatives()

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.20
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 23 - "._new_failure_tracker"
Cohesion: 0.12
Nodes (5): compute(), compute(), compute(), compute(), compute()

### Community 24 - "test_metrics.py"
Cohesion: 0.19
Nodes (4): Configuration, DataQualityError, check_failure_threshold(), TestCheckFailureThreshold

### Community 26 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "require_min_size"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.17
Nodes (5): _validate_edges(), main(), ConfigurationError, test_main_installs_logging(), TestMain

### Community 29 - "UniDetect"
Cohesion: 0.20
Nodes (7): build_spark(), main(), _run(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 30 - "AlgorithmResult"
Cohesion: 0.14
Nodes (7): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, AlgorithmResult, TestAlgorithmResult

### Community 31 - ".detect"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (10): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies, TestNullSentinel (+2 more)

### Community 34 - "pandas"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.24
Nodes (9): _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule(), test_internal_imports_use_new_paths_only(), test_module_shims_are_identity_preserving(), test_unknown_exception_attr_raises() (+1 more)

### Community 36 - "dataset_utils.py"
Cohesion: 0.13
Nodes (13): dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main(), _print_comparison(), _register_table() (+5 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (26): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+18 more)

### Community 38 - "HeuristicLabeler"
Cohesion: 0.18
Nodes (11): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs (+3 more)

### Community 39 - "bucket_by_edges"
Cohesion: 0.14
Nodes (9): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features() (+1 more)

### Community 40 - "._new_failure_tracker"
Cohesion: 0.17
Nodes (3): __getattr__(), __getattr__(), test_old_except_clause_catches_new_error()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.16
Nodes (8): A fully local example, How it works, Install, Uni-Detect, _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (8): get_algorithm(), get_algorithm_class(), test_registered_under_raha(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name(), test_unknown_algorithm_raises(), TestPluginDiscoveryViaRealDistInfo

### Community 44 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 45 - "`auto_validate`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "wiki_subset/run_benchmark.py"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 48 - "builder.py"
Cohesion: 0.20
Nodes (6): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), TestPluginDiscovery, worker()

### Community 49 - "CHANGELOG"
Cohesion: 0.10
Nodes (20): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+12 more)

### Community 50 - "clean_column"
Cohesion: 0.40
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "UniDetectAlgorithm"
Cohesion: 0.12
Nodes (11): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+3 more)

### Community 54 - "drop_nulls"
Cohesion: 0.20
Nodes (9): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Source (+1 more)

### Community 55 - "fmdv"
Cohesion: 0.11
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "perturbation.py"
Cohesion: 0.13
Nodes (9): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, _resolve_row_ids(), TestDuplicateValueIndices, TestPerturbFunctionalDependency (+1 more)

### Community 58 - "build_corpus_statistics.py"
Cohesion: 0.17
Nodes (5): open-detect, What is in the box, Why a common interface, CellResult, TestCellResultEvidence

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 63 - "pytest"
Cohesion: 0.33
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 65 - "featurization.py"
Cohesion: 0.14
Nodes (11): _score_pair(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+3 more)

### Community 66 - ".detect"
Cohesion: 0.23
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 68 - "builder.py"
Cohesion: 0.07
Nodes (3): ComparisonDirection, get_spark(), TestGetSpark

### Community 71 - "models.py"
Cohesion: 0.22
Nodes (3): test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 72 - "ErrorType"
Cohesion: 0.09
Nodes (13): ErrorType, BaseDetector, _hash_value(), make_evidence_json(), redact_evidence(), _candidate_row(), FunctionalDependencyDetector, _candidate_row() (+5 more)

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 76 - "ColumnDataType"
Cohesion: 0.36
Nodes (4): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables()

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "collections_abc"
Cohesion: 0.07
Nodes (12): _check_columns_present(), DriftResult, _iter_corpus_columns(), fpr_column(), impurity(), ValidationError, _check_columns_unique(), _check_dataframe_is_spark() (+4 more)

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 81 - "algorithms/uni-detect.md"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_date_index"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "`raha`"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 84 - "auto_validate/detector.py"
Cohesion: 0.16
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 88 - "list_algorithms"
Cohesion: 0.15
Nodes (12): Check it works, Installation, Installing from source, Pick your extra, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+4 more)

### Community 89 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 90 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 91 - "confusion_metrics"
Cohesion: 0.18
Nodes (5): confusion_metrics(), run_auto_validate(), _metrics(), run_raha(), _metrics()

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "uni_detect/text_utils.py"
Cohesion: 0.17
Nodes (4): is_integer_like(), is_mixed_alphanumeric(), TestIntegerLike, TestMixedAlphanumeric

### Community 95 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 96 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.21
Nodes (4): _date_index(), _date_values(), TestCoarseSignature, TestLargeGroups

### Community 97 - "algorithms.md"
Cohesion: 0.50
Nodes (3): Registry, Registry and results, Result types

### Community 98 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 99 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 101 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 102 - "hierarchy.py"
Cohesion: 0.27
Nodes (6): _append_literal(), _char_class(), _class_of_token(), _is_numeric(), _parse(), _part_matches()

### Community 103 - "OpenDetectError"
Cohesion: 0.19
Nodes (8): Errors, IndexNotBuiltError, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error(), test_open_detect_error_is_catchable_broadly(), test_relocated_exceptions_importable_from_every_path()

### Community 104 - "matches"
Cohesion: 0.31
Nodes (3): _conforms(), matches(), TestMatching

### Community 105 - "_segment_dp"
Cohesion: 0.28
Nodes (3): _segment_dp(), TestSegmentDp, solve()

### Community 107 - "sorted_patterns"
Cohesion: 0.25
Nodes (3): any_pattern(), matching_pattern(), sorted_patterns()

### Community 109 - "get_spec"
Cohesion: 0.15
Nodes (7): _require_min_rows(), all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 110 - "logging_utils.py"
Cohesion: 0.13
Nodes (6): configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 112 - "test_corpus_and_detectors.py"
Cohesion: 0.33
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 116 - "UnknownAlgorithmError"
Cohesion: 0.33
Nodes (5): Concepts, Configuration objects, One contract: `detect()`, The registry, UnknownAlgorithmError

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 647 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **32 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `test_auto_validate_fmdv_v.py`, `dataset_utils.py`, `AutoValidateAlgorithm`, `PatternIndex`, `_segment_dp`, `fmdv_v`, `collections_abc`, `InferredPattern`, `RahaConfig`, `UnknownAlgorithmError`, `fmdv`, `confusion_metrics`, `ConfigurationError`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.053923541247484906 - nodes in this community are weakly interconnected._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `verify_build_config`, `algorithms/__init__.py`, `real_world_gov/run_benchmark.py`, `FailureCounts`, `CorpusStatsBuilder`, `RahaConfig`, `test_metrics.py`, `test_hygiene.py`, `require_min_size`, `ConfigurationError`, `UniDetect`, `pandas`, `dataset_utils.py`, `CHANGELOG`, `UniDetectAlgorithm`, `featurization.py`, `config`, `builder.py`, `docs/index.md`, `ErrorType`, `UnityCatalogLocation`, `TestConfigThreshold`, `.detect`, `test_corpus_and_detectors.py`, `UnknownAlgorithmError`, `.__init__`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Are the 37 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 37 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._