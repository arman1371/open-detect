# Graph Report - open-detect  (2026-09-30)

## Corpus Check
- 123 files · ~97,172 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 226, (none) 3, .properties 1)

## Summary
- 1216 nodes · 2690 edges · 60 communities (43 shown, 17 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 213 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `27e5abfb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- collections_abc
- UnityCatalogLocation
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
- min_pairwise_edit_distance
- fd_compliance_ratio
- uniqueness_ratio
- AutoValidateConfig
- featurization.py
- RahaConfig
- patterns.py
- run_detection.py
- pipeline.py
- ErrorType
- list_tables_matching
- unidetect/config.py
- index.py
- tokenize
- build_corpus_statistics.py
- conftest.py
- unidetect
- features.py
- cluster_column
- gaussian_outlier_strategies
- test_featurization.py
- UniDetectConfig
- wiki_subset/run_benchmark.py
- UniDetectError
- metrics/spelling.py
- _score_single_column
- ColumnFeatures
- patterns_of
- hierarchy.py
- select_datasets.py
- spark_session.py
- tokenize
- detector.py
- Benchmark: real_world_gov
- bucket_by_edges
- clean_column
- infer_column_data_type
- .detect
- build_column_features
- confusion_metrics
- quickstart.py
- matches
- test_corpus_builder_helpers.py
- is_float_like
- duplicate_value_indices
- is_integer_like

## God Nodes (most connected - your core abstractions)
1. `ErrorType` - 66 edges
2. `UniDetectConfig` - 46 edges
3. `AutoValidateConfig` - 43 edges
4. `UniDetect` - 34 edges
5. `build_pattern_index()` - 30 edges
6. `RahaConfig` - 30 edges
7. `UnityCatalogLocation` - 26 edges
8. `ARCHITECTURE.md — Uni-Detect paper-to-code map` - 26 edges
9. `CorpusIngestor` - 21 edges
10. `CorpusStatsStore` - 21 edges

## Surprising Connections (you probably didn't know these)
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/pipeline.py
- `Scoring raha` --references--> `Labeler`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/algorithms/raha/labeling.py
- `Scoring raha` --references--> `GroundTruthLabeler`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/algorithms/raha/labeling.py
- `Running the benchmark` --references--> `CorpusStatsBuilder`  [INFERRED]
  benchmarks/real_world_gov/README.md → src/unidetect/corpus/builder.py
- `README.md — Uni-Detect overview` --references--> `CI workflow: Benchmark (wiki-subset, workflow_dispatch)`  [AMBIGUOUS]
  README.md → .github/workflows/benchmark.yml

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **graphify Skill Reference Documentation Set** — _claude_skills_graphify_skill, _claude_skills_graphify_references_add_watch, _claude_skills_graphify_references_exports, _claude_skills_graphify_references_extraction_spec, _claude_skills_graphify_references_github_and_merge, _claude_skills_graphify_references_hooks, _claude_skills_graphify_references_query, _claude_skills_graphify_references_transcribe, _claude_skills_graphify_references_update [EXTRACTED 1.00]
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (60 total, 17 thin omitted)

### Community 0 - "collections_abc"
Cohesion: 0.09
Nodes (10): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, compute(), NumericOutlierDetector, compute(), SpellingDetector, compute() (+2 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (6): ensure_schema_exists(), UnityCatalogLocation, ConfigurationError, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation

### Community 2 - "algorithms/__init__.py"
Cohesion: 0.06
Nodes (24): AlgorithmResult, CellResult, ErrorDetectionAlgorithm, _load_raha(), _load_uni_detect(), get_algorithm(), get_algorithm_class(), list_algorithms() (+16 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.14
Nodes (11): dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main(), _print_comparison(), _register_table() (+3 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.05
Nodes (45): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), ARCHITECTURE.md — Uni-Detect paper-to-code map, benchmarks/README.md — WIKI-subset benchmark, Algorithm comparison, By dataset (cell-level), By dataset (column-level), By dataset (column-level) (+37 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 6 - "graphify SKILL.md — main pipeline skill"
Cohesion: 0.10
Nodes (16): .claude/CLAUDE.md — graphify trigger, graphify reference: add-watch.md, graphify reference: exports.md, graphify reference: extraction-spec.md, graphify reference: github-and-merge.md, graphify reference: hooks.md, graphify reference: query.md, graphify reference: transcribe.md (+8 more)

### Community 7 - "outliers.py"
Cohesion: 0.12
Nodes (11): InsufficientDataError, drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+3 more)

### Community 8 - "UniDetect"
Cohesion: 0.06
Nodes (11): Methodology: uni_detect -- mapping real dirty data onto its four error types, CorpusIngestor, UniDetect, config(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestCorpusIngestorSkipsBadInputs (+3 more)

### Community 10 - "perturbation.py"
Cohesion: 0.12
Nodes (10): _max_drop(), perturb_functional_dependency(), perturb_numeric_outlier(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbNumericOutlier (+2 more)

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 12 - "min_pairwise_edit_distance"
Cohesion: 0.21
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 13 - "fd_compliance_ratio"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 15 - "AutoValidateConfig"
Cohesion: 0.06
Nodes (10): AutoValidateConfig, build_pattern_index(), PatternIndex, TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestIndexableValues (+2 more)

### Community 16 - "featurization.py"
Cohesion: 0.24
Nodes (7): bucket_row_count(), bucket_token_length(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket(), TestFeatureBucketBuilders

### Community 17 - "RahaConfig"
Cohesion: 0.18
Nodes (10): train_and_predict(), RahaConfig, RahaDetector, _features(), TestClassifierTrainingPath, TestDegenerateCases, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler() (+2 more)

### Community 18 - "patterns.py"
Cohesion: 0.15
Nodes (7): generality_weight(), Token, _alternatives(), _best_first_patterns(), common_patterns(), iter_patterns(), _ordered_alternatives()

### Community 20 - "pipeline.py"
Cohesion: 0.13
Nodes (4): get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 21 - "ErrorType"
Cohesion: 0.05
Nodes (24): ColumnDataType, ComparisonDirection, ErrorType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket (+16 more)

### Community 22 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 24 - "index.py"
Cohesion: 0.16
Nodes (4): token_count(), indexable_values(), fpr_column(), impurity()

### Community 25 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "build_corpus_statistics.py"
Cohesion: 0.20
Nodes (4): main(), parse_args(), TestMain, TestParseArgs

### Community 27 - "conftest.py"
Cohesion: 0.18
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 35 - "UniDetectConfig"
Cohesion: 0.05
Nodes (17): Running the benchmark, A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, UniDetectConfig (+9 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.20
Nodes (8): git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_uni_detect()

### Community 37 - "UniDetectError"
Cohesion: 0.19
Nodes (5): IndexNotBuiltError, UniDetectError, test_all_errors_derive_from_unidetect_error(), test_error_message_is_preserved(), test_unidetect_error_is_catchable_broadly()

### Community 38 - "metrics/spelling.py"
Cohesion: 0.17
Nodes (4): FDResult, _blocking_key(), _length_bucket(), MPDResult

### Community 39 - "_score_single_column"
Cohesion: 0.24
Nodes (5): _coerce_numeric(), compute(), _score_single_column(), TestCoerceNumeric, TestScoreSingleColumn

### Community 40 - "ColumnFeatures"
Cohesion: 0.46
Nodes (3): ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 41 - "patterns_of"
Cohesion: 0.19
Nodes (4): any_pattern(), patterns_of(), sorted_patterns(), TestPatternsOf

### Community 42 - "hierarchy.py"
Cohesion: 0.19
Nodes (7): _append_literal(), _char_class(), _class_of_token(), _is_numeric(), _iter_runs(), _parse(), _part_matches()

### Community 43 - "select_datasets.py"
Cohesion: 0.60
Nodes (3): candidates(), main(), select()

### Community 45 - "tokenize"
Cohesion: 0.22
Nodes (4): generalize(), tokenize(), TestGeneralize, TestTokenize

### Community 46 - "detector.py"
Cohesion: 0.09
Nodes (10): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), main(), CallableLabeler, GroundTruthLabeler, Labeler (+2 more)

### Community 47 - "Benchmark: real_world_gov"
Cohesion: 0.20
Nodes (9): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Layout, Methodology: raha, Reading the results, Source (+1 more)

### Community 48 - "bucket_by_edges"
Cohesion: 0.21
Nodes (4): bucket_by_edges(), bucket_leftness(), bucket_token_prevalence(), TestBucketing

### Community 49 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 52 - "build_column_features"
Cohesion: 0.25
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 53 - "confusion_metrics"
Cohesion: 0.25
Nodes (3): confusion_metrics(), run_raha(), _metrics()

### Community 55 - "matches"
Cohesion: 0.31
Nodes (3): matches(), matching_pattern(), TestMatching

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **37 isolated node(s):** `unidetect`, `Which 5 datasets, and why`, `Layout`, `Duration methodology`, `Reading the results` (+32 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 357 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `collections_abc`, `UnityCatalogLocation`, `algorithms/__init__.py`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `UniDetectConfig`, `_score_single_column`, `UniDetect`, `featurization.py`, `run_detection.py`, `pipeline.py`, `quickstart.py`, `unidetect/config.py`, `build_corpus_statistics.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `collections_abc`, `UnityCatalogLocation`, `algorithms/__init__.py`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `_score_single_column`, `UniDetect`, `run_detection.py`, `pipeline.py`, `ErrorType`, `quickstart.py`, `unidetect/config.py`, `test_corpus_builder_helpers.py`, `build_corpus_statistics.py`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `Benchmark: real_world_gov` connect `Benchmark: real_world_gov` to `UniDetect`, `UniDetectConfig`, `ARCHITECTURE.md — Uni-Detect paper-to-code map`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `AutoValidateConfig` (e.g. with `ConfigurationError` and `TestDefaults`) actually correct?**
  _`AutoValidateConfig` has 7 INFERRED edges - model-reasoned connections that need verification._