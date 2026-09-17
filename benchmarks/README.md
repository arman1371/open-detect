# Benchmark: WIKI subset

Uni-Detect's own paper evaluates against four corpora (Section 4.1), one of
which is **WIKI**:

> WIKI. WIKI a subset of WEB from the wikipedia.org domain with over 3M
> tables. As one would expect, WIKI is of high quality since these pages are
> collaboratively edited by millions of editors.
>
> — Wang & He, *Uni-Detect: A Unified Approach to Automated Error Detection
> in Tables*, SIGMOD 2019

This directory is a small, deterministic, CI-friendly benchmark inspired by
that corpus: it does **not** ship or crawl anything close to 3M tables (that
would be impractical to store in a git repo or run on every push). Instead
it captures the same *shapes* Wikipedia's list-article and infobox tables
take -- unique ID/code columns, key → label mappings, population/vote-share
figures, person/place-name columns -- built from real, well-known reference
facts (ISO 3166 country codes and names, common English surnames, ...)
rather than arbitrary synthetic strings, kept intentionally tiny so it runs
in a couple of minutes on a GitHub-hosted runner with no external network
access at benchmark-run time.

## Layout

```
benchmarks/
  generate_dataset.py   # regenerates data/wiki_subset/ deterministically (stdlib only)
  data/wiki_subset/
    corpus/<error_type>/*.csv   # background "T": ~140 small Wikipedia-shaped tables
    eval/targets.json           # 8 labeled evaluation targets + ground truth
  run_benchmark.py       # builds corpus stats, runs detection, scores vs. ground truth
  generate_report.py     # renders a results JSON as REPORT.md + SVG charts (stdlib only)
  results/
    baseline.json         # checked-in reference run, updated deliberately (see below)
    latest.json            # produced by the most recent run (gitignored)
    REPORT.md              # human-readable rendering of baseline.json, checked in
    charts/*.svg           # charts embedded in REPORT.md, checked in
```

### The corpus (`data/wiki_subset/corpus/`)

One error type per subdirectory, following the same
"boring-baseline-category-per-error-type" pattern
`tests/test_corpus_and_detectors.py` uses to validate against the paper's
own worked examples, scaled up with real-world content:

| Error type | Table shape | Example |
|---|---|---|
| `uniqueness` | common surnames (natural duplicates expected) vs. ID-style codes (should always be unique) | "notable people" lists vs. ISO/IATA code lists |
| `numeric_outlier` | small vote-share clusters vs. clustered population-scale figures | election results vs. population-by-region tables |
| `spelling` | short syntactically-close suffixes (not misspellings) vs. long distinct names | amendment numbering vs. biography name lists |
| `functional_dependency` | unrelated numeric pairs vs. a near-perfect key → label mapping | page views vs. edits, vs. ISO code → country name |

### The evaluation targets (`data/wiki_subset/eval/targets.json`)

Eight labeled tables, two per error type: one **true positive** (a genuine,
deliberately injected error -- a duplicated airport code, a decimal-point
population typo, a misspelled name, a broken country-code mapping) and one
**false positive** (superficially anomalous but not actually an error, e.g.
a coincidental duplicate surname or a legitimately large election winner).
Several of these are the paper's own worked examples (Figures 2 and 4).
Each target records `expected_significant: true/false` as ground truth.

Regenerate this data (after editing `generate_dataset.py`) with:

```bash
uv run python benchmarks/generate_dataset.py
```

## Running the benchmark

```bash
make benchmark
# or directly:
uv run python benchmarks/run_benchmark.py
```

This starts a local, Delta-enabled Spark session (same setup as
`tests/conftest.py`), loads the WIKI-subset corpus and eval tables, builds
corpus statistics per error type, runs `UniDetect.detect(...)` against every
eval target, and scores the results against `expected_significant`:

- **Precision / recall / F1 / accuracy**, overall and per error type, over
  the eval targets' predicted-vs-expected `is_significant` label.
