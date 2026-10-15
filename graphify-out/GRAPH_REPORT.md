# Graph Report - open-detect  (2026-10-15)

## Corpus Check
- 153 files · ~123,620 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 2, .properties 1)

## Summary
- 1788 nodes · 4383 edges · 94 communities (78 shown, 16 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 581 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0a0f6c9f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- json
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
- CorpusIngestor
- test_auto_validate_fmdv_v.py
- outliers.py
- AutoValidateConfig
- check_drift
- RahaConfig
- ._new_failure_tracker
- open_detect/__init__.py
- PatternIndex
- patterns.py
- wiki_subset/generate_report.py
- collections_abc
- test_metrics.py
- pipeline.py
- get_logger
- perturb_numeric_outlier
- pandas
- uni_detect/config.py
- AlgorithmResult
- .detect
- numpy
- main
- min_pairwise_edit_distance
- wiki_subset/run_benchmark.py
- AutoValidateAlgorithm
- auto_validate/detector.py
- raha/detector.py
- perturb_spelling
- real_world_gov benchmark results
- conftest.py
- dataset_utils.py
- featurization.py
- `raha`
- RahaDetector
- metrics/functional_dependency.py
- builder.py
- CHANGELOG
- Auto-Validate
- propagate_labels
- .detect
- docs/index.md
- FeatureBucket
- fmdv
- select_datasets.py
- CallableLabeler
- main
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _coerce_numeric
- Contributing
- pytest
- select_fd_column_pairs
- OpenDetectError
- get_spec
- CorpusNotFoundError
- algorithms/index.md
- algorithms/uni-detect.md
- Benchmark: real_world_gov
- ErrorType
- InsufficientDataError
- Uni-Detect
- Raha
- Auto-Validate
- infer_column_data_type
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- DataQualityError
- clean_column
- reference/index.md
- index.py
- Methodology: uni_detect -- mapping real dirty data onto its four error types
- duplicate_value_indices
- open-detect
- `auto_validate`
- Scoring auto_validate
- config
- finite_floats
- config
- TestConfigThreshold

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
- `Writing a class` --references--> `Labeler`  [INFERRED]
  docs/guides/custom-labelers.md → src/open_detect/algorithms/raha/labeling.py
- `How to read them` --references--> `HeuristicLabeler`  [INFERRED]
  docs/benchmarks.md → src/open_detect/algorithms/raha/labeling.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (94 total, 16 thin omitted)

### Community 0 - "json"
Cohesion: 0.10
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 2 - "algorithms/__init__.py"
Cohesion: 0.08
Nodes (22): Check it works, Errors, API reference, ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), get_algorithm() (+14 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.13
Nodes (10): git_commit(), spark_session(), SparkUnavailable, _build_config(), main(), _print_comparison(), _register_table(), run() (+2 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.17
Nodes (7): _score_pair(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 8 - "CorpusStatsStore"
Cohesion: 0.14
Nodes (4): CorpusStatsStore, config(), TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 9 - "UniDetect"
Cohesion: 0.18
Nodes (6): build_spark(), main(), UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.07
Nodes (12): compute(), compute(), _score_fd_pair(), check_failure_threshold(), FailureCounts, FailureCountsAccumulatorParam, compute(), _raise() (+4 more)

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.16
Nodes (13): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main() (+5 more)

### Community 12 - "CorpusIngestor"
Cohesion: 0.14
Nodes (4): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 13 - "test_auto_validate_fmdv_v.py"
Cohesion: 0.14
Nodes (7): _build_index(), _date_index(), _date_values(), TestFmdvV, TestFmdvVh, TestLargeGroups, _time_corpus()

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (8): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestCorpusInputShapes, TestFprAggregation, TestPatternIndex, TestTauPruning

### Community 16 - "check_drift"
Cohesion: 0.14
Nodes (6): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), _make_pattern(), TestCheckDrift

### Community 17 - "RahaConfig"
Cohesion: 0.15
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "._new_failure_tracker"
Cohesion: 0.09
Nodes (8): compute(), compute(), _score_column(), _score_column(), compute(), _score_column(), compute(), _StubDetector

### Community 19 - "open_detect/__init__.py"
Cohesion: 0.09
Nodes (12): Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, __getattr__(), TestCandidate, TestCorpusRecords (+4 more)

### Community 20 - "PatternIndex"
Cohesion: 0.06
Nodes (19): Variants, _clean(), fmdv_h(), InferredPattern, min_conforming(), _coarse_signature(), _fmdv_h_single(), _fmdv_single_segment() (+11 more)

### Community 21 - "patterns.py"
Cohesion: 0.06
Nodes (17): generality_weight(), generalize(), _iter_runs(), Token, tokenize(), _alternatives(), any_pattern(), _best_first_patterns() (+9 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.23
Nodes (12): comparison_table_markdown(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main(), _metrics_table_row(), _ranking_chart() (+4 more)

### Community 23 - "collections_abc"
Cohesion: 0.13
Nodes (7): BaseDetector, make_evidence_json(), FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker

### Community 24 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 26 - "get_logger"
Cohesion: 0.15
Nodes (4): get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.19
Nodes (3): perturb_numeric_outlier(), TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "pandas"
Cohesion: 0.23
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 29 - "uni_detect/config.py"
Cohesion: 0.10
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 30 - "AlgorithmResult"
Cohesion: 0.08
Nodes (19): Through the registry, The shared result schema, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table (+11 more)

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "numpy"
Cohesion: 0.11
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "main"
Cohesion: 0.21
Nodes (5): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.14
Nodes (7): _blocking_keys(), _closest_pair(), differing_token_lengths(), min_pairwise_edit_distance(), _result(), MPDResult, TestSpelling

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.13
Nodes (12): confusion_metrics(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_auto_validate() (+4 more)

### Community 37 - "AutoValidateAlgorithm"
Cohesion: 0.11
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 38 - "auto_validate/detector.py"
Cohesion: 0.23
Nodes (5): _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 39 - "raha/detector.py"
Cohesion: 0.20
Nodes (5): Who answers the labeling questions?, ColumnFeatures, HeuristicLabeler, Labeler, TestHeuristicLabeler

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.14
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.14
Nodes (10): A fully local example, How it works, Install, Reading the detections, Uni-Detect, Usage on Databricks, _delta_jars(), _download() (+2 more)

### Community 43 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 44 - "featurization.py"
Cohesion: 0.08
Nodes (10): bucket_by_edges(), bucket_leftness(), bucket_token_prevalence(), log_transform_fits_better(), token_prevalence(), tokenize(), TestBucketing, TestLogFit (+2 more)

### Community 45 - "`raha`"
Cohesion: 0.15
Nodes (12): Algorithm comparison, By corruption severity, By corruption severity (target-level), By error type, By error type (cell-level), By error type (target-level), Evaluation targets, Evaluation targets (+4 more)

### Community 46 - "RahaDetector"
Cohesion: 0.13
Nodes (11): run_raha(), Scoring raha, main(), RahaDetector, GroundTruthLabeler, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_registered_under_raha() (+3 more)

### Community 47 - "metrics/functional_dependency.py"
Cohesion: 0.19
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 48 - "builder.py"
Cohesion: 0.13
Nodes (10): _require_min_rows(), _score_single_column(), bucket_row_count(), bucket_token_length(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket() (+2 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.13
Nodes (14): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring, Unreleased (+6 more)

### Community 50 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 52 - ".detect"
Cohesion: 0.33
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 53 - "docs/index.md"
Cohesion: 0.22
Nodes (6): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box

### Community 55 - "fmdv"
Cohesion: 0.14
Nodes (5): fmdv(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "select_datasets.py"
Cohesion: 0.46
Nodes (3): candidates(), main(), select()

### Community 57 - "CallableLabeler"
Cohesion: 0.10
Nodes (13): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust (+5 more)

### Community 58 - "main"
Cohesion: 0.22
Nodes (4): main(), parse_args(), TestMain, TestParseArgs

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.22
Nodes (9): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+1 more)

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.24
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 63 - "pytest"
Cohesion: 0.14
Nodes (4): pair_table(), test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_open_detect_error_is_catchable_broadly()

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "OpenDetectError"
Cohesion: 0.12
Nodes (11): Inspecting a pattern, Reading the output, Usage, Concepts, Configuration objects, Errors, One contract: `detect()`, The registry (+3 more)

### Community 67 - "CorpusNotFoundError"
Cohesion: 0.22
Nodes (7): Operational notes, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, CorpusNotFoundError

### Community 68 - "algorithms/index.md"
Cohesion: 0.20
Nodes (6): Algorithms, Fidelity to the papers, Configuration, Detector, Labelers, Raha

### Community 69 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.18
Nodes (11): Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha, Reading the results (+3 more)

### Community 71 - "ErrorType"
Cohesion: 0.15
Nodes (7): all_specs(), ErrorTypeSpec, ColumnDataType, ComparisonDirection, ErrorType, TestScoreFdPair, TestAllSpecs

### Community 72 - "InsufficientDataError"
Cohesion: 0.20
Nodes (4): require_min_size(), uniqueness_ratio(), InsufficientDataError, TestUniquenessRatio

### Community 73 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 74 - "Raha"
Cohesion: 0.29
Nodes (7): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 76 - "infer_column_data_type"
Cohesion: 0.10
Nodes (8): infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), TestDataTypeInference, TestFloatLike, TestIntegerLike, TestMixedAlphanumeric

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.18
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.15
Nodes (7): ensure_schema_exists(), UnityCatalogLocation, _validate_edges(), ConfigurationError, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation

### Community 81 - "DataQualityError"
Cohesion: 0.33
Nodes (3): Configuration, DataQualityError, TestDetectorFailureGate

### Community 82 - "clean_column"
Cohesion: 0.28
Nodes (3): clean_column(), _is_null(), TestCleanColumn

### Community 83 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 84 - "index.py"
Cohesion: 0.08
Nodes (14): _append_literal(), _char_class(), _class_of_token(), _is_numeric(), matches(), _parse(), _part_matches(), token_count() (+6 more)

### Community 85 - "Methodology: uni_detect -- mapping real dirty data onto its four error types"
Cohesion: 0.40
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 88 - "`auto_validate`"
Cohesion: 0.40
Nodes (5): `auto_validate`, By corruption severity, By error type (cell-level), By error type (target-level), Evaluation targets

### Community 89 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 549 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ErrorType` connect `ErrorType` to `json`, `algorithms/__init__.py`, `real_world_gov/run_benchmark.py`, `CorpusStatsStore`, `UniDetect`, `FailureCounts`, `._new_failure_tracker`, `open_detect/__init__.py`, `collections_abc`, `pipeline.py`, `uni_detect/config.py`, `main`, `wiki_subset/run_benchmark.py`, `conftest.py`, `featurization.py`, `builder.py`, `.detect`, `FeatureBucket`, `main`, `get_spec`, `CorpusStatsBuilder`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `json` be split into smaller, more focused modules?**
  _Cohesion score 0.10359408033826638 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `OpenDetectError`, `algorithms/__init__.py`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `AutoValidateAlgorithm`, `auto_validate/detector.py`, `test_auto_validate_fmdv_v.py`, `UnityCatalogLocation`, `check_drift`, `index.py`, `PatternIndex`, `fmdv`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 53 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._