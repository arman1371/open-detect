# Graph Report - open-detect  (2026-09-18)

## Corpus Check
- 74 files · ~60,079 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 216 file(s) not represented in the graph (top: .csv 211, (none) 3, .typed 1)

## Summary
- 579 nodes · 1260 edges · 30 communities (28 shown, 2 thin omitted)
- Extraction: 93% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 81 edges (avg confidence: 0.92)
- Token cost: 427,612 input · 0 output

## Community Hubs (Navigation)
- Core Enums & Comparison Types
- Unity Catalog Utilities
- Text Tokenization Utilities
- Benchmark Runner
- Architecture & Design Rationale
- Synthetic Dataset Generation
- Graphify Skill Documentation
- Numeric Outlier Detection (MAD)
- UniDetect Facade & Integration
- Core Data Models
- Error Perturbation Injection
- Benchmark Report Rendering
- Spelling Error Detection (MPD)
- Functional Dependency Detection
- Uniqueness Detection
- Corpus Statistics Builder
- Featurization Bucketing
- Uniqueness Featurization Tests
- Numeric Outlier Perturbation Tests
- Bucketing Utility Tests
- Log-Fit Heuristic Tests
- F1 Score Benchmark Chart
- Overall Metrics Chart
- Detection Ranking Chart
- Corruption Severity Chart
- Feature Bucket Type
- FD Featurization
- Duplicate Value Utility
- Package Root

## God Nodes (most connected - your core abstractions)
1. `ErrorType` - 49 edges
2. `UniDetectConfig` - 33 edges
3. `UniDetect` - 25 edges
4. `ARCHITECTURE.md — Uni-Detect paper-to-code map` - 23 edges
5. `UnityCatalogLocation` - 20 edges
6. `BaseDetector` - 20 edges
7. `CorpusIngestor` - 16 edges
8. `CorpusStatsBuilder` - 15 edges
9. `CorpusStatsStore` - 15 edges
10. `build_uniqueness_bucket()` - 15 edges

## Surprising Connections (you probably didn't know these)
- `README.md — Uni-Detect overview` --references--> `CI workflow: Benchmark (wiki-subset, workflow_dispatch)`  [AMBIGUOUS]
  README.md → .github/workflows/benchmark.yml
- `WIKI-subset benchmark methodology redesign` --semantically_similar_to--> `functional_dependency metric (FR, Section 3.4)`  [INFERRED] [semantically similar]
  benchmarks/README.md → ARCHITECTURE.md
- `WIKI-subset benchmark methodology redesign` --semantically_similar_to--> `FD metric deviation from literal paper formula`  [INFERRED] [semantically similar]
  benchmarks/README.md → ARCHITECTURE.md
- `_build_config()` --uses--> `UniDetectConfig`  [INFERRED]
  benchmarks/run_benchmark.py → src/unidetect/config.py
- `run()` --uses--> `UnityCatalogLocation`  [INFERRED]
  benchmarks/run_benchmark.py → src/unidetect/config.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **graphify Skill Reference Documentation Set** — _claude_skills_graphify_skill, _claude_skills_graphify_references_add_watch, _claude_skills_graphify_references_exports, _claude_skills_graphify_references_extraction_spec, _claude_skills_graphify_references_github_and_merge, _claude_skills_graphify_references_hooks, _claude_skills_graphify_references_query, _claude_skills_graphify_references_transcribe, _claude_skills_graphify_references_update [EXTRACTED 1.00]
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]
- **WIKI-subset benchmark reporting pipeline** — readme, benchmarks_readme, benchmarks_results_report, _github_workflows_benchmark [EXTRACTED 1.00]

## Communities (30 total, 2 thin omitted)

### Community 0 - "Core Enums & Comparison Types"
Cohesion: 0.05
Nodes (63): ABC, collections_abc, Enum, functools, Logger, logging, pyspark_sql, pyspark_sql_types (+55 more)

### Community 1 - "Unity Catalog Utilities"
Cohesion: 0.06
Nodes (41): argparse, parametrize, pytest, ensure_schema_exists(), list_tables(), list_tables_matching(), SparkSession, Unity Catalog convenience helpers. Thin wrappers around Spark SQL DDL/catalog… (+33 more)

### Community 2 - "Text Tokenization Utilities"
Cohesion: 0.07
Nodes (20): re, Global token -> distinct-table document-frequency (``Prev(C)`` input). A…, ``Prev(C)`` (paper Sec. 3.3): average, over values and their tokens, of how…, token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric() (+12 more)

### Community 3 - "Benchmark Runner"
Cohesion: 0.08
Nodes (32): _build_config(), _confusion_metrics(), _git_commit(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), Any (+24 more)

