# Graph Report - open-detect  (2026-09-20)

## Corpus Check
- 90 files · ~70,741 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 226, (none) 3, .properties 1)

## Summary
- 784 nodes · 1722 edges · 48 communities (44 shown, 4 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 132 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c8cb778a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- detectors/base.py
- UnityCatalogLocation
- is_mixed_alphanumeric
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- graphify SKILL.md — main pipeline skill
- outliers.py
- UniDetect
- FeatureBucket
- perturb_functional_dependency
- wiki_subset/generate_report.py
- metrics/spelling.py
- perturbation.py
- drop_nulls
- CorpusStatsBuilder
- featurization.py
- CorpusStatsStore
- perturb_numeric_outlier
- pipeline.py
- builder.py
- ErrorType
- list_tables_matching
- config.py
- main
- tokenize
- build_corpus_statistics.py
- spark_session.py
- unidetect
- infer_column_data_type
- quickstart.py
- common/__init__.py
- bucket_by_edges
- test_featurization.py
- UniDetectConfig
- wiki_subset/run_benchmark.py
- ConfigurationError
- text_utils.py
- is_integer_like
- .batch_score
- WIKI-subset benchmark results
- Benchmark: WIKI subset
- select_datasets.py
- spark_session
- real_world_gov/README.md
- .detect
- Benchmark: real_world_gov

## God Nodes (most connected - your core abstractions)
1. `ErrorType` - 63 edges
2. `UniDetectConfig` - 42 edges
3. `UniDetect` - 31 edges
4. `UnityCatalogLocation` - 25 edges
5. `ARCHITECTURE.md — Uni-Detect paper-to-code map` - 23 edges
6. `CorpusIngestor` - 21 edges
7. `CorpusStatsStore` - 21 edges
8. `FeatureBucket` - 20 edges
9. `BaseDetector` - 20 edges
10. `log_duration()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Why not download the real WIKI corpus in CI?` --references--> `UniDetect`  [INFERRED]
  benchmarks/wiki_subset/README.md → src/unidetect/pipeline.py
- `Running the benchmark` --references--> `CorpusStatsBuilder`  [INFERRED]
  benchmarks/real_world_gov/README.md → src/unidetect/corpus/builder.py
- `WIKI-subset benchmark methodology redesign` --semantically_similar_to--> `functional_dependency metric (FR, Section 3.4)`  [INFERRED] [semantically similar]
  benchmarks/README.md → ARCHITECTURE.md
- `README.md — Uni-Detect overview` --references--> `CI workflow: Benchmark (wiki-subset, workflow_dispatch)`  [AMBIGUOUS]
  README.md → .github/workflows/benchmark.yml
- `WIKI-subset benchmark methodology redesign` --semantically_similar_to--> `FD metric deviation from literal paper formula`  [INFERRED] [semantically similar]
  benchmarks/README.md → ARCHITECTURE.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **graphify Skill Reference Documentation Set** — _claude_skills_graphify_skill, _claude_skills_graphify_references_add_watch, _claude_skills_graphify_references_exports, _claude_skills_graphify_references_extraction_spec, _claude_skills_graphify_references_github_and_merge, _claude_skills_graphify_references_hooks, _claude_skills_graphify_references_query, _claude_skills_graphify_references_transcribe, _claude_skills_graphify_references_update [EXTRACTED 1.00]
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (48 total, 4 thin omitted)

### Community 0 - "detectors/base.py"
Cohesion: 0.20
Nodes (18): ABC, collections_abc, pyspark_sql, BaseDetector, make_evidence_json(), Shared detection template implementing Uni-Detect's Definition 4 end-to-end.…, Template-method base class for a single error-type detector., FunctionalDependencyDetector (+10 more)

### Community 1 - "UnityCatalogLocation"
Cohesion: 0.20
Nodes (10): ensure_schema_exists(), Create the catalog/schema if they do not already exist. Requires ``CREATE…, A fully-qualified Unity Catalog three-level namespace., UnityCatalogLocation, Raised for failures interacting with Unity Catalog (naming, permissions)., UnityCatalogError, TestEnsureSchemaExists, TestUnityCatalogLocation (+2 more)

### Community 2 - "is_mixed_alphanumeric"
Cohesion: 0.38
Nodes (3): is_mixed_alphanumeric(), True for values like 'ICAO123', 'SKU-9981', 'AB12CD34' -- typical ID/code…, TestMixedAlphanumeric

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.16
Nodes (18): canonical_column(), dataset_paths(), load_changes(), load_csv(), Path, Shared helpers for reading the real_world_gov benchmark's checked-in CSVs.…, Strip ``dirty.csv``'s SQL-type-hint suffix (e.g. ``"zip(double precision)"``).…, Read a CSV into (canonical header, rows), treating ``""`` cells as null. (+10 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.10
Nodes (31): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), ARCHITECTURE.md — Uni-Detect paper-to-code map, ComparisonDirection generalization (INCREASING/DECREASING), Bounded corpus ingestion sampling, FD metric deviation from literal paper formula, Coarse feature-bucket featurization (Figure 5 cube diagram), MPD blocking optimization for spelling metric (+23 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (23): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+15 more)

### Community 6 - "graphify SKILL.md — main pipeline skill"
Cohesion: 0.10
Nodes (24): .claude/CLAUDE.md — graphify trigger, graphify reference: add-watch.md, graphify reference: exports.md, graphify reference: extraction-spec.md, graphify reference: github-and-merge.md, graphify reference: hooks.md, graphify reference: query.md, graphify reference: transcribe.md (+16 more)

### Community 7 - "outliers.py"
Cohesion: 0.16
Nodes (15): ndarray, Sized, require_min_size(), mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+7 more)

