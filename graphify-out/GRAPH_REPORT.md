# Graph Report - open-detect  (2026-10-11)

## Corpus Check
- 146 files · ~113,729 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 241 file(s) not represented in the graph (top: .csv 226, .j2 10, (none) 2)

## Summary
- 1527 nodes · 3606 edges · 86 communities (67 shown, 19 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 434 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2b9736df`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _is_null
- UniDetectConfig
- algorithms/__init__.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- outliers.py
- UniDetect
- CorpusIngestor
- perturbation.py
- wiki_subset/generate_report.py
- metrics/spelling.py
- metrics/functional_dependency.py
- uniqueness_ratio
- AutoValidateConfig
- auto_validate/__init__.py
- RahaConfig
- hierarchy.py
- ComparisonDirection
- pipeline.py
- patterns.py
- list_tables_matching
- ErrorType
- auto_validate/detector.py
- infer_column_data_type
- main
- conftest.py
- log_duration
- API reference
- AlgorithmResult
- .detect
- pandas
- matches
- FeatureBucket
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- CorpusStatsStore
- _score_single_column
- raha/detector.py
- real_world_gov benchmark results
- confusion_metrics
- argparse
- RahaDetector
- `raha`
- GroundTruthLabeler
- Benchmark: real_world_gov
- featurization.py
- clean_column
- Commit conventions and releases
- propagate_labels
- UniDetectAlgorithm
- docs/index.md
- UnityCatalogLocation
- fmdv
- TestValidation
- _build_index
- json
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- ConfigurationError
- algorithms/index.md
- OpenDetectError
- Raha
- Comparing algorithms
- CorpusNotFoundError
- drop_nulls
- Auto-Validate
- algorithms/uni-detect.md
- perturb_numeric_outlier
- Auto-Validate
- Methodology: auto_validate
- Uni-Detect
- Scoring auto_validate
- CHANGELOG
- `auto_validate`
- algorithms.md
- IndexNotBuiltError
- index.py
- config
- open-detect

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 105 edges
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
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `The simplest labeler: a function` --references--> `CallableLabeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `Configuration` --references--> `UniDetectConfig`  [INFERRED]
  docs/algorithms/uni-detect.md → src/open_detect/config.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (86 total, 19 thin omitted)

### Community 0 - "_is_null"
Cohesion: 0.22
Nodes (5): _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 2 - "algorithms/__init__.py"
Cohesion: 0.13
Nodes (13): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator() (+5 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "outliers.py"
Cohesion: 0.16
Nodes (8): require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 8 - "UniDetect"
Cohesion: 0.07
Nodes (18): Methodology: uni_detect -- mapping real dirty data onto its four error types, CorpusStatsBuilder, compute(), _stats_schema_without_error_type(), __getattr__(), main(), parse_args(), UniDetect (+10 more)

### Community 9 - "CorpusIngestor"
Cohesion: 0.16
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 10 - "perturbation.py"
Cohesion: 0.15
Nodes (8): _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbSpelling, TestPerturbUniqueness

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.11
Nodes (25): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct() (+17 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.15
Nodes (6): _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, TestSpelling

### Community 13 - "metrics/functional_dependency.py"
Cohesion: 0.19
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 14 - "uniqueness_ratio"
Cohesion: 0.31
Nodes (3): InsufficientDataError, uniqueness_ratio(), TestUniquenessRatio

### Community 15 - "AutoValidateConfig"
Cohesion: 0.11
Nodes (7): AutoValidateConfig, build_pattern_index(), TestDefaults, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "auto_validate/__init__.py"
Cohesion: 0.12
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "hierarchy.py"
Cohesion: 0.11
Nodes (12): _append_literal(), _char_class(), _class_of_token(), generalize(), _is_numeric(), _iter_runs(), _parse(), _part_matches() (+4 more)

### Community 19 - "ComparisonDirection"
Cohesion: 0.16
Nodes (6): ComparisonDirection, all_specs(), ErrorTypeSpec, get_spec(), TestAllSpecs, TestGetSpec

### Community 20 - "pipeline.py"
Cohesion: 0.07
Nodes (4): get_logger(), get_spark(), TestGetLogger, TestGetSpark

### Community 21 - "patterns.py"
Cohesion: 0.08
Nodes (12): generality_weight(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns(), matching_pattern() (+4 more)

### Community 22 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 23 - "ErrorType"
Cohesion: 0.11
Nodes (11): ErrorType, BaseDetector, make_evidence_json(), FunctionalDependencyDetector, compute(), NumericOutlierDetector, compute(), SpellingDetector (+3 more)

### Community 24 - "auto_validate/detector.py"
Cohesion: 0.09
Nodes (15): Variants, _clean(), fmdv_h(), InferredPattern, _coarse_class(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+7 more)

### Community 25 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 26 - "main"
Cohesion: 0.25
Nodes (4): main(), parse_args(), TestMain, TestParseArgs

### Community 27 - "conftest.py"
Cohesion: 0.18
Nodes (5): A fully local example, _delta_jars(), _download(), spark(), uc_location()

### Community 29 - "API reference"
Cohesion: 0.15
Nodes (11): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+3 more)

### Community 30 - "AlgorithmResult"
Cohesion: 0.13
Nodes (10): Through the registry, Auto-Validate: learn patterns from clean columns, Quickstart, Reading results, Uni-Detect: score tables in Unity Catalog, Combine, Why a common interface, AlgorithmResult (+2 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "pandas"
Cohesion: 0.08
Nodes (15): build_all_features(), build_column_features(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), test_build_all_features_covers_every_column() (+7 more)

### Community 34 - "matches"
Cohesion: 0.22
Nodes (4): matches(), fpr_column(), impurity(), TestMatching

### Community 35 - "FeatureBucket"
Cohesion: 0.09
Nodes (12): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, TestCandidate (+4 more)

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.14
Nodes (10): git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.11
Nodes (6): Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "CorpusStatsStore"
Cohesion: 0.17
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 39 - "_score_single_column"
Cohesion: 0.24
Nodes (5): _coerce_numeric(), compute(), _score_single_column(), TestCoerceNumeric, TestScoreSingleColumn

### Community 40 - "raha/detector.py"
Cohesion: 0.14
Nodes (11): Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, ColumnFeatures (+3 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "confusion_metrics"
Cohesion: 0.18
Nodes (5): confusion_metrics(), run_auto_validate(), _metrics(), run_raha(), _metrics()

### Community 43 - "argparse"
Cohesion: 0.46
Nodes (3): candidates(), main(), select()

### Community 44 - "RahaDetector"
Cohesion: 0.19
Nodes (7): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.13
Nodes (9): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Raha: find errors with a few labels, CallableLabeler, GroundTruthLabeler, TestCallableLabeler (+1 more)

### Community 47 - "Benchmark: real_world_gov"
Cohesion: 0.29
Nodes (7): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Which 5 datasets, and why

### Community 48 - "featurization.py"
Cohesion: 0.09
Nodes (13): bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket() (+5 more)

### Community 49 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 50 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 52 - "UniDetectAlgorithm"
Cohesion: 0.31
Nodes (4): UniDetectAlgorithm, _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 54 - "UnityCatalogLocation"
Cohesion: 0.21
Nodes (6): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config()

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 57 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.33
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 63 - "OpenDetectError"
Cohesion: 0.14
Nodes (12): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, The shared result schema, Errors, UnknownAlgorithmError (+4 more)

### Community 64 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 65 - "Comparing algorithms"
Cohesion: 0.40
Nodes (5): Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 66 - "CorpusNotFoundError"
Cohesion: 0.13
Nodes (13): Configuration, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks, Job arguments (+5 more)

### Community 67 - "drop_nulls"
Cohesion: 0.16
Nodes (4): drop_nulls(), duplicate_value_indices(), TestDropNulls, TestDuplicateValueIndices

### Community 68 - "Auto-Validate"
Cohesion: 0.13
Nodes (10): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, Configuration, Detector (+2 more)

### Community 69 - "algorithms/uni-detect.md"
Cohesion: 0.20
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 71 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 72 - "Methodology: auto_validate"
Cohesion: 0.50
Nodes (4): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

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
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 490 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `CorpusNotFoundError`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `FeatureBucket`, `CorpusStatsStore`, `_score_single_column`, `UniDetect`, `main`, `featurization.py`, `ComparisonDirection`, `UniDetectAlgorithm`, `pipeline.py`, `json`, `API reference`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `algorithms/__init__.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13227513227513227 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `_is_null`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `confusion_metrics`, `auto_validate/__init__.py`, `index.py`, `ConfigurationError`, `fmdv`, `auto_validate/detector.py`, `_build_index`, `TestValidation`, `API reference`, `OpenDetectError`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 40 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._