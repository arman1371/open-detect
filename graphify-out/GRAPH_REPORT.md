# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 153 files · ~124,040 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1800 nodes · 4411 edges · 105 communities (83 shown, 22 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 582 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8ae637bf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- OpenDetectError
- wiki_subset/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- perturbation.py
- CorpusStatsStore
- UniDetect
- FailureCounts
- real_world_gov/generate_report.py
- CorpusIngestor
- fmdv_v
- numpy
- AutoValidateConfig
- check_drift
- RahaConfig
- _StubDetector
- get_spec
- auto_validate/detector.py
- patterns.py
- wiki_subset/generate_report.py
- collections_abc
- test_metrics.py
- builder.py
- get_logger
- perturb_numeric_outlier
- pandas
- catalog.py
- AlgorithmResult
- cluster_column
- gaussian_outlier_strategies
- main
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- AutoValidateAlgorithm
- GroundTruthLabeler
- HeuristicLabeler
- perturb_spelling
- real_world_gov benchmark results
- conftest.py
- dataset_utils.py
- featurization.py
- `auto_validate`
- RahaDetector
- metrics/functional_dependency.py
- _score_single_column
- CHANGELOG
- reference/index.md
- .detect
- UniDetectAlgorithm
- concepts.md
- FeatureBucket
- _build_index
- argparse
- labeling.py
- build_corpus_statistics.py
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- Contributing
- infer_column_data_type
- select_fd_column_pairs
- Comparing algorithms
- Running on Databricks
- algorithms/uni-detect.md
- benchmarks.md
- Benchmark: real_world_gov
- ErrorType
- uniqueness_ratio
- Uni-Detect
- Raha
- Auto-Validate
- tokenize
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- check_failure_threshold
- clean_column
- Registry and results
- index.py
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- raha/detector.py
- open-detect
- FailureCountsAccumulatorParam
- ColumnDataType
- TestAttempt
- log_transform_fits_better
- ConfigurationError
- text_utils.py
- TestConfigThreshold
- fd_violation_strategies
- Detection
- diff_fingerprints
- is_integer_like
- `raha`
- Quickstart
- finite_floats
- Concepts

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
- `The registry` --references--> `UnknownAlgorithmError`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/registry.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (105 total, 22 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.15
Nodes (10): property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, TestLegacyCorpus, TestMismatch (+2 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.17
Nodes (3): UniDetectConfig, TestUniDetectConfig, config()

### Community 2 - "OpenDetectError"
Cohesion: 0.09
Nodes (21): Check it works, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, Errors, get_algorithm() (+13 more)

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.14
Nodes (10): git_commit(), spark_session(), SparkUnavailable, _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison() (+2 more)

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
Cohesion: 0.14
Nodes (6): Errors, Practical advice, CorpusStatsStore, CorpusNotFoundError, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 9 - "UniDetect"
Cohesion: 0.20
Nodes (7): build_spark(), main(), UniDetect, __getattr__(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.17
Nodes (8): compute(), _score_fd_pair(), compute(), compute(), compute(), compute(), FailureCounts, TestPerElementFunctions

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.29
Nodes (9): _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name(), _slug() (+1 more)

### Community 12 - "CorpusIngestor"
Cohesion: 0.14
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 13 - "fmdv_v"
Cohesion: 0.08
Nodes (10): _coarse_signature(), fmdv_v(), _build_index(), _date_index(), _date_values(), TestCoarseSignature, TestFmdvV, TestFmdvVh (+2 more)

### Community 14 - "numpy"
Cohesion: 0.12
Nodes (10): drop_nulls(), require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores() (+2 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (10): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestFprAggregation (+2 more)

### Community 16 - "check_drift"
Cohesion: 0.10
Nodes (6): check_drift(), _clean_series(), _fisher_two_tailed(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.14
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 19 - "get_spec"
Cohesion: 0.14
Nodes (3): get_spec(), TestScoreFdPair, TestGetSpec

### Community 20 - "auto_validate/detector.py"
Cohesion: 0.07
Nodes (18): Variants, _clean(), fmdv(), fmdv_h(), InferredPattern, min_conforming(), _fmdv_h_single(), _fmdv_single_segment() (+10 more)

### Community 21 - "patterns.py"
Cohesion: 0.06
Nodes (17): generality_weight(), generalize(), _iter_runs(), Token, token_count(), tokenize(), _alternatives(), any_pattern() (+9 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.15
Nodes (16): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart() (+8 more)

### Community 23 - "collections_abc"
Cohesion: 0.16
Nodes (7): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 24 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 25 - "builder.py"
Cohesion: 0.08
Nodes (4): _require_min_rows(), InsufficientDataError, test_error_message_is_preserved(), test_open_detect_error_is_catchable_broadly()

### Community 26 - "get_logger"
Cohesion: 0.12
Nodes (5): get_logger(), log_duration(), pair_table(), TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.20
Nodes (4): _score_column(), perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "pandas"
Cohesion: 0.21
Nodes (7): main(), build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 29 - "catalog.py"
Cohesion: 0.14
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 30 - "AlgorithmResult"
Cohesion: 0.14
Nodes (9): Through the registry, The shared result schema, 1. Implement `ErrorDetectionAlgorithm`, Why a common interface, API reference, AlgorithmResult, CellResult, TestAlgorithmResult (+1 more)

### Community 31 - "cluster_column"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "gaussian_outlier_strategies"
Cohesion: 0.14
Nodes (7): gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestGaussianOutlierStrategies, TestHistogramOutlierStrategies, TestPatternCharacterStrategies

### Community 34 - "main"
Cohesion: 0.21
Nodes (5): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.10
Nodes (7): _blocking_keys(), _closest_pair(), differing_token_lengths(), min_pairwise_edit_distance(), _result(), MPDResult, TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (13): confusion_metrics(), _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate(), run_raha() (+5 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.05
Nodes (27): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+19 more)

### Community 38 - "GroundTruthLabeler"
Cohesion: 0.18
Nodes (6): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), GroundTruthLabeler, TestGroundTruthLabeler

### Community 39 - "HeuristicLabeler"
Cohesion: 0.29
Nodes (6): Reading the output, Usage, Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 40 - "perturb_spelling"
Cohesion: 0.29
Nodes (3): _score_column(), perturb_spelling(), TestPerturbSpelling

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.12
Nodes (11): A fully local example, How it works, Install, Operational notes, Reading the detections, Uni-Detect, Usage on Databricks, _delta_jars() (+3 more)

### Community 43 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 44 - "featurization.py"
Cohesion: 0.10
Nodes (13): _score_pair(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket() (+5 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "RahaDetector"
Cohesion: 0.36
Nodes (5): RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 47 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 48 - "_score_single_column"
Cohesion: 0.31
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 49 - "CHANGELOG"
Cohesion: 0.12
Nodes (16): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring (+8 more)

### Community 50 - "reference/index.md"
Cohesion: 0.25
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 52 - "UniDetectAlgorithm"
Cohesion: 0.19
Nodes (5): UniDetectAlgorithm, __getattr__(), _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "concepts.md"
Cohesion: 0.28
Nodes (4): Getting started, At a glance, Choosing an algorithm, Rules of thumb

### Community 55 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 57 - "labeling.py"
Cohesion: 0.14
Nodes (9): Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function, Writing a class, CallableLabeler, Labeler (+1 more)

### Community 58 - "build_corpus_statistics.py"
Cohesion: 0.11
Nodes (6): main(), parse_args(), get_spark(), TestMain, TestParseArgs, TestGetSpark

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "Comparing algorithms"
Cohesion: 0.25
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 67 - "Running on Databricks"
Cohesion: 0.40
Nodes (4): Job arguments, Jobs, Notebooks, Running on Databricks

### Community 68 - "algorithms/uni-detect.md"
Cohesion: 0.26
Nodes (4): Algorithms, Fidelity to the papers, open-detect, What is in the box

### Community 69 - "benchmarks.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.29
Nodes (7): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Which 5 datasets, and why

### Community 71 - "ErrorType"
Cohesion: 0.12
Nodes (7): all_specs(), ErrorTypeSpec, ComparisonDirection, ErrorType, TestAllSpecs, test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class()

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Raha"
Cohesion: 0.40
Nodes (5): Configuration, How it works, Install, Raha, Scope

### Community 75 - "Auto-Validate"
Cohesion: 0.29
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 76 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.21
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.18
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config(), config()

### Community 81 - "check_failure_threshold"
Cohesion: 0.19
Nodes (4): Configuration, check_failure_threshold(), DataQualityError, TestCheckFailureThreshold

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "Registry and results"
Cohesion: 0.67
Nodes (3): Registry, Registry and results, Result types

### Community 84 - "index.py"
Cohesion: 0.07
Nodes (13): _conforms(), DriftResult, _append_literal(), _char_class(), _class_of_token(), _is_numeric(), _parse(), _part_matches() (+5 more)

### Community 85 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.40
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 86 - "raha/detector.py"
Cohesion: 0.19
Nodes (6): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), register_algorithm(), decorator()

### Community 89 - "ColumnDataType"
Cohesion: 0.16
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 93 - "text_utils.py"
Cohesion: 0.17
Nodes (4): is_float_like(), is_mixed_alphanumeric(), TestFloatLike, TestMixedAlphanumeric

### Community 100 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 101 - "Quickstart"
Cohesion: 0.40
Nodes (5): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog

### Community 103 - "Concepts"
Cohesion: 0.50
Nodes (4): Concepts, Configuration objects, One contract: `detect()`, The registry

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 554 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **22 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `wiki_subset/run_benchmark.py`, `CorpusStatsStore`, `UniDetect`, `FailureCounts`, `_StubDetector`, `get_spec`, `collections_abc`, `builder.py`, `AlgorithmResult`, `main`, `real_world_gov/run_benchmark.py`, `conftest.py`, `featurization.py`, `_score_single_column`, `UniDetectAlgorithm`, `FeatureBucket`, `build_corpus_statistics.py`, `CorpusStatsBuilder`, `raha/detector.py`, `ColumnDataType`, `Detection`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.14838709677419354 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `AutoValidateAlgorithm`, `Concepts`, `fmdv_v`, `check_drift`, `index.py`, `auto_validate/detector.py`, `_build_index`, `ConfigurationError`, `AlgorithmResult`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 53 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._