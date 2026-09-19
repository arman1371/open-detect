# Graph Report - open-detect  (2026-09-19)

## Corpus Check
- 89 files · ~69,773 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 232 file(s) not represented in the graph (top: .csv 226, (none) 3, .properties 1)

## Summary
- 753 nodes · 1655 edges · 41 communities (35 shown, 6 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 129 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0fcc7aa2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ErrorType
- UniDetectConfig
- text_utils.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- graphify SKILL.md — main pipeline skill
- outliers.py
- UniDetect
- FeatureBucket
- perturbation.py
- wiki_subset/generate_report.py
- metrics/spelling.py
- metrics/functional_dependency.py
- uniqueness_ratio
- CorpusStatsBuilder
- featurization.py
- CorpusStatsStore
- perturb_numeric_outlier
- pipeline.py
- log_duration
- strategies.py
- list_tables_matching
- config.py
- main
- tokenize
- main
- test_metrics.py
- unidetect
- infer_column_data_type
- enums.py
- common/__init__.py
- bucket_by_edges
- test_featurization.py
- _score_single_column
- store.py
- builder.py
- is_float_like
- is_integer_like
- _coerce_numeric

## God Nodes (most connected - your core abstractions)
1. `ErrorType` - 62 edges
2. `UniDetectConfig` - 36 edges
3. `UniDetect` - 30 edges
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

## Communities (41 total, 6 thin omitted)

### Community 0 - "ErrorType"
Cohesion: 0.08
Nodes (35): ABC, collections_abc, pyspark_sql_types, ErrorType, The four error classes Uni-Detect is instantiated for (paper Section 3). Each…, BaseDetector, make_evidence_json(), DataFrame (+27 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.07
Nodes (29): build_spark(), main(), SparkSession, ensure_schema_exists(), Create the catalog/schema if they do not already exist. Requires ``CREATE…, A fully-qualified Unity Catalog three-level namespace., Tunable knobs for both the offline corpus builder and the online detectors.…, UniDetectConfig (+21 more)

### Community 2 - "text_utils.py"
Cohesion: 0.21
Nodes (6): re, is_mixed_alphanumeric(), Tokenization and data-type inference shared by featurization and corpus…, True for values like 'ICAO123', 'SKU-9981', 'AB12CD34' -- typical ID/code…, Unit tests for text_utils.py., TestMixedAlphanumeric

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.06
Nodes (54): confusion_metrics(), Confusion-matrix scoring shared by every benchmark's evaluation targets. Every…, Precision/recall/F1/accuracy over ``rows``' boolean…, git_commit(), Any, Exception, Path, Local, Delta-enabled Spark session bootstrap shared by every benchmark.… (+46 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.06
Nodes (41): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), ARCHITECTURE.md — Uni-Detect paper-to-code map, ComparisonDirection generalization (INCREASING/DECREASING), Bounded corpus ingestion sampling, FD metric deviation from literal paper formula, Coarse feature-bucket featurization (Figure 5 cube diagram), MPD blocking optimization for spelling metric (+33 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (23): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+15 more)

### Community 6 - "graphify SKILL.md — main pipeline skill"
Cohesion: 0.10
Nodes (24): .claude/CLAUDE.md — graphify trigger, graphify reference: add-watch.md, graphify reference: exports.md, graphify reference: extraction-spec.md, graphify reference: github-and-merge.md, graphify reference: hooks.md, graphify reference: query.md, graphify reference: transcribe.md (+16 more)

### Community 7 - "outliers.py"
Cohesion: 0.14
Nodes (19): ndarray, numpy, Sized, drop_nulls(), Remove ``None``/``NaN``-like values, preserving order. Real-world corpus…, require_min_size(), mad_scores(), MADResult (+11 more)

### Community 8 - "UniDetect"
Cohesion: 0.09
Nodes (18): CorpusIngestor, DataFrame, SparkSession, Build the ``corpus_column_pairs`` DataFrame used for FD statistics., Global token -> distinct-table document-frequency (``Prev(C)`` input). A…, Builds ``corpus_columns``, ``corpus_column_pairs`` and ``token_stats``.…, Build the ``corpus_columns`` DataFrame from a list of UC table FQNs. Each…, SparkSession (+10 more)

### Community 9 - "FeatureBucket"
Cohesion: 0.08
Nodes (29): Enum, ColumnDataType, ComparisonDirection, Coarse data-type classification used for featurization (paper Fig. 5). This is…, Direction in which a metric moves once the anomalous subset is removed. Uni-…, Candidate, CorpusColumnRecord, CorpusPairRecord (+21 more)

### Community 10 - "perturbation.py"
Cohesion: 0.15
Nodes (13): _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, Per-error-type instantiations of epsilon-perturbation (paper Definition 2).…, Drop minority rows from the smallest violating LHS groups (paper Section 3.4)., Drop duplicate occurrences (paper Example 2). (+5 more)

### Community 11 - "wiki_subset/generate_report.py"
Cohesion: 0.13
Nodes (27): grouped_bar_chart(), _nice_ceiling(), Pure-stdlib SVG bar-chart rendering shared by every benchmark's report.…, A bar path rounded at the top (far end from the baseline) only., _rounded_top_rect(), _by_dataset_chart(), _fmt_pct(), main() (+19 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.16
Nodes (11): itertools, rapidfuzz_distance, _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, Minimum pairwise edit-distance (MPD) metric for spelling errors. See paper… (+3 more)

### Community 13 - "metrics/functional_dependency.py"
Cohesion: 0.23
Nodes (7): collections, fd_compliance_ratio(), FDResult, minority_violation_rows(), FD-compliance-ratio metric (paper Section 3.4, ``FR``). Note on fidelity to the…, Rows to drop to repair the *smallest* FD-violating groups first. For each LHS…, TestFunctionalDependency

### Community 14 - "uniqueness_ratio"
Cohesion: 0.31
Nodes (5): InsufficientDataError, Raised when a target column/table does not have enough data to score., ``UR(C) = num-distinct-values(C) / num-total-values(C)``. A ``UR`` close to 1.0…, uniqueness_ratio(), TestUniquenessRatio

### Community 15 - "CorpusStatsBuilder"
Cohesion: 0.10
Nodes (20): Benchmark: real_world_gov, Comparing across versions, Layout, Methodology: mapping real dirty data onto UniDetect's four error types, Reading the results, Running the benchmark, Which 5 datasets, and why, CorpusStatsBuilder (+12 more)

### Community 16 - "featurization.py"
Cohesion: 0.22
Nodes (10): bucket_leftness(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_outlier_bucket(), build_spelling_bucket(), build_uniqueness_bucket(), Featurization / corpus-subsetting (paper Section 2.2.2 and Figure 5). Each… (+2 more)

### Community 17 - "CorpusStatsStore"
Cohesion: 0.09
Nodes (20): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Layout, Reading the results without JSON, Running the benchmark, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`) (+12 more)

### Community 18 - "perturb_numeric_outlier"
Cohesion: 0.47
Nodes (3): perturb_numeric_outlier(), Drop the single most outlying value by MAD-score (paper Section 3.1)., TestPerturbNumericOutlier

### Community 19 - "pipeline.py"
Cohesion: 0.14
Nodes (14): argparse, delta, Standalone quickstart: build a tiny corpus and run Uni-Detect against it. Run…, functools, pyspark_sql, Databricks Job entrypoint: offline Uni-Detect corpus-statistics build. Intended…, Databricks Job entrypoint: online Uni-Detect error scanning. Example:…, Public, high-level API: :class:`UniDetect`. This is the single entry point most… (+6 more)

### Community 20 - "log_duration"
Cohesion: 0.17
Nodes (11): Logger, logging, get_logger(), log_duration(), Structured logging helpers. Uses the standard :mod:`logging` module so behavior…, Return a namespaced logger under the ``unidetect`` hierarchy. Parameters…, Log the wall-clock duration of a block, tagged with ``action``. Example -------…, Unit tests for logging_utils.py (no Spark required). (+3 more)

### Community 21 - "strategies.py"
Cohesion: 0.18
Nodes (8): dataclasses, all_specs(), ErrorTypeSpec, get_spec(), Registry tying each :class:`ErrorType` to its Definition-4 configuration. The…, Unit tests for strategies.py (no Spark required)., TestAllSpecs, TestGetSpec

### Community 22 - "list_tables_matching"
Cohesion: 0.16
Nodes (10): list_tables(), list_tables_matching(), SparkSession, Return fully-qualified names of every table in ``catalog.schema``., Return fully-qualified table names across one or more schemas in ``catalog``.…, table_exists(), TestListTables, TestListTablesMatching (+2 more)

### Community 23 - "config.py"
Cohesion: 0.22
Nodes (7): pytest, Unity Catalog convenience helpers. Thin wrappers around Spark SQL DDL/catalog…, Central configuration for a Uni-Detect deployment. A single…, Exception hierarchy for unidetect. All library-raised exceptions derive from…, Unit tests for catalog.py using a mocked SparkSession (no real cluster…, Unit tests for config.py validation (no Spark required)., End-to-end tests: ingest a tiny synthetic corpus into Delta tables, build…

### Community 24 - "main"
Cohesion: 0.27
Nodes (5): main(), parse_args(), Namespace, TestMain, TestParseArgs

### Community 25 - "tokenize"
Cohesion: 0.24
Nodes (6): ``Prev(C)`` (paper Sec. 3.3): average, over values and their tokens, of how…, token_prevalence(), Split a value into alphanumeric tokens, discarding punctuation/whitespace., tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "main"
Cohesion: 0.25
Nodes (5): main(), parse_args(), Namespace, TestMain, TestParseArgs

### Community 27 - "test_metrics.py"
Cohesion: 0.33
Nodes (4): duplicate_value_indices(), Indices of values that participate in at least one duplicate group. This is the…, Unit tests for metrics/*, validated against the paper's own worked numbers.…, TestDuplicateValueIndices

### Community 30 - "infer_column_data_type"
Cohesion: 0.33
Nodes (3): infer_column_data_type(), Classify a column into the coarse types used for featurization (paper Fig. 5).…, TestDataTypeInference

### Community 31 - "enums.py"
Cohesion: 0.25
Nodes (5): json, Core enumerations shared across the unidetect package., Unit tests for jobs/build_corpus_statistics.py (argument parsing +…, Unit tests for jobs/run_detection.py (argument parsing + orchestration only).…, unittest_mock

### Community 33 - "bucket_by_edges"
Cohesion: 0.36
Nodes (3): bucket_by_edges(), Map ``value`` into one of ``len(edges) + 1`` half-open ranges. ``edges=(20, 50,…, TestBucketing

### Community 34 - "test_featurization.py"
Cohesion: 0.29
Nodes (4): log_transform_fits_better(), Heuristic for the "whether logarithm-transform better fits the data" dimension.…, Unit tests for featurization.py and text_utils.py., TestLogFit

### Community 35 - "_score_single_column"
Cohesion: 0.43
Nodes (3): compute(), _score_single_column(), TestScoreSingleColumn

### Community 36 - "store.py"
Cohesion: 0.33
Nodes (3): Turn a set of Unity Catalog tables into the canonical corpus representation.…, Online scoring: batch likelihood-ratio lookups against materialized corpus…, Edge-case tests for corpus/store.py, corpus/ingestion.py and detectors/base.py.…

### Community 37 - "builder.py"
Cohesion: 0.40
Nodes (3): Offline "learning" phase: materialize corpus statistics (paper Sec. 2.2.3). For…, Canonical Delta table schemas used by the corpus builder and store. Keeping…, Unit tests for the pure-Python helpers in corpus/builder.py.…

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **29 isolated node(s):** `unidetect`, `Which 5 datasets, and why`, `Layout`, `Reading the results`, `Comparing across versions` (+24 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 209 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `_score_single_column`, `builder.py`, `store.py`, `UniDetect`, `FeatureBucket`, `CorpusStatsBuilder`, `featurization.py`, `CorpusStatsStore`, `pipeline.py`, `strategies.py`, `main`, `main`, `enums.py`?**
  _High betweenness centrality (0.204) - this node is a cross-community bridge._
- **Why does `UniDetect` connect `UniDetect` to `ErrorType`, `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `FeatureBucket`, `CorpusStatsBuilder`, `CorpusStatsStore`, `pipeline.py`, `main`, `main`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `ErrorType` (e.g. with `run()` and `run()`) actually correct?**
  _`ErrorType` has 36 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `UniDetect` (e.g. with `run()` and `Why not download the real WIKI corpus in CI?`) actually correct?**
  _`UniDetect` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `UnityCatalogLocation` (e.g. with `run()` and `run()`) actually correct?**
  _`UnityCatalogLocation` has 10 INFERRED edges - model-reasoned connections that need verification._