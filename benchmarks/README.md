# Benchmarks

This repo ships two independent benchmarks, as sibling directories sharing
common infrastructure (`common/` -- a local Spark-session bootstrap,
confusion-matrix scoring, and SVG/Markdown report rendering) so a third can
reuse the same pieces rather than being copy-pasted:

| Benchmark | What it measures | Data |
|---|---|---|
| **[`wiki_subset`](wiki_subset/README.md)** | Synthetic, programmatically-injected errors at three graded severities, built to mirror the paper's own WIKI corpus. CI-friendly: a couple of minutes, no external network access. | Hand-built, checked in. |
| **[`real_world_gov`](real_world_gov/README.md)** | Real government open-data tables with real, historically-injected errors and independently-produced ground truth. | 5 datasets sampled from [LUH-DBS/Matelda](https://github.com/LUH-DBS/Matelda)'s `DGov_NTR` corpus, checked in. |

```
benchmarks/
  common/              # shared: Spark session bootstrap, confusion-matrix scoring, SVG charts
  wiki_subset/         # benchmark 1: data/, run_benchmark.py, generate_report.py, results/
  real_world_gov/      # benchmark 2: data/, run_benchmark.py, generate_report.py, results/
```

Run either with `make benchmark` / `make benchmark-real-world-gov` (or
`make benchmark-all` for both); see each benchmark's own README for how its
data was built/selected and how to read its results.

Adding a third benchmark means creating a new `benchmarks/<name>/` directory
with the same shape as the two above: its own `data/` (or equivalent
inputs), a `run_benchmark.py` built on `common.spark_session`/
`common.metrics`, a `generate_report.py` built on `common.charts`, a
checked-in `results/baseline.json` + `REPORT.md` + `charts/`, and a README
following `wiki_subset/README.md`'s or `real_world_gov/README.md`'s shape.
