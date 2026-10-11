# Graph Report - open-detect-f922b0c61f86  (2026-10-11)

## Corpus Check
- 147 files · ~113,981 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 241 file(s) not represented in the graph (top: .csv 226, .j2 10, (none) 2)

## Summary
- 1531 nodes · 3616 edges · 83 communities (69 shown, 14 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 436 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `72a1a8f5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _is_null
- UniDetectConfig
- registry.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- pytest
- CorpusIngestor
- _score_single_column
- wiki_subset/generate_report.py
- metrics/spelling.py
- UniDetect
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- list_tables_matching
- ErrorType
- builder.py
- patterns.py
- .build_corpus_statistics
- collections_abc
- PatternIndex
- infer_column_data_type
- test_auto_validate_fmdv_v.py
- Uni-Detect
- build_corpus_statistics.py
- metrics/functional_dependency.py
- AlgorithmResult
- .detect
- raha/strategies.py
- auto_validate/detector.py
- ColumnDataType
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- HeuristicLabeler
- run_detection.py
- raha/detector.py
- real_world_gov benchmark results
- json
- argparse
- pandas
- `auto_validate`
- GroundTruthLabeler
- Benchmark: real_world_gov
- featurization.py
- clean_column
- Commit conventions and releases
- propagate_labels
- algorithms/__init__.py
- choosing-an-algorithm.md
- main
- fmdv
- test_metrics.py
- FeatureBucket
- pipeline.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- UnityCatalogLocation
- algorithms/uni-detect.md
- OpenDetectError
- Raha
- concepts.md
- CorpusStatsStore
- log_transform_fits_better
- reference/index.md
- Benchmarks
- Detection
- Auto-Validate
- Methodology: auto_validate
- Uni-Detect
- Scoring auto_validate
- `raha`
- CHANGELOG
- duplicate_value_indices
- main
- Registry and results
- indexable_values
- open-detect

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 105 edges
2. `ErrorType` - 68 edges
3. `UniDetectConfig` - 49 edges
4. `build_pattern_index()` - 39 edges
5. `UniDetect` - 37 edges
6. `AutoValidateAlgorithm` - 36 edges
7. `RahaConfig` - 33 edges
8. `PatternIndex` - 31 edges
9. `AlgorithmResult` - 29 edges
10. `UnityCatalogLocation` - 27 edges

## Surprising Connections (you probably didn't know these)
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `Configuration` --references--> `UniDetectConfig`  [INFERRED]
  docs/algorithms/uni-detect.md → src/open_detect/algorithms/uni_detect/config.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (83 total, 14 thin omitted)

### Community 0 - "_is_null"
Cohesion: 0.22
Nodes (5): _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 1 - "UniDetectConfig"
Cohesion: 0.15
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 2 - "registry.py"
Cohesion: 0.10
Nodes (18): Check it works, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, get_algorithm(), get_algorithm_class() (+10 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.15
Nodes (8): _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbSpelling, TestPerturbUniqueness

### Community 8 - "pytest"
Cohesion: 0.14
Nodes (6): config(), test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_open_detect_error_is_catchable_broadly(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 9 - "CorpusIngestor"
Cohesion: 0.18
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 10 - "_score_single_column"
Cohesion: 0.16
Nodes (7): _coerce_numeric(), compute(), _score_single_column(), perturb_numeric_outlier(), TestCoerceNumeric, TestScoreSingleColumn, TestPerturbNumericOutlier

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.14
Nodes (7): MADResult, _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, TestSpelling

### Community 13 - "UniDetect"
Cohesion: 0.26
Nodes (4): UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 14 - "outliers.py"
Cohesion: 0.14
Nodes (9): drop_nulls(), require_min_size(), mad_scores(), max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), InsufficientDataError (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (9): AutoValidateConfig, build_pattern_index(), _iter_corpus_columns(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex (+1 more)

### Community 16 - "check_drift"
Cohesion: 0.15
Nodes (5): check_drift(), _clean_series(), _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.14
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 19 - "ErrorType"
Cohesion: 0.16
Nodes (7): all_specs(), ErrorTypeSpec, get_spec(), ComparisonDirection, ErrorType, TestAllSpecs, TestGetSpec

### Community 20 - "builder.py"
Cohesion: 0.13
Nodes (4): get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 21 - "patterns.py"
Cohesion: 0.06
Nodes (20): _char_class(), _class_of_token(), generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize() (+12 more)

### Community 22 - ".build_corpus_statistics"
Cohesion: 0.25
Nodes (4): CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType

### Community 23 - "collections_abc"
Cohesion: 0.09
Nodes (10): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, compute(), NumericOutlierDetector, compute(), SpellingDetector, compute() (+2 more)

### Community 24 - "PatternIndex"
Cohesion: 0.10
Nodes (12): InferredPattern, _coarse_class(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_v(), fmdv_vh(), _infer_cmp() (+4 more)

### Community 25 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 26 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.21
Nodes (4): _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 27 - "Uni-Detect"
Cohesion: 0.29
Nodes (7): A fully local example, Configuration, How it works, Install, Reading the detections, Uni-Detect, Usage on Databricks

### Community 28 - "build_corpus_statistics.py"
Cohesion: 0.20
Nodes (4): main(), parse_args(), TestMain, TestParseArgs

### Community 29 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 30 - "AlgorithmResult"
Cohesion: 0.12
Nodes (9): Through the registry, The shared result schema, Combine, 1. Implement `ErrorDetectionAlgorithm`, Why a common interface, API reference, AlgorithmResult, CellResult (+1 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "auto_validate/detector.py"
Cohesion: 0.09
Nodes (9): DriftResult, _append_literal(), _is_numeric(), matches(), _parse(), _part_matches(), fpr_column(), impurity() (+1 more)

### Community 35 - "ColumnDataType"
Cohesion: 0.16
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.09
Nodes (14): git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.12
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "HeuristicLabeler"
Cohesion: 0.23
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 40 - "raha/detector.py"
Cohesion: 0.11
Nodes (9): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, Labeler (+1 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "json"
Cohesion: 0.18
Nodes (5): confusion_metrics(), run_auto_validate(), _metrics(), run_raha(), _metrics()

### Community 43 - "argparse"
Cohesion: 0.52
Nodes (3): candidates(), main(), select()

### Community 44 - "pandas"
Cohesion: 0.18
Nodes (7): main(), build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 45 - "`auto_validate`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.22
Nodes (7): GroundTruthLabeler, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler(), TestGroundTruthLabeler

### Community 47 - "Benchmark: real_world_gov"
Cohesion: 0.17
Nodes (10): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark, Which 5 datasets, and why (+2 more)

### Community 48 - "featurization.py"
Cohesion: 0.11
Nodes (11): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 49 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 50 - "Commit conventions and releases"
Cohesion: 0.14
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 52 - "algorithms/__init__.py"
Cohesion: 0.12
Nodes (10): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, UniDetectAlgorithm, __getattr__(), _config() (+2 more)

### Community 53 - "choosing-an-algorithm.md"
Cohesion: 0.20
Nodes (7): Getting started, Installation, Installing from source, Pick your extra, At a glance, Choosing an algorithm, Rules of thumb

### Community 54 - "main"
Cohesion: 0.27
Nodes (4): main(), parse_args(), TestMain, TestParseArgs

### Community 55 - "fmdv"
Cohesion: 0.11
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "test_metrics.py"
Cohesion: 0.21
Nodes (3): uniqueness_ratio(), TestDropNulls, TestUniquenessRatio

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.20
Nodes (10): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, Scoring raha, The corpus (`data/corpus/`) (+2 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 61 - "UnityCatalogLocation"
Cohesion: 0.16
Nodes (6): ensure_schema_exists(), UnityCatalogLocation, ConfigurationError, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation

### Community 62 - "algorithms/uni-detect.md"
Cohesion: 0.26
Nodes (4): Algorithms, Fidelity to the papers, open-detect, What is in the box

### Community 63 - "OpenDetectError"
Cohesion: 0.09
Nodes (18): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+10 more)

### Community 64 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 65 - "concepts.md"
Cohesion: 0.29
Nodes (5): Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 66 - "CorpusStatsStore"
Cohesion: 0.11
Nodes (10): Operational notes, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, CorpusStatsStore, CorpusNotFoundError (+2 more)

### Community 68 - "reference/index.md"
Cohesion: 0.22
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 69 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 71 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 72 - "Methodology: auto_validate"
Cohesion: 0.50
Nodes (4): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 75 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 79 - "Registry and results"
Cohesion: 0.67
Nodes (3): Registry, Registry and results, Result types

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 492 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `_is_null`, `auto_validate/detector.py`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `json`, `check_drift`, `fmdv`, `PatternIndex`, `test_auto_validate_fmdv_v.py`, `UnityCatalogLocation`, `AlgorithmResult`, `OpenDetectError`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `UniDetectConfig` be split into smaller, more focused modules?**
  _Cohesion score 0.14666666666666667 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `real_world_gov/run_benchmark.py`, `_score_single_column`, `UniDetect`, `builder.py`, `.build_corpus_statistics`, `collections_abc`, `Uni-Detect`, `build_corpus_statistics.py`, `AlgorithmResult`, `ColumnDataType`, `wiki_subset/run_benchmark.py`, `run_detection.py`, `featurization.py`, `algorithms/__init__.py`, `main`, `FeatureBucket`, `pipeline.py`, `CorpusStatsStore`, `Detection`, `main`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 40 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._