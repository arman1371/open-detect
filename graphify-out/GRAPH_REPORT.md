# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 153 files · ~124,507 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1816 nodes · 4486 edges · 98 communities (77 shown, 21 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 597 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3052b589`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CorpusStatsStore
- UniDetectConfig
- registry.py
- wiki_subset/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturb_functional_dependency
- PatternIndex
- UniDetect
- FailureCounts
- real_world_gov/generate_report.py
- CorpusIngestor
- fmdv_v
- outliers.py
- AutoValidateConfig
- InferredPattern
- RahaConfig
- _StubDetector
- get_spec
- auto_validate/detector.py
- hierarchy.py
- wiki_subset/generate_report.py
- ErrorType
- test_metrics.py
- open_detect/exceptions.py
- builder.py
- perturb_numeric_outlier
- pandas
- build_corpus_statistics.py
- AlgorithmResult
- .detect
- raha/strategies.py
- main
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- GroundTruthLabeler
- HeuristicLabeler
- perturb_spelling
- real_world_gov benchmark results
- conftest.py
- bucket_by_edges
- featurization.py
- `auto_validate`
- metrics/spelling.py
- ValidationError
- _score_single_column
- CHANGELOG
- algorithms/raha.md
- propagate_labels
- algorithms/__init__.py
- docs/index.md
- _is_null
- fmdv
- argparse
- labeling.py
- Scoring auto_validate
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- algorithms/index.md
- Benchmarks
- select_fd_column_pairs
- score
- config
- Auto-Validate
- algorithms/uni-detect.md
- confusion_metrics
- open_detect/__init__.py
- uniqueness_ratio
- Uni-Detect
- Raha
- Auto-Validate
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- check_failure_threshold
- clean_column
- __getattr__
- collections_abc
- test_corpus_and_detectors.py
- open-detect
- FailureCountsAccumulatorParam
- FeatureBucket
- TestAttempt
- log_transform_fits_better
- ConfigurationError
- infer_column_data_type
- TestConfigThreshold
- `raha`
- finite_floats
- OpenDetectError

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 115 edges
2. `ErrorType` - 84 edges
3. `UniDetectConfig` - 74 edges
4. `FailureCounts` - 56 edges
5. `build_pattern_index()` - 45 edges
6. `UniDetect` - 38 edges
7. `AutoValidateAlgorithm` - 36 edges
8. `RahaConfig` - 33 edges
9. `PatternIndex` - 32 edges
10. `ConfigurationError` - 32 edges

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

## Communities (98 total, 21 thin omitted)

### Community 0 - "CorpusStatsStore"
Cohesion: 0.05
Nodes (22): Operational notes, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, diff_fingerprints(), property_key() (+14 more)

### Community 2 - "registry.py"
Cohesion: 0.10
Nodes (18): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, get_algorithm() (+10 more)

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.13
Nodes (10): git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturb_functional_dependency"
Cohesion: 0.13
Nodes (9): _score_column(), duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency (+1 more)

### Community 8 - "PatternIndex"
Cohesion: 0.08
Nodes (8): _fmdv_single_segment(), _segment_fmdv_v(), PatternIndex, any_pattern(), matching_pattern(), patterns_of(), sorted_patterns(), TestPatternsOf

