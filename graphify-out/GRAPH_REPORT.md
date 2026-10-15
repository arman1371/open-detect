# Graph Report - ope74-wt  (2026-10-15)

## Corpus Check
- 153 files · ~122,272 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 242 file(s) not represented in the graph (top: .csv 226, .j2 10, (none) 3)

## Summary
- 1808 nodes · 4421 edges · 87 communities (70 shown, 17 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 572 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f15a48e8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- registry.py
- wiki_subset/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- CorpusStatsStore
- UniDetect
- FailureCounts
- real_world_gov/generate_report.py
- list_tables_matching
- fmdv_v
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- tokenize
- open_detect/__init__.py
- PatternIndex
- patterns.py
- wiki_subset/generate_report.py
- ErrorType
- test_metrics.py
- get_spec
- get_logger
- perturb_numeric_outlier
- hierarchy.py
- AlgorithmResult
- cluster_column
- gaussian_outlier_strategies
- build_column_features
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- API reference
- ConfigurationError
- perturb_spelling
- real_world_gov benchmark results
- spark_session.py
- Uni-Detect
- featurization.py
- `raha`
- spark_session
- metrics/functional_dependency.py
- _score_single_column
- CHANGELOG
- is_integer_like
- .detect
- algorithm.py
- algorithms/uni-detect.md
- FeatureBucket
- fmdv
- argparse
- labeling.py
- build_corpus_statistics.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- algorithms/index.md
- OpenDetectError
- select_fd_column_pairs
- score
- Running on Databricks
- algorithms/raha.md
- choosing-an-algorithm.md
- Benchmark: real_world_gov
- ColumnDataType
- uniqueness_ratio
- reference/index.md
- Raha
- Auto-Validate
- infer_column_data_type
- Commit conventions and releases
- `auto_validate`
- UnityCatalogLocation
- pandas
- raha/detector.py
- open-detect
- log_transform_fits_better
- TestConfigThreshold
- numpy

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 114 edges
2. `ErrorType` - 84 edges
3. `UniDetectConfig` - 74 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 44 edges
6. `UniDetect` - 37 edges
7. `AutoValidateAlgorithm` - 36 edges
8. `RahaConfig` - 33 edges
9. `PatternIndex` - 32 edges
10. `UnityCatalogLocation` - 31 edges

## Surprising Connections (you probably didn't know these)
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `The registry` --references--> `UnknownAlgorithmError`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/registry.py
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/open_detect/algorithms/uni_detect/pipeline.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (87 total, 17 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.11
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.16
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 2 - "registry.py"
Cohesion: 0.13
Nodes (10): get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), test_builtin_algorithms_are_registered(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy() (+2 more)

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
Cohesion: 0.10
Nodes (11): _score_pair(), _score_column(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, _resolve_row_ids() (+3 more)

### Community 8 - "CorpusStatsStore"
Cohesion: 0.12
Nodes (6): Errors, Practical advice, CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 9 - "UniDetect"
Cohesion: 0.05
Nodes (21): build_spark(), main(), CorpusStatsBuilder, _stats_schema_without_error_type(), CorpusIngestor, main(), parse_args(), UniDetect (+13 more)

### Community 10 - "FailureCounts"
Cohesion: 0.06
Nodes (20): Configuration, compute(), compute(), _score_fd_pair(), compute(), compute(), compute(), compute() (+12 more)

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.20
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 12 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 13 - "fmdv_v"
Cohesion: 0.07
Nodes (13): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), _date_index(), _date_values(), TestCoarseSignature (+5 more)

### Community 14 - "outliers.py"
Cohesion: 0.11
Nodes (11): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+3 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.10
Nodes (8): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "check_drift"
Cohesion: 0.13
Nodes (4): check_drift(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.24
Nodes (6): ColumnPredictions, train_and_predict(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 19 - "open_detect/__init__.py"
Cohesion: 0.15
Nodes (7): Candidate, MetricObservation, __getattr__(), TestCandidate, TestMetricObservation, test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 20 - "PatternIndex"
Cohesion: 0.08
Nodes (14): _clean(), fmdv_h(), InferredPattern, min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), _infer_cmp(), _segment_dp() (+6 more)

### Community 21 - "patterns.py"
Cohesion: 0.07
Nodes (15): generality_weight(), generalize(), Token, token_count(), tokenize(), _alternatives(), any_pattern(), _best_first_patterns() (+7 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 23 - "ErrorType"
Cohesion: 0.14
Nodes (12): BaseDetector, make_evidence_json(), _candidate_row(), FunctionalDependencyDetector, _candidate_row(), NumericOutlierDetector, _candidate_row(), SpellingDetector (+4 more)

### Community 24 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 25 - "get_spec"
Cohesion: 0.09
Nodes (8): _require_min_rows(), all_specs(), ErrorTypeSpec, get_spec(), ComparisonDirection, TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 26 - "get_logger"
Cohesion: 0.12
Nodes (5): get_logger(), log_duration(), pair_table(), TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "hierarchy.py"
Cohesion: 0.09
Nodes (14): _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), _append_literal(), _char_class(), _class_of_token(), _is_numeric() (+6 more)

### Community 30 - "AlgorithmResult"
Cohesion: 0.12
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Reading results, Uni-Detect: score tables in Unity Catalog, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.14
Nodes (6): gaussian_outlier_strategies(), histogram_outlier_strategies(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies, TestPatternCharacterStrategies

### Community 34 - "build_column_features"
Cohesion: 0.25
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.13
Nodes (7): _blocking_keys(), _closest_pair(), differing_token_lengths(), min_pairwise_edit_distance(), _result(), MPDResult, TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): git_commit(), dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main(), _print_comparison() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.06
Nodes (22): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+14 more)

### Community 38 - "API reference"
Cohesion: 0.19
Nodes (11): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+3 more)

### Community 40 - "perturb_spelling"
Cohesion: 0.29
Nodes (3): _score_column(), perturb_spelling(), TestPerturbSpelling

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "spark_session.py"
Cohesion: 0.13
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "Uni-Detect"
Cohesion: 0.29
Nodes (7): A fully local example, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks

### Community 44 - "featurization.py"
Cohesion: 0.12
Nodes (11): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 47 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 49 - "CHANGELOG"
Cohesion: 0.13
Nodes (14): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring, Unreleased (+6 more)

### Community 52 - "algorithm.py"
Cohesion: 0.18
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "algorithms/uni-detect.md"
Cohesion: 0.31
Nodes (5): open-detect, What is in the box, Registry, Registry and results, Result types

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "labeling.py"
Cohesion: 0.08
Nodes (17): Scoring raha, Raha: find errors with a few labels, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class (+9 more)

### Community 58 - "build_corpus_statistics.py"
Cohesion: 0.12
Nodes (6): main(), parse_args(), get_spark(), TestMain, TestParseArgs, TestGetSpark

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 63 - "OpenDetectError"
Cohesion: 0.21
Nodes (6): Errors, UnknownAlgorithmError, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_open_detect_error_is_catchable_broadly()

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "score"
Cohesion: 0.15
Nodes (13): Through the registry, Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema, Combine, Comparing algorithms (+5 more)

### Community 67 - "Running on Databricks"
Cohesion: 0.40
Nodes (4): Job arguments, Jobs, Notebooks, Running on Databricks

### Community 68 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 69 - "choosing-an-algorithm.md"
Cohesion: 0.14
Nodes (11): Benchmarks, How to read them, Latest results, Running them, Getting started, Installation, Installing from source, Pick your extra (+3 more)

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.13
Nodes (12): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+4 more)