### Community 4 - "Architecture & Design Rationale"
Cohesion: 0.10
Nodes (32): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), ARCHITECTURE.md — Uni-Detect paper-to-code map, ComparisonDirection generalization (INCREASING/DECREASING), Bounded corpus ingestion sampling, FD metric deviation from literal paper formula, Coarse feature-bucket featurization (Figure 5 cube diagram), MPD blocking optimization for spelling metric (+24 more)

### Community 5 - "Synthetic Dataset Generation"
Cohesion: 0.18
Nodes (24): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+16 more)

### Community 6 - "Graphify Skill Documentation"
Cohesion: 0.10
Nodes (24): .claude/CLAUDE.md — graphify trigger, graphify reference: add-watch.md, graphify reference: exports.md, graphify reference: extraction-spec.md, graphify reference: github-and-merge.md, graphify reference: hooks.md, graphify reference: query.md, graphify reference: transcribe.md (+16 more)

### Community 7 - "Numeric Outlier Detection (MAD)"
Cohesion: 0.15
Nodes (16): ndarray, drop_nulls(), Remove ``None``/``NaN``-like values, preserving order. Real-world corpus…, mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation() (+8 more)

### Community 8 - "UniDetect Facade & Integration"
Cohesion: 0.17
Nodes (12): DataFrame, Score ``table_names`` for the requested error types and rank all results…, Append (or overwrite) a detection result set to the configured UC table., Facade over the offline corpus builder and the four online detectors., UniDetect, config(), corpus_tables_by_category(), fixture (+4 more)

### Community 9 - "Core Data Models"
Cohesion: 0.16
Nodes (16): ColumnDataType, Coarse data-type classification used for featurization (paper Fig. 5). This is…, Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, MetricObservation, Any (+8 more)

### Community 10 - "Error Perturbation Injection"
Cohesion: 0.15
Nodes (13): _max_drop(), perturb_functional_dependency(), perturb_spelling(), perturb_uniqueness(), PerturbationOutcome, Per-error-type instantiations of epsilon-perturbation (paper Definition 2).…, Drop minority rows from the smallest violating LHS groups (paper Section 3.4)., Drop duplicate occurrences (paper Example 2). (+5 more)

### Community 11 - "Benchmark Report Rendering"
Cohesion: 0.21
Nodes (17): _f1_by_error_type_chart(), _fmt_pct(), grouped_bar_chart(), main(), _metrics_table_row(), _nice_ceiling(), _overall_metrics_chart(), Path (+9 more)

### Community 12 - "Spelling Error Detection (MPD)"
Cohesion: 0.16
Nodes (11): itertools, rapidfuzz_distance, _blocking_key(), differing_token_lengths(), _length_bucket(), min_pairwise_edit_distance(), MPDResult, Minimum pairwise edit-distance (MPD) metric for spelling errors. See paper… (+3 more)

