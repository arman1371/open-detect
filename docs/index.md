---
title: open-detect
hide:
  - navigation
---

# open-detect

**Pluggable, paper-backed error detection for tabular data.**

`open-detect` implements published error-detection research behind one small, uniform API.
Pick an algorithm by name, run it on your data, and get back results in a common schema
you can rank, compare, and union across algorithms.

[Get started](getting-started/quickstart.md){ .md-button .md-button--primary }
[Choose an algorithm](guides/choosing-an-algorithm.md){ .md-button }

```python
import pandas as pd
from open_detect.algorithms import get_algorithm

dirty = pd.DataFrame({"city": ["Paris", "London", "MISSING", "123"]})

raha = get_algorithm("raha")
result = raha.detect(dirty, table_id="cities")
result.errors()          # every cell the algorithm calls dirty
result.to_pandas()       # the same, as a DataFrame in the shared schema
```

## What is in the box

<div class="grid cards" markdown>

-   **Raha**

    Semi-supervised, single table, pandas-native. You label a handful of cells (20 by default);
    Raha learns the rest.

    [:octicons-arrow-right-24: Raha guide](algorithms/raha.md)

-   **Auto-Validate**

    Learns a pattern per column from a corpus of clean columns, then flags cells that break it.
    Pandas-native, unsupervised.

    [:octicons-arrow-right-24: Auto-Validate guide](algorithms/auto-validate.md)

-   **Uni-Detect**

    Corpus-driven statistical tests for duplicates, outliers, misspellings and broken functional
    dependencies. Runs on Spark and Unity Catalog.

    [:octicons-arrow-right-24: Uni-Detect guide](algorithms/uni-detect.md)

-   **Your own algorithm**

    Implement one method, register it by name or through a Python entry point.

    [:octicons-arrow-right-24: Extend the library](guides/writing-an-algorithm.md)

</div>

## Why a common interface

| | Raha | Auto-Validate | Uni-Detect |
|---|---|---|---|
| Paper | Mahdavi et al., SIGMOD 2019 | Song & He, SIGMOD 2021 | Wang & He, SIGMOD 2019 |
| Registry name | `raha` | `auto_validate` | `uni_detect` |
| Needs labels | Yes, a few | No | No |
| Needs a clean corpus | No | Yes (columns) | Yes (tables in Unity Catalog) |
| Input to `detect()` | `pandas.DataFrame` | `pandas.DataFrame` | list of table names |
| Runtime | pandas, scikit-learn | pandas | Spark + Delta |

The papers have almost nothing in common methodologically, so `open-detect` does not pretend their
inputs are the same. It unifies the **output**: every algorithm returns an
[`AlgorithmResult`](reference/algorithms.md) made of per-cell
[`CellResult`](reference/algorithms.md) records, so results are directly comparable.