### Community 71 - "ColumnDataType"
Cohesion: 0.16
Nodes (6): ColumnDataType, CorpusColumnRecord, CorpusPairRecord, Detection, TestCorpusRecords, TestDetection

### Community 73 - "reference/index.md"
Cohesion: 0.22
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 76 - "infer_column_data_type"
Cohesion: 0.12
Nodes (6): infer_column_data_type(), is_float_like(), is_mixed_alphanumeric(), TestDataTypeInference, TestFloatLike, TestMixedAlphanumeric

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.18
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config(), config()

### Community 84 - "pandas"
Cohesion: 0.07
Nodes (13): _feasible_evidence(), _infeasible_evidence(), _is_null(), _value_matches(), IndexNotBuiltError, clean_column(), indexable_values(), _is_null() (+5 more)

### Community 86 - "raha/detector.py"
Cohesion: 0.17
Nodes (9): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema() (+1 more)

### Community 98 - "numpy"
Cohesion: 0.13
Nodes (3): _default_classifier_factory(), fd_violation_strategies(), TestFdViolationStrategies

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 561 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `wiki_subset/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `API reference`, `ColumnDataType`, `CorpusStatsStore`, `UniDetect`, `FailureCounts`, `Uni-Detect`, `featurization.py`, `_score_single_column`, `open_detect/__init__.py`, `algorithm.py`, `FeatureBucket`, `get_spec`, `build_corpus_statistics.py`, `builder.py`?**
  _High betweenness centrality (0.152) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11095305832147938 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `score`, `wiki_subset/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `API reference`, `ConfigurationError`, `fmdv_v`, `check_drift`, `pandas`, `PatternIndex`, `fmdv`, `hierarchy.py`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 53 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._