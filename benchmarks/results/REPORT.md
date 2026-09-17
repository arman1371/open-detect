# WIKI-subset benchmark results

Human-readable view of the checked-in benchmark run. See [benchmarks/README.md](../README.md) for how this benchmark works and how to regenerate this file.

**Generated at:** 2026-09-17T17:55:20+00:00  
**Commit:** `a74765d`  
**Dataset:** wiki_subset

## Overall

| Metric | Value |
|---|---|
| Targets evaluated | 8 |
| Precision | 1.000 |
| Recall | 1.000 |
| F1 | 1.000 |
| Accuracy | 1.000 |

![Overall metrics](charts/overall_metrics.svg)

## By error type

| Error type | n | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|
| **overall** | 8 | 1.000 | 1.000 | 1.000 | 1.000 |
| `uniqueness` | 2 | 1.000 | 1.000 | 1.000 | 1.000 |
| `numeric_outlier` | 2 | 1.000 | 1.000 | 1.000 | 1.000 |
| `spelling` | 2 | 1.000 | 1.000 | 1.000 | 1.000 |
| `functional_dependency` | 2 | 1.000 | 1.000 | 1.000 | 1.000 |

![F1 by error type](charts/f1_by_error_type.svg)

## Ranking correctness

For each error type: is the true-positive (genuine error) target scored as *more surprising* (lower `lr_ratio`) than the false-positive target? This is the paper's central claim.

| Error type | TP lr_ratio | FP lr_ratio | Correctly ranked |
|---|---|---|---|
| `uniqueness` | 0.1000 | 1.0000 | ✅ |
| `numeric_outlier` | 0.1667 | 1.0000 | ✅ |
| `spelling` | 0.1667 | 1.0000 | ✅ |
| `functional_dependency` | 0.0909 | 0.3333 | ✅ |

![Detection ranking](charts/ranking_lr_ratio.svg)

## Evaluation targets

| Target | Error type | Expected | Predicted | lr_ratio | Result | Description |
|---|---|---|---|---|---|---|
| `uniqueness_fp_common_surnames` | `uniqueness` | False | False | 1.0000 | ✅ | A 'List of notable people named Smith' style table: one coincidental duplicate surname among common names. Not a real error. |
| `uniqueness_tp_airport_codes` | `uniqueness` | True | True | 0.1000 | ✅ | An airport-code-style ID column with one injected duplicate -- codes like this are expected to always be unique. |
| `outlier_fp_election_result` | `numeric_outlier` | False | False | 1.0000 | ✅ | Election vote shares: many small candidates plus one legitimately larger winner (paper's own 'C-' false-positive worked example). |
| `outlier_tp_population_typo` | `numeric_outlier` | True | True | 0.1667 | ✅ | Population figures (thousands) with a decimal-point typo ('8.716' instead of '8716') -- paper's own 'C+' true-positive example. |
| `spelling_fp_amendment_list` | `spelling` | False | False | 1.0000 | ✅ | Consecutive amendment numerals: syntactically close by design, not misspellings. |
| `spelling_tp_biography_typo` | `spelling` | True | True | 0.1667 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among unrelated long biography names -- paper's own true-positive example. |
| `fd_fp_pageviews_vs_edits` | `functional_dependency` | False | False | 0.3333 | ✅ | Two independent numeric-ish columns with no real dependency. |
| `fd_tp_country_code_violation` | `functional_dependency` | True | True | 0.0909 | ✅ | ISO code -> country name table (a hard functional dependency on Wikipedia) with one injected violating row. |

---

_Regenerate this file (and the charts above) from a results JSON with:_

```bash
uv run python benchmarks/generate_report.py
```

