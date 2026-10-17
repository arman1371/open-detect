# Graph Report - ope87-wt  (2026-10-17)

## Corpus Check
- 166 files · ~137,717 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 244 file(s) not represented in the graph (top: .csv 227, .j2 10, (none) 4)

## Summary
- 1984 nodes · 4511 edges · 115 communities (89 shown, 26 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 485 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `feee33c9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CorpusStatsStore
- UniDetectConfig
- get_algorithm
- wiki_subset/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- duplicate_value_indices
- PatternIndex
- UniDetect
- FailureCounts
- real_world_gov/generate_report.py
- CorpusIngestor
- _build_index
- outliers.py
- AutoValidateAlgorithm
- InferredPattern
- RahaConfig
- hierarchy.py
- ErrorType
- auto_validate/detector.py
- patterns.py
- wiki_subset/generate_report.py
- collections_abc
- test_metrics.py
- detectors/base.py
- perturb_numeric_outlier
- InsufficientDataError
- list_tables_matching
- CellResult
- .detect
- raha/strategies.py
- main
- min_pairwise_edit_distance
- real_world_gov/run_benchmark.py
- IndexNotBuiltError
- RahaDetector
- build_pattern_index
- perturb_spelling
- real_world_gov benchmark results
- conftest.py
- What You Must Do When Invoked
- bucket_by_edges
- `auto_validate`
- _search_mpd
- require_min_size
- test_algorithms_registry.py
- .build_corpus_statistics
- ValidationError
- labeling.py
- ErrorDetectionAlgorithm
- algorithms/uni-detect.md
- .detect
- fmdv
- select_datasets.py
- Labeler
- AutoValidateConfig
- Benchmark: WIKI subset
- README.md — Uni-Detect overview
- TestPerElementFunctions
- BaseDetector
- OPE-138 Progress Report — Final (2026-10-17)
- select_fd_column_pairs
- AlgorithmResult
- dataset_utils.py
- OpenDetectError
- make_evidence_json
- TestConfigThreshold
- Benchmark: real_world_gov
- _coerce_numeric
- uniqueness_ratio
- graphify reference: extra exports and benchmark
- Raha
- Auto-Validate
- Commit conventions and releases
- CorpusStatsBuilder
- UnityCatalogLocation
- list_algorithms
- clean_column
- _score_single_column
- test_corpus_ingestion.py
- corpus_tables_by_category
- get_spark
- open-detect
- open_detect/__init__.py
- graphify reference: query, path, explain
- log_transform_fits_better
- ConfigurationError
- infer_column_data_type
- Contributing
- algorithms/index.md
- fmdv_v
- algorithms/raha.md
- reference/index.md
- TestFprAggregation
- `raha`
- Uni-Detect
- _config
- graphify reference: add a URL and watch a folder
- graphify reference: commit hook and native CLAUDE.md integration
- graphify reference: incremental update and cluster-only
- Benchmarks
- TestConfigureLogging
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- extraction-spec.md
- _default_classifier_factory
- Choosing an algorithm
- __getattr__

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
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/open_detect/algorithms/uni_detect/pipeline.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (115 total, 26 thin omitted)

### Community 0 - "CorpusStatsStore"
Cohesion: 0.06
Nodes (22): Operational notes, Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks, diff_fingerprints(), property_key() (+14 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.16
Nodes (4): UniDetectConfig, TestRedactEvidence, TestUniDetectConfig, config()

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
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 8 - "PatternIndex"
Cohesion: 0.07
Nodes (10): min_conforming(), _fmdv_h_single(), _fmdv_single_segment(), _segment_dp(), _segment_fmdv_v(), _segment_fmdv_vh(), PatternIndex, TestMinConforming (+2 more)

### Community 9 - "UniDetect"
Cohesion: 0.26
Nodes (4): UniDetect, TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 10 - "FailureCounts"
Cohesion: 0.09
Nodes (7): NumericOutlierDetector, compute(), FailureCounts, FailureCountsAccumulatorParam, finite_floats(), TestFailureCounts, TestFiniteFloats

### Community 11 - "real_world_gov/generate_report.py"
Cohesion: 0.20
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 12 - "CorpusIngestor"
Cohesion: 0.23
Nodes (3): CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table()

### Community 13 - "_build_index"
Cohesion: 0.14
Nodes (4): _build_index(), TestFmdvV, TestFmdvVh, _time_corpus()

### Community 14 - "outliers.py"
Cohesion: 0.13
Nodes (9): drop_nulls(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestDropNulls (+1 more)

### Community 15 - "AutoValidateAlgorithm"
Cohesion: 0.11
Nodes (3): AutoValidateAlgorithm, _make_tiny_corpus(), TestAutoValidateDetector

### Community 16 - "InferredPattern"
Cohesion: 0.10
Nodes (8): check_drift(), _clean_series(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern(), TestCheckDrift, TestCheckDriftVerticalCutPatterns

### Community 17 - "RahaConfig"
Cohesion: 0.11
Nodes (12): ColumnPredictions, train_and_predict(), RahaConfig, build_all_features(), build_column_features(), _features(), TestClassifierTrainingPath, TestDegenerateCases (+4 more)

### Community 18 - "hierarchy.py"
Cohesion: 0.08
Nodes (17): _conforms(), _append_literal(), _char_class(), _class_of_token(), generalize(), _is_numeric(), _iter_runs(), matches() (+9 more)

### Community 19 - "ErrorType"
Cohesion: 0.09
Nodes (12): _require_min_rows(), _score_fd_pair(), build_functional_dependency_bucket(), build_uniqueness_bucket(), all_specs(), ErrorTypeSpec, get_spec(), ErrorType (+4 more)

### Community 21 - "patterns.py"
Cohesion: 0.08
Nodes (12): generality_weight(), Token, _alternatives(), any_pattern(), _best_first_patterns(), common_patterns(), iter_patterns(), matching_pattern() (+4 more)

### Community 22 - "wiki_subset/generate_report.py"
Cohesion: 0.20
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 23 - "collections_abc"
Cohesion: 0.11
Nodes (9): _score_column(), bucket_row_count(), bucket_token_length(), build_outlier_bucket(), build_spelling_bucket(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness() (+1 more)

### Community 24 - "test_metrics.py"
Cohesion: 0.18
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 26 - "detectors/base.py"
Cohesion: 0.15
Nodes (4): get_logger(), log_duration(), TestGetLogger, TestLogDuration

### Community 27 - "perturb_numeric_outlier"
Cohesion: 0.13
Nodes (5): perturb_numeric_outlier(), TestPerturbFunctionalDependency, TestPerturbNumericNonFinite, TestPerturbNumericOutlier, TestPerturbUniqueness

### Community 28 - "InsufficientDataError"
Cohesion: 0.15
Nodes (8): main(), parse_args(), _run(), InsufficientDataError, configure_logging(), test_main_installs_logging(), TestMain, TestParseArgs

### Community 29 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 33 - "raha/strategies.py"
Cohesion: 0.10
Nodes (12): Full diff review (end-to-end), Implementation, _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), normalize_to_str(), pattern_character_strategies() (+4 more)

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "min_pairwise_edit_distance"
Cohesion: 0.18
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 36 - "real_world_gov/run_benchmark.py"
Cohesion: 0.12
Nodes (10): spark_session(), SparkUnavailable, _build_config(), main(), _print_comparison(), _register_table(), run(), run_auto_validate() (+2 more)

### Community 37 - "IndexNotBuiltError"
Cohesion: 0.14
Nodes (11): Auto-Validate, Configuration, Drift checking, How it works, Inspecting a pattern, Install, Reading the output, Usage (+3 more)

### Community 38 - "RahaDetector"
Cohesion: 0.20
Nodes (6): main(), RahaDetector, test_empty_dataframe_returns_no_cells(), test_recovers_known_errors_with_ground_truth_labeler(), test_result_to_pandas_matches_shared_schema(), test_runs_end_to_end_with_default_heuristic_labeler()

### Community 39 - "build_pattern_index"
Cohesion: 0.15
Nodes (4): build_pattern_index(), TestCorpusInputShapes, TestPatternIndex, TestTauPruning

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 42 - "conftest.py"
Cohesion: 0.15
Nodes (8): A fully local example, How it works, Install, Uni-Detect, _delta_jars(), _download(), spark(), uc_location()

### Community 43 - "What You Must Do When Invoked"
Cohesion: 0.08
Nodes (24): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+16 more)

### Community 44 - "bucket_by_edges"
Cohesion: 0.19
Nodes (4): bucket_by_edges(), bucket_leftness(), bucket_token_prevalence(), TestBucketing

### Community 45 - "`auto_validate`"
Cohesion: 0.17
Nodes (12): Algorithm comparison, `auto_validate`, By corruption severity, By corruption severity, By error type, By error type (cell-level), By error type (target-level), Evaluation targets (+4 more)

### Community 46 - "_search_mpd"
Cohesion: 0.27
Nodes (6): _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 47 - "require_min_size"
Cohesion: 0.15
Nodes (5): require_min_size(), fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.13
Nodes (11): get_algorithm_class(), register_lazy(), _FakeEntryPoint, fresh_registry(), _good_plugin_class(), detect(), test_register_lazy_is_lazy(), test_register_lazy_overrides_existing_name() (+3 more)

### Community 49 - ".build_corpus_statistics"
Cohesion: 0.07
Nodes (24): Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Methodology: auto_validate, The `m` override, Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing (+16 more)

### Community 50 - "ValidationError"
Cohesion: 0.18
Nodes (7): ValidationError, _check_columns_unique(), _check_dataframe_is_spark(), _check_expected_type(), _check_unknown_kwargs(), _ensure_sequence_of_str(), _validate_literal_value()

### Community 51 - "labeling.py"
Cohesion: 0.16
Nodes (5): ColumnFeatures, HeuristicLabeler, propagate_labels(), TestHeuristicLabeler, TestPropagateLabels

### Community 52 - "ErrorDetectionAlgorithm"
Cohesion: 0.14
Nodes (9): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+1 more)

### Community 53 - "algorithms/uni-detect.md"
Cohesion: 0.24
Nodes (4): Getting started, open-detect, What is in the box, Why a common interface

### Community 54 - ".detect"
Cohesion: 0.17
Nodes (7): _check_columns_present(), _feasible_evidence(), _infeasible_evidence(), _is_null(), _non_null_cells(), _value_matches(), _reject_unknown_kwargs()

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "select_datasets.py"
Cohesion: 0.39
Nodes (3): candidates(), main(), select()

### Community 57 - "Labeler"
Cohesion: 0.08
Nodes (20): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results (+12 more)

### Community 58 - "AutoValidateConfig"
Cohesion: 0.17
Nodes (4): API reference, AutoValidateConfig, TestDefaults, TestValidation

### Community 59 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (6): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?

### Community 60 - "README.md — Uni-Detect overview"
Cohesion: 0.23
Nodes (9): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, databricks.yml — Databricks Asset Bundle, Wang & He, "Uni-Detect" (SIGMOD 2019), README.md — Uni-Detect overview, catalog.list_tables_matching, functional_dependency metric (FR, Section 3.4) (+1 more)

### Community 62 - "BaseDetector"
Cohesion: 0.13
Nodes (4): BaseDetector, FailureTracker, _NoCandidatesDetector, test_table_names_logged_as_count_at_info_and_list_at_debug()

### Community 63 - "OPE-138 Progress Report — Final (2026-10-17)"
Cohesion: 0.12
Nodes (16): Blocker, Branch & Commit, Disposition, Durable evidence written, Heartbeat 27608cd2 (2026-10-17, workspace = ope87-wt), Heartbeat 27608cd2 — final disposition (2026-10-17, workspace = ope87-wt), Heartbeat 2e7a3d6b (2026-10-17 04:50Z) — re-verification, no state change, Heartbeat 51309a75 (2026-10-17 05:21Z) — GitHub identity re-probe, no state change (+8 more)

### Community 64 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 65 - "AlgorithmResult"
Cohesion: 0.10
Nodes (13): Reading the detections, Through the registry, Usage on Databricks, The shared result schema, Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs (+5 more)

### Community 66 - "dataset_utils.py"
Cohesion: 0.18
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 67 - "OpenDetectError"
Cohesion: 0.16
Nodes (9): The registry, OpenDetectError, UnknownAlgorithmError, test_all_errors_derive_from_open_detect_error(), test_error_message_is_preserved(), test_insufficient_data_error_is_not_a_value_error(), test_open_detect_error_is_catchable_broadly(), test_relocated_exceptions_importable_from_every_path() (+1 more)

### Community 68 - "make_evidence_json"
Cohesion: 0.16
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), _score_column(), SpellingDetector, compute(), TestRedactEvidence

### Community 69 - "TestConfigThreshold"
Cohesion: 0.24
Nodes (3): _raise(), TestAttempt, TestConfigThreshold

### Community 70 - "Benchmark: real_world_gov"
Cohesion: 0.22
Nodes (9): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: raha, Methodology: uni_detect -- mapping real dirty data onto its four error types, Reading the results, Running the benchmark, Which 5 datasets, and why (+1 more)

### Community 73 - "graphify reference: extra exports and benchmark"
Cohesion: 0.22
Nodes (8): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7a - FalkorDB export (only if --falkordb or --falkordb-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 74 - "Raha"
Cohesion: 0.25
Nodes (8): Configuration, How it works, Install, Raha, Reading the output, Scope, Usage, Who answers the labeling questions?

### Community 75 - "Auto-Validate"
Cohesion: 0.33
Nodes (6): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference

### Community 77 - "Commit conventions and releases"
Cohesion: 0.33
Nodes (6): Commit conventions and releases, First release bootstrap, How a release happens, Publishing to PyPI (optional, off by default), Required repository settings, Writing commits and PR titles

### Community 78 - "CorpusStatsBuilder"
Cohesion: 0.07
Nodes (15): Configuration, CorpusStatsBuilder, compute(), compute(), _stats_schema_without_error_type(), check_failure_threshold(), DataQualityError, TestStatsSchemaWithoutErrorType (+7 more)

### Community 79 - "UnityCatalogLocation"
Cohesion: 0.13
Nodes (9): build_spark(), main(), ensure_schema_exists(), UnityCatalogLocation, UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation, config() (+1 more)

### Community 81 - "list_algorithms"
Cohesion: 0.22
Nodes (8): 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, list_algorithms(), test_builtin_algorithms_are_registered()

### Community 82 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 86 - "get_spark"
Cohesion: 0.10
Nodes (8): FunctionalDependencyDetector, compute(), _score_pair(), _score_column(), UniquenessDetector, compute(), get_spark(), TestGetSpark

### Community 89 - "open_detect/__init__.py"
Cohesion: 0.06
Nodes (15): ColumnDataType, ComparisonDirection, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation (+7 more)

### Community 90 - "graphify reference: query, path, explain"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 92 - "ConfigurationError"
Cohesion: 0.17
Nodes (8): Concepts, Configuration objects, Errors, One contract: `detect()`, _validate_edges(), _require_columns(), ConfigurationError, TestRequireColumns

### Community 93 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 94 - "Contributing"
Cohesion: 0.25
Nodes (5): Adding an algorithm, Contributing, Everyday commands, Knowledge graph automation, Working on these docs

### Community 95 - "algorithms/index.md"
Cohesion: 0.29
Nodes (3): Algorithms, Fidelity to the papers, Errors

### Community 96 - "fmdv_v"
Cohesion: 0.13
Nodes (9): Variants, _coarse_signature(), fmdv_v(), fmdv_vh(), _infer_cmp(), _date_index(), _date_values(), TestCoarseSignature (+1 more)

### Community 97 - "algorithms/raha.md"
Cohesion: 0.29
Nodes (4): Configuration, Detector, Labelers, Raha

### Community 98 - "reference/index.md"
Cohesion: 0.29
Nodes (3): Registry, Registry and results, Result types

### Community 100 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 101 - "Uni-Detect"
Cohesion: 0.33
Nodes (6): Configuration, Enumerations, Pipeline, Registry adapter, Uni-Detect, Unity Catalog helpers

### Community 102 - "_config"
Cohesion: 0.53
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 103 - "graphify reference: add a URL and watch a folder"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 104 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 105 - "graphify reference: incremental update and cluster-only"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 106 - "Benchmarks"
Cohesion: 0.50
Nodes (4): Benchmarks, How to read them, Latest results, Running them

### Community 112 - "Choosing an algorithm"
Cohesion: 0.67
Nodes (3): At a glance, Choosing an algorithm, Rules of thumb

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **162 isolated node(s):** `open-detect`, `Usage`, `What graphify is for`, `Step 0 - GitHub repos and multi-path merge (only if a URL or several paths)`, `Step 1 - Ensure graphify is installed` (+157 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 669 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `CorpusStatsStore`, `wiki_subset/run_benchmark.py`, `UniDetect`, `FailureCounts`, `collections_abc`, `pipeline.py`, `detectors/base.py`, `InsufficientDataError`, `CellResult`, `main`, `real_world_gov/run_benchmark.py`, `conftest.py`, `.build_corpus_statistics`, `ErrorDetectionAlgorithm`, `AutoValidateConfig`, `TestPerElementFunctions`, `BaseDetector`, `make_evidence_json`, `._validate_inputs`, `CorpusStatsBuilder`, `UnityCatalogLocation`, `_score_single_column`, `get_spark`, `open_detect/__init__.py`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `CorpusStatsStore`, `wiki_subset/run_benchmark.py`, `UniDetect`, `CorpusIngestor`, `ErrorType`, `collections_abc`, `pipeline.py`, `detectors/base.py`, `InsufficientDataError`, `main`, `real_world_gov/run_benchmark.py`, `.build_corpus_statistics`, `ErrorDetectionAlgorithm`, `AutoValidateConfig`, `BaseDetector`, `make_evidence_json`, `TestConfigThreshold`, `Benchmark: real_world_gov`, `CorpusStatsBuilder`, `UnityCatalogLocation`, `_score_single_column`, `get_spark`, `open_detect/__init__.py`, `ConfigurationError`, `_config`, `.build_fingerprint`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `fmdv_v`, `wiki_subset/run_benchmark.py`, `real_world_gov/run_benchmark.py`, `TestFprAggregation`, `build_pattern_index`, `PatternIndex`, `_build_index`, `AutoValidateAlgorithm`, `InferredPattern`, `auto_validate/detector.py`, `.detect`, `fmdv`, `ConfigurationError`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 33 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 33 INFERRED edges - model-reasoned connections that need verification._
- **Are the 54 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 33 INFERRED edges - model-reasoned connections that need verification._