# Performance Baseline — OPE-87

Reference for Uni-Detect Spark-performance work (OPE-63): timings, Spark job/stage
counts per phase, and a detections snapshot that later changes must reproduce.

## Scope and status

| Benchmark | Snapshot | Job counts | Status |
|---|---|---|---|
| `wiki_subset` | `benchmarks/wiki_subset/results/profile/baseline/detections.csv` | `perf.json` + table below | measured |
| `real_world_gov` | not committed | not measured | **pending** — needs a host with >= 8 GB free RAM (the runner requests `driver_memory=8g`); the driver JVM was OOM-killed on the 5 GB host used here |

The Java-free tooling is unchanged for gov: once a larger host is available run
`make benchmark-profile PROFILE_NAME=baseline`, commit
`benchmarks/real_world_gov/results/profile/baseline/`, and fill in the gov table.

## Environment (wiki_subset measurement)

- Hardware: 4 vCPU, ~5 GB RAM (cgroup-limited), Linux 6.8
- Java: JDK 17.0.20.1+1 (JRE); Python 3.12.14; PySpark 3.5.9 + Delta 3.3.3
- Spark: `local[2]`, `spark.driver.memory=3g`, `spark.sql.shuffle.partitions=2`
- Code measured: Uni-Detect from `main` as of capture (this PR changes only `benchmarks/`, `tests/benchmarks/`, `Makefile`; no `src/` changes). Captured at `2dfbbe73` on the earlier `chore/ope-87-perf-baseline-v2` branch, whose `src/` matched `main`.

## wiki_subset: Uni-Detect jobs / stages per phase

Each phase is one `build_corpus_statistics` or `detect()` call for a single error type
(`benchmarks/common/spark_jobs.py` counts jobs and stages submitted inside the phase).

| Phase | Spark jobs | Stages | Wall (s) |
|---|---|---|---|
| `build_corpus_statistics[uniqueness]` | 292 | 960 | 114.3 |
| `build_corpus_statistics[numeric_outlier]` | 515 | 1529 | 185.0 |
| `build_corpus_statistics[spelling]` | 347 | 1025 | 126.9 |
| `build_corpus_statistics[functional_dependency]` | 800 | 2530 | 233.3 |
| `detect[uniqueness]` | 151 | 397 | 58.4 |
| `detect[numeric_outlier]` | 149 | 382 | 53.7 |
| `detect[spelling]` | 148 | 378 | 48.7 |
| `detect[functional_dependency]` | 181 | 535 | 58.3 |

Total `detect()` jobs across the four error types: 629. Whole Uni-Detect run
including profiling overhead: 1048 s.
Detections snapshot: 71 rows.

## Earlier timings (no job counts)

From the committed `baseline.json` files (older commits, shown for context only; wall time on this
host differs from the reference machine):

| Benchmark | Algorithm | Duration (s) | Commit |
|---|---|---|---|
| real_world_gov | raha | 5.68 | `5976e33` |
| real_world_gov | auto_validate | 153.33 | `5976e33` |
| real_world_gov | uni_detect | 484.07 | `5976e33` |
| wiki_subset | raha | 4.58 | `84b5982` |
| wiki_subset | auto_validate | 75.24 | `84b5982` |
| wiki_subset | uni_detect | 1013.24 | `84b5982` |

## How to use

```bash
export JAVA_HOME=/path/to/jdk-17
make benchmark-profile                 # writes benchmarks/*/results/profile/latest
make benchmark-diff                    # diff latest vs baseline; exits non-zero on any difference
make benchmark-profile PROFILE_NAME=baseline   # regenerate the baseline (deliberate only)
```

`benchmark-diff` compares exact on `error_type`/`table_id`/`candidate_id`/`column_names`/`row_ids`/
`is_significant`, 1e-9 tolerance on `lr_ratio`, order-insensitive. Datasets without a baseline or latest
snapshot are skipped, but it fails if no dataset could be compared.
Profiling is opt-in (`--profile-dir`); without it benchmarks run exactly as before. For `real_world_gov`
the reported `duration_seconds` excludes the extra per-error-type `detect()` profiling pass; `perf.json`
records the total including it.
