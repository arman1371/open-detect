# Benchmarks

The repository tracks detection quality with two benchmarks that run **every registered
algorithm** against the same targets and report precision, recall, F1, accuracy and wall-clock time.

| Benchmark | Data |
|---|---|
| [`wiki_subset`](https://github.com/arman1371/open-detect/tree/main/benchmarks/wiki_subset) | 60 hand-built targets with injected errors at graded severity (`subtle`, `moderate`, `obvious`), plus clean false-positive shapes. Modeled on the Uni-Detect paper's WIKI corpus. |
| [`real_world_gov`](https://github.com/arman1371/open-detect/tree/main/benchmarks/real_world_gov) | Five real government open-data tables with real errors and independent ground truth, from [Matelda](https://github.com/LUH-DBS/Matelda). |

## Latest results

F1 per algorithm, from the checked-in reports.

| Algorithm | `wiki_subset` F1 | `real_world_gov` F1 | Notes |
|---|---|---|---|
| `raha` | 0.904 | 1.000 | Fastest by far (seconds). Used a ground-truth labeler with 20 labels. |
| `uni_detect` | 0.805 | 0.812 | Lower precision on functional dependencies. Slowest, since it builds a corpus. |
| `auto_validate` | 0.431 | 0.419 | Precision 1.000, recall about 0.27. |

Full tables, per-error-type and per-severity breakdowns, and charts are in
[`wiki_subset/results/REPORT.md`](https://github.com/arman1371/open-detect/blob/main/benchmarks/wiki_subset/results/REPORT.md)
and
[`real_world_gov/results/REPORT.md`](https://github.com/arman1371/open-detect/blob/main/benchmarks/real_world_gov/results/REPORT.md).

## How to read them

- **Raha's numbers assume a good labeler.** The benchmarks answer its labeling questions from the
  known-clean data. With a human it should be close; with the default `HeuristicLabeler` expect
  less.
- **Auto-Validate is a format method.** It catches values that break a column's pattern and cannot
  catch well-formatted-but-wrong values such as a numeric outlier or an FD violation. Low recall
  there is expected, not a misconfiguration.
- **Functional dependencies are hard.** The Uni-Detect paper reports the same: precision there is
  the weakest of its four error types.
- **Durations are not like-for-like.** Uni-Detect's includes building corpus statistics with a
  local Spark session.
- **Small datasets.** Treat results as a comparison of relative strengths, not absolute accuracy
  on your data.

## Running them

```bash
make benchmark                  # wiki_subset
make benchmark-real-world-gov   # real_world_gov
make benchmark-all
```

Uni-Detect's half needs a local Spark/Delta session on **JDK 17**; see
[Installation](getting-started/installation.md). Each benchmark compares against a checked-in
baseline so a change's effect on quality shows up before it merges.