### Community 8 - "UniDetect"
Cohesion: 0.06
Nodes (27): Methodology: mapping real dirty data onto UniDetect's four error types, CorpusIngestor, DataFrame, SparkSession, Build the ``corpus_column_pairs`` DataFrame used for FD statistics., Global token -> distinct-table document-frequency (``Prev(C)`` input). A…, Builds ``corpus_columns``, ``corpus_column_pairs`` and ``token_stats``.…, Build the ``corpus_columns`` DataFrame from a list of UC table FQNs. Each… (+19 more)

### Community 9 - "FeatureBucket"
Cohesion: 0.08
Nodes (25): ColumnDataType, Coarse data-type classification used for featurization (paper Fig. 5). This is…, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation (+17 more)

### Community 10 - "perturb_functional_dependency"
Cohesion: 0.09
Nodes (18): compute(), DataFrame, DataFrame, compute(), DataFrame, compute(), _max_drop(), perturb_functional_dependency() (+10 more)

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.13
Nodes (27): grouped_bar_chart(), _nice_ceiling(), Pure-stdlib SVG bar-chart rendering shared by every benchmark's report.…, A bar path rounded at the top (far end from the baseline) only., _rounded_top_rect(), _by_dataset_chart(), _fmt_pct(), main() (+19 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.13
Nodes (12): collections, itertools, rapidfuzz_distance, _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult (+4 more)

### Community 13 - "perturbation.py"
Cohesion: 0.18
Nodes (8): dataclasses, fd_compliance_ratio(), FDResult, minority_violation_rows(), FD-compliance-ratio metric (paper Section 3.4, ``FR``). Note on fidelity to the…, Rows to drop to repair the *smallest* FD-violating groups first. For each LHS…, Per-error-type instantiations of epsilon-perturbation (paper Definition 2).…, TestFunctionalDependency

### Community 14 - "drop_nulls"
Cohesion: 0.11
Nodes (15): InsufficientDataError, Raised when a target column/table does not have enough data to score., drop_nulls(), Shared helpers for metric-function implementations., Remove ``None``/``NaN``-like values, preserving order. Real-world corpus…, duplicate_value_indices(), Uniqueness-ratio metric (paper Section 3.3, ``UR``)., ``UR(C) = num-distinct-values(C) / num-total-values(C)``. A ``UR`` close to 1.0… (+7 more)

### Community 15 - "CorpusStatsBuilder"
Cohesion: 0.11
Nodes (14): _coerce_numeric(), CorpusStatsBuilder, compute(), compute(), DataFrame, SparkSession, Persist a stats DataFrame, replacing only its own ``error_type`` partition(s).…, Builds and persists the ``unidetect_corpus_stats`` Delta table. Parameters… (+6 more)

