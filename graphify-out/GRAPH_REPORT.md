# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 154 files · ~126,038 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1881 nodes · 4649 edges · 94 communities (76 shown, 18 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 614 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5fa63469`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CorpusStatsStore
- UniDetectConfig
- API reference
- wiki_subset/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- PatternIndex
- UniDetect
- FailureCounts
- real_world_gov/generate_report.py
- CorpusIngestor
- fmdv_v
- outliers.py
- AutoValidateConfig
- check_drift
- raha/config.py
- _StubDetector
- get_spec
- auto_validate/detector.py
- hierarchy.py
- wiki_subset/generate_report.py
- pipeline.py
- test_metrics.py
- builder.py
- logging_utils.py
- perturb_numeric_outlier
- ErrorType
- list_tables_matching
- AlgorithmResult
- cluster_column
- numpy
- main
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- pandas
- HeuristicLabeler
- perturb_spelling
- real_world_gov benchmark results
- conftest.py
- bucket_by_edges
- featurization.py
- `auto_validate`
- metrics/spelling.py
- ValidationError
- list_algorithms
- CHANGELOG
- algorithms/raha.md
- propagate_labels
- ErrorDetectionAlgorithm
- docs/index.md
- dataset_utils.py
- fmdv
- argparse
- labeling.py
- CellResult
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _score_single_column
- algorithms/index.md
- Benchmarks
- select_fd_column_pairs
- score
- algorithms/uni-detect.md
- config
- redact_evidence
- reference/index.md
- confusion_metrics
- .detect
- uniqueness_ratio
- Uni-Detect
- Raha
- Auto-Validate
- _require_columns
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- build_spark
- clean_column
- __getattr__
- __getattr__
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- open-detect
- open_detect/__init__.py
- log_transform_fits_better
- ConfigurationError
- infer_column_data_type
- TestConfigThreshold
- `raha`
- OpenDetectError

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 115 edges
2. `ErrorType` - 85 edges
3. `UniDetectConfig` - 80 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 45 edges
6. `UniDetect` - 38 edges
7. `UnityCatalogLocation` - 37 edges
8. `AutoValidateAlgorithm` - 36 edges
9. `ConfigurationError` - 36 edges
10. `RahaConfig` - 33 edges

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

## Communities (94 total, 18 thin omitted)

### Community 0 - "CorpusStatsStore"
Cohesion: 0.06
Nodes (21): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, diff_fingerprints(), property_key(), read_build_config() (+13 more)

### Community 2 - "API reference"
Cohesion: 0.17
Nodes (9): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference, get_algorithm() (+1 more)

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.17
Nodes (8): git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_uni_detect()

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.12
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 8 - "PatternIndex"
Cohesion: 0.07
Nodes (13): InferredPattern, _fmdv_h_single(), _fmdv_single_segment(), _infer_cmp(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), PatternIndex (+5 more)

