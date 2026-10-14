# Graph Report - open-detect  (2026-10-14)

## Corpus Check
- 150 files · ~119,217 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1638 nodes · 3962 edges · 86 communities (69 shown, 17 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 530 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6bc2c9af`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- real_world_gov/generate_report.py
- UnityCatalogLocation
- registry.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- UniDetectConfig
- CorpusIngestor
- FailureCounts
- wiki_subset/generate_report.py
- metrics/spelling.py
- algorithms/__init__.py
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- list_tables_matching
- ColumnDataType
- Commit conventions and releases
- patterns.py
- Running on Databricks
- ErrorType
- drop_nulls
- infer_column_data_type
- builder.py
- Uni-Detect
- main
- metrics/functional_dependency.py
- AlgorithmResult
- numpy
- raha/strategies.py
- auto_validate/detector.py
- FeatureBucket
- spark_session.py
- AutoValidateAlgorithm
- API reference
- hierarchy.py
- CallableLabeler
- real_world_gov benchmark results
- _is_null
- wiki_subset/run_benchmark.py
- features.py
- `raha`
- RahaDetector
- open_detect/__init__.py
- featurization.py
- concepts.md
- .detect
- .detect
- choosing-an-algorithm.md
- parse_args
- fmdv
- InsufficientDataError
- raha/detector.py
- pipeline.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- UniDetect
- algorithms/uni-detect.md
- ConfigurationError
- Raha
- Comparing algorithms
- CorpusStatsStore
- main
- reference/index.md
- get_algorithm
- Benchmark: real_world_gov
- Auto-Validate
- _StubDetector
- Uni-Detect
- perturb_numeric_outlier
- TestConfigThreshold
- CHANGELOG
- `auto_validate`
- CorpusStatsBuilder
- parse_args
- pandas
- Registry and results
- __getattr__
- open-detect

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 105 edges
2. `ErrorType` - 70 edges
3. `UniDetectConfig` - 64 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 39 edges
6. `UniDetect` - 37 edges
7. `AutoValidateAlgorithm` - 36 edges
8. `RahaConfig` - 33 edges
9. `PatternIndex` - 31 edges
10. `UnityCatalogLocation` - 30 edges

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

## Communities (86 total, 17 thin omitted)

### Community 0 - "real_world_gov/generate_report.py"
Cohesion: 0.21
Nodes (11): comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name() (+3 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.18
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config(), config()

### Community 2 - "registry.py"
Cohesion: 0.16
Nodes (9): get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), UnknownAlgorithmError, test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name() (+1 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.15
Nodes (11): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), _register_table() (+3 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.15
Nodes (8): _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbSpelling, TestPerturbUniqueness

### Community 8 - "UniDetectConfig"
Cohesion: 0.24
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 9 - "CorpusIngestor"
Cohesion: 0.16
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 10 - "FailureCounts"
Cohesion: 0.05
Nodes (22): Configuration, _coerce_numeric(), compute(), compute(), _score_fd_pair(), _score_single_column(), compute(), compute() (+14 more)

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.17
Nodes (15): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct() (+7 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.15
Nodes (6): _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, TestSpelling

### Community 13 - "algorithms/__init__.py"
Cohesion: 0.27
Nodes (5): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), UniDetectAlgorithm

### Community 14 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (12): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _build_index(), TestFmdvV, TestFmdvVh, _time_corpus() (+4 more)

### Community 16 - "check_drift"
Cohesion: 0.14
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 19 - "ColumnDataType"
Cohesion: 0.14
Nodes (7): all_specs(), ErrorTypeSpec, get_spec(), ColumnDataType, ComparisonDirection, TestAllSpecs, TestGetSpec

### Community 20 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 21 - "patterns.py"
Cohesion: 0.06
Nodes (17): generality_weight(), generalize(), Token, token_count(), tokenize(), _alternatives(), any_pattern(), _best_first_patterns() (+9 more)

### Community 22 - "Running on Databricks"
Cohesion: 0.40
Nodes (4): Job arguments, Jobs, Notebooks, Running on Databricks

### Community 23 - "ErrorType"
Cohesion: 0.15
Nodes (8): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, ErrorType

### Community 24 - "drop_nulls"
Cohesion: 0.16
Nodes (4): drop_nulls(), duplicate_value_indices(), TestDropNulls, TestDuplicateValueIndices

### Community 25 - "infer_column_data_type"
Cohesion: 0.06
Nodes (14): log_transform_fits_better(), token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference (+6 more)

### Community 26 - "builder.py"
Cohesion: 0.11
Nodes (4): get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 27 - "Uni-Detect"
Cohesion: 0.29
Nodes (7): A fully local example, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks

### Community 29 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 30 - "AlgorithmResult"
Cohesion: 0.16
Nodes (7): Through the registry, The shared result schema, Combine, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult

### Community 31 - "numpy"
Cohesion: 0.14
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (16): Variants, IndexNotBuiltError, _clean(), fmdv_h(), InferredPattern, _coarse_class(), _coarse_signature(), _fmdv_h_single() (+8 more)

### Community 35 - "FeatureBucket"
Cohesion: 0.10
Nodes (11): Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, TestCandidate, TestCorpusRecords (+3 more)

### Community 36 - "spark_session.py"
Cohesion: 0.11
Nodes (8): spark_session(), candidates(), main(), select(), _delta_jars(), _download(), spark(), uc_location()

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.07
Nodes (20): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+12 more)

### Community 38 - "API reference"
Cohesion: 0.20
Nodes (9): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference, list_algorithms() (+1 more)

### Community 39 - "hierarchy.py"
Cohesion: 0.14
Nodes (9): _append_literal(), _char_class(), _class_of_token(), _is_numeric(), _iter_runs(), matches(), _parse(), _part_matches() (+1 more)

### Community 40 - "CallableLabeler"
Cohesion: 0.10
Nodes (13): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust (+5 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "_is_null"
Cohesion: 0.22
Nodes (5): _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 43 - "wiki_subset/run_benchmark.py"
Cohesion: 0.10
Nodes (15): confusion_metrics(), git_commit(), SparkUnavailable, main(), _build_config(), _load_corpus_tables(), _load_targets(), main() (+7 more)

### Community 44 - "features.py"
Cohesion: 0.23
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "RahaDetector"
Cohesion: 0.13
Nodes (10): run_raha(), Scoring raha, main(), RahaDetector, GroundTruthLabeler, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema() (+2 more)

### Community 47 - "open_detect/__init__.py"
Cohesion: 0.22
Nodes (3): __getattr__(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 48 - "featurization.py"
Cohesion: 0.09
Nodes (15): _score_pair(), _score_column(), _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length() (+7 more)

### Community 52 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "choosing-an-algorithm.md"
Cohesion: 0.18
Nodes (8): Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 54 - "parse_args"
Cohesion: 0.14
Nodes (3): parse_args(), TestParseArgs, TestGetSpark

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "InsufficientDataError"
Cohesion: 0.31
Nodes (3): uniqueness_ratio(), InsufficientDataError, TestUniquenessRatio

### Community 57 - "raha/detector.py"
Cohesion: 0.20
Nodes (5): Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, Labeler, TestHeuristicLabeler

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 61 - "UniDetect"
Cohesion: 0.18
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 62 - "algorithms/uni-detect.md"
Cohesion: 0.26
Nodes (4): Algorithms, Fidelity to the papers, open-detect, What is in the box

### Community 63 - "ConfigurationError"
Cohesion: 0.13
Nodes (10): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, ConfigurationError, OpenDetectError, test_all_errors_derive_from_open_detect_error() (+2 more)

### Community 64 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 65 - "Comparing algorithms"
Cohesion: 0.40
Nodes (5): Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 66 - "CorpusStatsStore"
Cohesion: 0.15
Nodes (5): Practical advice, CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "reference/index.md"
Cohesion: 0.25
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 69 - "get_algorithm"
Cohesion: 0.20
Nodes (7): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.17
Nodes (10): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark, Which 5 datasets, and why (+2 more)

### Community 71 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 77 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 82 - "pandas"
Cohesion: 0.08
Nodes (8): clean_column(), indexable_values(), _is_null(), _iter_corpus_columns(), fpr_column(), impurity(), TestCleanColumn, TestIndexableValues

### Community 83 - "Registry and results"
Cohesion: 0.67
Nodes (3): Registry, Registry and results, Result types

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 516 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `real_world_gov/run_benchmark.py`, `FailureCounts`, `algorithms/__init__.py`, `ColumnDataType`, `builder.py`, `Uni-Detect`, `main`, `FeatureBucket`, `API reference`, `wiki_subset/run_benchmark.py`, `open_detect/__init__.py`, `featurization.py`, `.detect`, `parse_args`, `pipeline.py`, `UniDetect`, `CorpusStatsStore`, `main`, `_StubDetector`, `CorpusStatsBuilder`, `parse_args`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `real_world_gov/run_benchmark.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14855072463768115 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `auto_validate/detector.py`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `API reference`, `_is_null`, `wiki_subset/run_benchmark.py`, `check_drift`, `pandas`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 42 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._