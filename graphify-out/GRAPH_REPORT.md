# Graph Report - open-detect  (2026-09-19)

## Corpus Check
- 78 files · ~67,388 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 231 file(s) not represented in the graph (top: .csv 226, (none) 3, .typed 1)

## Summary
- 639 nodes · 1396 edges · 33 communities (28 shown, 5 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 93 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8c42da01`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- detectors/base.py
- UniDetectConfig
- text_utils.py
- real_world_gov/run_benchmark.py
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- graphify SKILL.md — main pipeline skill
- outliers.py
- UniDetect
- ErrorType
- perturbation.py
- benchmarks/generate_report.py
- metrics/spelling.py
- metrics/functional_dependency.py
- uniqueness_ratio
- CorpusStatsBuilder
- featurization.py
- CorpusIngestor
- perturb_numeric_outlier
- bucket_by_edges
- test_featurization.py
- F1 Score by Error Type (Chart)
- Overall Metrics Chart
- Detection ranking chart: lr_ratio
- Accuracy by Corruption Severity (Chart)
- tokenize
- infer_column_data_type
- duplicate_value_indices
- unidetect
- is_float_like
- is_integer_like
- common/__init__.py

## God Nodes (most connected - your core abstractions)
1. `ErrorType` - 50 edges
2. `UniDetectConfig` - 34 edges
3. `UniDetect` - 26 edges
4. `ARCHITECTURE.md — Uni-Detect paper-to-code map` - 23 edges
5. `UnityCatalogLocation` - 21 edges
6. `BaseDetector` - 20 edges
7. `CorpusStatsBuilder` - 16 edges
8. `CorpusIngestor` - 16 edges
9. `CorpusStatsStore` - 15 edges
10. `build_uniqueness_bucket()` - 15 edges

## Surprising Connections (you probably didn't know these)
- `Running the benchmark` --references--> `CorpusStatsBuilder`  [INFERRED]
  benchmarks/real_world_gov/README.md → src/unidetect/corpus/builder.py
- `WIKI-subset benchmark methodology redesign` --semantically_similar_to--> `functional_dependency metric (FR, Section 3.4)`  [INFERRED] [semantically similar]
  benchmarks/README.md → ARCHITECTURE.md
- `README.md — Uni-Detect overview` --references--> `CI workflow: Benchmark (wiki-subset, workflow_dispatch)`  [AMBIGUOUS]
  README.md → .github/workflows/benchmark.yml
- `WIKI-subset benchmark methodology redesign` --semantically_similar_to--> `FD metric deviation from literal paper formula`  [INFERRED] [semantically similar]
  benchmarks/README.md → ARCHITECTURE.md
- `Methodology: mapping real dirty data onto UniDetect's four error types` --references--> `confusion_metrics()`  [INFERRED]
  benchmarks/real_world_gov/README.md → benchmarks/common/metrics.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **WIKI-subset benchmark reporting pipeline** — readme, benchmarks_readme, benchmarks_results_report, _github_workflows_benchmark [EXTRACTED 1.00]
- **graphify Skill Reference Documentation Set** — _claude_skills_graphify_skill, _claude_skills_graphify_references_add_watch, _claude_skills_graphify_references_exports, _claude_skills_graphify_references_extraction_spec, _claude_skills_graphify_references_github_and_merge, _claude_skills_graphify_references_hooks, _claude_skills_graphify_references_query, _claude_skills_graphify_references_transcribe, _claude_skills_graphify_references_update [EXTRACTED 1.00]
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (33 total, 5 thin omitted)

### Community 0 - "detectors/base.py"
Cohesion: 0.07
Nodes (36): ABC, collections_abc, pyspark_sql, pyspark_sql_types, Turn a set of Unity Catalog tables into the canonical corpus representation.…, Canonical Delta table schemas used by the corpus builder and store. Keeping…, BaseDetector, make_evidence_json() (+28 more)

### Community 1 - "UniDetectConfig"
Cohesion: 0.05
Nodes (54): argparse, delta, build_spark(), main(), SparkSession, Standalone quickstart: build a tiny corpus and run Uni-Detect against it. Run…, functools, json (+46 more)

### Community 2 - "text_utils.py"
Cohesion: 0.21
Nodes (6): re, is_mixed_alphanumeric(), Tokenization and data-type inference shared by featurization and corpus…, True for values like 'ICAO123', 'SKU-9981', 'AB12CD34' -- typical ID/code…, Unit tests for text_utils.py., TestMixedAlphanumeric

### Community 3 - "real_world_gov/run_benchmark.py"
Cohesion: 0.07
Nodes (49): confusion_metrics(), Confusion-matrix scoring shared by every benchmark's evaluation targets. Every…, Precision/recall/F1/accuracy over ``rows``' boolean…, git_commit(), Any, Exception, Path, Local, Delta-enabled Spark session bootstrap shared by every benchmark.… (+41 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.10
Nodes (32): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), ARCHITECTURE.md — Uni-Detect paper-to-code map, ComparisonDirection generalization (INCREASING/DECREASING), Bounded corpus ingestion sampling, FD metric deviation from literal paper formula, Coarse feature-bucket featurization (Figure 5 cube diagram), MPD blocking optimization for spelling metric (+24 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.15
Nodes (28): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+20 more)

### Community 6 - "graphify SKILL.md — main pipeline skill"
Cohesion: 0.10
Nodes (24): .claude/CLAUDE.md — graphify trigger, graphify reference: add-watch.md, graphify reference: exports.md, graphify reference: extraction-spec.md, graphify reference: github-and-merge.md, graphify reference: hooks.md, graphify reference: query.md, graphify reference: transcribe.md (+16 more)

### Community 7 - "outliers.py"
Cohesion: 0.14
Nodes (19): ndarray, numpy, Sized, drop_nulls(), Remove ``None``/``NaN``-like values, preserving order. Real-world corpus…, require_min_size(), mad_scores(), MADResult (+11 more)

### Community 8 - "UniDetect"
Cohesion: 0.16
Nodes (13): Methodology: mapping real dirty data onto UniDetect's four error types, DataFrame, Score ``table_names`` for the requested error types and rank all results…, Append (or overwrite) a detection result set to the configured UC table., Facade over the offline corpus builder and the four online detectors., UniDetect, config(), corpus_tables_by_category() (+5 more)

### Community 9 - "ErrorType"
Cohesion: 0.06
Nodes (44): Enum, Logger, ColumnDataType, ComparisonDirection, ErrorType, Core enumerations shared across the unidetect package., Coarse data-type classification used for featurization (paper Fig. 5). This is…, Direction in which a metric moves once the anomalous subset is removed. Uni-… (+36 more)

### Community 10 - "perturbation.py"
Cohesion: 0.15
Nodes (13): _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, Per-error-type instantiations of epsilon-perturbation (paper Definition 2).…, Drop minority rows from the smallest violating LHS groups (paper Section 3.4)., Drop duplicate occurrences (paper Example 2). (+5 more)

### Community 11 - "benchmarks/generate_report.py"
Cohesion: 0.13
Nodes (27): grouped_bar_chart(), _nice_ceiling(), Pure-stdlib SVG bar-chart rendering shared by every benchmark's report.…, A bar path rounded at the top (far end from the baseline) only., _rounded_top_rect(), _f1_by_error_type_chart(), _fmt_pct(), main() (+19 more)

### Community 12 - "metrics/spelling.py"
Cohesion: 0.16
Nodes (11): itertools, rapidfuzz_distance, _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, Minimum pairwise edit-distance (MPD) metric for spelling errors. See paper… (+3 more)

### Community 13 - "metrics/functional_dependency.py"
Cohesion: 0.18
Nodes (9): collections, dataclasses, fd_compliance_ratio(), FDResult, minority_violation_rows(), FD-compliance-ratio metric (paper Section 3.4, ``FR``). Note on fidelity to the…, Rows to drop to repair the *smallest* FD-violating groups first. For each LHS…, Unit tests for metrics/*, validated against the paper's own worked numbers.… (+1 more)

### Community 14 - "uniqueness_ratio"
Cohesion: 0.31
Nodes (5): InsufficientDataError, Raised when a target column/table does not have enough data to score., ``UR(C) = num-distinct-values(C) / num-total-values(C)``. A ``UR`` close to 1.0…, uniqueness_ratio(), TestUniquenessRatio

### Community 15 - "CorpusStatsBuilder"
Cohesion: 0.11
Nodes (17): Benchmark: real_world_gov, Comparing across versions, Layout, Reading the results, Running the benchmark, Which 5 datasets, and why, By dataset, Evaluated columns (+9 more)

### Community 16 - "featurization.py"
Cohesion: 0.23
Nodes (11): _coerce_numeric(), compute(), _score_single_column(), bucket_row_count(), bucket_token_length(), bucket_token_prevalence(), build_outlier_bucket(), build_spelling_bucket() (+3 more)

### Community 17 - "CorpusIngestor"
Cohesion: 0.17
Nodes (8): CorpusIngestor, DataFrame, SparkSession, Build the ``corpus_column_pairs`` DataFrame used for FD statistics., Global token -> distinct-table document-frequency (``Prev(C)`` input). A…, Builds ``corpus_columns``, ``corpus_column_pairs`` and ``token_stats``.…, Build the ``corpus_columns`` DataFrame from a list of UC table FQNs. Each…, SparkSession

### Community 18 - "perturb_numeric_outlier"
Cohesion: 0.47
Nodes (3): perturb_numeric_outlier(), Drop the single most outlying value by MAD-score (paper Section 3.1)., TestPerturbNumericOutlier

### Community 19 - "bucket_by_edges"
Cohesion: 0.24
Nodes (5): bucket_by_edges(), bucket_leftness(), Map ``value`` into one of ``len(edges) + 1`` half-open ranges. ``edges=(20, 50,…, Column position from the left (paper Sec. 3.3), capped to bound cardinality., TestBucketing

### Community 20 - "test_featurization.py"
Cohesion: 0.29
Nodes (4): log_transform_fits_better(), Heuristic for the "whether logarithm-transform better fits the data" dimension.…, Unit tests for featurization.py and text_utils.py., TestLogFit

### Community 21 - "F1 Score by Error Type (Chart)"
Cohesion: 0.33
Nodes (7): F1 Score by Error Type (Chart), F1 Score, Functional Dependency Error Type (F1 = 0.67), Numeric Outlier Error Type (F1 = 0.91), Overall (F1 = 0.78), Spelling Error Type (F1 = 0.82), Uniqueness Error Type (F1 = 0.74)

### Community 22 - "Overall Metrics Chart"
Cohesion: 0.53
Nodes (6): Accuracy, Overall Metrics Chart, Evaluation Targets (n=60), F1, Precision, Recall

### Community 23 - "Detection ranking chart: lr_ratio"
Cohesion: 0.40
Nodes (6): Detection ranking chart: lr_ratio, functional_dependency error category, lr_ratio detection metric, numeric_outlier error category, spelling error category, uniqueness error category

### Community 24 - "Accuracy by Corruption Severity (Chart)"
Cohesion: 0.40
Nodes (6): Accuracy by Corruption Severity (Chart), Clean (No Injection) Severity: 0.56 accuracy, Moderate Corruption Severity: 1.00 accuracy, Obvious Corruption Severity: 0.50 accuracy, Paper Example Severity: 0.88 accuracy, Subtle Corruption Severity: 0.75 accuracy

### Community 25 - "tokenize"
Cohesion: 0.24
Nodes (6): ``Prev(C)`` (paper Sec. 3.3): average, over values and their tokens, of how…, token_prevalence(), Split a value into alphanumeric tokens, discarding punctuation/whitespace., tokenize(), TestTokenPrevalence, TestTokenize

### Community 26 - "infer_column_data_type"
Cohesion: 0.39
Nodes (3): infer_column_data_type(), Classify a column into the coarse types used for featurization (paper Fig. 5).…, TestDataTypeInference

### Community 27 - "duplicate_value_indices"
Cohesion: 0.50
Nodes (3): duplicate_value_indices(), Indices of values that participate in at least one duplicate group. This is the…, TestDuplicateValueIndices

## Ambiguous Edges - Review These
- `Moderate Corruption Severity: 1.00 accuracy` → `Obvious Corruption Severity: 0.50 accuracy`  [AMBIGUOUS]
  benchmarks/results/charts/severity_accuracy.svg · relation: conceptually_related_to
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **31 isolated node(s):** `unidetect`, `Which 5 datasets, and why`, `Layout`, `Reading the results`, `Comparing across versions` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 198 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Moderate Corruption Severity: 1.00 accuracy` and `Obvious Corruption Severity: 0.50 accuracy`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `ErrorType` connect `ErrorType` to `detectors/base.py`, `UniDetectConfig`, `real_world_gov/run_benchmark.py`, `UniDetect`, `CorpusStatsBuilder`, `featurization.py`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Why does `Benchmark: real_world_gov` connect `CorpusStatsBuilder` to `UniDetect`, `real_world_gov/run_benchmark.py`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `benchmarks/README.md — WIKI-subset benchmark` connect `ARCHITECTURE.md — Uni-Detect paper-to-code map` to `CorpusStatsBuilder`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 24 inferred relationships involving `ErrorType` (e.g. with `run()` and `run()`) actually correct?**
  _`ErrorType` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `_build_config()`) actually correct?**
  _`UniDetectConfig` has 11 INFERRED edges - model-reasoned connections that need verification._