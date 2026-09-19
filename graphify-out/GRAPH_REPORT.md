# Graph Report - open-detect  (2026-09-19)

## Corpus Check
- 79 files · ~67,441 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 3, .typed 1)

## Summary
- 630 nodes · 1388 edges · 23 communities (20 shown, 3 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 89 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `faa7cd14`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ErrorType
- UniDetectConfig
- infer_column_data_type
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- graphify SKILL.md — main pipeline skill
- outliers.py
- UniDetect
- unidetect/__init__.py
- perturbation.py
- wiki_subset/generate_report.py
- metrics/spelling.py
- metrics/functional_dependency.py
- require_min_size
- CorpusStatsBuilder
- featurization.py
- .batch_score
- perturb_numeric_outlier
- duplicate_value_indices
- unidetect
- common/__init__.py

## God Nodes (most connected - your core abstractions)
1. `ErrorType` - 50 edges
2. `UniDetectConfig` - 34 edges
3. `UniDetect` - 27 edges
4. `ARCHITECTURE.md — Uni-Detect paper-to-code map` - 23 edges
5. `UnityCatalogLocation` - 21 edges
6. `BaseDetector` - 20 edges
7. `CorpusStatsBuilder` - 16 edges
8. `CorpusIngestor` - 16 edges
9. `CorpusStatsStore` - 15 edges
10. `build_uniqueness_bucket()` - 15 edges

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

## Communities (23 total, 3 thin omitted)

### Community 0 - "ErrorType"
Cohesion: 0.05
Nodes (60): ABC, collections_abc, Enum, functools, Logger, logging, pyspark_sql, pyspark_sql_types (+52 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.06
Nodes (40): parametrize, pytest, ensure_schema_exists(), list_tables(), list_tables_matching(), SparkSession, Unity Catalog convenience helpers. Thin wrappers around Spark SQL DDL/catalog…, Create the catalog/schema if they do not already exist. Requires ``CREATE… (+32 more)

### Community 2 - "infer_column_data_type"
Cohesion: 0.10
Nodes (13): re, infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), Tokenization and data-type inference shared by featurization and corpus…, True for values like 'ICAO123', 'SKU-9981', 'AB12CD34' -- typical ID/code…, Classify a column into the coarse types used for featurization (paper Fig. 5).… (+5 more)

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.05
Nodes (62): argparse, confusion_metrics(), Confusion-matrix scoring shared by every benchmark's evaluation targets. Every…, Precision/recall/F1/accuracy over ``rows``' boolean…, git_commit(), Any, Exception, Path (+54 more)

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
Cohesion: 0.15
Nodes (16): ndarray, drop_nulls(), Remove ``None``/``NaN``-like values, preserving order. Real-world corpus…, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+8 more)

### Community 8 - "UniDetect"
Cohesion: 0.16
Nodes (13): Methodology: mapping real dirty data onto UniDetect's four error types, DataFrame, Score ``table_names`` for the requested error types and rank all results…, Append (or overwrite) a detection result set to the configured UC table., Facade over the offline corpus builder and the four online detectors., UniDetect, config(), corpus_tables_by_category() (+5 more)

### Community 9 - "unidetect/__init__.py"
Cohesion: 0.16
Nodes (16): ColumnDataType, Coarse data-type classification used for featurization (paper Fig. 5). This is…, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, Any (+8 more)

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
Cohesion: 0.18
Nodes (9): collections, dataclasses, fd_compliance_ratio(), FDResult, minority_violation_rows(), FD-compliance-ratio metric (paper Section 3.4, ``FR``). Note on fidelity to the…, Rows to drop to repair the *smallest* FD-violating groups first. For each LHS…, Unit tests for metrics/*, validated against the paper's own worked numbers.… (+1 more)

### Community 14 - "require_min_size"
Cohesion: 0.20
Nodes (9): Sized, InsufficientDataError, Raised when a target column/table does not have enough data to score., Shared helpers for metric-function implementations., require_min_size(), Uniqueness-ratio metric (paper Section 3.3, ``UR``)., ``UR(C) = num-distinct-values(C) / num-total-values(C)``. A ``UR`` close to 1.0…, uniqueness_ratio() (+1 more)

### Community 15 - "CorpusStatsBuilder"
Cohesion: 0.23
Nodes (8): CorpusStatsBuilder, compute(), compute(), DataFrame, SparkSession, Persist a stats DataFrame, replacing only its own ``error_type`` partition(s).…, Builds and persists the ``unidetect_corpus_stats`` Delta table. Parameters…, _stats_schema_without_error_type()

### Community 16 - "featurization.py"
Cohesion: 0.05
Nodes (37): numpy, FeatureBucket, A discretized point in the featurization "cube" (paper Figure 5). Instances of…, Stable string encoding, used as a Delta partition/grouping column., _coerce_numeric(), _score_single_column(), compute(), DataFrame (+29 more)

### Community 17 - ".batch_score"
Cohesion: 0.06
Nodes (28): Benchmark: real_world_gov, Comparing across versions, Layout, Reading the results, Running the benchmark, Which 5 datasets, and why, By dataset, Evaluated columns (+20 more)

### Community 18 - "perturb_numeric_outlier"
Cohesion: 0.28
Nodes (5): compute(), DataFrame, perturb_numeric_outlier(), Drop the single most outlying value by MAD-score (paper Section 3.1)., TestPerturbNumericOutlier

### Community 27 - "duplicate_value_indices"
Cohesion: 0.50
Nodes (3): duplicate_value_indices(), Indices of values that participate in at least one duplicate group. This is the…, TestDuplicateValueIndices

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **29 isolated node(s):** `unidetect`, `Which 5 datasets, and why`, `Layout`, `Reading the results`, `Comparing across versions` (+24 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 196 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `UniDetect`, `unidetect/__init__.py`, `CorpusStatsBuilder`, `featurization.py`, `.batch_score`?**
  _High betweenness centrality (0.162) - this node is a cross-community bridge._
- **Why does `UniDetect` connect `UniDetect` to `ErrorType`, `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `unidetect/__init__.py`, `CorpusStatsBuilder`, `.batch_score`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Why does `Benchmark: real_world_gov` connect `.batch_score` to `UniDetect`, `real_world_gov/run_benchmark.py`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 24 inferred relationships involving `ErrorType` (e.g. with `run()` and `run()`) actually correct?**
  _`ErrorType` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `UniDetect` (e.g. with `run()` and `Why not download the real WIKI corpus in CI?`) actually correct?**
  _`UniDetect` has 10 INFERRED edges - model-reasoned connections that need verification._