# Graph Report - open-detect  (2026-10-08)

## Corpus Check
- 153 files · ~122,325 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 226, (none) 3, .properties 1)

## Summary
- 1538 nodes · 3444 edges · 89 communities (63 shown, 26 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 350 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `079a99f0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- .detect
- UniDetectConfig
- algorithms/__init__.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- graphify SKILL.md — main pipeline skill
- outliers.py
- UniDetect
- text_utils.py
- perturbation.py
- wiki_subset/generate_report.py
- metrics/spelling.py
- metrics/functional_dependency.py
- uniqueness_ratio
- AutoValidateConfig
- check_drift
- raha/detector.py
- hierarchy.py
- main
- pipeline.py
- patterns.py
- test_catalog.py
- ErrorType
- auto_validate/detector.py
- tokenize
- main
- spark_session.py
- log_duration
- spark
- AlgorithmResult
- .detect
- raha/strategies.py
- log_transform_fits_better
- FeatureBucket
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- CorpusStatsStore
- _score_single_column
- labeling.py
- real_world_gov benchmark results
- confusion_metrics
- select_datasets.py
- RahaConfig
- `raha`
- Labeler
- Benchmark: real_world_gov
- featurization.py
- clean_column
- infer_column_data_type
- propagate_labels
- features.py
- docs/index.md
- UnityCatalogLocation
- fmdv
- TestValidation
- _build_index
- patterns_of
- is_integer_like
- README.md — Uni-Detect overview
- ConfigurationError
- algorithms/index.md
- OpenDetectError
- Raha
- Comparing algorithms
- CorpusNotFoundError
- drop_nulls
- algorithms/raha.md
- algorithms/uni-detect.md
- is_mixed_alphanumeric
- reference/index.md
- Auto-Validate
- Uni-Detect
- test_featurization.py
- `auto_validate`
- algorithms.md
- IndexNotBuiltError
- indexable_values
- FD metric deviation from literal paper formula
- compute
- config
- open-detect

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 89 edges
2. `ErrorType` - 68 edges
3. `UniDetectConfig` - 49 edges
4. `build_pattern_index()` - 39 edges
5. `AutoValidateAlgorithm` - 36 edges
6. `UniDetect` - 35 edges
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
- `As a plugin package (no changes to `open-detect`)` --references--> `list_algorithms()`  [INFERRED]
  docs/guides/writing-an-algorithm.md → src/open_detect/algorithms/registry.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **graphify Skill Reference Documentation Set** — _claude_skills_graphify_skill, _claude_skills_graphify_references_add_watch, _claude_skills_graphify_references_exports, _claude_skills_graphify_references_extraction_spec, _claude_skills_graphify_references_github_and_merge, _claude_skills_graphify_references_hooks, _claude_skills_graphify_references_query, _claude_skills_graphify_references_transcribe, _claude_skills_graphify_references_update [EXTRACTED 1.00]
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (89 total, 26 thin omitted)

### Community 0 - ".detect"
Cohesion: 0.08
Nodes (22): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+14 more)

### Community 2 - "algorithms/__init__.py"
Cohesion: 0.08
Nodes (23): The registry, API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), get_algorithm(), get_algorithm_class() (+15 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (13): git_commit(), dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main(), _print_comparison() (+5 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 6 - "graphify SKILL.md — main pipeline skill"
Cohesion: 0.10
Nodes (16): .claude/CLAUDE.md — graphify trigger, graphify reference: add-watch.md, graphify reference: exports.md, graphify reference: extraction-spec.md, graphify reference: github-and-merge.md, graphify reference: hooks.md, graphify reference: query.md, graphify reference: transcribe.md (+8 more)

### Community 7 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 8 - "UniDetect"
Cohesion: 0.06
Nodes (16): Methodology: uni_detect -- mapping real dirty data onto its four error types, A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, CorpusIngestor (+8 more)

### Community 10 - "perturbation.py"
Cohesion: 0.12
Nodes (10): _max_drop(), perturb_functional_dependency(), perturb_numeric_outlier(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbNumericOutlier (+2 more)

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.14
Nodes (6): _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, TestSpelling

### Community 13 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 15 - "AutoValidateConfig"
Cohesion: 0.15
Nodes (6): AutoValidateConfig, build_pattern_index(), TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "check_drift"
Cohesion: 0.14
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "raha/detector.py"
Cohesion: 0.13
Nodes (6): ColumnPredictions, train_and_predict(), _default_classifier_factory(), _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "hierarchy.py"
Cohesion: 0.09
Nodes (14): _append_literal(), _char_class(), _class_of_token(), generalize(), _is_numeric(), _iter_runs(), matches(), _parse() (+6 more)

### Community 19 - "main"
Cohesion: 0.23
Nodes (4): main(), parse_args(), TestMain, TestParseArgs

### Community 20 - "pipeline.py"
Cohesion: 0.10
Nodes (3): get_logger(), get_spark(), TestGetLogger

### Community 21 - "patterns.py"
Cohesion: 0.11
Nodes (9): generality_weight(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns(), matching_pattern() (+1 more)

### Community 22 - "test_catalog.py"
Cohesion: 0.15
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 23 - "ErrorType"
Cohesion: 0.11
Nodes (13): ErrorType, BaseDetector, make_evidence_json(), FunctionalDependencyDetector, compute(), NumericOutlierDetector, compute(), SpellingDetector (+5 more)

### Community 24 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (16): _clean(), InferredPattern, _coarse_class(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment(), fmdv_v(), fmdv_vh() (+8 more)

### Community 25 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "main"
Cohesion: 0.13
Nodes (5): main(), parse_args(), TestMain, TestParseArgs, TestGetSpark

### Community 28 - "log_duration"
Cohesion: 0.17
Nodes (5): CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), log_duration(), TestLogDuration

### Community 29 - "spark"
Cohesion: 0.12
Nodes (14): A fully local example, Configuration, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks (+6 more)

### Community 30 - "AlgorithmResult"
Cohesion: 0.09
Nodes (12): Through the registry, The shared result schema, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm (+4 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.09
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 35 - "FeatureBucket"
Cohesion: 0.05
Nodes (20): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation (+12 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.16
Nodes (9): spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+1 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "CorpusStatsStore"
Cohesion: 0.17
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 39 - "_score_single_column"
Cohesion: 0.12
Nodes (7): _coerce_numeric(), compute(), _score_single_column(), config(), TestCoerceNumeric, TestScoreSingleColumn, TestStatsSchemaWithoutErrorType

### Community 40 - "labeling.py"
Cohesion: 0.26
Nodes (3): ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "confusion_metrics"
Cohesion: 0.18
Nodes (5): confusion_metrics(), run_auto_validate(), _metrics(), run_raha(), _metrics()

### Community 43 - "select_datasets.py"
Cohesion: 0.60
Nodes (3): candidates(), main(), select()

### Community 44 - "RahaConfig"
Cohesion: 0.20
Nodes (8): main(), RahaConfig, RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "Labeler"
Cohesion: 0.08
Nodes (20): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results (+12 more)

### Community 47 - "Benchmark: real_world_gov"
Cohesion: 0.20
Nodes (9): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Source (+1 more)

### Community 48 - "featurization.py"
Cohesion: 0.18
Nodes (7): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_spelling_bucket(), TestBucketing

### Community 49 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 52 - "features.py"
Cohesion: 0.23
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 53 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 54 - "UnityCatalogLocation"
Cohesion: 0.13
Nodes (7): build_spark(), main(), ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation

### Community 55 - "fmdv"
Cohesion: 0.13
Nodes (7): Variants, fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 57 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.31
Nodes (8): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, UniDetect pipeline facade

### Community 61 - "ConfigurationError"
Cohesion: 0.22
Nodes (5): Concepts, Configuration objects, Errors, One contract: `detect()`, ConfigurationError

### Community 62 - "algorithms/index.md"
Cohesion: 0.22
Nodes (6): Algorithms, Fidelity to the papers, Adding an algorithm, Contributing, Everyday commands, Working on these docs

### Community 63 - "OpenDetectError"
Cohesion: 0.28
Nodes (4): OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_open_detect_error_is_catchable_broadly()

### Community 64 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 65 - "Comparing algorithms"
Cohesion: 0.25
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 66 - "CorpusNotFoundError"
Cohesion: 0.25
Nodes (6): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, CorpusNotFoundError

### Community 67 - "drop_nulls"
Cohesion: 0.14
Nodes (5): InsufficientDataError, drop_nulls(), duplicate_value_indices(), TestDropNulls, TestDuplicateValueIndices

### Community 68 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 69 - "algorithms/uni-detect.md"
Cohesion: 0.33
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 72 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 78 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 79 - "algorithms.md"
Cohesion: 0.50
Nodes (3): Registry, Registry and results, Result types

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **99 isolated node(s):** `open-detect`, `Which 5 datasets, and why`, `Layout`, `Expected weakness: read Auto-Validate's numbers honestly`, `Duration methodology` (+94 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 495 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `algorithms/__init__.py`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `FeatureBucket`, `CorpusStatsStore`, `_score_single_column`, `UniDetect`, `.batch_score`, `test_featurization.py`, `featurization.py`, `main`, `pipeline.py`, `UnityCatalogLocation`, `main`, `log_duration`, `spark`, `AlgorithmResult`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Why does `API reference` connect `algorithms/__init__.py` to `UniDetectConfig`, `AutoValidateAlgorithm`, `reference/index.md`, `UniDetect`, `RahaConfig`, `AutoValidateConfig`, `UnityCatalogLocation`, `ErrorType`, `AlgorithmResult`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `.detect`, `algorithms/__init__.py`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `confusion_metrics`, `.uses_horizontal_cuts`, `check_drift`, `fmdv`, `auto_validate/detector.py`, `_build_index`, `TestValidation`, `ConfigurationError`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 40 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 19 INFERRED edges - model-reasoned connections that need verification._