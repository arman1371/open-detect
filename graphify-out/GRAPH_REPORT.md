# Graph Report - open-detect  (2026-10-19)

## Corpus Check
- 158 files · ~130,348 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1970 nodes · 4792 edges · 112 communities (87 shown, 25 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 620 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ff332b5f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- test_spelling_detector.py
- wiki_subset/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- InferredPattern
- UniDetect
- FailureCounts
- check_failure_threshold
- CorpusIngestor
- fmdv_v
- numpy
- AutoValidateConfig
- check_drift
- RahaConfig
- open_detect/__init__.py
- FailureCountsAccumulatorParam
- auto_validate/detector.py
- patterns.py
- real_world_gov/generate_report.py
- get_spec
- test_metrics.py
- open_detect/exceptions.py
- build_corpus_statistics.py
- perturb_numeric_outlier
- ConfigurationError
- ErrorType
- AlgorithmResult
- .detect
- raha/strategies.py
- run_detection.py
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- CallableLabeler
- pandas
- perturb_spelling
- real_world_gov benchmark results
- spark_session.py
- list_algorithms
- featurization.py
- `auto_validate`
- InsufficientDataError
- ValidationError
- test_algorithms_registry.py
- CHANGELOG
- algorithms/raha.md
- propagate_labels
- ErrorDetectionAlgorithm
- Contributing
- Benchmark: real_world_gov
- fmdv
- argparse
- GroundTruthLabeler
- CellResult
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- algorithms/index.md
- Benchmarks
- select_fd_column_pairs
- score
- algorithms/uni-detect.md
- CorpusStatsStore
- make_evidence_json
- test_failures.py
- TestValidation
- .detect
- builder.py
- Uni-Detect
- Raha
- Auto-Validate
- PatternIndex
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- Current Status: BLOCKED
- clean_column
- wiki_subset/generate_report.py
- test_package_init.py
- bucket_by_edges
- tokenize
- open-detect
- get_algorithm
- MetricObservation
- raha/detector.py
- FeatureBucket
- Current Status: BLOCKED
- infer_column_data_type
- TestConfigThreshold
- _score_single_column
- DataQualityError
- reference/index.md
- Running on Databricks
- is_float_like
- main
- is_integer_like
- Choosing an algorithm
- OpenDetectError
- uniqueness_ratio
- Detection
- _date_index
- `uni_detect`
- ErrorTypeSpec
- log_duration
- config

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 115 edges
2. `ErrorType` - 85 edges
3. `UniDetectConfig` - 84 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 45 edges
6. `UnityCatalogLocation` - 39 edges
7. `UniDetect` - 38 edges
8. `AutoValidateAlgorithm` - 36 edges
9. `ConfigurationError` - 36 edges
10. `RahaConfig` - 33 edges

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
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (112 total, 25 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.12
Nodes (13): confusion_metrics(), git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+5 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.12
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 8 - "InferredPattern"
Cohesion: 0.12
Nodes (11): InferredPattern, min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), _infer_cmp(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh() (+3 more)

### Community 9 - "UniDetect"
Cohesion: 0.21
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.15
Nodes (7): compute(), compute(), _score_fd_pair(), compute(), FailureCounts, compute(), TestPerElementFunctions

### Community 12 - "CorpusIngestor"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 13 - "fmdv_v"
Cohesion: 0.10
Nodes (8): _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV, TestFmdvVh, _time_corpus()

### Community 14 - "numpy"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.14
Nodes (7): AutoValidateConfig, build_pattern_index(), TestCorpusInputShapes, TestFprAggregation, TestIndexableValues, TestPatternIndex, TestTauPruning

### Community 16 - "check_drift"
Cohesion: 0.11
Nodes (6): check_drift(), _clean_series(), _fisher_two_tailed(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.13
Nodes (12): API reference, ColumnPredictions, train_and_predict(), RahaConfig, RahaDetector, _features(), TestClassifierTrainingPath, TestDegenerateCases (+4 more)

### Community 18 - "open_detect/__init__.py"
Cohesion: 0.16
Nodes (6): ColumnDataType, ComparisonDirection, CorpusColumnRecord, CorpusPairRecord, __getattr__(), TestCorpusRecords

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (13): _conforms(), DriftResult, _append_literal(), _char_class(), _class_of_token(), _is_numeric(), matches(), _parse() (+5 more)

### Community 21 - "patterns.py"
Cohesion: 0.06
Nodes (18): generality_weight(), generalize(), _iter_runs(), Token, tokenize(), _alternatives(), any_pattern(), _best_first_patterns() (+10 more)

### Community 22 - "real_world_gov/generate_report.py"
Cohesion: 0.16
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main() (+5 more)

### Community 23 - "get_spec"
Cohesion: 0.11
Nodes (7): _require_min_rows(), compute(), compute(), compute(), get_spec(), TestScoreFdPair, TestGetSpec

### Community 24 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 25 - "open_detect/exceptions.py"
Cohesion: 0.09
Nodes (3): _default_classifier_factory(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 26 - "build_corpus_statistics.py"
Cohesion: 0.08
Nodes (11): list_tables(), list_tables_matching(), table_exists(), configure_logging(), get_logger(), TestListTables, TestListTablesMatching, fake_sql() (+3 more)

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.19
Nodes (4): _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 29 - "ErrorType"
Cohesion: 0.27
Nodes (4): parse_args(), _run(), ErrorType, TestParseArgs

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.09
Nodes (10): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies (+2 more)

### Community 34 - "run_detection.py"
Cohesion: 0.12
Nodes (8): main(), parse_args(), get_spark(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs, TestGetSpark

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.16
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (26): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+18 more)

### Community 38 - "CallableLabeler"
Cohesion: 0.13
Nodes (13): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust (+5 more)

### Community 39 - "pandas"
Cohesion: 0.15
Nodes (8): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "spark_session.py"
Cohesion: 0.10
Nodes (6): spark_session(), SparkUnavailable, _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "list_algorithms"
Cohesion: 0.13
Nodes (9): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, list_algorithms(), test_builtin_algorithms_are_registered() (+1 more)

### Community 44 - "featurization.py"
Cohesion: 0.10
Nodes (13): _score_pair(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+5 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity (target-level), By error type (cell-level), By error type (cell-level), By error type (target-level), By error type (target-level) (+4 more)

### Community 46 - "InsufficientDataError"
Cohesion: 0.21
Nodes (8): require_min_size(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance(), InsufficientDataError

### Community 47 - "ValidationError"
Cohesion: 0.18
Nodes (5): fd_compliance_ratio(), FDResult, minority_violation_rows(), ValidationError, TestFunctionalDependency

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (9): _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), real_plugin_path(), test_unknown_algorithm_raises(), TestPluginDiscovery, worker() (+1 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.10
Nodes (20): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+12 more)

### Community 50 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.10
Nodes (15): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm_class(), _load_entry_points(), register_algorithm() (+7 more)

### Community 53 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.17
Nodes (10): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark, Which 5 datasets, and why (+2 more)

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "GroundTruthLabeler"
Cohesion: 0.15
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.33
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "algorithms/index.md"
Cohesion: 0.29
Nodes (3): Algorithms, Fidelity to the papers, Errors

### Community 63 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 65 - "score"
Cohesion: 0.11
Nodes (17): Reading the output, Reading the detections, Through the registry, Usage on Databricks, Concepts, Configuration objects, One contract: `detect()`, The registry (+9 more)

### Community 66 - "algorithms/uni-detect.md"
Cohesion: 0.24
Nodes (4): Getting started, open-detect, What is in the box, Why a common interface

### Community 67 - "CorpusStatsStore"
Cohesion: 0.15
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "make_evidence_json"
Cohesion: 0.29
Nodes (4): _hash_value(), make_evidence_json(), redact_evidence(), TestRedactEvidence

### Community 71 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 72 - "builder.py"
Cohesion: 0.07
Nodes (6): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.20
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.16
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config()

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.24
Nodes (12): comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart() (+4 more)

### Community 84 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 85 - "bucket_by_edges"
Cohesion: 0.23
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 86 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 88 - "get_algorithm"
Cohesion: 0.20
Nodes (7): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 89 - "MetricObservation"
Cohesion: 0.29
Nodes (4): Candidate, MetricObservation, TestCandidate, TestMetricObservation

### Community 90 - "raha/detector.py"
Cohesion: 0.18
Nodes (5): ColumnFeatures, HeuristicLabeler, Labeler, _resolve_position(), TestHeuristicLabeler

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.18
Nodes (4): infer_column_data_type(), is_mixed_alphanumeric(), TestDataTypeInference, TestMixedAlphanumeric

### Community 96 - "DataQualityError"
Cohesion: 0.17
Nodes (9): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, DataQualityError, _StubDetector (+1 more)

### Community 97 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 98 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 100 - "main"
Cohesion: 0.36
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 102 - "Choosing an algorithm"
Cohesion: 0.67
Nodes (3): At a glance, Choosing an algorithm, Rules of thumb

### Community 103 - "OpenDetectError"
Cohesion: 0.16
Nodes (9): Errors, CorpusNotFoundError, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error(), test_open_detect_error_is_catchable_broadly(), test_relocated_exceptions_importable_from_every_path() (+1 more)

### Community 107 - "_date_index"
Cohesion: 0.40
Nodes (3): _date_index(), _date_values(), TestLargeGroups

### Community 108 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 109 - "ErrorTypeSpec"
Cohesion: 0.50
Nodes (3): all_specs(), ErrorTypeSpec, TestAllSpecs

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 624 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UniDetectConfig` connect `UniDetectConfig` to `verify_build_config`, `test_spelling_detector.py`, `wiki_subset/run_benchmark.py`, `UniDetect`, `FailureCounts`, `RahaConfig`, `open_detect/__init__.py`, `open_detect/exceptions.py`, `build_corpus_statistics.py`, `perturb_numeric_outlier`, `ConfigurationError`, `ErrorType`, `run_detection.py`, `real_world_gov/run_benchmark.py`, `featurization.py`, `CHANGELOG`, `ErrorDetectionAlgorithm`, `Benchmark: real_world_gov`, `score`, `CorpusStatsStore`, `.detect`, `builder.py`, `CorpusStatsBuilder`, `UnityCatalogLocation`, `TestConfigThreshold`, `_score_single_column`, `DataQualityError`, `config`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11025641025641025 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `score`, `wiki_subset/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `TestValidation`, `InferredPattern`, `_date_index`, `fmdv_v`, `check_drift`, `RahaConfig`, `auto_validate/detector.py`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._