- **Ranking correctness** per error type: is the true-positive target scored
  as *more* surprising (lower `lr_ratio`) than the false-positive target? --
  the paper's central claim, and the thing the existing unit tests already
  assert one pair at a time.

Results are written to `benchmarks/results/latest.json`, and if
`benchmarks/results/baseline.json` exists, a version-over-version comparison
table is printed (and, in CI, appended to the job summary).

## Reading the results without JSON

Raw JSON isn't a great way to eyeball how detection is doing.
[`benchmarks/results/REPORT.md`](results/REPORT.md) is a checked-in,
human-readable rendering of `baseline.json` -- overall/per-error-type
precision/recall/F1/accuracy tables, the ranking-correctness table, the full
target list, and the charts below, generated straight from the same JSON (no
plotting library, just stdlib SVG generation):

| ![Overall metrics](results/charts/overall_metrics.svg) | ![F1 by error type](results/charts/f1_by_error_type.svg) |
|---|---|

![Detection ranking](results/charts/ranking_lr_ratio.svg)

`REPORT.md` and `results/charts/` are regenerated automatically whenever the
baseline is refreshed (`--update-baseline`, see below). To regenerate them
by hand from any results JSON (e.g. to preview `latest.json` locally without
touching the checked-in baseline report):

```bash
uv run python benchmarks/generate_report.py --input benchmarks/results/latest.json --output-dir /tmp/preview
# or, to (re)write the checked-in baseline report:
uv run python benchmarks/generate_report.py
```

**Requires JDK 17** locally for the same reason the main test suite does --
see the "JDK version" note in the top-level `README.md`. On a JDK 21+
machine the Spark/Delta session either fails to start or fails partway
through with an Arrow/JDK incompatibility; GitHub Actions runs this under
JDK 17 (see `.github/workflows/benchmark.yml`).

## Comparing across versions

`benchmarks/results/baseline.json` is a checked-in snapshot of a benchmark
run, meant to answer "did this change make detection better or worse?" It
is **not** auto-updated by CI -- a run producing worse numbers than the
baseline should not silently overwrite the reference point. Every push and
pull request runs the benchmark and prints/uploads a comparison against the
current baseline (as a workflow artifact and in the job summary), but the
build does not fail on a regression; use the comparison table to decide
whether a change is worth landing.

When a change is deliberately meant to improve (or is accepted to trade off)
detection quality, refresh the baseline as part of that PR:

```bash
uv run python benchmarks/run_benchmark.py --update-baseline
git add benchmarks/results/baseline.json benchmarks/results/REPORT.md benchmarks/results/charts
```

(`--update-baseline` regenerates `REPORT.md` and `results/charts/` from the
new baseline automatically -- just remember to stage them too.)

## Why not download the real WIKI corpus in CI?

A few reasons this benchmark uses a small, hand-curated, checked-in dataset
instead of fetching real Wikipedia tables at benchmark-run time:

- **Determinism.** A checked-in dataset gives every run (and every
  version-over-version comparison) the exact same input; live scraping does
  not, and Wikipedia's table markup changes over time.
- **CI network policy.** GitHub-hosted runners can reach the internet, but
  depending on a live, uncached fetch from an external site on every push is
  fragile (rate limits, transient failures, markup changes breaking table
  extraction) for a check that's meant to run on every commit.
- **Size.** The paper's WIKI corpus is 3M+ tables; this benchmark exists to
  catch regressions quickly, not to reproduce the paper's absolute numbers,
  so a corpus sized in the tens of tables per error type (mirroring the
  scale the existing unit-test corpus already uses successfully) is enough
  signal at a fraction of the runtime and storage cost.

If you want to run this benchmark against a larger, real Wikipedia-table
sample, `unidetect.pipeline.UniDetect` takes any list of Unity-Catalog-style
table names -- point `benchmarks/run_benchmark.py`'s corpus/eval loading at
your own ingested tables instead.