### Community 9 - "UniDetect"
Cohesion: 0.20
Nodes (7): build_spark(), main(), UniDetect, __getattr__(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.19
Nodes (6): compute(), _score_fd_pair(), compute(), compute(), FailureCounts, TestPerElementFunctions

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.20
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 12 - "CorpusIngestor"
Cohesion: 0.16
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 13 - "fmdv_v"
Cohesion: 0.09
Nodes (13): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _build_index(), _date_index(), _date_values() (+5 more)

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.07
Nodes (11): AutoValidateConfig, _segment_dp(), build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (9): check_drift(), _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift (+1 more)

### Community 17 - "RahaConfig"
Cohesion: 0.14
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 19 - "get_spec"
Cohesion: 0.08
Nodes (9): compute(), _score_pair(), FailureTracker, all_specs(), ErrorTypeSpec, get_spec(), TestScoreFdPair, TestAllSpecs (+1 more)

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.08
Nodes (11): min_conforming(), _fmdv_h_single(), _segment_fmdv_vh(), matches(), indexable_values(), _iter_corpus_columns(), fpr_column(), impurity() (+3 more)

### Community 21 - "hierarchy.py"
Cohesion: 0.07
Nodes (19): _append_literal(), _char_class(), _class_of_token(), generality_weight(), generalize(), _is_numeric(), _iter_runs(), _parse() (+11 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.20
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 23 - "ErrorType"
Cohesion: 0.17
Nodes (7): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, ErrorType

### Community 24 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 26 - "builder.py"
Cohesion: 0.11
Nodes (5): _require_min_rows(), get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.19
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "pandas"
Cohesion: 0.23
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 29 - "build_corpus_statistics.py"
Cohesion: 0.08
Nodes (14): ensure_schema_exists(), list_tables(), list_tables_matching(), table_exists(), parse_args(), _run(), get_spark(), UnityCatalogError (+6 more)

### Community 30 - "AlgorithmResult"
Cohesion: 0.13
Nodes (5): Combine, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "main"
Cohesion: 0.21
Nodes (5): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (14): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _build_config(), _dataset_frames(), main() (+6 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.11
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "GroundTruthLabeler"
Cohesion: 0.12
Nodes (12): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), main(), GroundTruthLabeler, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler() (+4 more)

### Community 39 - "HeuristicLabeler"
Cohesion: 0.21
Nodes (9): Who answers the labeling questions?, Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, ColumnFeatures, HeuristicLabeler (+1 more)

### Community 40 - "perturb_spelling"
Cohesion: 0.29
Nodes (3): _score_column(), perturb_spelling(), TestPerturbSpelling

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.13
Nodes (11): A fully local example, Configuration, How it works, Install, Reading the detections, Uni-Detect, Usage on Databricks, _delta_jars() (+3 more)

### Community 43 - "bucket_by_edges"
Cohesion: 0.21
Nodes (3): bucket_by_edges(), bucket_leftness(), TestBucketing

### Community 44 - "featurization.py"
Cohesion: 0.11
Nodes (12): bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket(), ColumnDataType (+4 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 47 - "ValidationError"
Cohesion: 0.18
Nodes (5): fd_compliance_ratio(), FDResult, minority_violation_rows(), ValidationError, TestFunctionalDependency

### Community 48 - "_score_single_column"
Cohesion: 0.29
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 49 - "CHANGELOG"
Cohesion: 0.12
Nodes (16): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring (+8 more)

### Community 50 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "algorithms/__init__.py"
Cohesion: 0.12
Nodes (11): API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), RahaDetector, register_algorithm(), UniDetectAlgorithm (+3 more)

### Community 53 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 54 - "_is_null"
Cohesion: 0.22
Nodes (5): _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "labeling.py"
Cohesion: 0.13
Nodes (9): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, Labeler (+1 more)

### Community 58 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 63 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.19
Nodes (4): select_fd_column_pairs(), pair_table(), TestSelectFdColumnPairs, by_name()

### Community 65 - "score"
Cohesion: 0.15
Nodes (11): Inspecting a pattern, Reading the output, Usage, Through the registry, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat (+3 more)

### Community 68 - "Auto-Validate"
Cohesion: 0.22
Nodes (7): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly, Errors

### Community 69 - "algorithms/uni-detect.md"
Cohesion: 0.18
Nodes (6): Installation, Installing from source, Pick your extra, Registry, Registry and results, Result types

### Community 70 - "confusion_metrics"
Cohesion: 0.09
Nodes (16): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+8 more)

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
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.22
Nodes (5): UnityCatalogLocation, TestEnsureSchemaExists, TestUnityCatalogLocation, config(), config()

### Community 81 - "check_failure_threshold"
Cohesion: 0.20
Nodes (3): check_failure_threshold(), DataQualityError, TestCheckFailureThreshold

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 84 - "collections_abc"
Cohesion: 0.16
Nodes (4): compute(), _score_column(), require_min_size(), InsufficientDataError

### Community 85 - "test_corpus_and_detectors.py"
Cohesion: 0.33
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 89 - "FeatureBucket"
Cohesion: 0.12
Nodes (8): Candidate, Detection, FeatureBucket, MetricObservation, TestCandidate, TestDetection, TestFeatureBucket, TestMetricObservation

### Community 92 - "ConfigurationError"
Cohesion: 0.18
Nodes (4): _validate_edges(), main(), ConfigurationError, TestMain

### Community 93 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 100 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 103 - "OpenDetectError"
Cohesion: 0.12
Nodes (15): Concepts, Configuration objects, Errors, One contract: `detect()`, The registry, The shared result schema, IndexNotBuiltError, OpenDetectError (+7 more)

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 559 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `CorpusStatsStore`, `wiki_subset/run_benchmark.py`, `UniDetect`, `FailureCounts`, `_StubDetector`, `get_spec`, `open_detect/exceptions.py`, `builder.py`, `build_corpus_statistics.py`, `main`, `real_world_gov/run_benchmark.py`, `conftest.py`, `featurization.py`, `_score_single_column`, `algorithms/__init__.py`, `open_detect/__init__.py`, `CorpusStatsBuilder`, `collections_abc`, `FeatureBucket`, `ConfigurationError`?**
  _High betweenness centrality (0.133) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CorpusStatsStore` be split into smaller, more focused modules?**
  _Cohesion score 0.053994732221246705 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `confusion_metrics`, `OpenDetectError`, `PatternIndex`, `fmdv_v`, `InferredPattern`, `auto_validate/detector.py`, `algorithms/__init__.py`, `_is_null`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 53 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._