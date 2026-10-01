# Benchmarks

This repo ships two independent benchmarks, as sibling directories sharing
common infrastructure (`common/` -- a local Spark-session bootstrap,
confusion-matrix scoring, cross-algorithm comparison rendering, and
SVG/Markdown report rendering) so a third can reuse the same pieces rather
than being copy-pasted:

| Benchmark | What it measures | Data |
|---|---|---|
| **[`wiki_subset`](wiki_subset/README.md)** | Synthetic, programmatically-injected errors at three graded severities, built to mirror the paper's own WIKI corpus. CI-friendly: a couple of minutes, no external network access. | Hand-built, checked in. |
| **[`real_world_gov`](real_world_gov/README.md)** | Real government open-data tables with real, historically-injected errors and independently-produced ground truth. | 5 datasets sampled from [LUH-DBS/Matelda](https://github.com/LUH-DBS/Matelda)'s `DGov_NTR` corpus, checked in. |

Both benchmarks score **every registered algorithm** (see
[`unidetect.algorithms`](../ARCHITECTURE.md) -- `uni_detect`, `raha` and
`auto_validate` today) against the same targets and render a side-by-side
comparison table -- precision/recall/F1/accuracy *and* wall-clock duration --
rather than one algorithm's numbers reported in isolation. See each
benchmark's `results/REPORT.md` for the current comparison.

## The three algorithms, and what they each bring

| Algorithm | Operating model | Extra deps |
|---|---|---|
| `uni_detect` | Per-column/pair "how surprising is this relative to corpus `T`", via a likelihood ratio. Offline corpus-statistics build + online scoring. | Spark + Delta (**JDK 17**) |
| `raha` | Per-cell classification from sampled human labels, one classifier per column. No corpus phase. | `scikit-learn`, `scipy` |
| `auto_validate` | Per-cell "does this value match the validation pattern inferred from corpus `T`" (Song & He, SIGMOD 2021). Offline pattern-index build + online pattern inference + cell matching. | `pandas` only |

Two notes on how the comparison should be read:

- **`auto_validate` is a string-format-pattern method.** It infers a pattern
  per *column* (character-class/token-level: `<alphanum>{11}`, `Amendment
  <alphanum>+`, ...) and flags cells that don't match. That makes it a good
  fit for format/shape errors and a poor fit for errors that are perfectly
  well-formatted but wrong: a numeric outlier (`8716` → `8.716`) still matches
  `<num>+`, and a functional-dependency violation (`USA` → `Nonexistent
  Country`) is still a perfectly ordinary `<letter>+ <letter>+` value. Low
  recall on `numeric_outlier` / `functional_dependency` in both benchmarks'
  reports is therefore the *expected* result, not a misconfiguration -- it is
  reported as-is and no hyperparameter was tuned to compensate.
- **Each benchmark overrides Auto-Validate's `m`.** The library default `m=100`
  is the paper's, calibrated for a 7.2M-column web-scale corpus. These
  benchmarks' corpora are 39-104 columns (`wiki_subset`) and 47 columns
  (`real_world_gov`), where `m=100` would make every single pattern
  infeasible. Each benchmark therefore overrides `m` as a documented fraction
  of *its own* corpus size, decided from corpus size alone before looking at
  any result -- see each benchmark's README for the exact value and
  reasoning. No other hyperparameter (`r`, `tau`, `theta`, `variant`) is
  overridden; those keep their paper/library defaults.
- **Timing is not apples-to-apples across all three.** `uni_detect` and
  `auto_validate` both have a corpus-build phase folded into
  `duration_seconds`; `raha` has none. Each benchmark's README documents
  exactly what its own `duration_seconds` covers.

```
benchmarks/
  common/              # shared: Spark session bootstrap, confusion-matrix scoring,
                        # cross-algorithm comparison table/charts, SVG charts
  wiki_subset/         # benchmark 1: data/, run_benchmark.py, generate_report.py, results/
  real_world_gov/      # benchmark 2: data/, run_benchmark.py, generate_report.py, results/
```

Run either with `make benchmark` / `make benchmark-real-world-gov` (or
`make benchmark-all` for both); see each benchmark's own README for how its
data was built/selected and how to read its results.

Adding a third benchmark means creating a new `benchmarks/<name>/` directory
with the same shape as the two above: its own `data/` (or equivalent
inputs), a `run_benchmark.py` built on `common.spark_session`/
`common.metrics` that runs each available algorithm independently (skipping
one gracefully -- with a printed message -- if its dependencies aren't
installed) and writes a results JSON with an `"algorithms": {name: {targets,
metrics, duration_seconds, duration_note}}` map, a `generate_report.py`
built on `common.charts`/`common.comparison`, a checked-in
`results/baseline.json` + `REPORT.md` + `charts/`, and a README following
`wiki_subset/README.md`'s or `real_world_gov/README.md`'s shape. Adding a
*fourth algorithm* to either existing benchmark needs no new benchmark at
all -- just a new `run_<algorithm>(...)` function in that benchmark's
`run_benchmark.py` producing the same per-algorithm shape.
