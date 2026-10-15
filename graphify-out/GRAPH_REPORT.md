# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 153 files · ~122,035 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1727 nodes · 4239 edges · 88 communities (71 shown, 17 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 567 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fedf1921`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- build_metadata.py
- UniDetectConfig
- registry.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- _build_index
- hierarchy.py
- FailureCounts
- real_world_gov/generate_report.py
- check_failure_threshold
- algorithms/__init__.py
- outliers.py
- TestValidation
- check_drift
- RahaConfig
- UnityCatalogLocation
- enums.py
- Commit conventions and releases
- patterns.py
- json
- collections_abc
- test_metrics.py
- infer_column_data_type
- get_logger
- pipeline.py
- FailureCountsAccumulatorParam
- builder.py
- AlgorithmResult
- .detect
- numpy
- auto_validate/detector.py
- min_pairwise_edit_distance
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- API reference
- FeatureBucket
- CallableLabeler
- real_world_gov benchmark results
- conftest.py
- confusion_metrics
- pandas
- `raha`
- RahaDetector
- fd_compliance_ratio
- featurization.py
- ._new_failure_tracker
- algorithms/index.md
- propagate_labels
- .detect
- algorithms/uni-detect.md
- metrics/spelling.py
- AutoValidateConfig
- argparse
- raha/detector.py
- build_corpus_statistics.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- Contributing
- OpenDetectError
- Raha
- Comparing algorithms
- CorpusStatsStore
- TestAttempt
- algorithms/raha.md
- Benchmarks
- Benchmark: real_world_gov
- ErrorType
- uniqueness_ratio
- Uni-Detect
- _StubDetector
- Auto-Validate
- drop_nulls
- `auto_validate`
- UniDetect
- test_failures.py
- Choosing an algorithm
- clean_column
- reference/index.md
- index.py
- quickstart.py
- open-detect

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 105 edges
2. `ErrorType` - 84 edges
3. `UniDetectConfig` - 74 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 39 edges
6. `UniDetect` - 37 edges
7. `AutoValidateAlgorithm` - 36 edges
8. `RahaConfig` - 33 edges
9. `PatternIndex` - 31 edges
10. `UnityCatalogLocation` - 31 edges

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

## Communities (88 total, 17 thin omitted)

### Community 0 - "build_metadata.py"
Cohesion: 0.12
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.05
Nodes (19): Bug Fixes, Bug Fixes, CHANGELOG, Refactoring, Unreleased, v0.2.0 (2026-10-08), v0.2.1 (2026-10-14), v0.2.2 (2026-10-15) (+11 more)

### Community 2 - "registry.py"
Cohesion: 0.18
Nodes (8): get_algorithm_class(), _load_entry_points(), register_lazy(), UnknownAlgorithmError, test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name(), test_unknown_algorithm_raises()

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.15
Nodes (11): dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main(), _print_comparison(), _register_table() (+3 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.10
Nodes (23): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+15 more)

### Community 7 - "perturbation.py"
Cohesion: 0.08
Nodes (14): _score_pair(), _score_column(), _score_column(), _score_column(), _max_drop(), perturb_functional_dependency(), perturb_numeric_outlier(), perturb_spelling() (+6 more)

### Community 8 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 9 - "hierarchy.py"
Cohesion: 0.09
Nodes (14): _append_literal(), _char_class(), _class_of_token(), generalize(), _is_numeric(), _iter_runs(), matches(), _parse() (+6 more)

### Community 10 - "FailureCounts"
Cohesion: 0.20
Nodes (5): compute(), compute(), _score_fd_pair(), FailureCounts, TestPerElementFunctions

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.17
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main() (+5 more)

### Community 12 - "check_failure_threshold"
Cohesion: 0.19
Nodes (4): Configuration, check_failure_threshold(), DataQualityError, TestCheckFailureThreshold

### Community 13 - "algorithms/__init__.py"
Cohesion: 0.21
Nodes (7): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), register_algorithm(), decorator(), UniDetectAlgorithm

### Community 14 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 16 - "check_drift"
Cohesion: 0.13
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "UnityCatalogLocation"
Cohesion: 0.10
Nodes (12): ensure_schema_exists(), list_tables(), list_tables_matching(), table_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestListTables (+4 more)

### Community 19 - "enums.py"
Cohesion: 0.09
Nodes (12): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, __getattr__() (+4 more)

