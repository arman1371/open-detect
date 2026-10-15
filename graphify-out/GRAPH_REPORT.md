# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 153 files · ~123,715 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1786 nodes · 4381 edges · 98 communities (71 shown, 27 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 581 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1862498f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- algorithms/__init__.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- CorpusStatsStore
- UniDetect
- FailureCounts
- real_world_gov/generate_report.py
- check_failure_threshold
- test_auto_validate_fmdv_v.py
- outliers.py
- AutoValidateConfig
- auto_validate/__init__.py
- RahaConfig
- list_tables_matching
- FeatureBucket
- auto_validate/detector.py
- hierarchy.py
- wiki_subset/generate_report.py
- collections_abc
- test_metrics.py
- tokenize
- get_logger
- perturb_numeric_outlier
- FailureCountsAccumulatorParam
- AlgorithmResult
- raha/detector.py
- pandas
- PatternIndex
- min_pairwise_edit_distance
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- API reference
- HeuristicLabeler
- perturb_spelling
- real_world_gov benchmark results
- spark_session.py
- dataset_utils.py
- bucket_by_edges
- `raha`
- RahaDetector
- metrics/functional_dependency.py
- ErrorType
- CHANGELOG
- algorithms/index.md
- .detect
- UniDetectAlgorithm
- concepts.md
- _score_single_column
- fmdv
- select_datasets.py
- labeling.py
- main
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- Contributing
- OpenDetectError
- select_fd_column_pairs
- score
- TestAttempt
- reference/index.md
- Benchmarks
- Benchmark: real_world_gov
- get_spec
- uniqueness_ratio
- Uni-Detect
- Raha
- Auto-Validate
- infer_column_data_type
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- log_transform_fits_better
- clean_column
- algorithms/uni-detect.md
- index.py
- open-detect
- `auto_validate`
- ConfigurationError
- is_mixed_alphanumeric
- finite_floats
- is_float_like
- is_integer_like
- TestConfigThreshold
- diff_fingerprints
- raha/config.py
- config

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

## Communities (98 total, 27 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.15
Nodes (10): property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, TestLegacyCorpus, TestMismatch (+2 more)