### Community 16 - "featurization.py"
Cohesion: 0.21
Nodes (11): numpy, bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_functional_dependency_bucket(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket() (+3 more)

### Community 17 - "CorpusStatsStore"
Cohesion: 0.18
Nodes (9): CorpusStatsStore, SparkSession, Read-side access to the materialized ``unidetect_corpus_stats`` table.…, Collect the token-document-frequency table to the driver as a dict. Used to…, CorpusNotFoundError, Raised when the corpus statistics table has not been built yet., These tests need a corpus-stats/token-stats table that has genuinely never been…, TestCorpusStatsStoreBeforeBuild (+1 more)

### Community 18 - "perturb_numeric_outlier"
Cohesion: 0.28
Nodes (5): compute(), DataFrame, perturb_numeric_outlier(), Drop the single most outlying value by MAD-score (paper Section 3.1)., TestPerturbNumericOutlier

### Community 19 - "pipeline.py"
Cohesion: 0.15
Nodes (10): functools, Databricks Job entrypoint: online Uni-Detect error scanning. Example:…, Public, high-level API: :class:`UniDetect`. This is the single entry point most…, get_spark(), SparkSession, Spark session helpers. Kept deliberately tiny: on Databricks,…, Unit tests for jobs/run_detection.py (argument parsing + orchestration only).…, Unit tests for spark_utils.py using a mocked SparkSession (no real cluster… (+2 more)

### Community 20 - "builder.py"
Cohesion: 0.11
Nodes (17): Logger, logging, pyspark_sql_types, Offline "learning" phase: materialize corpus statistics (paper Sec. 2.2.3). For…, Turn a set of Unity Catalog tables into the canonical corpus representation.…, Canonical Delta table schemas used by the corpus builder and store. Keeping…, Online scoring: batch likelihood-ratio lookups against materialized corpus…, get_logger() (+9 more)

### Community 21 - "ErrorType"
Cohesion: 0.16
Nodes (14): Enum, ComparisonDirection, ErrorType, Core enumerations shared across the unidetect package., Direction in which a metric moves once the anomalous subset is removed. Uni-…, The four error classes Uni-Detect is instantiated for (paper Section 3). Each…, all_specs(), ErrorTypeSpec (+6 more)

### Community 22 - "list_tables_matching"
Cohesion: 0.36
Nodes (4): list_tables_matching(), Return fully-qualified table names across one or more schemas in ``catalog``.…, TestListTablesMatching, fake_sql()

### Community 23 - "config.py"
Cohesion: 0.15
Nodes (12): pytest, list_tables(), SparkSession, Unity Catalog convenience helpers. Thin wrappers around Spark SQL DDL/catalog…, Return fully-qualified names of every table in ``catalog.schema``., table_exists(), Central configuration for a Uni-Detect deployment. A single…, Exception hierarchy for unidetect. All library-raised exceptions derive from… (+4 more)

### Community 24 - "main"
Cohesion: 0.27
Nodes (5): main(), parse_args(), Namespace, TestMain, TestParseArgs

### Community 25 - "tokenize"
Cohesion: 0.23
Nodes (6): ``Prev(C)`` (paper Sec. 3.3): average, over values and their tokens, of how…, token_prevalence(), Split a value into alphanumeric tokens, discarding punctuation/whitespace., tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "build_corpus_statistics.py"
Cohesion: 0.20
Nodes (7): main(), parse_args(), Namespace, Databricks Job entrypoint: offline Uni-Detect corpus-statistics build. Intended…, Unit tests for jobs/build_corpus_statistics.py (argument parsing +…, TestMain, TestParseArgs

### Community 27 - "spark_session.py"
Cohesion: 0.13
Nodes (17): Local, Delta-enabled Spark session bootstrap shared by every benchmark.…, contextlib, shutil, subprocess, sys, tempfile, _delta_jars(), _download() (+9 more)

### Community 30 - "infer_column_data_type"
Cohesion: 0.33
Nodes (3): infer_column_data_type(), Classify a column into the coarse types used for featurization (paper Fig. 5).…, TestDataTypeInference

### Community 31 - "quickstart.py"
Cohesion: 0.29
Nodes (7): delta, build_spark(), main(), SparkSession, Standalone quickstart: build a tiny corpus and run Uni-Detect against it. Run…, json, os

### Community 33 - "bucket_by_edges"
Cohesion: 0.23
Nodes (5): bucket_by_edges(), bucket_leftness(), Map ``value`` into one of ``len(edges) + 1`` half-open ranges. ``edges=(20, 50,…, Column position from the left (paper Sec. 3.3), capped to bound cardinality., TestBucketing

### Community 34 - "test_featurization.py"
Cohesion: 0.28
Nodes (4): log_transform_fits_better(), Heuristic for the "whether logarithm-transform better fits the data" dimension.…, Unit tests for featurization.py and text_utils.py., TestLogFit

### Community 35 - "UniDetectConfig"
Cohesion: 0.22
Nodes (6): Tunable knobs for both the offline corpus builder and the online detectors.…, UniDetectConfig, parametrize, TestUniDetectConfig, config(), fixture

### Community 36 - "wiki_subset/run_benchmark.py"
Cohesion: 0.19
Nodes (13): confusion_metrics(), Confusion-matrix scoring shared by every benchmark's evaluation targets. Every…, Precision/recall/F1/accuracy over ``rows``' boolean…, git_commit(), Path, _build_config(), _load_corpus_tables(), _load_targets() (+5 more)

### Community 37 - "ConfigurationError"
Cohesion: 0.19
Nodes (10): ConfigurationError, Exception, Base class for all unidetect errors., Raised when a :class:`~unidetect.config.UniDetectConfig` is invalid., UniDetectError, parametrize, Unit tests for the exception hierarchy (no Spark required)., test_all_errors_derive_from_unidetect_error() (+2 more)

### Community 38 - "text_utils.py"
Cohesion: 0.25
Nodes (5): re, is_float_like(), Tokenization and data-type inference shared by featurization and corpus…, Unit tests for text_utils.py., TestFloatLike

### Community 40 - ".batch_score"
Cohesion: 0.29
Nodes (5): Running the benchmark, Reading the results without JSON, DataFrame, Score a batch of candidates against the corpus for one error type. Parameters…, Return the (partition-pruned) corpus statistics for one error type.

### Community 41 - "WIKI-subset benchmark results"
Cohesion: 0.25
Nodes (6): By corruption severity, By error type, Evaluation targets, Overall, Ranking correctness, WIKI-subset benchmark results

### Community 42 - "Benchmark: WIKI subset"
Cohesion: 0.25
Nodes (8): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), Why not download the real WIKI corpus in CI?

### Community 43 - "select_datasets.py"
Cohesion: 0.48
Nodes (6): argparse, candidates(), main(), Path, Reproduces how this benchmark's 5 datasets were picked from Matelda's DGov_NTR…, select()

### Community 44 - "spark_session"
Cohesion: 0.33
Nodes (6): Any, Exception, Raised only when a local Delta-enabled Spark session cannot be started at all.…, Start a local, single-process, Delta-enabled Spark session for a benchmark run.…, spark_session(), SparkUnavailable

### Community 45 - "real_world_gov/README.md"
Cohesion: 0.33
Nodes (4): By dataset, Evaluated columns, Overall, real_world_gov benchmark results

### Community 46 - ".detect"
Cohesion: 0.47
Nodes (3): DataFrame, Return a DataFrame with the columns in :data:`CANDIDATE_COLUMNS`., Run the full Definition-4 pipeline for ``table_names`` and rank results.…

### Community 47 - "Benchmark: real_world_gov"
Cohesion: 0.40
Nodes (5): Benchmark: real_world_gov, Comparing across versions, Layout, Reading the results, Which 5 datasets, and why

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **29 isolated node(s):** `unidetect`, `Which 5 datasets, and why`, `Layout`, `Reading the results`, `Comparing across versions` (+24 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 214 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `detectors/base.py`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `.batch_score`, `FeatureBucket`, `UniDetect`, `CorpusStatsBuilder`, `featurization.py`, `CorpusStatsStore`, `pipeline.py`, `builder.py`, `main`, `build_corpus_statistics.py`, `quickstart.py`?**
  _High betweenness centrality (0.200) - this node is a cross-community bridge._
- **Why does `UniDetect` connect `UniDetect` to `detectors/base.py`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `UniDetectConfig`, `FeatureBucket`, `Benchmark: WIKI subset`, `CorpusStatsBuilder`, `pipeline.py`, `ErrorType`, `main`, `build_corpus_statistics.py`, `quickstart.py`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Why does `UniDetectConfig` connect `UniDetectConfig` to `detectors/base.py`, `UnityCatalogLocation`, `real_world_gov/run_benchmark.py`, `wiki_subset/run_benchmark.py`, `ConfigurationError`, `UniDetect`, `FeatureBucket`, `CorpusStatsBuilder`, `CorpusStatsStore`, `pipeline.py`, `builder.py`, `config.py`, `main`, `build_corpus_statistics.py`, `quickstart.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 37 inferred relationships involving `ErrorType` (e.g. with `run()` and `run()`) actually correct?**
  _`ErrorType` has 37 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 14 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `UniDetect` (e.g. with `run()` and `Why not download the real WIKI corpus in CI?`) actually correct?**
  _`UniDetect` has 12 INFERRED edges - model-reasoned connections that need verification._