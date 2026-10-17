# Graph Report - ope87-wt  (2026-10-17)

## Corpus Check
- 165 files · ~135,534 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 244 file(s) not represented in the graph (top: .csv 227, .j2 10, (none) 4)

## Summary
- 1963 nodes · 4480 edges · 111 communities (83 shown, 28 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 476 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8766a1d4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- UniDetectConfig
- get_algorithm
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
- RahaConfig
- _StubDetector
- get_spec
- index.py
- patterns.py
- wiki_subset/generate_report.py
- ErrorType
- test_metrics.py
- enums.py
- logging_utils.py
- perturb_numeric_outlier
- main
- list_tables_matching
- AlgorithmResult
- raha/detector.py
- raha/strategies.py
- main
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- Auto-Validate
- RahaDetector
- HeuristicLabeler
- perturb_spelling
- real_world_gov benchmark results
- spark_session.py
- What You Must Do When Invoked
- featurization.py
- `auto_validate`
- metrics/spelling.py
- InsufficientDataError
- registry.py
- CHANGELOG
- ValidationError
- .detect
- ErrorDetectionAlgorithm
- algorithms/uni-detect.md
- auto_validate/detector.py
- fmdv
- select_datasets.py
- labeling.py
- .build_corpus_statistics
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- _score_single_column
- features.py
- CorpusStatsBuilder
- select_fd_column_pairs
- score
- check_failure_threshold
- tokenize
- make_evidence_json
- FeatureBucket
- Benchmark: real_world_gov
- infer_column_data_type
- uniqueness_ratio
- graphify reference: extra exports and benchmark
- Raha
- API reference
- _require_columns
- Commit conventions and releases
- ._build_single_column_stats
- open_detect/exceptions.py
- quickstart.py
- clean_column
- test_package_init.py
- test_corpus_ingestion.py
- test_corpus_and_detectors.py
- get_spark
- open-detect
- Detection
- ColumnDataType
- graphify reference: query, path, explain
- log_transform_fits_better
- UnknownAlgorithmError
- text_utils.py
- Running on Databricks
- is_float_like
- _date_index
- min_conforming
- _score_pair
- _score_column
- `raha`
- _score_column
- parse_args
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- indexable_values
- TestConfigureLogging
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- extraction-spec.md

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 94 edges
2. `ErrorType` - 86 edges
3. `UniDetectConfig` - 80 edges
4. `build_pattern_index()` - 45 edges
5. `UniDetect` - 39 edges
6. `UnityCatalogLocation` - 37 edges
7. `FailureCounts` - 37 edges
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

## Communities (111 total, 28 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.12
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.06
Nodes (10): UniDetectConfig, CorpusStatsStore, TestRedactEvidence, TestUniDetectConfig, config(), TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap, _raise() (+2 more)

### Community 2 - "get_algorithm"
Cohesion: 0.20
Nodes (7): Check it works, Installation, Installing from source, Pick your extra, get_algorithm(), test_registered_under_raha(), test_get_algorithm_constructs_with_args()

### Community 3 - "wiki_subset/run_benchmark.py"
Cohesion: 0.11
Nodes (13): confusion_metrics(), git_commit(), _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run() (+5 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.18
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 8 - "PatternIndex"
Cohesion: 0.09
Nodes (6): _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), PatternIndex, TestSegmentDp, solve()

### Community 9 - "UniDetect"
Cohesion: 0.21
Nodes (5): UniDetect, __getattr__(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.10
Nodes (3): FailureCounts, FailureCountsAccumulatorParam, TestFailureCounts

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.26
Nodes (10): comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown(), _short_name() (+2 more)

### Community 12 - "CorpusIngestor"
Cohesion: 0.16
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 13 - "fmdv_v"
Cohesion: 0.10
Nodes (9): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV, TestFmdvVh (+1 more)

### Community 14 - "outliers.py"
Cohesion: 0.12
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateConfig"
Cohesion: 0.05
Nodes (11): AutoValidateConfig, AutoValidateAlgorithm, build_pattern_index(), TestDefaults, TestValidation, _make_tiny_corpus(), TestAutoValidateDetector, TestCorpusInputShapes (+3 more)

### Community 16 - "check_drift"
Cohesion: 0.13
Nodes (4): check_drift(), _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.14
Nodes (7): ColumnPredictions, train_and_predict(), _default_classifier_factory(), RahaConfig, _features(), TestClassifierTrainingPath, TestDegenerateCases

### Community 18 - "_StubDetector"
Cohesion: 0.33
Nodes (3): _StubDetector, compute(), TestDetectorFailureGate

### Community 19 - "get_spec"
Cohesion: 0.14
Nodes (5): all_specs(), ErrorTypeSpec, get_spec(), TestAllSpecs, TestGetSpec

### Community 20 - "index.py"
Cohesion: 0.08
Nodes (13): _clean_series(), _conforms(), DriftResult, _fisher_two_tailed(), InferredPattern, _infer_cmp(), _append_literal(), _is_numeric() (+5 more)

### Community 21 - "patterns.py"
Cohesion: 0.05
Nodes (23): _fmdv_h_single(), _fmdv_single_segment(), _char_class(), _class_of_token(), generality_weight(), generalize(), _iter_runs(), Token (+15 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.17
Nodes (15): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), comparison_charts(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct() (+7 more)

### Community 23 - "ErrorType"
Cohesion: 0.11
Nodes (8): _require_min_rows(), BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker, ErrorType

### Community 24 - "test_metrics.py"
Cohesion: 0.24
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 25 - "enums.py"
Cohesion: 0.08
Nodes (5): ComparisonDirection, config(), config(), _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 26 - "logging_utils.py"
Cohesion: 0.15
Nodes (5): configure_logging(), get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 28 - "main"
Cohesion: 0.36
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 29 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 30 - "AlgorithmResult"
Cohesion: 0.08
Nodes (8): Combine, open-detect, What is in the box, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 31 - "raha/detector.py"
Cohesion: 0.13
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (9): fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies(), TestFdViolationStrategies, TestGaussianOutlierStrategies, TestHistogramOutlierStrategies (+1 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.11
Nodes (14): spark_session(), SparkUnavailable, dataset_paths(), load_changes(), load_csv(), _build_config(), _dataset_frames(), main() (+6 more)

### Community 37 - "Auto-Validate"
Cohesion: 0.16
Nodes (9): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Usage, Using the parts directly (+1 more)

### Community 38 - "RahaDetector"
Cohesion: 0.16
Nodes (8): main(), RahaDetector, GroundTruthLabeler, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler(), TestGroundTruthLabeler

### Community 39 - "HeuristicLabeler"
Cohesion: 0.46
Nodes (3): ColumnFeatures, HeuristicLabeler, TestHeuristicLabeler

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "spark_session.py"
Cohesion: 0.10
Nodes (10): A fully local example, Configuration, How it works, Install, Operational notes, Uni-Detect, _delta_jars(), _download() (+2 more)

### Community 43 - "What You Must Do When Invoked"
Cohesion: 0.08
Nodes (24): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+16 more)

### Community 44 - "featurization.py"
Cohesion: 0.11
Nodes (12): _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket() (+4 more)

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "metrics/spelling.py"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 47 - "InsufficientDataError"
Cohesion: 0.15
Nodes (6): require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), InsufficientDataError, TestFunctionalDependency

### Community 48 - "registry.py"
Cohesion: 0.09
Nodes (17): _constant_factory(), get_algorithm_class(), list_algorithms(), _load_entry_points(), register_algorithm(), decorator(), register_lazy(), _FakeEntryPoint (+9 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.12
Nodes (15): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, CHANGELOG, Refactoring (+7 more)

### Community 50 - "ValidationError"
Cohesion: 0.16
Nodes (8): ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _ensure_sequence_of_str(), _reject_unknown_kwargs(), _validate_literal_value()

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.13
Nodes (9): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), UniDetectAlgorithm, __getattr__(), _config(), _row() (+1 more)

### Community 53 - "algorithms/uni-detect.md"
Cohesion: 0.07
Nodes (20): Algorithms, Fidelity to the papers, Benchmarks, How to read them, Latest results, Running them, Getting started, At a glance (+12 more)

### Community 54 - "auto_validate/detector.py"
Cohesion: 0.21
Nodes (6): _check_columns_present(), _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches()

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "select_datasets.py"
Cohesion: 0.48
Nodes (3): candidates(), main(), select()

### Community 57 - "labeling.py"
Cohesion: 0.07
Nodes (18): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results (+10 more)

### Community 58 - ".build_corpus_statistics"
Cohesion: 0.18
Nodes (9): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+1 more)

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 61 - "_score_single_column"
Cohesion: 0.08
Nodes (7): _coerce_numeric(), _score_fd_pair(), _score_single_column(), TestCoerceNumeric, TestScoreFdPair, TestScoreSingleColumn, TestPerElementFunctions

### Community 62 - "features.py"
Cohesion: 0.23
Nodes (6): build_all_features(), build_column_features(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features()

### Community 63 - "CorpusStatsBuilder"
Cohesion: 0.30
Nodes (4): CorpusStatsBuilder, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "score"
Cohesion: 0.12
Nodes (16): Reading the output, Reading the detections, Through the registry, Usage on Databricks, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat (+8 more)

### Community 67 - "tokenize"
Cohesion: 0.23
Nodes (4): token_prevalence(), tokenize(), TestTokenPrevalence, TestTokenize

### Community 68 - "make_evidence_json"
Cohesion: 0.21
Nodes (5): _hash_value(), make_evidence_json(), redact_evidence(), compute(), TestRedactEvidence

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.20
Nodes (9): canonical_column(), Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Reading the results, Running the benchmark, Source (+1 more)

### Community 73 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 74 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 75 - "API reference"
Cohesion: 0.14
Nodes (11): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, API reference, Configuration (+3 more)

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "._build_single_column_stats"
Cohesion: 0.20
Nodes (4): compute(), compute(), _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType

### Community 79 - "open_detect/exceptions.py"
Cohesion: 0.07
Nodes (19): Errors, ensure_schema_exists(), UnityCatalogLocation, _validate_edges(), _run(), ConfigurationError, CorpusNotFoundError, DataQualityError (+11 more)

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 85 - "test_corpus_and_detectors.py"
Cohesion: 0.33
Nodes (3): Methodology: uni_detect -- mapping real dirty data onto its four error types, config(), corpus_tables_by_category()

### Community 89 - "ColumnDataType"
Cohesion: 0.16
Nodes (8): ColumnDataType, Candidate, CorpusColumnRecord, CorpusPairRecord, MetricObservation, TestCandidate, TestCorpusRecords, TestMetricObservation

### Community 90 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 92 - "UnknownAlgorithmError"
Cohesion: 0.29
Nodes (6): Concepts, Configuration objects, One contract: `detect()`, The registry, The shared result schema, UnknownAlgorithmError

### Community 93 - "text_utils.py"
Cohesion: 0.16
Nodes (4): is_integer_like(), is_mixed_alphanumeric(), TestIntegerLike, TestMixedAlphanumeric

### Community 94 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 96 - "_date_index"
Cohesion: 0.40
Nodes (3): _date_index(), _date_values(), TestLargeGroups

### Community 100 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 103 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 104 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 105 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **148 isolated node(s):** `open-detect`, `Usage`, `What graphify is for`, `Step 0 - GitHub repos and multi-path merge (only if a URL or several paths)`, `Step 1 - Ensure graphify is installed` (+143 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 653 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **28 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `verify_build_config`, `UniDetectConfig`, `wiki_subset/run_benchmark.py`, `UniDetect`, `_StubDetector`, `get_spec`, `enums.py`, `logging_utils.py`, `main`, `AlgorithmResult`, `main`, `real_world_gov/run_benchmark.py`, `spark_session.py`, `featurization.py`, `ErrorDetectionAlgorithm`, `.build_corpus_statistics`, `_score_single_column`, `CorpusStatsBuilder`, `FeatureBucket`, `API reference`, `_require_columns`, `._build_single_column_stats`, `open_detect/exceptions.py`, `quickstart.py`, `Detection`, `ColumnDataType`, `parse_args`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `_date_index`, `wiki_subset/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `PatternIndex`, `API reference`, `fmdv_v`, `open_detect/exceptions.py`, `check_drift`, `index.py`, `patterns.py`, `auto_validate/detector.py`, `fmdv`, `UnknownAlgorithmError`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `verify_build_config`, `wiki_subset/run_benchmark.py`, `UniDetect`, `ErrorType`, `enums.py`, `logging_utils.py`, `main`, `real_world_gov/run_benchmark.py`, `spark_session.py`, `featurization.py`, `ErrorDetectionAlgorithm`, `.build_corpus_statistics`, `_score_single_column`, `CorpusStatsBuilder`, `API reference`, `open_detect/exceptions.py`, `quickstart.py`, `test_corpus_and_detectors.py`, `UnknownAlgorithmError`, `_score_pair`, `_score_column`, `_score_column`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 33 INFERRED edges - model-reasoned connections that need verification._