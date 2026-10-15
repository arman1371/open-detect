# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 153 files · ~122,534 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1752 nodes · 4302 edges · 104 communities (74 shown, 30 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 578 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e5bcac1c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CorpusStatsStore
- UniDetectConfig
- registry.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- UniDetect
- CorpusIngestor
- FailureCounts
- real_world_gov/generate_report.py
- check_failure_threshold
- raha/detector.py
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- list_tables_matching
- open_detect/__init__.py
- fmdv_vh
- patterns.py
- wiki_subset/generate_report.py
- ErrorType
- test_metrics.py
- tokenize
- get_logger
- main
- FailureCountsAccumulatorParam
- builder.py
- AlgorithmResult
- .detect
- numpy
- PatternIndex
- metrics/spelling.py
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- API reference
- FeatureBucket
- Quickstart
- real_world_gov benchmark results
- conftest.py
- dataset_utils.py
- bucket_by_edges
- `auto_validate`
- GroundTruthLabeler
- metrics/functional_dependency.py
- featurization.py
- CHANGELOG
- Auto-Validate
- test_raha_labeling.py
- UniDetectAlgorithm
- docs/index.md
- _score_single_column
- fmdv
- argparse
- labeling.py
- uni_detect/config.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- Commit conventions and releases
- OpenDetectError
- select_fd_column_pairs
- Comparing algorithms
- TestAttempt
- Raha
- choosing-an-algorithm.md
- Benchmark: real_world_gov
- get_spec
- perturb_uniqueness
- Uni-Detect
- DataQualityError
- Auto-Validate
- infer_column_data_type
- _segment_dp
- CorpusStatsBuilder
- UnityCatalogLocation
- test_featurization.py
- clean_column
- algorithms/uni-detect.md
- pandas
- spark_session.py
- open-detect
- Layout
- ConfigurationError
- is_mixed_alphanumeric
- main
- is_float_like
- is_integer_like
- TestConfigThreshold
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- `raha`
- parse_args
- installation.md
- indexable_values
- uni_detect/__init__.py
- _default_classifier_factory
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
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py
- `Configuration` --references--> `RahaConfig`  [INFERRED]
  docs/algorithms/raha.md → src/open_detect/algorithms/raha/config.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/open_detect/algorithms/uni_detect/pipeline.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (104 total, 30 thin omitted)

### Community 0 - "CorpusStatsStore"
Cohesion: 0.06
Nodes (21): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, diff_fingerprints(), property_key(), read_build_config() (+13 more)