### Community 2 - "algorithms/__init__.py"
Cohesion: 0.13
Nodes (13): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator() (+5 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.14
Nodes (11): confusion_metrics(), dataset_paths(), _build_config(), _dataset_frames(), _register_table(), run(), run_auto_validate(), run_raha() (+3 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 8 - "CorpusStatsStore"
Cohesion: 0.10
Nodes (10): Errors, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, CorpusStatsStore, CorpusNotFoundError (+2 more)

### Community 9 - "UniDetect"
Cohesion: 0.06
Nodes (19): Methodology: uni_detect -- mapping real dirty data onto its four error types, build_spark(), main(), CorpusIngestor, __getattr__(), main(), parse_args(), UniDetect (+11 more)

### Community 10 - "FailureCounts"
Cohesion: 0.16
Nodes (10): compute(), _score_fd_pair(), make_evidence_json(), compute(), compute(), compute(), compute(), FailureCounts (+2 more)

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.18
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), _metrics_table_row(), render_markdown(), _short_name() (+3 more)

### Community 13 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.19
Nodes (5): min_conforming(), _date_index(), _date_values(), TestLargeGroups, TestMinConforming

### Community 14 - "outliers.py"
Cohesion: 0.12
Nodes (10): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (12): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _build_index(), TestFmdvV, TestFmdvVh, _time_corpus() (+4 more)

### Community 16 - "auto_validate/__init__.py"
Cohesion: 0.12
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.22
Nodes (6): ColumnPredictions, train_and_predict(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 19 - "FeatureBucket"
Cohesion: 0.07
Nodes (16): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation (+8 more)

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.11
Nodes (12): Variants, InferredPattern, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _segment_dp(), _segment_fmdv_v() (+4 more)

### Community 21 - "hierarchy.py"
Cohesion: 0.06
Nodes (23): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), matches() (+15 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), _metrics_table_row() (+5 more)

### Community 23 - "collections_abc"
Cohesion: 0.16
Nodes (6): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 24 - "test_metrics.py"
Cohesion: 0.20
Nodes (5): _brute_force_mpd(), _random_words(), _single_edit(), TestDropNulls, TestSpellingBlocking

### Community 25 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "get_logger"
Cohesion: 0.10
Nodes (5): get_logger(), log_duration(), pair_table(), TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.20
Nodes (4): _score_column(), perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 30 - "AlgorithmResult"
Cohesion: 0.13
Nodes (8): Auto-Validate: learn patterns from clean columns, Quickstart, Reading results, Uni-Detect: score tables in Unity Catalog, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult

### Community 31 - "raha/detector.py"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "pandas"
Cohesion: 0.09
Nodes (14): build_column_features(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), test_build_all_features_covers_every_column(), test_drops_constant_features() (+6 more)

### Community 34 - "PatternIndex"
Cohesion: 0.10
Nodes (6): _fmdv_h_single(), _fmdv_single_segment(), PatternIndex, patterns_of(), sorted_patterns(), TestPatternsOf

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.14
Nodes (7): _blocking_keys(), _closest_pair(), differing_token_lengths(), min_pairwise_edit_distance(), _result(), MPDResult, TestSpelling

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.15
Nodes (13): git_commit(), main(), main(), main(), _build_config(), _load_corpus_tables(), _load_targets(), main() (+5 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (27): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+19 more)

### Community 38 - "API reference"
Cohesion: 0.12
Nodes (15): Check it works, Installation, Installing from source, Pick your extra, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`) (+7 more)

### Community 39 - "HeuristicLabeler"
Cohesion: 0.38
Nodes (4): Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "spark_session.py"
Cohesion: 0.12
Nodes (6): spark_session(), SparkUnavailable, _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "dataset_utils.py"
Cohesion: 0.23
Nodes (4): canonical_column(), load_changes(), load_csv(), Source

### Community 44 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "RahaDetector"
Cohesion: 0.16
Nodes (8): main(), RahaDetector, GroundTruthLabeler, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler(), TestGroundTruthLabeler

### Community 47 - "metrics/functional_dependency.py"
Cohesion: 0.19
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 48 - "ErrorType"
Cohesion: 0.13
Nodes (13): _require_min_rows(), _score_pair(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket() (+5 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.15
Nodes (12): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring, Unreleased, v0.2.0 (2026-10-08) (+4 more)

### Community 51 - ".detect"
Cohesion: 0.18
Nodes (3): build_all_features(), propagate_labels(), TestPropagateLabels

### Community 52 - "UniDetectAlgorithm"
Cohesion: 0.31
Nodes (4): UniDetectAlgorithm, _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "concepts.md"
Cohesion: 0.24
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 54 - "_score_single_column"
Cohesion: 0.31
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "select_datasets.py"
Cohesion: 0.46
Nodes (3): candidates(), main(), select()

### Community 57 - "labeling.py"
Cohesion: 0.10
Nodes (14): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Raha: find errors with a few labels, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust (+6 more)

### Community 58 - "main"
Cohesion: 0.14
Nodes (6): main(), parse_args(), get_spark(), TestMain, TestParseArgs, TestGetSpark

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.33
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 63 - "OpenDetectError"
Cohesion: 0.21
Nodes (6): Errors, UnknownAlgorithmError, OpenDetectError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_open_detect_error_is_catchable_broadly()

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "score"
Cohesion: 0.13
Nodes (13): Through the registry, Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema, Combine, Comparing algorithms (+5 more)

### Community 68 - "reference/index.md"
Cohesion: 0.25
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 69 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.29
Nodes (7): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Which 5 datasets, and why

### Community 71 - "get_spec"
Cohesion: 0.10
Nodes (6): all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.09
Nodes (17): A fully local example, Configuration, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks (+9 more)

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.18
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config(), config()

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "algorithms/uni-detect.md"
Cohesion: 0.25
Nodes (5): open-detect, What is in the box, Registry, Registry and results, Result types

### Community 84 - "index.py"
Cohesion: 0.09
Nodes (5): indexable_values(), _iter_corpus_columns(), fpr_column(), impurity(), TestIndexableValues

### Community 88 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 548 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `API reference`, `get_spec`, `CorpusStatsStore`, `UniDetect`, `FailureCounts`, `CorpusStatsBuilder`, `FeatureBucket`, `UniDetectAlgorithm`, `_score_single_column`, `collections_abc`, `main`, `enums.py`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.14838709677419354 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `score`, `PatternIndex`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `AutoValidateAlgorithm`, `API reference`, `test_auto_validate_fmdv_v.py`, `auto_validate/__init__.py`, `index.py`, `auto_validate/detector.py`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 53 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._