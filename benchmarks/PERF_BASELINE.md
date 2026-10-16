# Performance Baseline — OPE-87

> Generated: 2026-10-16
> Branch: `chore/ope-87-perf-baseline-v2`

## Environment

- **Hardware**: 4 vCPU, ~5 GB RAM (cgroup-limited)
- **Java**: JDK 17.0.20.1+1-jre
- **Python**: 3.12.14 (venv)
- **PySpark**: 3.5.9 + Delta 3.3.3
- **Note**: Spark local mode is significantly slower here than the reference environment; full benchmark runs time out at 300s. Baseline figures below are from prior successful runs on the same codebase.

## Baseline Results (Prior Runs)

### real_world_gov (5 datasets, 47 columns)

| Algorithm | Precision | Recall | F1 | Accuracy | Duration (s) |
|---|---|---|---|---|---|
| raha | 1.000 | 1.000 | 1.000 | 1.000 | 5.68 |
| auto_validate | 1.000 | 0.265 | 0.419 | 0.468 | 153.33 |
| uni_detect | 0.800 | 0.824 | 0.812 | 0.723 | 484.07 |

Source: `benchmarks/real_world_gov/results/baseline.json` (commit `5976e33`, 2026-10-06)

### wiki_subset (60 tables)

| Algorithm | Precision | Recall | F1 | Accuracy | Duration (s) |
|---|---|---|---|---|---|
| raha | 1.000 | 0.825 | 0.904 | 0.883 | 4.58 |
| uni_detect | 0.838 | 0.775 | 0.805 | 0.750 | 1013.24 |
| auto_validate | 1.000 | 0.275 | 0.431 | 0.517 | 75.24 |

Source: `benchmarks/wiki_subset/results/baseline.json` (commit `84b5982`, 2026-10-05)

## Key Observations

1. **Raha** is fast (<6s) but only evaluates on gov data where ground-truth labels exist.
2. **Uni-Detect** dominates runtime (484–1013s) due to per-column Spark ingestion + mapInPandas scoring.
3. **Auto-Validate** is moderate speed (75–153s) but has low recall (~27%) — it misses many errors.
4. The Spark job-count helper (`benchmarks/common/spark_jobs.py`) and snapshot diff tool (`benchmarks/common/snapshot.py`) are ready for future runs.

## How to Re-run

```bash
export JAVA_HOME=/path/to/jdk-17
export PYSPARK_PYTHON=$(which python)
export PYSPARK_DRIVER_PYTHON=$(which python)
export PYTHONPATH=src

# Gov benchmark
python benchmarks/real_world_gov/run_benchmark.py --profile-dir benchmarks/real_world_gov/results/profile/latest

# Wiki benchmark
python benchmarks/wiki_subset/run_benchmark.py --profile-dir benchmarks/wiki_subset/results/profile/latest

# Diff against baseline
python benchmarks/common/snapshot.py diff benchmarks/real_world_gov/results/profile/baseline benchmarks/real_world_gov/results/profile/latest
```

## Bug Fixes Applied in This Branch

1. **Raha detector**: Removed `_ensure_dataframe_is_spark()` call — Raha accepts `pd.DataFrame`, not Spark DataFrames. The OPE-77 validation hardening incorrectly added this check.
2. **validation.py**: Fixed `_check_unknown_kwargs()` signature to accept optional `param_name` argument (auto_validate calls it with 3 args).
3. **auto_validate hierarchy**: Fixed `_value_matches()` to handle nested list patterns returned by `fmdv_vh` (multi-segment columns produce `list[list[str]]` instead of `list[str]`).