### Community 20 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 21 - "patterns.py"
Cohesion: 0.08
Nodes (12): generality_weight(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns(), matching_pattern() (+4 more)

### Community 22 - "json"
Cohesion: 0.27
Nodes (11): _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart(), render_markdown() (+3 more)

### Community 25 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 26 - "get_logger"
Cohesion: 0.19
Nodes (3): get_logger(), TestGetLogger, TestLogDuration

### Community 27 - "pipeline.py"
Cohesion: 0.24
Nodes (5): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector

### Community 29 - "builder.py"
Cohesion: 0.11
Nodes (5): _require_min_rows(), _score_single_column(), InsufficientDataError, TestScoreFdPair, TestScoreSingleColumn

### Community 30 - "AlgorithmResult"
Cohesion: 0.13
Nodes (8): Through the registry, The shared result schema, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, config(), score()

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "numpy"
Cohesion: 0.11
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (16): Variants, IndexNotBuiltError, _clean(), fmdv_h(), InferredPattern, _coarse_class(), _coarse_signature(), _fmdv_h_single() (+8 more)

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.21
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.13
Nodes (11): comparison_table_markdown(), git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main() (+3 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.06
Nodes (25): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+17 more)

### Community 38 - "API reference"
Cohesion: 0.12
Nodes (15): Check it works, Installation, Installing from source, Pick your extra, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+7 more)

### Community 40 - "CallableLabeler"
Cohesion: 0.10
Nodes (13): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust (+5 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.21
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "confusion_metrics"
Cohesion: 0.18
Nodes (5): confusion_metrics(), run_auto_validate(), _metrics(), run_raha(), _metrics()

### Community 44 - "pandas"
Cohesion: 0.23
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "RahaDetector"
Cohesion: 0.14
Nodes (10): run_raha(), Scoring raha, main(), RahaDetector, GroundTruthLabeler, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema() (+2 more)

### Community 47 - "fd_compliance_ratio"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 48 - "featurization.py"
Cohesion: 0.09
Nodes (13): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+5 more)

### Community 49 - "._new_failure_tracker"
Cohesion: 0.14
Nodes (4): compute(), compute(), compute(), compute()

### Community 50 - "algorithms/index.md"
Cohesion: 0.29
Nodes (3): Algorithms, Fidelity to the papers, Errors

### Community 52 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "algorithms/uni-detect.md"
Cohesion: 0.27
Nodes (3): Getting started, open-detect, What is in the box

### Community 54 - "metrics/spelling.py"
Cohesion: 0.25
Nodes (4): FDResult, _blocking_key(), _length_bucket(), MPDResult

### Community 55 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (11): AutoValidateConfig, fmdv(), build_pattern_index(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus(), TestCorpusInputShapes (+3 more)

### Community 56 - "argparse"
Cohesion: 0.46
Nodes (3): candidates(), main(), select()

### Community 57 - "raha/detector.py"
Cohesion: 0.20
Nodes (5): Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, Labeler, TestHeuristicLabeler

### Community 58 - "build_corpus_statistics.py"
Cohesion: 0.12
Nodes (6): main(), parse_args(), get_spark(), TestMain, TestParseArgs, TestGetSpark

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 63 - "OpenDetectError"
Cohesion: 0.16
Nodes (9): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved() (+1 more)

### Community 64 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 65 - "Comparing algorithms"
Cohesion: 0.25
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 66 - "CorpusStatsStore"
Cohesion: 0.07
Nodes (16): A fully local example, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks, Job arguments (+8 more)

### Community 68 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 69 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.13
Nodes (12): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark (+4 more)

### Community 71 - "ErrorType"
Cohesion: 0.20
Nodes (6): all_specs(), ErrorTypeSpec, get_spec(), ErrorType, TestAllSpecs, TestGetSpec

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 78 - "UniDetect"
Cohesion: 0.05
Nodes (19): CorpusStatsBuilder, _stats_schema_without_error_type(), CorpusIngestor, FailureTracker, __getattr__(), UniDetect, log_duration(), TestCorpusBuilderAndDetectors (+11 more)

### Community 81 - "Choosing an algorithm"
Cohesion: 0.67
Nodes (3): At a glance, Choosing an algorithm, Rules of thumb

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 84 - "index.py"
Cohesion: 0.10
Nodes (5): indexable_values(), _iter_corpus_columns(), fpr_column(), impurity(), TestIndexableValues

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 535 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `build_metadata.py`, `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `FailureCounts`, `algorithms/__init__.py`, `enums.py`, `collections_abc`, `get_logger`, `pipeline.py`, `builder.py`, `wiki_subset/run_benchmark.py`, `API reference`, `FeatureBucket`, `featurization.py`, `.detect`, `build_corpus_statistics.py`, `CorpusStatsStore`, `_StubDetector`, `UniDetect`, `quickstart.py`?**
  _High betweenness centrality (0.161) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `build_metadata.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12010796221322537 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `UniDetectConfig`, `auto_validate/detector.py`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `API reference`, `_build_index`, `confusion_metrics`, `TestValidation`, `check_drift`, `index.py`, `OpenDetectError`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 53 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._