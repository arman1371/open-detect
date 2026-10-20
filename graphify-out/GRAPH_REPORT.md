# Graph Report - open-detect  (2026-10-20)

## Corpus Check
- 158 files · ~131,230 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 2001 nodes · 4871 edges · 94 communities (77 shown, 17 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 622 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `856255b4`
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
- auto_validate/detector.py
- UniDetect
- FailureCounts
- numpy
- CorpusIngestor
- test_auto_validate_fmdv_v.py
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- fd_violation_strategies
- _require_columns
- index.py
- patterns.py
- real_world_gov/generate_report.py
- get_spec
- test_metrics.py
- pipeline.py
- list_tables_matching
- perturb_numeric_outlier
- ConfigurationError
- parse_args
- AlgorithmResult
- .detect
- gaussian_outlier_strategies
- main
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- reference/index.md
- pandas
- perturb_spelling
- real_world_gov benchmark results
- spark_session.py
- list_algorithms
- featurization.py
- `auto_validate`
- metrics/spelling.py
- InsufficientDataError
- test_algorithms_registry.py
- CHANGELOG
- Raha
- propagate_labels
- ErrorDetectionAlgorithm
- diff_fingerprints
- Benchmark: real_world_gov
- _build_index
- argparse
- raha/detector.py
- CellResult
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _score_single_column
- algorithms/index.md
- algorithms/uni-detect.md
- select_fd_column_pairs
- test_corpus_ingestion.py
- docs/index.md
- CorpusStatsStore
- .detect
- collections_abc
- Uni-Detect
- Auto-Validate
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- Current Status: BLOCKED
- clean_column
- wiki_subset/generate_report.py
- open_detect/__init__.py
- open-detect
- get_algorithm
- HeuristicLabeler
- Current Status: BLOCKED
- infer_column_data_type
- TestConfigThreshold
- algorithms.md
- OpenDetectError
- uniqueness_ratio
- `uni_detect`
- ErrorType
- logging_utils.py

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
- `Operational notes` --references--> `CorpusNotFoundError`  [INFERRED]
  docs/algorithms/uni-detect.md → src/open_detect/exceptions.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (94 total, 17 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.15
Nodes (10): property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, TestLegacyCorpus, TestMismatch (+2 more)

### Community 2 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.13
Nodes (12): confusion_metrics(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_auto_validate() (+4 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.11
Nodes (10): _score_pair(), _score_column(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices (+2 more)

### Community 8 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (15): Variants, _clean(), fmdv(), fmdv_h(), InferredPattern, _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+7 more)

### Community 9 - "UniDetect"
Cohesion: 0.24
Nodes (7): build_spark(), main(), _run(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.06
Nodes (20): Configuration, compute(), compute(), _score_fd_pair(), compute(), compute(), compute(), compute() (+12 more)

### Community 11 - "numpy"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 12 - "CorpusIngestor"
Cohesion: 0.14
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 13 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.09
Nodes (10): min_conforming(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV, TestFmdvVh, TestLargeGroups (+2 more)

### Community 14 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "check_drift"
Cohesion: 0.09
Nodes (8): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.11
Nodes (13): API reference, ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, RahaDetector, _features(), TestClassifierTrainingPath (+5 more)

### Community 18 - "fd_violation_strategies"
Cohesion: 0.18
Nodes (4): fd_violation_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls, TestFdViolationStrategies

### Community 20 - "index.py"
Cohesion: 0.06
Nodes (17): _append_literal(), _char_class(), _class_of_token(), _is_numeric(), _iter_runs(), matches(), _parse(), _part_matches() (+9 more)

### Community 21 - "patterns.py"
Cohesion: 0.07
Nodes (14): generality_weight(), generalize(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns() (+6 more)

### Community 22 - "real_world_gov/generate_report.py"
Cohesion: 0.29
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 23 - "get_spec"
Cohesion: 0.14
Nodes (3): get_spec(), TestScoreFdPair, TestGetSpec

### Community 24 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 25 - "pipeline.py"
Cohesion: 0.08
Nodes (3): get_spark(), configure_logging(), TestGetSpark

### Community 26 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ConfigurationError"
Cohesion: 0.17
Nodes (5): _validate_edges(), main(), ConfigurationError, test_main_installs_logging(), TestMain

### Community 30 - "AlgorithmResult"
Cohesion: 0.12
Nodes (10): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Combine, AlgorithmResult, _good_plugin_class() (+2 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.10
Nodes (10): _factorize_column(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies, TestNullSentinel (+2 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.11
Nodes (15): git_commit(), canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames() (+7 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (26): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+18 more)

### Community 39 - "pandas"
Cohesion: 0.14
Nodes (9): main(), build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features() (+1 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "spark_session.py"
Cohesion: 0.09
Nodes (11): spark_session(), SparkUnavailable, A fully local example, How it works, Install, Operational notes, Uni-Detect, _delta_jars() (+3 more)

### Community 43 - "list_algorithms"
Cohesion: 0.13
Nodes (9): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, list_algorithms(), test_builtin_algorithms_are_registered() (+1 more)

### Community 44 - "featurization.py"
Cohesion: 0.11
Nodes (12): _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+4 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity (target-level), By error type (cell-level), By error type (cell-level), By error type (target-level), By error type (target-level) (+4 more)

### Community 46 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 47 - "InsufficientDataError"
Cohesion: 0.15
Nodes (6): fd_compliance_ratio(), FDResult, minority_violation_rows(), InsufficientDataError, ValidationError, TestFunctionalDependency

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (7): _FakeEntryPoint, fresh_registry(), real_plugin_path(), test_unknown_algorithm_raises(), TestPluginDiscovery, worker(), _write_distinfo_plugin()

### Community 49 - "CHANGELOG"
Cohesion: 0.10
Nodes (20): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG (+12 more)

### Community 50 - "Raha"
Cohesion: 0.40
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.12
Nodes (14): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm_class(), _load_entry_points(), register_algorithm() (+6 more)

### Community 54 - "Benchmark: real_world_gov"
Cohesion: 0.17
Nodes (10): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark, Which 5 datasets, and why (+2 more)

### Community 55 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "raha/detector.py"
Cohesion: 0.07
Nodes (17): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+9 more)

### Community 58 - "CellResult"
Cohesion: 0.14
Nodes (8): Reading the detections, Through the registry, Usage on Databricks, open-detect, What is in the box, Why a common interface, CellResult, TestCellResultEvidence

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.33
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 61 - "_score_single_column"
Cohesion: 0.10
Nodes (12): Reading the output, The shared result schema, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table, _coerce_numeric() (+4 more)

### Community 63 - "algorithms/uni-detect.md"
Cohesion: 0.33
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 66 - "docs/index.md"
Cohesion: 0.23
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 67 - "CorpusStatsStore"
Cohesion: 0.14
Nodes (4): CorpusStatsStore, config(), TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 71 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 72 - "collections_abc"
Cohesion: 0.10
Nodes (10): BaseDetector, _hash_value(), make_evidence_json(), redact_evidence(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector (+2 more)

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "wiki_subset/generate_report.py"
Cohesion: 0.15
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 84 - "open_detect/__init__.py"
Cohesion: 0.06
Nodes (20): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, __getattr__() (+12 more)

### Community 88 - "get_algorithm"
Cohesion: 0.20
Nodes (7): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 90 - "HeuristicLabeler"
Cohesion: 0.18
Nodes (11): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions? (+3 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 93 - "infer_column_data_type"
Cohesion: 0.06
Nodes (14): log_transform_fits_better(), token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference (+6 more)

### Community 97 - "algorithms.md"
Cohesion: 0.50
Nodes (3): Registry, Registry and results, Result types

### Community 103 - "OpenDetectError"
Cohesion: 0.09
Nodes (19): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Job arguments, Jobs, Notebooks (+11 more)

### Community 108 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 109 - "ErrorType"
Cohesion: 0.11
Nodes (8): _require_min_rows(), all_specs(), ErrorTypeSpec, ComparisonDirection, ErrorType, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug(), TestAllSpecs

### Community 110 - "logging_utils.py"
Cohesion: 0.12
Nodes (5): get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 625 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `wiki_subset/run_benchmark.py`, `UniDetect`, `FailureCounts`, `RahaConfig`, `get_spec`, `pipeline.py`, `ConfigurationError`, `parse_args`, `main`, `real_world_gov/run_benchmark.py`, `spark_session.py`, `featurization.py`, `ErrorDetectionAlgorithm`, `_score_single_column`, `CorpusStatsStore`, `.detect`, `collections_abc`, `CorpusStatsBuilder`, `open_detect/__init__.py`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.14838709677419354 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `wiki_subset/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `OpenDetectError`, `auto_validate/detector.py`, `test_auto_validate_fmdv_v.py`, `check_drift`, `RahaConfig`, `index.py`, `_build_index`, `ConfigurationError`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._