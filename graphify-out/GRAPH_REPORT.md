# Graph Report - open-detect  (2026-09-30)

## Corpus Check
- 131 files · ~104,015 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 226, (none) 3, .properties 1)

## Summary
- 1373 nodes · 3137 edges · 66 communities (48 shown, 18 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 258 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `900c1dc8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ErrorType
- UniDetectConfig
- registry.py
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
- check_drift
- RahaConfig
- patterns.py
- pipeline.py
- log_duration
- unidetect/__init__.py
- list_tables_matching
- index.py
- tokenize
- build_corpus_statistics.py
- conftest.py
- unidetect
- AlgorithmResult
- numpy
- raha/strategies.py
- log_transform_fits_better
- CorpusStatsStore
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- collections_abc
- builder.py
- raha/detector.py
- PatternIndex
- hierarchy.py
- select_datasets.py
- RahaDetector
- algorithms/__init__.py
- CallableLabeler
- Benchmark: real_world_gov
- featurization.py
- clean_column
- infer_column_data_type
- .detect
- features.py
- spark_session.py
- quickstart.py
- _build_index
- real_world_gov/generate_report.py
- _build_index
- CorpusStatsBuilder
- is_integer_like
- FeatureBucket
- Detection
- drop_nulls
- perturb_numeric_outlier

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 78 edges
2. `ErrorType` - 66 edges
3. `UniDetectConfig` - 46 edges
4. `build_pattern_index()` - 38 edges
5. `UniDetect` - 34 edges
6. `RahaConfig` - 30 edges
7. `PatternIndex` - 29 edges
8. `AutoValidateAlgorithm` - 28 edges
9. `UnityCatalogLocation` - 26 edges
10. `ARCHITECTURE.md — Uni-Detect paper-to-code map` - 26 edges

## Surprising Connections (you probably didn't know these)
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/pipeline.py
- `Scoring raha` --references--> `Labeler`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/algorithms/raha/labeling.py
- `Running the benchmark` --references--> `CorpusStatsBuilder`  [INFERRED]
  benchmarks/real_world_gov/README.md → src/unidetect/corpus/builder.py
- `Scoring raha` --references--> `GroundTruthLabeler`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/algorithms/raha/labeling.py
- `README.md — Uni-Detect overview` --references--> `CI workflow: Benchmark (wiki-subset, workflow_dispatch)`  [AMBIGUOUS]
  README.md → .github/workflows/benchmark.yml

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **graphify Skill Reference Documentation Set** — _claude_skills_graphify_skill, _claude_skills_graphify_references_add_watch, _claude_skills_graphify_references_exports, _claude_skills_graphify_references_extraction_spec, _claude_skills_graphify_references_github_and_merge, _claude_skills_graphify_references_hooks, _claude_skills_graphify_references_query, _claude_skills_graphify_references_transcribe, _claude_skills_graphify_references_update [EXTRACTED 1.00]
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (66 total, 18 thin omitted)

### Community 0 - "ErrorType"
Cohesion: 0.13
Nodes (10): ErrorType, BaseDetector, make_evidence_json(), FunctionalDependencyDetector, compute(), NumericOutlierDetector, compute(), SpellingDetector (+2 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.06
Nodes (16): ensure_schema_exists(), UniDetectConfig, UnityCatalogLocation, ConfigurationError, UniDetectError, UnityCatalogError, main(), TestEnsureSchemaExists (+8 more)

### Community 2 - "registry.py"
Cohesion: 0.11
Nodes (14): get_algorithm(), get_algorithm_class(), list_algorithms(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), UnknownAlgorithmError (+6 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.13
Nodes (11): git_commit(), dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main(), _print_comparison() (+3 more)

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
Cohesion: 0.15
Nodes (8): InsufficientDataError, require_min_size(), mad_scores(), max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 8 - "UniDetect"
Cohesion: 0.06
Nodes (11): Methodology: uni_detect -- mapping real dirty data onto its four error types, CorpusIngestor, UniDetect, config(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestCorpusIngestorSkipsBadInputs (+3 more)

### Community 9 - "text_utils.py"
Cohesion: 0.17
Nodes (4): is_float_like(), is_mixed_alphanumeric(), TestFloatLike, TestMixedAlphanumeric

### Community 10 - "perturbation.py"
Cohesion: 0.12
Nodes (10): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency (+2 more)

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.17
Nodes (15): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct() (+7 more)

### Community 12 - "min_pairwise_edit_distance"
Cohesion: 0.21
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 13 - "fd_compliance_ratio"
Cohesion: 0.26
Nodes (3): fd_compliance_ratio(), minority_violation_rows(), TestFunctionalDependency

### Community 15 - "AutoValidateConfig"
Cohesion: 0.10
Nodes (8): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "check_drift"
Cohesion: 0.14
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "patterns.py"
Cohesion: 0.06
Nodes (16): generality_weight(), generalize(), Token, token_count(), tokenize(), _alternatives(), any_pattern(), _best_first_patterns() (+8 more)

### Community 19 - "pipeline.py"
Cohesion: 0.13
Nodes (4): parse_args(), get_spark(), TestParseArgs, TestGetSpark

### Community 20 - "log_duration"
Cohesion: 0.13
Nodes (4): get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 21 - "unidetect/__init__.py"
Cohesion: 0.14
Nodes (9): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, __getattr__(), TestCandidate, TestCorpusRecords (+1 more)

### Community 22 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 24 - "index.py"
Cohesion: 0.11
Nodes (4): indexable_values(), fpr_column(), impurity(), TestIndexableValues

### Community 25 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "build_corpus_statistics.py"
Cohesion: 0.20
Nodes (4): main(), parse_args(), TestMain, TestParseArgs

### Community 27 - "conftest.py"
Cohesion: 0.18
Nodes (4): _delta_jars(), _download(), spark(), uc_location()

### Community 30 - "AlgorithmResult"
Cohesion: 0.12
Nodes (3): AlgorithmResult, CellResult, TestAlgorithmResult

### Community 31 - "numpy"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 35 - "CorpusStatsStore"
Cohesion: 0.06
Nodes (17): Running the benchmark, A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, ComparisonDirection (+9 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.12
Nodes (11): comparison_table_markdown(), confusion_metrics(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+3 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.10
Nodes (4): AutoValidateAlgorithm, IndexNotBuiltError, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "collections_abc"
Cohesion: 0.18
Nodes (5): FDResult, MADResult, _blocking_key(), _length_bucket(), MPDResult

### Community 39 - "builder.py"
Cohesion: 0.11
Nodes (12): _coerce_numeric(), compute(), _score_single_column(), compute(), bucket_row_count(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+4 more)

### Community 40 - "raha/detector.py"
Cohesion: 0.19
Nodes (4): ColumnFeatures, HeuristicLabeler, Labeler, TestHeuristicLabeler

### Community 41 - "PatternIndex"
Cohesion: 0.08
Nodes (15): _clean(), fmdv(), fmdv_h(), InferredPattern, _coarse_class(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+7 more)

### Community 42 - "hierarchy.py"
Cohesion: 0.11
Nodes (11): _is_null(), _value_matches(), _append_literal(), _char_class(), _class_of_token(), _is_numeric(), _iter_runs(), matches() (+3 more)

### Community 43 - "select_datasets.py"
Cohesion: 0.39
Nodes (3): candidates(), main(), select()

### Community 44 - "RahaDetector"
Cohesion: 0.12
Nodes (13): run_raha(), Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), main(), RahaDetector, GroundTruthLabeler (+5 more)

### Community 45 - "algorithms/__init__.py"
Cohesion: 0.17
Nodes (8): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), UniDetectAlgorithm, _config(), _row(), TestUniDetectAlgorithm

### Community 47 - "Benchmark: real_world_gov"
Cohesion: 0.20
Nodes (9): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Layout, Methodology: raha, Reading the results, Source (+1 more)

### Community 48 - "featurization.py"
Cohesion: 0.16
Nodes (5): bucket_by_edges(), bucket_leftness(), bucket_token_length(), bucket_token_prevalence(), TestBucketing

### Community 49 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 52 - "features.py"
Cohesion: 0.23
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 55 - "_build_index"
Cohesion: 0.16
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "real_world_gov/generate_report.py"
Cohesion: 0.32
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 57 - "_build_index"
Cohesion: 0.16
Nodes (4): _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 58 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (4): CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **37 isolated node(s):** `unidetect`, `Which 5 datasets, and why`, `Layout`, `Duration methodology`, `Reading the results` (+32 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 422 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `Detection`, `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `CorpusStatsStore`, `build_corpus_statistics.py`, `builder.py`, `UniDetect`, `algorithms/__init__.py`, `featurization.py`, `pipeline.py`, `unidetect/__init__.py`, `quickstart.py`, `enums.py`, `CorpusStatsBuilder`, `FeatureBucket`, `AlgorithmResult`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `UniDetectConfig`, `AutoValidateAlgorithm`, `PatternIndex`, `check_drift`, `_build_index`, `index.py`, `_build_index`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `ErrorType`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `CorpusStatsStore`, `build_corpus_statistics.py`, `builder.py`, `UniDetect`, `algorithms/__init__.py`, `pipeline.py`, `unidetect/__init__.py`, `quickstart.py`, `enums.py`, `CorpusStatsBuilder`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `AutoValidateConfig` (e.g. with `ConfigurationError` and `AutoValidateAlgorithm`) actually correct?**
  _`AutoValidateConfig` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 38 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 16 INFERRED edges - model-reasoned connections that need verification._