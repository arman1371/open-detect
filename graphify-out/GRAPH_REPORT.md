# Graph Report - open-detect  (2026-11-19)

## Corpus Check
- 206 files · ~162,411 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 234 file(s) not represented in the graph (top: .csv 227, (none) 3, .properties 1)
- WARNING: 234 of 468 files seen (50%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 3021 nodes · 6618 edges · 157 communities (131 shown, 26 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 852 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6a46b108`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- verify_build_config
- dataset_utils.py
- pandas
- deploy
- ARCHITECTURE.md — Uni-Detect paper-to-code map
- generate_dataset.py
- .claude/CLAUDE.md — graphify trigger
- builder.py
- README.md — Uni-Detect overview
- json
- FailureCounts
- PRD: User Feedback Tooltips
- ValidationError
- new_cluster
- CellResult
- AutoValidateConfig
- InferredPattern
- test_spelling_detector.py
- 7.2 Key Features
- perturbation.py
- fmdv_v
- permissions
- with
- update-graph
- check_failure_threshold
- with
- get_spec
- UnityCatalogLocation
- Completed Work
- _check_expected_type
- UniDetectConfig
- .detect
- pytest
- _check_unknown_kwargs
- main
- ScoringJobCounter
- algorithms/uni-detect.md
- build_column_features
- FailureCountsAccumulatorParam
- InsufficientDataError
- metrics/functional_dependency.py
- real_world_gov benchmark results
- propagate_labels
- test_build_corpus_statistics.py
- main
- Benchmark: WIKI subset
- GroundTruthLabeler
- Auto-Validate
- test_algorithms_registry.py
- CHANGELOG
- .detect
- index.py
- raha/detector.py
- Running on Databricks
- _ensure_dataframe_is_spark
- fmdv
- updates
- Raha
- jobs
- .build_corpus_statistics
- _ensure_sequence_of_str
- _score_single_column
- build
- uses
- confusion_metrics
- env
- perturb_spelling
- CorpusStatsStore
- dry_run
- Appendix: Validation Function Reference
- FeatureBucket
- CorpusIngestor
- variables
- KnownIndexLabeler
- PRD: API Validation Framework for open-detect
- dev
- clean_column
- Commit conventions and releases
- labeling.py
- UnknownAlgorithmError
- Current Status: BLOCKED
- _aggregate_scored_rows
- UniDetect
- numpy
- test
- hooks
- release.yml
- release
- test_raha_strategies.py
- featurization.py
- pypi
- Current Status: BLOCKED
- log_transform_fits_better
- spark_session.py
- with
- on
- _check_dataframe_is_spark
- steps
- argparse
- CallableLabeler
- PatternIndex
- FakeConf
- open_detect/exceptions.py
- sonarqube
- profile.py
- infer_column_data_type
- docs
- force
- _reject_unknown_kwargs
- list_tables_matching
- docs/index.md
- select_fd_column_pairs
- _date_index
- open-detect
- OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate
- test_package_init.py
- `uni_detect`
- `raha`
- OPE-86 / PR #96 — Copilot Review Fixes
- Comparing algorithms
- AutoValidateAlgorithm
- _FakeDetector
- paperclip-issue-update.sh
- algorithms/index.md
- Auto-Validate
- __getattr__
- Uni-Detect
- auto_validate/detector.py
- TestConfigThreshold
- drop_nulls
- _StubDetector
- sys
- CorpusStatsBuilder
- __getattr__
- Scoring auto_validate
- test_hygiene.py
- _detector
- test_metrics.py
- scoped_conf
- get_logger
- ErrorType
- make_evidence_json
- patterns.py
- perturb_numeric_outlier
- outliers.py
- min_pairwise_edit_distance
- snapshot.py
- real_world_gov/run_benchmark.py
- RahaConfig
- wiki_subset/generate_report.py
- Performance Baseline — OPE-87
- real_world_gov/generate_report.py
- conftest.py
- Summary

## God Nodes (most connected - your core abstractions)
1. `AutoValidateConfig` - 122 edges
2. `ErrorType` - 97 edges
3. `UniDetectConfig` - 95 edges
4. `UniDetect` - 70 edges
5. `FailureCounts` - 62 edges
6. `ValidationError` - 48 edges
7. `UnityCatalogLocation` - 47 edges
8. `build_pattern_index()` - 46 edges
9. `AutoValidateAlgorithm` - 39 edges
10. `CellResult` - 38 edges

## Surprising Connections (you probably didn't know these)
- `Bug Fixes` --references--> `_value_matches()`  [INFERRED]
  RELEASE-NOTES-OPE-162.md → src/open_detect/algorithms/auto_validate/detector.py
- `Phase 1: Core Tooltip Engine (4 weeks)` --references--> `CellResult`  [INFERRED]
  PRD-user-feedback-tooltips.md → src/open_detect/algorithms/base.py
- `Reading results` --references--> `AlgorithmResult`  [INFERRED]
  docs/getting-started/quickstart.md → src/open_detect/algorithms/base.py
- `3.1 Context` --references--> `AlgorithmResult`  [INFERRED]
  PRD-API-Validation-Framework.md → src/open_detect/algorithms/base.py
- `One contract: `detect()`` --references--> `ErrorDetectionAlgorithm`  [INFERRED]
  docs/concepts.md → src/open_detect/algorithms/base.py

## Import Cycles
- 2-file cycle: `src/open_detect/algorithms/uni_detect/exceptions.py -> src/open_detect/exceptions.py -> src/open_detect/algorithms/uni_detect/exceptions.py`

## Hyperedges (group relationships)
- **Uni-Detect paper-to-code mapping table** — architecture, paper_unidetect, unidetect_detectors_base_basedetector, unidetect_corpus_builder_corpusstatsbuilder, unidetect_corpus_store_corpusstatsstore [EXTRACTED 1.00]

## Communities (157 total, 26 thin omitted)

### Community 0 - "verify_build_config"
Cohesion: 0.12
Nodes (12): diff_fingerprints(), property_key(), read_build_config(), verify_build_config(), write_build_config(), _config(), FakeSpark, test_diff_fingerprints_reports_missing_fields() (+4 more)

### Community 1 - "dataset_utils.py"
Cohesion: 0.22
Nodes (6): canonical_column(), dataset_paths(), load_changes(), load_csv(), Source, _dataset_frames()

### Community 2 - "pandas"
Cohesion: 0.07
Nodes (35): _city_column(), _count_detect_calls(), _counting_value_matches(), counting(), _counting_value_matches_groups(), counting(), _detect(), _detector() (+27 more)

### Community 3 - "deploy"
Cohesion: 0.06
Nodes (33): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, permissions (+25 more)

### Community 4 - "ARCHITECTURE.md — Uni-Detect paper-to-code map"
Cohesion: 0.15
Nodes (15): ARCHITECTURE.md — Uni-Detect paper-to-code map, ErrorType enum (Definition 1), CorpusStatsBuilder (offline learning phase), CorpusStatsStore.batch_score (LR test / online lookup), BaseDetector template method (Definition 4), functional_dependency detector, numeric_outlier detector, spelling detector (+7 more)

### Community 5 - "generate_dataset.py"
Cohesion: 0.20
Nodes (19): build_corpus(), build_eval_targets(), build_fd_targets(), build_outlier_targets(), build_spelling_targets(), build_uniqueness_targets(), _clear_dir(), _fd_fp_variants() (+11 more)

### Community 7 - "builder.py"
Cohesion: 0.08
Nodes (3): _spark_available(), TestCorpusStatsSchema, TestCorpusStatsSchemaWeightType

### Community 8 - "README.md — Uni-Detect overview"
Cohesion: 0.13
Nodes (15): CI workflow: Benchmark (wiki-subset, workflow_dispatch), CI workflow: CI (lint/test/type-check), benchmarks/README.md — WIKI-subset benchmark, artifacts, open_detect_wheel, bundle, name, build (+7 more)

### Community 9 - "json"
Cohesion: 0.15
Nodes (11): _build_config(), _load_corpus_tables(), _load_targets(), main(), _print_comparison(), run(), run_auto_validate(), _metrics() (+3 more)

### Community 10 - "FailureCounts"
Cohesion: 0.12
Nodes (9): compute(), compute(), _score_fd_pair(), compute(), FailureCounts, compute(), _raise(), TestAttempt (+1 more)

### Community 11 - "PRD: User Feedback Tooltips"
Cohesion: 0.06
Nodes (35): 1. Summary, 2. Contacts, 3. Background, 4. Objective, 5. Market Segments, 6. Value Propositions, 7.1 UX / Prototypes, 7.2 Key Features (+27 more)

### Community 12 - "ValidationError"
Cohesion: 0.19
Nodes (8): 8.1 Timeline, 8.2 Versioning, 8.3 Migration Path, 8.4 Future Extensions (Post-MVP), 8. Release, ValidationError, _validate_literal_value(), TestValidateLiteralValue

### Community 13 - "new_cluster"
Cohesion: 0.09
Nodes (31): job_clusters, name, schedule, tags, tasks, job_cluster_key, new_cluster, build_corpus_statistics_job (+23 more)

### Community 14 - "CellResult"
Cohesion: 0.10
Nodes (7): Through the registry, The shared result schema, Why a common interface, AlgorithmResult, CellResult, TestAlgorithmResult, TestCellResultEvidence

### Community 15 - "AutoValidateConfig"
Cohesion: 0.08
Nodes (11): AutoValidateConfig, build_pattern_index(), TestDefaults, TestValidation, TestSegmentDp, solve(), TestCorpusInputShapes, TestEquivalenceToReferenceBuild (+3 more)

### Community 16 - "InferredPattern"
Cohesion: 0.09
Nodes (10): check_drift(), _clean_series(), _conforms(), _conforms_segments(), DriftResult, _fisher_two_tailed(), InferredPattern, _make_pattern() (+2 more)

### Community 17 - "test_spelling_detector.py"
Cohesion: 0.13
Nodes (13): _build_row(), _drop_nulls(), _original_row_ids(), _positions_of(), _row(), _score(), test_build_row_maps_row_ids_via_original_positions(), test_candidate_id_suffix_uses_first_mapped_row_id() (+5 more)

### Community 18 - "7.2 Key Features"
Cohesion: 0.17
Nodes (12): 7.1 Architecture Overview, 7.2.1 Unknown Kwargs Rejection, 7.2.2 Type Checking with Sequence[str] Special Handling, 7.2.3 Literal Value Validation, 7.2.4 Column Uniqueness Check, 7.2.5 DataFrame Type Validation (Spark + pandas), 7.2.6 Sequence of Strings Validation, 7.2.7 Column Presence Check (Algorithm-specific) (+4 more)

### Community 19 - "perturbation.py"
Cohesion: 0.13
Nodes (8): duplicate_value_indices(), _max_drop(), perturb_functional_dependency(), perturb_uniqueness(), PerturbationOutcome, TestDuplicateValueIndices, TestPerturbFunctionalDependency, TestPerturbUniqueness

### Community 20 - "fmdv_v"
Cohesion: 0.10
Nodes (10): Variants, Recent Changes, _coarse_signature(), fmdv_v(), fmdv_vh(), _build_index(), TestCoarseSignature, TestFmdvV (+2 more)

### Community 21 - "permissions"
Cohesion: 0.07
Nodes (28): if, permissions, runs-on, steps, types, types, jobs, claude (+20 more)

### Community 22 - "with"
Cohesion: 0.09
Nodes (26): UV_PYTHON, jobs, real-world-gov, wiki-subset, name, on, workflow_dispatch, env (+18 more)

### Community 23 - "update-graph"
Cohesion: 0.08
Nodes (24): concurrency, cancel-in-progress, group, jobs, update-graph, name, on, push (+16 more)

### Community 25 - "with"
Cohesion: 0.12
Nodes (16): with, cache, cache-dependency-path, distribution, enable-cache, fetch-depth, if-no-files-found, java-version (+8 more)

### Community 26 - "get_spec"
Cohesion: 0.13
Nodes (9): ComparisonDirection, _require_min_rows(), all_specs(), ErrorTypeSpec, get_spec(), TestBatchScoreOptimization, TestScoreFdPair, TestAllSpecs (+1 more)

### Community 27 - "UnityCatalogLocation"
Cohesion: 0.11
Nodes (11): ensure_schema_exists(), UnityCatalogLocation, _validate_edges(), _run(), _require_columns(), ConfigurationError, TestEnsureSchemaExists, TestRedactEvidence (+3 more)

### Community 28 - "Completed Work"
Cohesion: 0.22
Nodes (8): Blockers, Completed Work, Next Steps, OPE-89: Fix Spark Cache Lifecycle in Uni-Detect, Progress, Related Issues, Related Work, Status

### Community 30 - "UniDetectConfig"
Cohesion: 0.14
Nodes (4): UniDetectConfig, config(), TestUniDetectConfig, config()

### Community 31 - ".detect"
Cohesion: 0.11
Nodes (4): cluster_column(), sample_tuple(), TestClusterColumn, TestSampleTuple

### Community 32 - "pytest"
Cohesion: 0.08
Nodes (12): __getattr__(), __getattr__(), pair_table(), _fresh_import(), test_core_missing_attr_raises(), test_core_package_getattr_shim(), test_exceptions_getattr_shim(), test_from_core_import_submodule() (+4 more)

### Community 33 - "_check_unknown_kwargs"
Cohesion: 0.22
Nodes (7): 6.1 Customer Jobs/Needs, 6.2 Gains, 6.3 Pain Avoidance, 6.4 Competitive Advantage, 6. Value Proposition(s), _check_unknown_kwargs(), TestCheckUnknownKwargs

### Community 34 - "main"
Cohesion: 0.17
Nodes (6): main(), parse_args(), TestEpsilonAndMismatchFlags, TestMain, TestMainConfiguresLogging, TestParseArgs

### Community 35 - "ScoringJobCounter"
Cohesion: 0.07
Nodes (12): ScopeStats, ScoringJobCounter, counting_batch_score(), SparkJobCounter, TestDetectCacheLifecycleSpark, _FakeContext, _FakeTracker, _spark() (+4 more)

### Community 36 - "algorithms/uni-detect.md"
Cohesion: 0.22
Nodes (7): Benchmarks, How to read them, Latest results, Running them, Installation, Installing from source, Pick your extra

### Community 37 - "build_column_features"
Cohesion: 0.15
Nodes (8): build_all_features(), build_column_features(), _compact_dtype(), test_build_all_features_covers_every_column(), test_drops_constant_features(), test_feature_values_are_binary(), test_keeps_informative_features(), TestFeatureMatrixDtype

### Community 39 - "InsufficientDataError"
Cohesion: 0.21
Nodes (8): InsufficientDataError, require_min_size(), _blocking_keys(), _closest_pair(), MPDResult, _search_mpd(), _result(), try_min_pairwise_edit_distance()

### Community 40 - "metrics/functional_dependency.py"
Cohesion: 0.21
Nodes (4): fd_compliance_ratio(), FDResult, minority_violation_rows(), TestFunctionalDependency

### Community 41 - "real_world_gov benchmark results"
Cohesion: 0.15
Nodes (13): Algorithm comparison, `auto_validate`, By dataset (cell-level), By dataset (cell-level), By dataset (column-level), By dataset (column-level), By dataset (column-level), Evaluated columns (column-level) (+5 more)

### Community 43 - "test_build_corpus_statistics.py"
Cohesion: 0.31
Nodes (4): _config(), test_build_corpus_statistics_calls_ingest_and_unpersist(), test_build_corpus_statistics_token_path(), test_detect_exception_calls_release()

### Community 44 - "main"
Cohesion: 0.36
Nodes (3): main(), test_main_installs_logging(), TestMain

### Community 45 - "Benchmark: WIKI subset"
Cohesion: 0.13
Nodes (13): A note on methodology (read this before trusting the numbers), Benchmark: WIKI subset, Comparing across versions, Reading the results without JSON, Running the benchmark, Why not download the real WIKI corpus in CI?, Algorithm comparison, `auto_validate` (+5 more)

### Community 46 - "GroundTruthLabeler"
Cohesion: 0.26
Nodes (3): GroundTruthLabeler, _values_equal(), TestGroundTruthLabeler

### Community 47 - "Auto-Validate"
Cohesion: 0.25
Nodes (6): Auto-Validate, Configuration, Drift checking, How it works, Install, Using the parts directly

### Community 48 - "test_algorithms_registry.py"
Cohesion: 0.06
Nodes (24): Check it works, 1. Implement `ErrorDetectionAlgorithm`, 2. Register it, 3. Test it, As a plugin package (no changes to `open-detect`), In your own code, Writing your own algorithm, API reference (+16 more)

### Community 49 - "CHANGELOG"
Cohesion: 0.07
Nodes (28): Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes, Bug Fixes (+20 more)

### Community 50 - ".detect"
Cohesion: 0.29
Nodes (3): _config(), _row(), TestUniDetectAlgorithm

### Community 51 - "index.py"
Cohesion: 0.08
Nodes (14): _append_literal(), _is_numeric(), matches(), matches_tokens(), _parse(), _part_matches(), token_count(), indexable_values() (+6 more)

### Community 52 - "raha/detector.py"
Cohesion: 0.14
Nodes (11): ErrorDetectionAlgorithm, _load_auto_validate(), _load_raha(), _load_uni_detect(), _constant_factory(), _load_entry_points(), register_algorithm(), decorator() (+3 more)

### Community 53 - "Running on Databricks"
Cohesion: 0.33
Nodes (5): Job arguments, Jobs, Notebooks, Practical advice, Running on Databricks

### Community 55 - "fmdv"
Cohesion: 0.12
Nodes (7): _clean(), fmdv(), fmdv_h(), _build_index(), TestFmdvBasic, TestFmdvH, _tiny_corpus()

### Community 56 - "updates"
Cohesion: 0.13
Nodes (14): prefix, patterns, github-actions, python-dependencies, patterns, update-types, interval, updates (+6 more)

### Community 57 - "Raha"
Cohesion: 0.17
Nodes (9): Configuration, How it works, Install, Raha, Scope, Configuration, Detector, Labelers (+1 more)

### Community 58 - "jobs"
Cohesion: 0.15
Nodes (12): if, name, needs, runs-on, concurrency, cancel-in-progress, group, jobs (+4 more)

### Community 59 - ".build_corpus_statistics"
Cohesion: 0.14
Nodes (6): build_spark(), main(), corpus_tables_by_category(), TestCorpusBuilderAndDetectors, _write_table(), TestDetectReturnsEmptyResultWhenNoCandidates

### Community 61 - "_score_single_column"
Cohesion: 0.13
Nodes (6): _coerce_numeric(), _score_single_column(), config(), TestCoerceNumeric, TestScoreSingleColumn, score()

### Community 62 - "build"
Cohesion: 0.17
Nodes (12): env, name, runs-on, timeout-minutes, UV_PYTHON, build, lint, env (+4 more)

### Community 63 - "uses"
Cohesion: 0.23
Nodes (12): steps, steps, type-check, steps, name, run, timeout-minutes, uses (+4 more)

### Community 64 - "confusion_metrics"
Cohesion: 0.13
Nodes (14): confusion_metrics(), Benchmark: real_world_gov, Comparing across versions, Duration methodology, Expected weakness: read Auto-Validate's numbers honestly, Layout, Methodology: auto_validate, Methodology: raha (+6 more)

### Community 65 - "env"
Cohesion: 0.17
Nodes (12): GITHUB_TOKEN, NEEDS, SONAR_HOST_URL, SONAR_TOKEN, pr-title, pull-requests, if, name (+4 more)

### Community 67 - "CorpusStatsStore"
Cohesion: 0.11
Nodes (3): CorpusStatsStore, TestCorpusStatsStoreBeforeBuild, TestLoadTokenStatsMapCap

### Community 68 - "dry_run"
Cohesion: 0.18
Nodes (11): default, description, type, dry_run, on, workflow_dispatch, workflow_run, inputs (+3 more)

### Community 69 - "Appendix: Validation Function Reference"
Cohesion: 0.28
Nodes (4): Appendix: Validation Function Reference, _check_columns_present(), _check_columns_unique(), TestCheckColumnsUnique

### Community 70 - "FeatureBucket"
Cohesion: 0.09
Nodes (11): Candidate, CorpusColumnRecord, CorpusPairRecord, Detection, FeatureBucket, MetricObservation, TestCandidate, TestCorpusRecords (+3 more)

### Community 71 - "CorpusIngestor"
Cohesion: 0.12
Nodes (5): balanced_union(), CorpusIngestor, TestCorpusIngestorSkipsBadInputs, _write_table(), TestIngestColumnPairsNullAlignment

### Community 72 - "variables"
Cohesion: 0.20
Nodes (10): default, description, default, description, default, description, variables, corpus_catalog (+2 more)

### Community 73 - "KnownIndexLabeler"
Cohesion: 0.23
Nodes (7): Layout, Scoring raha, The corpus (`data/corpus/`), The evaluation targets (`data/eval/targets.json`), KnownIndexLabeler, test_position_argument_takes_precedence(), test_two_argument_call_still_works()

### Community 74 - "PRD: API Validation Framework for open-detect"
Cohesion: 0.12
Nodes (16): 1. Summary, 2. Contacts, 3.1 Context, 3.2 Why Now?, 3.3 Recent Changes, 3. Background, 4.1 Primary Objective, 4.2 Business Benefits (+8 more)

### Community 75 - "dev"
Cohesion: 0.22
Nodes (10): default, mode, workspace, mode, workspace, targets, dev, prod (+2 more)

### Community 76 - "clean_column"
Cohesion: 0.22
Nodes (4): clean_column(), _is_null(), _iter_corpus_columns(), TestCleanColumn

### Community 77 - "Commit conventions and releases"
Cohesion: 0.18
Nodes (11): Adding an algorithm, Commit conventions and releases, Contributing, Everyday commands, First release bootstrap, How a release happens, Knowledge graph automation, Publishing to PyPI (optional, off by default) (+3 more)

### Community 78 - "labeling.py"
Cohesion: 0.11
Nodes (14): Reading the output, Usage, Who answers the labeling questions?, Choosing a budget, Custom labelers (Raha), Labeling with rules you already trust, Reproducibility, The simplest labeler: a function (+6 more)

### Community 79 - "UnknownAlgorithmError"
Cohesion: 0.29
Nodes (6): Concepts, Configuration objects, One contract: `detect()`, The registry, Errors, UnknownAlgorithmError

### Community 81 - "Current Status: BLOCKED"
Cohesion: 0.11
Nodes (17): Blocking Issues (Resolved vs Remaining):, CI Workflow (`.github/workflows/ci.yml`):, Completed Tasks:, Current Status: BLOCKED, CURRENTLY BLOCKING ISSUES:, Dependencies:, Next Steps:, Project Structure: (+9 more)

### Community 82 - "_aggregate_scored_rows"
Cohesion: 0.12
Nodes (8): Changes Verified, Mathematical Equivalence Verified, Review Complete: OPE-194 (PR #106), Summary, Test Results, _aggregate_scored_rows(), TestAggregateScoredRows, TestBuilderWeightOutput

### Community 83 - "UniDetect"
Cohesion: 0.11
Nodes (10): UniDetect, _config(), _mock_detector_result(), _mock_spark(), _mock_spark_context(), TestUniDetectBuildCorpusStatistics, TestUniDetectDetect, TestUniDetectInit (+2 more)

### Community 84 - "numpy"
Cohesion: 0.07
Nodes (14): _factorize_column(), fd_violation_strategies(), gaussian_outlier_strategies(), histogram_outlier_strategies(), _is_float_like(), pattern_character_strategies(), TestEmptyFrames, TestFdRepeatedGroupsAndNulls (+6 more)

### Community 85 - "test"
Cohesion: 0.20
Nodes (10): TMPDIR, test, python-version, fail-fast, matrix, env, name, runs-on (+2 more)

### Community 86 - "hooks"
Cohesion: 0.14
Nodes (13): additional_dependencies, args, entry, files, id, language, language_version, name (+5 more)

### Community 87 - "release.yml"
Cohesion: 0.20
Nodes (9): concurrency, cancel-in-progress, group, jobs, name, permissions, actions, contents (+1 more)

### Community 88 - "release"
Cohesion: 0.20
Nodes (10): GH_TOKEN, release, released, tag, version, env, if, outputs (+2 more)

### Community 89 - "test_raha_strategies.py"
Cohesion: 0.33
Nodes (8): _assert_same(), _naive_fd(), _naive_gaussian(), _naive_histogram(), _naive_pattern(), _naive_str(), _random_column(), TestRandomizedEquivalenceWithNaiveReference

### Community 90 - "featurization.py"
Cohesion: 0.08
Nodes (15): _score_pair(), _score_column(), _score_column(), _score_column(), bucket_by_edges(), bucket_leftness(), bucket_row_count(), bucket_token_length() (+7 more)

### Community 91 - "pypi"
Cohesion: 0.20
Nodes (10): name, url, pypi, id-token, environment, if, name, needs (+2 more)

### Community 92 - "Current Status: BLOCKED"
Cohesion: 0.17
Nodes (11): Current Blockers:, Current Status: BLOCKED, Dependencies:, Emergency Rollback Plan:, Next Steps (Ordered):, OPE-97 Resolution Notes, Resolution Strategy:, Risk Assessment: (+3 more)

### Community 94 - "spark_session.py"
Cohesion: 0.21
Nodes (4): _cap_driver_memory(), _host_memory_bytes(), spark_session(), SparkUnavailable

### Community 95 - "with"
Cohesion: 0.20
Nodes (10): steps, uses, with, enable-cache, fetch-depth, if-no-files-found, name, path (+2 more)

### Community 96 - "on"
Cohesion: 0.25
Nodes (8): on, pull_request, push, schedule, workflow_dispatch, types, branches, cron

### Community 98 - "steps"
Cohesion: 0.25
Nodes (8): FORCE, TESTED_SHA, steps, env, id, if, name, run

### Community 99 - "argparse"
Cohesion: 0.42
Nodes (3): candidates(), main(), select()

### Community 100 - "CallableLabeler"
Cohesion: 0.18
Nodes (9): Auto-Validate: learn patterns from clean columns, Quickstart, Raha: find errors with a few labels, Reading results, Uni-Detect: score tables in Unity Catalog, CallableLabeler, TestCallableLabeler, fn() (+1 more)

### Community 101 - "PatternIndex"
Cohesion: 0.07
Nodes (16): Code Review State, Completed Actions, Current PR State, Documents Updated, Final Fixes Pushed, Next Action, Next Steps, OPE-133 Review Summary (+8 more)

### Community 103 - "open_detect/exceptions.py"
Cohesion: 0.06
Nodes (15): Errors, CorpusNotFoundError, DataQualityError, UnityCatalogError, parse_args(), IndexNotBuiltError, OpenDetectError, TestParseArgs (+7 more)

### Community 104 - "sonarqube"
Cohesion: 0.33
Nodes (6): sonarqube, if, name, needs, runs-on, timeout-minutes

### Community 105 - "profile.py"
Cohesion: 0.22
Nodes (3): ProfileRunSkippedUniDetect, require_uni_detect(), test_require_uni_detect_fails_when_undetected()

### Community 106 - "infer_column_data_type"
Cohesion: 0.07
Nodes (12): token_prevalence(), infer_column_data_type(), is_float_like(), is_integer_like(), is_mixed_alphanumeric(), tokenize(), TestDataTypeInference, TestTokenPrevalence (+4 more)

### Community 107 - "docs"
Cohesion: 0.40
Nodes (5): name, runs-on, steps, timeout-minutes, docs

### Community 108 - "force"
Cohesion: 0.40
Nodes (5): default, description, options, type, force

### Community 110 - "list_tables_matching"
Cohesion: 0.16
Nodes (7): list_tables(), list_tables_matching(), table_exists(), TestListTables, TestListTablesMatching, fake_sql(), TestTableExists

### Community 111 - "docs/index.md"
Cohesion: 0.16
Nodes (9): Getting started, At a glance, Choosing an algorithm, Rules of thumb, open-detect, What is in the box, Registry, Registry and results (+1 more)

### Community 112 - "select_fd_column_pairs"
Cohesion: 0.29
Nodes (3): select_fd_column_pairs(), TestSelectFdColumnPairs, by_name()

### Community 113 - "_date_index"
Cohesion: 0.40
Nodes (3): _date_index(), _date_values(), TestLargeGroups

### Community 115 - "OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate"
Cohesion: 0.20
Nodes (9): Auto-Validate: Per-Distinct-Value Verdict Caching, Bug Fixes, Empty String Handling, Improvements, Migration Notes, OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate, Related Work, Robust Type Handling (+1 more)

### Community 116 - "test_package_init.py"
Cohesion: 0.14
Nodes (7): _console_scripts(), test_all_four_console_scripts_are_declared(), test_console_script_targets_match_pyproject(), test_primary_and_alias_resolve_to_identical_callables(), test_lazy_import_raises_for_unknown_attribute(), test_lazy_import_resolves_open_detect_class(), test_registry_does_not_import_spelling_or_rapidfuzz()

### Community 117 - "`uni_detect`"
Cohesion: 0.40
Nodes (5): By corruption severity, By error type, Evaluation targets, Ranking correctness, `uni_detect`

### Community 118 - "`raha`"
Cohesion: 0.40
Nodes (5): By corruption severity (target-level), By error type (cell-level), By error type (target-level), Evaluation targets, `raha`

### Community 119 - "OPE-86 / PR #96 — Copilot Review Fixes"
Cohesion: 0.40
Nodes (4): Fixes Applied, OPE-86 / PR #96 — Copilot Review Fixes, Resolution, Verification

### Community 120 - "Comparing algorithms"
Cohesion: 0.33
Nodes (6): Combine, Comparing algorithms, Find the cells they agree on, Mixed inputs, Ranking caveat, Run two algorithms on the same table

### Community 121 - "AutoValidateAlgorithm"
Cohesion: 0.09
Nodes (7): Inspecting a pattern, Reading the output, Usage, AutoValidateAlgorithm, segment(), _make_tiny_corpus(), TestAutoValidateDetector

### Community 127 - "Auto-Validate"
Cohesion: 0.13
Nodes (12): Auto-Validate, Configuration, Detector, Drift, Pattern index, Pattern inference, Configuration, Enumerations (+4 more)

### Community 131 - "Uni-Detect"
Cohesion: 0.22
Nodes (9): A fully local example, Configuration, Corpus Statistics Schema (OPE-92), How it works, Install, Operational notes, Reading the detections, Uni-Detect (+1 more)

### Community 134 - "auto_validate/detector.py"
Cohesion: 0.06
Nodes (29): Code Review State, Implementation Status, OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV), PR Status, Test Results, Changes Made, Current State, OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part) (+21 more)

### Community 136 - "drop_nulls"
Cohesion: 0.18
Nodes (4): drop_nulls(), uniqueness_ratio(), TestDropNulls, TestUniquenessRatio

### Community 141 - "CorpusStatsBuilder"
Cohesion: 0.17
Nodes (6): CorpusStatsBuilder, _stats_schema_without_error_type(), TestStatsSchemaWithoutErrorType, _config(), _pairs(), TestCorpusBuilderFailureGate

### Community 144 - "Scoring auto_validate"
Cohesion: 0.50
Nodes (4): Expected weakness: read Auto-Validate's low recall honestly, Scoring auto_validate, The `m` override, Timing

### Community 205 - "_detector"
Cohesion: 0.12
Nodes (5): _config(), _detector(), TestDetectCacheContract, TestReleaseIsIdempotentAndSafe, TestScoredResultReleasesOnExit

### Community 251 - "test_metrics.py"
Cohesion: 0.27
Nodes (4): _brute_force_mpd(), _random_words(), _single_edit(), TestSpellingBlocking

### Community 426 - "get_logger"
Cohesion: 0.08
Nodes (9): get_spark(), configure_logging(), get_logger(), log_duration(), TestGetSparkExtended, TestGetSpark, TestConfigureLogging, TestGetLogger (+1 more)

### Community 433 - "ErrorType"
Cohesion: 0.10
Nodes (9): ColumnDataType, ErrorType, BaseDetector, FunctionalDependencyDetector, NumericOutlierDetector, SpellingDetector, UniquenessDetector, FailureTracker (+1 more)

### Community 458 - "make_evidence_json"
Cohesion: 0.13
Nodes (7): _hash_value(), make_evidence_json(), redact_evidence(), compute(), compute(), compute(), TestRedactEvidence

### Community 530 - "patterns.py"
Cohesion: 0.06
Nodes (19): _char_class(), _class_of_token(), generality_weight(), generalize(), _iter_runs(), Token, tokenize(), _alternatives() (+11 more)

### Community 639 - "perturb_numeric_outlier"
Cohesion: 0.16
Nodes (5): finite_floats(), perturb_numeric_outlier(), TestFiniteFloats, TestPerturbNumericNonFinite, TestPerturbNumericOutlier

### Community 686 - "outliers.py"
Cohesion: 0.16
Nodes (7): mad_scores(), MADResult, max_mad(), MaxMADResult, median_absolute_deviation(), sd_scores(), TestNumericOutliers

### Community 699 - "min_pairwise_edit_distance"
Cohesion: 0.16
Nodes (3): differing_token_lengths(), min_pairwise_edit_distance(), TestSpelling

### Community 783 - "snapshot.py"
Cohesion: 0.22
Nodes (8): _as_json_list(), diff_snapshots(), _list_keys(), load_snapshot(), _lr_equal(), main(), normalize(), save_snapshot()

### Community 835 - "real_world_gov/run_benchmark.py"
Cohesion: 0.10
Nodes (12): maybe_scope(), UniDetectProfile, git_commit(), _build_config(), main(), _print_comparison(), _register_table(), run() (+4 more)

### Community 1156 - "RahaConfig"
Cohesion: 0.07
Nodes (17): main(), ColumnPredictions, _make_classifier(), train_and_predict(), _default_classifier_factory(), RahaConfig, RahaDetector, _features() (+9 more)

### Community 1218 - "wiki_subset/generate_report.py"
Cohesion: 0.19
Nodes (14): grouped_bar_chart(), _nice_ceiling(), _rounded_top_rect(), _algorithm_section(), _by_error_type_section(), _f1_by_error_type_chart(), _fmt_pct(), main() (+6 more)

### Community 1252 - "Performance Baseline — OPE-87"
Cohesion: 0.29
Nodes (6): Earlier timings (no job counts), Environment (wiki_subset measurement), How to use, Performance Baseline — OPE-87, Scope and status, wiki_subset: Uni-Detect jobs / stages per phase

### Community 1267 - "real_world_gov/generate_report.py"
Cohesion: 0.19
Nodes (11): comparison_charts(), comparison_table_markdown(), _algorithm_section(), _by_dataset_chart(), _fmt_pct(), main(), _metrics_table_row(), render_markdown() (+3 more)

### Community 1430 - "conftest.py"
Cohesion: 0.16
Nodes (6): _cap_driver_memory(), _delta_jars(), _download(), _host_memory_bytes(), spark(), uc_location()

### Community 1540 - "Summary"
Cohesion: 0.25
Nodes (7): ✅ Completed Implementation, 📊 Graphify Update, 📋 Next Steps (when GitHub identity is restored), OPE-89 Cache Lifecycle - Implementation Status, ⚠️ Remaining Operational Blockers, Summary, Test Status

## Ambiguous Edges - Review These
- `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` → `README.md — Uni-Detect overview`  [AMBIGUOUS]
  README.md · relation: references

## Knowledge Gaps
- **9 isolated node(s):** `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)`, `uniqueness metric (UR, Section 3.3)`, `perturb_* epsilon-perturbation functions (Definition 2)` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1128 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ValidationError` connect `ValidationError` to `auto_validate/detector.py`, `builder.py`, `AutoValidateConfig`, `_check_expected_type`, `_check_unknown_kwargs`, `InsufficientDataError`, `metrics/functional_dependency.py`, `ErrorType`, `index.py`, `.build_corpus_statistics`, `min_pairwise_edit_distance`, `_ensure_sequence_of_str`, `_score_single_column`, `Appendix: Validation Function Reference`, `PRD: API Validation Framework for open-detect`, `clean_column`, `UniDetect`, `_check_dataframe_is_spark`, `open_detect/exceptions.py`, `_reject_unknown_kwargs`, `OPE-86 / PR #96 — Copilot Review Fixes`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 36 inferred relationships involving `AutoValidateConfig` (e.g. with `run_auto_validate()` and `run_auto_validate()`) actually correct?**
  _`AutoValidateConfig` has 36 INFERRED edges - model-reasoned connections that need verification._
- **What connects `open-detect`, `ErrorType enum (Definition 1)`, `outliers metric (max-MAD, Section 3.1)` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `verify_build_config` be split into smaller, more focused modules?**
  _Cohesion score 0.11904761904761904 - nodes in this community are weakly interconnected._
- **Why does `AutoValidateConfig` connect `AutoValidateConfig` to `real_world_gov/run_benchmark.py`, `PatternIndex`, `auto_validate/detector.py`, `json`, `UnknownAlgorithmError`, `test_algorithms_registry.py`, `InferredPattern`, `_date_index`, `index.py`, `fmdv_v`, `fmdv`, `AutoValidateAlgorithm`, `UnityCatalogLocation`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `ErrorType` (e.g. with `run_uni_detect()` and `run_uni_detect()`) actually correct?**
  _`ErrorType` has 65 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `CI workflow: Benchmark (wiki-subset, workflow_dispatch)` and `README.md — Uni-Detect overview`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._