### Community 2 - "registry.py"
Cohesion: 0.15
Nodes (10): get_algorithm_class(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), test_builtin_algorithms_are_registered(), test_get_algorithm_constructs_with_args(), test_register_lazy_is_lazy() (+2 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.16
Nodes (10): spark_session(), SparkUnavailable, _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate() (+2 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.14
Nodes (7): perturb_functional_dependency(), perturb_numeric_outlier(), perturb_spelling(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbNumericOutlier, TestPerturbSpelling

### Community 8 - "UniDetect"
Cohesion: 0.23
Nodes (6): main(), UniDetect, __getattr__(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 9 - "CorpusIngestor"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 10 - "FailureCounts"
Cohesion: 0.16
Nodes (10): compute(), _score_fd_pair(), make_evidence_json(), compute(), compute(), compute(), compute(), FailureCounts (+2 more)

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.16
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main() (+5 more)

### Community 13 - "raha/detector.py"
Cohesion: 0.17
Nodes (9): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema() (+1 more)

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (12): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, _build_index(), TestFmdvV, TestFmdvVh, _time_corpus() (+4 more)

### Community 16 - "check_drift"
Cohesion: 0.14
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.11
Nodes (12): ColumnPredictions, train_and_predict(), RahaConfig, build_all_features(), build_column_features(), _features(), TestClassifierTrainingPath, TestDegenerateCases (+4 more)

### Community 18 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 19 - "open_detect/__init__.py"
Cohesion: 0.08
Nodes (12): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, TestCandidate, TestCorpusRecords (+4 more)

### Community 20 - "fmdv_vh"
Cohesion: 0.15
Nodes (6): _coarse_signature(), fmdv_vh(), _date_index(), _date_values(), TestCoarseSignature, TestLargeGroups

### Community 21 - "patterns.py"
Cohesion: 0.06
Nodes (19): generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize(), _alternatives(), any_pattern() (+11 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.24
Nodes (12): comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart() (+4 more)

### Community 23 - "ErrorType"
Cohesion: 0.15
Nodes (7): BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, ErrorType

### Community 24 - "test_metrics.py"
Cohesion: 0.22
Nodes (3): duplicate_value_indices(), TestDropNulls, TestDuplicateValueIndices

### Community 25 - "tokenize"
Cohesion: 0.19
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "get_logger"
Cohesion: 0.12
Nodes (5): get_logger(), log_duration(), pair_table(), TestGetLogger, TestLogDuration

### Community 27 - "main"
Cohesion: 0.21
Nodes (5): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestParseArgs

### Community 30 - "AlgorithmResult"
Cohesion: 0.12
Nodes (9): Reading the output, Through the registry, The shared result schema, Combine, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult (+1 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "numpy"
Cohesion: 0.11
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "PatternIndex"
Cohesion: 0.10
Nodes (5): min_conforming(), _fmdv_h_single(), _segment_fmdv_vh(), PatternIndex, TestMinConforming

### Community 35 - "metrics/spelling.py"
Cohesion: 0.15
Nodes (6): _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, TestSpelling

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.12
Nodes (13): confusion_metrics(), git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+5 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.09
Nodes (9): Inspecting a pattern, Usage, AutoValidateAlgorithm, _feasible_evidence(), _infeasible_evidence(), _non_null_cells(), segment(), _make_tiny_corpus() (+1 more)

### Community 38 - "API reference"
Cohesion: 0.15
Nodes (11): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+3 more)

### Community 40 - "Quickstart"
Cohesion: 0.50
Nodes (4): Auto-Validate: learn patterns from clean columns, Quickstart, Reading results, Uni-Detect: score tables in Unity Catalog

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.13
Nodes (11): A fully local example, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks, _delta_jars() (+3 more)

### Community 43 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 44 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.20
Nodes (3): main(), GroundTruthLabeler, TestGroundTruthLabeler

### Community 47 - "metrics/functional_dependency.py"
Cohesion: 0.19
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 48 - "featurization.py"
Cohesion: 0.13
Nodes (12): _score_pair(), _score_column(), _score_column(), _score_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket() (+4 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.18
Nodes (10): Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring, Unreleased, v0.2.0 (2026-10-08), v0.2.1 (2026-10-14) (+2 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.18
Nodes (8): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly, Algorithms, Fidelity to the papers

### Community 52 - "UniDetectAlgorithm"
Cohesion: 0.27
Nodes (4): UniDetectAlgorithm, _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "docs/index.md"
Cohesion: 0.31
Nodes (3): Getting started, open-detect, What is in the box

### Community 54 - "_score_single_column"
Cohesion: 0.31
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 55 - "fmdv"
Cohesion: 0.11
Nodes (8): Variants, _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.46
Nodes (3): candidates(), main(), select()

### Community 57 - "labeling.py"
Cohesion: 0.10
Nodes (16): Reading the output, Usage, Who answers the labeling questions?, Raha: find errors with a few labels, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility (+8 more)

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "Commit conventions and releases"
Cohesion: 0.14
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 63 - "OpenDetectError"
Cohesion: 0.15
Nodes (11): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, Errors, UnknownAlgorithmError, OpenDetectError (+3 more)

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "Comparing algorithms"
Cohesion: 0.40
Nodes (5): Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 68 - "Raha"
Cohesion: 0.17
Nodes (9): Configuration, How it works, Install, Raha, Scope, Configuration, Detector, Labelers (+1 more)

### Community 69 - "choosing-an-algorithm.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, At a glance, Choosing an algorithm, Rules of thumb

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.18
Nodes (11): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha, Reading the results (+3 more)

### Community 71 - "get_spec"
Cohesion: 0.09
Nodes (8): _require_min_rows(), all_specs(), ErrorTypeSpec, get_spec(), InsufficientDataError, TestScoreFdPair, TestAllSpecs, TestGetSpec

### Community 72 - "perturb_uniqueness"
Cohesion: 0.21
Nodes (5): uniqueness_ratio(), _max_drop(), perturb_uniqueness(), TestUniquenessRatio, TestPerturbUniqueness

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "DataQualityError"
Cohesion: 0.25
Nodes (4): Configuration, DataQualityError, _StubDetector, TestDetectorFailureGate

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "_segment_dp"
Cohesion: 0.28
Nodes (3): _segment_dp(), TestSegmentDp, solve()

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.18
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config(), config()

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 83 - "algorithms/uni-detect.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 84 - "pandas"
Cohesion: 0.07
Nodes (17): _is_null(), _value_matches(), IndexNotBuiltError, InferredPattern, _fmdv_single_segment(), fmdv_v(), _infer_cmp(), _segment_fmdv_v() (+9 more)

### Community 88 - "Layout"
Cohesion: 0.25
Nodes (8): Expected weakness: read Auto-Validate's low recall honestly, Layout, Scoring auto_validate, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), The `m` override, Timing

### Community 95 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.40
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 96 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 98 - "installation.md"
Cohesion: 0.50
Nodes (3): Installation, Installing from source, Pick your extra

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 543 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **30 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `CorpusStatsStore`, `real_world_gov/run_benchmark.py`, `UniDetect`, `FailureCounts`, `open_detect/__init__.py`, `main`, `builder.py`, `wiki_subset/run_benchmark.py`, `API reference`, `FeatureBucket`, `conftest.py`, `featurization.py`, `UniDetectAlgorithm`, `_score_single_column`, `uni_detect/config.py`, `get_spec`, `DataQualityError`, `CorpusStatsBuilder`, `main`, `parse_args`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CorpusStatsStore` be split into smaller, more focused modules?**
  _Cohesion score 0.055178652193577565 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `PatternIndex`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `AutoValidateAlgorithm`, `API reference`, `_segment_dp`, `check_drift`, `pandas`, `fmdv_vh`, `fmdv`, `ConfigurationError`, `OpenDetectError`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 53 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._