# Auto-Validate

**Unsupervised pattern validation for a single table.** Song & He, SIGMOD 2021.

Auto-Validate answers: "given what clean columns look like in my data lake, what pattern should
this column follow, and which cells break it?" It suits columns with a machine-generated shape:
dates, IDs, emails, phone numbers, codes.

## How it works

1. **Offline: build an index.** `build_index(corpus)` generalizes each value of each clean corpus
   column into candidate patterns (`<digit>+`, `<alphanum>+<symbol>+<alphanum>+`, ...) and
   records, for each pattern, its estimated false-positive rate (`FPR_T`) and coverage (`Cov_T`).
2. **Online: infer a pattern.** For each column of your table, pick the pattern that is
   specific enough to catch errors yet has an FPR at most `r` and coverage at least `m`.
3. **Flag mismatches.** Every non-null cell that does not match its column's pattern is an error.

## Install

```bash
pip install "open-detect[auto_validate]"
```

## Usage

```python
import pandas as pd
from open_detect.algorithms.auto_validate import AutoValidateAlgorithm, AutoValidateConfig

corpus = [
    pd.Series(["2024-01-15", "2024-02-20", "2024-03-10"]),
    pd.Series(["john@example.com", "jane@test.org", "admin@site.net"]),
    pd.Series(["New York", "London", "Tokyo"]),
]

detector = AutoValidateAlgorithm(AutoValidateConfig(m=1, tau=16))
detector.build_index(corpus)

dirty = pd.DataFrame(
    {"email": ["john@example.com", "invalid-email", "admin@site.net", "user@test.com"]}
)
result = detector.detect(dirty, table_id="contacts")
print([c.row_index for c in result.errors()])   # [1]
```

`corpus` is any iterable of `pandas.Series`, `pandas.DataFrame` (each column becomes a corpus
column), or plain sequences of values. It should be **clean**; the algorithm assumes the corpus
patterns are right.

!!! important "Build the index before detecting"
    Calling `detect()` or `infer_pattern()` first raises
    [`IndexNotBuiltError`](../reference/exceptions.md). The index is held in memory on the
    detector instance (`detector.index`).

### Inspecting a pattern

```python
inferred = detector.infer_pattern(dirty["email"])
inferred.pattern   # the validation pattern (a string, or a list for vertical-cut variants)
inferred.fpr_t     # estimated false-positive rate against the corpus
inferred.cov_t     # how many corpus columns the pattern covers
```

`infer_pattern` returns `None` when no pattern satisfies the thresholds. In `detect()` such a
column produces no errors, and its cells carry `evidence["reason"] == "no_feasible_pattern"`.

### Reading the output

`score` is `1 - FPR_T` for flagged cells and `0.0` for all others. `evidence` carries the
`pattern`, `fpr_t`, `cov_t`, `theta_c`, and the `variant`, `r`, `m`, `tau` used. Null and empty
cells are skipped entirely.

## Variants

| `variant` | What it adds |
|---|---|
| `fmdv` | The basic problem: one pattern per column |
| `fmdv_v` | **Vertical cuts**: split values into token segments and validate each segment |
| `fmdv_h` | **Horizontal cuts**: tolerate up to a fraction `theta` of non-conforming values |
| `fmdv_vh` | Both. The paper's best performer and the default. |

## Configuration

| Setting | Default | Notes |
|---|---|---|
| `variant` | `"fmdv_vh"` | See above |
| `r` | `0.05` | Maximum FPR for a pattern. The paper reports insensitivity for `r >= 0.02`. |
| `m` | `100` | Minimum corpus coverage. **Calibrated to a 7.2M-column corpus; lower it for small corpora.** |
| `tau` | `8` | Token limit: caps indexed value length and vertical-segment width |
| `theta` | `0.1` | Horizontal-cut tolerance. The paper gives no default; `0.1` is this library's choice. |
| `drift_significance` | `0.01` | Significance level for the drift test |

!!! tip "Match `m` to your corpus"
    If `detect()` flags nothing and `infer_pattern` returns `None`, `m` is usually too high for
    the size of your corpus. The Quickstart uses `m=1` for a three-column toy corpus.

## Drift checking

The paper's drift test is available as a helper. It compares a training column with a later
column and reports whether the share of values breaking the pattern has shifted significantly. It is **not** part of `detect()`,
since a single-table scan has no "future" column to compare against.

```python
from open_detect.algorithms.auto_validate import check_drift

inferred = detector.infer_pattern(train_df["col_a"])
drift = check_drift(train_df["col_a"], future_df["col_a"], inferred)
drift.drifted      # True if the share of non-conforming values changed significantly
drift.p_value      # two-tailed Fisher's exact test
```

## Using the parts directly

```python
from open_detect.algorithms.auto_validate import (
    AutoValidateConfig, build_pattern_index, fmdv_vh, patterns_of, matches, tokenize
)

config = AutoValidateConfig(m=1)
index = build_pattern_index(corpus, config)
pattern = fmdv_vh(dirty["email"], index, config)
```
