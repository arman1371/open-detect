# Graph Report - open-detect  (2026-10-13)

## Corpus Check
- 147 files · ~114,178 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 241 file(s) not represented in the graph (top: .csv 226, .j2 10, (none) 2)

## Summary
- 1531 nodes · 3626 edges · 75 communities (63 shown, 12 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 444 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `56b276ce`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- real_world_gov/generate_report.py
- UniDetectConfig
- registry.py
- dataset_utils.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- pytest
- UniDetect
- _score_single_column
- wiki_subset/generate_report.py
- metrics/spelling.py
- algorithms/__init__.py
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- test_catalog.py
- ErrorType
- Commit conventions and releases
- patterns.py
- Running on Databricks
- collections_abc
- PatternIndex
- infer_column_data_type
- fmdv_v
- spark
- main
- metrics/functional_dependency.py
- AlgorithmResult
- .detect
- raha/strategies.py
- auto_validate/detector.py
- FeatureBucket
- spark_session.py
- AutoValidateAlgorithm
- Writing your own algorithm
- TestMatching
- labeling.py
- real_world_gov benchmark results
- real_world_gov/run_benchmark.py
- wiki_subset/run_benchmark.py
- pandas
- `auto_validate`
- GroundTruthLabeler
- featurization.py
- clean_column
- Contributing
- propagate_labels
- algorithm.py
- docs/index.md
- parse_args
- fmdv
- test_metrics.py
- pipeline.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- algorithms/index.md
- OpenDetectError
- Raha
- Comparing algorithms
- CorpusStatsStore
- log_transform_fits_better
- reference/index.md
- algorithms/uni-detect.md
- Auto-Validate
- Uni-Detect
- `raha`
- CHANGELOG
- duplicate_value_indices
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
- `As a plugin package (no changes to `open-detect`)` --references--> `list_algorithms()`  [INFERRED]
  docs/guides/writing-an-algorithm.md → src/open_detect/algorithms/registry.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (75 total, 12 thin omitted)

### Community 0 - "real_world_gov/generate_report.py"
Cohesion: 0.17
Nodes (12): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.08
Nodes (10): ensure_schema_exists(), UniDetectConfig, UnityCatalogLocation, ConfigurationError, UnityCatalogError, TestEnsureSchemaExists, TestUniDetectConfig, TestUnityCatalogLocation (+2 more)

### Community 2 - "registry.py"
Cohesion: 0.14
Nodes (11): Check it works, get_algorithm(), get_algorithm_class(), list_algorithms(), _load_entry_points(), register_lazy(), test_builtin_algorithms_are_registered(), test_get_algorithm_constructs_with_args() (+3 more)

### Community 3 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

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
Cohesion: 0.15
Nodes (3): TestGetLogger, test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 9 - "UniDetect"
Cohesion: 0.05
Nodes (25): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark, Which 5 datasets, and why (+17 more)

### Community 10 - "_score_single_column"
Cohesion: 0.16
Nodes (7): _coerce_numeric(), compute(), _score_single_column(), perturb_numeric_outlier(), TestCoerceNumeric, TestScoreSingleColumn, TestPerturbNumericOutlier

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.20
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), _metrics_table_row() (+5 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.14
Nodes (7): MADResult, _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, TestSpelling

### Community 13 - "algorithms/__init__.py"
Cohesion: 0.20
Nodes (8): API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, register_algorithm(), decorator()

### Community 14 - "outliers.py"
Cohesion: 0.14
Nodes (9): drop_nulls(), require_min_size(), mad_scores(), max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), InsufficientDataError (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.09
Nodes (9): AutoValidateConfig, build_pattern_index(), _iter_corpus_columns(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex (+1 more)

### Community 16 - "check_drift"
Cohesion: 0.14
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.13
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "test_catalog.py"
Cohesion: 0.12
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 19 - "ErrorType"
Cohesion: 0.14
Nodes (8): all_specs(), ErrorTypeSpec, get_spec(), ComparisonDirection, ErrorType, __getattr__(), TestAllSpecs, TestGetSpec

### Community 20 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 21 - "patterns.py"
Cohesion: 0.06
Nodes (18): _char_class(), _class_of_token(), generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize() (+10 more)

### Community 22 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 23 - "collections_abc"
Cohesion: 0.08
Nodes (8): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, compute(), UniquenessDetector, compute()

### Community 25 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 26 - "fmdv_v"
Cohesion: 0.11
Nodes (9): Variants, _coarse_class(), _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestFmdvV, TestFmdvVh (+1 more)

### Community 27 - "spark"
Cohesion: 0.18
Nodes (9): A fully local example, Configuration, How it works, Install, Reading the detections, Uni-Detect, Usage on Databricks, spark() (+1 more)

### Community 28 - "main"
Cohesion: 0.13
Nodes (6): main(), parse_args(), get_spark(), TestMain, TestParseArgs, TestGetSpark

### Community 29 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 30 - "AlgorithmResult"
Cohesion: 0.13
Nodes (6): Through the registry, Combine, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (16): InferredPattern, _fmdv_h_single(), _fmdv_single_segment(), _infer_cmp(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), _append_literal() (+8 more)

### Community 35 - "FeatureBucket"
Cohesion: 0.09
Nodes (12): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, TestCandidate (+4 more)

### Community 36 - "spark_session.py"
Cohesion: 0.12
Nodes (7): spark_session(), SparkUnavailable, candidates(), main(), select(), _delta_jars(), _download()

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (25): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+17 more)

### Community 38 - "Writing your own algorithm"
Cohesion: 0.33
Nodes (6): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm

### Community 40 - "labeling.py"
Cohesion: 0.10
Nodes (12): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, ColumnFeatures, CallableLabeler (+4 more)

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "real_world_gov/run_benchmark.py"
Cohesion: 0.13
Nodes (11): confusion_metrics(), _build_config(), _register_table(), run(), run_auto_validate(), run_raha(), run_uni_detect(), run_auto_validate() (+3 more)

### Community 43 - "wiki_subset/run_benchmark.py"
Cohesion: 0.21
Nodes (10): git_commit(), main(), main(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

### Community 44 - "pandas"
Cohesion: 0.21
Nodes (7): main(), build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.11
Nodes (16): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results (+8 more)

### Community 48 - "featurization.py"
Cohesion: 0.10
Nodes (13): compute(), compute(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket() (+5 more)

### Community 49 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 50 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 52 - "algorithm.py"
Cohesion: 0.18
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "docs/index.md"
Cohesion: 0.19
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "test_metrics.py"
Cohesion: 0.21
Nodes (3): uniqueness_ratio(), TestDropNulls, TestUniquenessRatio

### Community 58 - "pipeline.py"
Cohesion: 0.09
Nodes (3): get_logger(), log_duration(), TestLogDuration

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "algorithms/index.md"
Cohesion: 0.20
Nodes (6): Algorithms, Fidelity to the papers, Configuration, Detector, Labelers, Raha

### Community 63 - "OpenDetectError"
Cohesion: 0.12
Nodes (13): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, The shared result schema, Errors, IndexNotBuiltError (+5 more)

### Community 64 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 65 - "Comparing algorithms"
Cohesion: 0.40
Nodes (5): Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 66 - "CorpusStatsStore"
Cohesion: 0.15
Nodes (5): Operational notes, CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 69 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 71 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 75 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 488 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `UniDetectConfig`, `auto_validate/detector.py`, `AutoValidateAlgorithm`, `real_world_gov/run_benchmark.py`, `algorithms/__init__.py`, `check_drift`, `fmdv`, `fmdv_v`, `OpenDetectError`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 29 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 29 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `UniDetectConfig` be split into smaller, more focused modules?**
  _Cohesion score 0.08115942028985507 - nodes in this community are weakly interconnected._
- **Why does `ErrorType` connect `ErrorType` to `CorpusStatsStore`, `FeatureBucket`, `UniDetect`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `_score_single_column`, `algorithms/__init__.py`, `featurization.py`, `algorithm.py`, `parse_args`, `collections_abc`, `pipeline.py`, `spark`, `main`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 40 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._