### Community 9 - "UniDetect"
Cohesion: 0.21
Nodes (5): main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.05
Nodes (17): compute(), compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), check_failure_threshold() (+9 more)

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.20
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 12 - "CorpusIngestor"
Cohesion: 0.14
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 13 - "fmdv_v"
Cohesion: 0.07
Nodes (14): Variants, min_conforming(), _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), _date_index(), _date_values() (+6 more)

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.09
Nodes (9): AutoValidateConfig, build_pattern_index(), _iter_corpus_columns(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex (+1 more)

### Community 16 - "check_drift"
Cohesion: 0.10
Nodes (7): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "raha/config.py"
Cohesion: 0.13
Nodes (6): ColumnPredictions, train_and_predict(), _default_classifier_factory(), _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 19 - "get_spec"
Cohesion: 0.12
Nodes (6): all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.09
Nodes (8): _clean(), fmdv_h(), matches(), indexable_values(), fpr_column(), impurity(), TestIndexableValues, TestMatching

### Community 21 - "hierarchy.py"
Cohesion: 0.06
Nodes (22): _conforms(), _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs() (+14 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 23 - "pipeline.py"
Cohesion: 0.12
Nodes (7): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 24 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 25 - "builder.py"
Cohesion: 0.08
Nodes (4): _require_min_rows(), InsufficientDataError, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 26 - "logging_utils.py"
Cohesion: 0.10
Nodes (6): configure_logging(), get_logger(), log_duration(), TestConfigureLogging, TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.14
Nodes (6): _score_column(), finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "ErrorType"
Cohesion: 0.11
Nodes (9): main(), parse_args(), _run(), get_spark(), ErrorType, test_main_installs_logging(), TestMain, TestParseArgs (+1 more)

### Community 29 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 30 - "AlgorithmResult"
Cohesion: 0.17
Nodes (3): Combine, AlgorithmResult, TestAlgorithmResult

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "numpy"
Cohesion: 0.10
Nodes (10): build_column_features(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies (+2 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.16
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.16
Nodes (10): spark_session(), SparkUnavailable, _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate() (+2 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (26): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+18 more)

### Community 38 - "pandas"
Cohesion: 0.15
Nodes (12): main(), RahaConfig, RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler() (+4 more)

### Community 39 - "HeuristicLabeler"
Cohesion: 0.20
Nodes (4): build_all_features(), ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.14
Nodes (10): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, _delta_jars(), _download() (+2 more)

### Community 43 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 44 - "featurization.py"
Cohesion: 0.10
Nodes (13): _score_pair(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+5 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "metrics/spelling.py"
Cohesion: 0.26
Nodes (7): require_min_size(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 47 - "ValidationError"
Cohesion: 0.18
Nodes (5): fd_compliance_ratio(), FDResult, minority_violation_rows(), ValidationError, TestFunctionalDependency

### Community 48 - "list_algorithms"
Cohesion: 0.15
Nodes (9): Check it works, list_algorithms(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), test_builtin_algorithms_are_registered(), TestPluginDiscovery (+1 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.12
Nodes (16): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring (+8 more)

### Community 50 - "algorithms/raha.md"
Cohesion: 0.33
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.11
Nodes (14): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), get_algorithm_class(), _load_entry_points(), register_algorithm() (+6 more)

### Community 53 - "docs/index.md"
Cohesion: 0.19
Nodes (6): At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box, Why a common interface

### Community 54 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "labeling.py"
Cohesion: 0.07
Nodes (20): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results (+12 more)

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 61 - "_score_single_column"
Cohesion: 0.15
Nodes (4): _coerce_numeric(), _score_single_column(), TestCoerceNumeric, TestScoreSingleColumn

### Community 63 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 65 - "score"
Cohesion: 0.18
Nodes (11): Reading the output, Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Comparing algorithms, Find the cells they agree on, Mixed inputs (+3 more)

### Community 66 - "algorithms/uni-detect.md"
Cohesion: 0.24
Nodes (4): Getting started, Installation, Installing from source, Pick your extra

### Community 68 - "redact_evidence"
Cohesion: 0.27
Nodes (3): _hash_value(), redact_evidence(), TestRedactEvidence

### Community 69 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 70 - "confusion_metrics"
Cohesion: 0.11
Nodes (12): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Which 5 datasets, and why (+4 more)

### Community 71 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.14
Nodes (8): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestRedactEvidence, TestUnityCatalogLocation, config(), config()

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 85 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.40
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 89 - "open_detect/__init__.py"
Cohesion: 0.08
Nodes (13): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, TestCandidate (+5 more)

### Community 92 - "ConfigurationError"
Cohesion: 0.20
Nodes (6): Concepts, Configuration objects, Errors, One contract: `detect()`, _validate_edges(), ConfigurationError

### Community 93 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 100 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 103 - "OpenDetectError"
Cohesion: 0.16
Nodes (10): The registry, Errors, OpenDetectError, UnknownAlgorithmError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error(), test_open_detect_error_is_catchable_broadly() (+2 more)

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 575 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `CorpusStatsStore`, `API reference`, `wiki_subset/run_benchmark.py`, `UniDetect`, `FailureCounts`, `_StubDetector`, `get_spec`, `pipeline.py`, `builder.py`, `logging_utils.py`, `main`, `real_world_gov/run_benchmark.py`, `conftest.py`, `featurization.py`, `ErrorDetectionAlgorithm`, `_score_single_column`, `.detect`, `CorpusStatsBuilder`, `open_detect/__init__.py`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CorpusStatsStore` be split into smaller, more focused modules?**
  _Cohesion score 0.057692307692307696 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `API reference`, `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `confusion_metrics`, `PatternIndex`, `fmdv_v`, `check_drift`, `auto_validate/detector.py`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.107) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._