### Community 13 - "Functional Dependency Detection"
Cohesion: 0.18
Nodes (9): collections, dataclasses, fd_compliance_ratio(), FDResult, minority_violation_rows(), FD-compliance-ratio metric (paper Section 3.4, ``FR``). Note on fidelity to the…, Rows to drop to repair the *smallest* FD-violating groups first. For each LHS…, Unit tests for metrics/*, validated against the paper's own worked numbers.… (+1 more)

### Community 14 - "Uniqueness Detection"
Cohesion: 0.20
Nodes (9): Sized, InsufficientDataError, Raised when a target column/table does not have enough data to score., Shared helpers for metric-function implementations., require_min_size(), Uniqueness-ratio metric (paper Section 3.3, ``UR``)., ``UR(C) = num-distinct-values(C) / num-total-values(C)``. A ``UR`` close to 1.0…, uniqueness_ratio() (+1 more)

### Community 15 - "Corpus Statistics Builder"
Cohesion: 0.23
Nodes (8): CorpusStatsBuilder, compute(), compute(), DataFrame, SparkSession, Persist a stats DataFrame, replacing only its own ``error_type`` partition(s).…, Builds and persists the ``unidetect_corpus_stats`` Delta table. Parameters…, _stats_schema_without_error_type()

### Community 16 - "Featurization Bucketing"
Cohesion: 0.19
Nodes (10): numpy, _coerce_numeric(), _score_single_column(), DataFrame, compute(), bucket_row_count(), bucket_token_length(), build_outlier_bucket() (+2 more)

### Community 17 - "Uniqueness Featurization Tests"
Cohesion: 0.22
Nodes (6): DataFrame, compute(), bucket_leftness(), build_uniqueness_bucket(), Column position from the left (paper Sec. 3.3), capped to bound cardinality., TestFeatureBucketBuilders

### Community 18 - "Numeric Outlier Perturbation Tests"
Cohesion: 0.28
Nodes (5): compute(), DataFrame, perturb_numeric_outlier(), Drop the single most outlying value by MAD-score (paper Section 3.1)., TestPerturbNumericOutlier

### Community 19 - "Bucketing Utility Tests"
Cohesion: 0.36
Nodes (4): bucket_by_edges(), bucket_token_prevalence(), Map ``value`` into one of ``len(edges) + 1`` half-open ranges. ``edges=(20, 50,…, TestBucketing

### Community 20 - "Log-Fit Heuristic Tests"
Cohesion: 0.29
Nodes (4): log_transform_fits_better(), Heuristic for the "whether logarithm-transform better fits the data" dimension.…, Unit tests for featurization.py and text_utils.py., TestLogFit

### Community 21 - "F1 Score Benchmark Chart"
Cohesion: 0.33
Nodes (7): F1 Score by Error Type (Chart), F1 Score, Functional Dependency Error Type (F1 = 0.67), Numeric Outlier Error Type (F1 = 0.91), Overall (F1 = 0.78), Spelling Error Type (F1 = 0.82), Uniqueness Error Type (F1 = 0.74)

### Community 22 - "Overall Metrics Chart"
Cohesion: 0.53
Nodes (6): Accuracy, Overall Metrics Chart, Evaluation Targets (n=60), F1, Precision, Recall

### Community 23 - "Detection Ranking Chart"
Cohesion: 0.40
Nodes (6): Detection ranking chart: lr_ratio, functional_dependency error category, lr_ratio detection metric, numeric_outlier error category, spelling error category, uniqueness error category

### Community 24 - "Corruption Severity Chart"
Cohesion: 0.40
Nodes (6): Accuracy by Corruption Severity (Chart), Clean (No Injection) Severity: 0.56 accuracy, Moderate Corruption Severity: 1.00 accuracy, Obvious Corruption Severity: 0.50 accuracy, Paper Example Severity: 0.88 accuracy, Subtle Corruption Severity: 0.75 accuracy

### Community 25 - "Feature Bucket Type"
Cohesion: 0.40
Nodes (3): FeatureBucket, A discretized point in the featurization "cube" (paper Figure 5). Instances of…, Stable string encoding, used as a Delta partition/grouping column.

### Community 26 - "FD Featurization"
Cohesion: 0.40
Nodes (4): compute(), DataFrame, build_functional_dependency_bucket(), FD reuses the uniqueness featurization, applied to the RHS column (Sec. 3.4).

### Community 27 - "Duplicate Value Utility"
Cohesion: 0.50
Nodes (3): duplicate_value_indices(), Indices of values that participate in at least one duplicate group. This is the…, TestDuplicateValueIndices

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references
- `Obvious Corruption Severity: 0.50 accuracy` → `Moderate Corruption Severity: 1.00 accuracy`  [AMBIGUOUS]
  benchmarks/results/charts/severity_accuracy.svg · relation: conceptually_related_to

## Knowledge Gaps
- **24 isolated node(s):** `unidetect`, `graphify reference: github-and-merge.md`, `CI workflow: CI (lint/test/type-check)`, `benchmarks/results/REPORT.md — benchmark results`, `ErrorType enum (Definition 1)` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 178 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Obvious Corruption Severity: 0.50 accuracy` and `Moderate Corruption Severity: 1.00 accuracy`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `ErrorType` connect `Core Enums & Comparison Types` to `Unity Catalog Utilities`, `Benchmark Runner`, `UniDetect Facade & Integration`, `Core Data Models`, `Corpus Statistics Builder`, `Featurization Bucketing`, `Uniqueness Featurization Tests`, `Feature Bucket Type`, `FD Featurization`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `UniDetectConfig` connect `Unity Catalog Utilities` to `Core Enums & Comparison Types`, `Benchmark Runner`, `UniDetect Facade & Integration`, `Core Data Models`, `Corpus Statistics Builder`, `Featurization Bucketing`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Why does `UniDetect` connect `UniDetect Facade & Integration` to `Core Enums & Comparison Types`, `Unity Catalog Utilities`, `Benchmark Runner`, `Core Data Models`, `Corpus Statistics Builder`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `ErrorType` (e.g. with `run()` and `main()`) actually correct?**
  _`ErrorType` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `UniDetectConfig` (e.g. with `_build_config()` and `main()`) actually correct?**
  _`UniDetectConfig` has 10 INFERRED edges - model-reasoned connections that need verification._