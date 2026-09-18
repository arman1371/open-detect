# WIKI-subset benchmark results

Human-readable view of the checked-in benchmark run. See [benchmarks/README.md](../README.md) for how this benchmark works and how to regenerate this file.

**Generated at:** 2026-09-17T23:44:36.797081+00:00  
**Commit:** `f99a32d`  
**Dataset:** wiki_subset

## Overall

| Metric | Value |
|---|---|
| Targets evaluated | 60 |
| Precision | 0.795 |
| Recall | 0.775 |
| F1 | 0.785 |
| Accuracy | 0.717 |

![Overall metrics](charts/overall_metrics.svg)

## By error type

| Error type | n | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|
| **overall** | 60 | 0.795 | 0.775 | 0.785 | 0.717 |
| `uniqueness` | 15 | 0.778 | 0.700 | 0.737 | 0.667 |
| `numeric_outlier` | 15 | 0.833 | 1.000 | 0.909 | 0.867 |
| `spelling` | 15 | 1.000 | 0.700 | 0.824 | 0.800 |
| `functional_dependency` | 15 | 0.636 | 0.700 | 0.667 | 0.533 |

![F1 by error type](charts/f1_by_error_type.svg)

## By corruption severity

How detection holds up as injected errors get harder to spot. `paper_example` are the paper's own canonical worked examples (a mix of true- and false-positive shapes); `obvious`/`moderate`/`subtle` are true-positive targets with graded, programmatically-injected corruption; `clean` are false-positive shapes with no injected error at all. Precision/recall are not shown here because most of these tiers are single-class by construction (see [benchmarks/README.md](../README.md)) -- accuracy is the one metric that is meaningful across all of them.

| Severity | n | TP | FP | FN | TN | Accuracy |
|---|---|---|---|---|---|---|
| `paper_example` | 8 | 4 | 1 | 0 | 3 | 0.875 |
| `obvious` | 12 | 6 | 0 | 6 | 0 | 0.500 |
| `moderate` | 12 | 12 | 0 | 0 | 0 | 1.000 |
| `subtle` | 12 | 9 | 0 | 3 | 0 | 0.750 |
| `clean` | 16 | 0 | 7 | 0 | 9 | 0.562 |

![Accuracy by corruption severity](charts/severity_accuracy.svg)

## Ranking correctness

For each error type: is the true-positive (genuine error) target scored as *more surprising* (lower `lr_ratio`) than the false-positive target? This is the paper's central claim.

| Error type | TP lr_ratio | FP lr_ratio | Correctly ranked |
|---|---|---|---|
| `uniqueness` | 0.1667 | 1.0000 | ✅ |
| `numeric_outlier` | 0.1667 | 0.8333 | ✅ |
| `spelling` | 0.1053 | 1.0000 | ✅ |
| `functional_dependency` | 0.0588 | 0.1000 | ✅ |

![Detection ranking](charts/ranking_lr_ratio.svg)

## Evaluation targets

| Target | Error type | Severity | Expected | Predicted | lr_ratio | Result | Description |
|---|---|---|---|---|---|---|---|
| `uniqueness_fp_common_surnames` | `uniqueness` | `paper_example` | False | False | 1.0000 | ✅ | Paper Figure 2(a)-style: a 'List of notable people named Smith' table with one coincidental duplicate surname among common names. |
| `uniqueness_fp_surname_pool4_00` | `uniqueness` | `clean` | False | False | 1.0000 | ✅ | A 'notable people' list drawn from only 4 common surnames -- natural collisions expected, not a data error. |
| `uniqueness_fp_surname_pool6_01` | `uniqueness` | `clean` | False | False | 1.0000 | ✅ | A 'notable people' list drawn from only 6 common surnames -- natural collisions expected, not a data error. |
| `uniqueness_fp_surname_pool8_02` | `uniqueness` | `clean` | False | True | 0.1111 | ❌ | A 'notable people' list drawn from only 8 common surnames -- natural collisions expected, not a data error. |
| `uniqueness_fp_surname_pool10_03` | `uniqueness` | `clean` | False | True | 0.2000 | ❌ | A 'notable people' list drawn from only 10 common surnames -- natural collisions expected, not a data error. |
| `uniqueness_tp_part_number_paper_example` | `uniqueness` | `paper_example` | True | True | 0.1667 | ✅ | Paper Figure 6-style: a 'Part No.' column with one exact duplicate alphanumeric code -- codes like this are expected to always be unique. |
| `uniqueness_tp_subtle_00` | `uniqueness` | `subtle` | True | True | 0.0833 | ✅ | An airport/ISO-code-style ID column (subtle corruption: 1 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_subtle_01` | `uniqueness` | `subtle` | True | True | 0.0833 | ✅ | An airport/ISO-code-style ID column (subtle corruption: 1 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_subtle_02` | `uniqueness` | `subtle` | True | True | 0.0833 | ✅ | An airport/ISO-code-style ID column (subtle corruption: 1 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_moderate_00` | `uniqueness` | `moderate` | True | True | 0.0833 | ✅ | An airport/ISO-code-style ID column (moderate corruption: 4 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_moderate_01` | `uniqueness` | `moderate` | True | True | 0.0833 | ✅ | An airport/ISO-code-style ID column (moderate corruption: 4 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_moderate_02` | `uniqueness` | `moderate` | True | True | 0.0833 | ✅ | An airport/ISO-code-style ID column (moderate corruption: 4 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_obvious_00` | `uniqueness` | `obvious` | True | False | 1.0000 | ❌ | An airport/ISO-code-style ID column (obvious corruption: 10 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_obvious_01` | `uniqueness` | `obvious` | True | False | 1.0000 | ❌ | An airport/ISO-code-style ID column (obvious corruption: 10 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `uniqueness_tp_obvious_02` | `uniqueness` | `obvious` | True | False | 1.0000 | ❌ | An airport/ISO-code-style ID column (obvious corruption: 10 injected duplicate(s)) -- codes like this are expected to always be unique. |
| `outlier_fp_election_result` | `numeric_outlier` | `paper_example` | False | False | 0.8333 | ✅ | Election vote shares: many small candidates plus one legitimately larger winner (paper's own 'C-' false-positive worked example). |
| `outlier_fp_election_margin18_00` | `numeric_outlier` | `clean` | False | False | 0.2500 | ✅ | Election vote shares with a legitimate ~18% winner among many small candidates -- not a data error. |
| `outlier_fp_election_margin28_01` | `numeric_outlier` | `clean` | False | False | 0.2500 | ✅ | Election vote shares with a legitimate ~28% winner among many small candidates -- not a data error. |
| `outlier_fp_election_margin38_02` | `numeric_outlier` | `clean` | False | True | 0.0526 | ❌ | Election vote shares with a legitimate ~38% winner among many small candidates -- not a data error. |
| `outlier_fp_election_margin52_03` | `numeric_outlier` | `clean` | False | True | 0.0667 | ❌ | Election vote shares with a legitimate ~52% winner among many small candidates -- not a data error. |
| `outlier_tp_population_typo_paper_example` | `numeric_outlier` | `paper_example` | True | True | 0.1667 | ✅ | Population figures (thousands) with a decimal-point typo ('8.716' instead of '8716') -- paper's own 'C+' true-positive example. |
| `outlier_tp_subtle_00` | `numeric_outlier` | `subtle` | True | True | 0.0714 | ✅ | Population figures (thousands) with a subtle decimal-point error injected into one value. |
| `outlier_tp_subtle_01` | `numeric_outlier` | `subtle` | True | True | 0.1111 | ✅ | Population figures (thousands) with a subtle decimal-point error injected into one value. |
| `outlier_tp_subtle_02` | `numeric_outlier` | `subtle` | True | True | 0.1000 | ✅ | Population figures (thousands) with a subtle decimal-point error injected into one value. |
| `outlier_tp_moderate_00` | `numeric_outlier` | `moderate` | True | True | 0.0625 | ✅ | Population figures (thousands) with a moderate decimal-point error injected into one value. |
| `outlier_tp_moderate_01` | `numeric_outlier` | `moderate` | True | True | 0.1429 | ✅ | Population figures (thousands) with a moderate decimal-point error injected into one value. |
| `outlier_tp_moderate_02` | `numeric_outlier` | `moderate` | True | True | 0.0588 | ✅ | Population figures (thousands) with a moderate decimal-point error injected into one value. |
| `outlier_tp_obvious_00` | `numeric_outlier` | `obvious` | True | True | 0.0714 | ✅ | Population figures (thousands) with an obvious decimal-point error injected into one value. |
| `outlier_tp_obvious_01` | `numeric_outlier` | `obvious` | True | True | 0.0714 | ✅ | Population figures (thousands) with an obvious decimal-point error injected into one value. |
| `outlier_tp_obvious_02` | `numeric_outlier` | `obvious` | True | True | 0.1000 | ✅ | Population figures (thousands) with an obvious decimal-point error injected into one value. |
| `spelling_fp_amendment_list` | `spelling` | `paper_example` | False | False | 1.0000 | ✅ | Consecutive amendment numerals: syntactically close by design, not misspellings. |
| `spelling_fp_amendments_n6_00` | `spelling` | `clean` | False | False | 1.0000 | ✅ | 6 consecutive amendment numerals -- syntactically close pairs throughout by design, not misspellings. |
| `spelling_fp_amendments_n10_01` | `spelling` | `clean` | False | False | 1.0000 | ✅ | 10 consecutive amendment numerals -- syntactically close pairs throughout by design, not misspellings. |
| `spelling_fp_amendments_n14_02` | `spelling` | `clean` | False | False | 1.0000 | ✅ | 14 consecutive amendment numerals -- syntactically close pairs throughout by design, not misspellings. |
| `spelling_fp_amendments_n20_03` | `spelling` | `clean` | False | False | 1.0000 | ✅ | 20 consecutive amendment numerals -- syntactically close pairs throughout by design, not misspellings. |
| `spelling_tp_biography_typo_paper_example` | `spelling` | `paper_example` | True | True | 0.1053 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among unrelated long biography names -- paper's own true-positive example. |
| `spelling_tp_subtle_00` | `spelling` | `subtle` | True | False | 0.6667 | ❌ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, subtle corruption (diluted by one legitimate distractor pair 2 edits apart). |
| `spelling_tp_subtle_01` | `spelling` | `subtle` | True | False | 0.6667 | ❌ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, subtle corruption (diluted by one legitimate distractor pair 2 edits apart). |
| `spelling_tp_subtle_02` | `spelling` | `subtle` | True | False | 0.6667 | ❌ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, subtle corruption (diluted by one legitimate distractor pair 2 edits apart). |
| `spelling_tp_moderate_00` | `spelling` | `moderate` | True | True | 0.1667 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, moderate corruption (diluted by one legitimate distractor pair 4 edits apart). |
| `spelling_tp_moderate_01` | `spelling` | `moderate` | True | True | 0.1667 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, moderate corruption (diluted by one legitimate distractor pair 4 edits apart). |
| `spelling_tp_moderate_02` | `spelling` | `moderate` | True | True | 0.1667 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, moderate corruption (diluted by one legitimate distractor pair 4 edits apart). |
| `spelling_tp_obvious_00` | `spelling` | `obvious` | True | True | 0.0833 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, obvious corruption (no distractor pair). |
| `spelling_tp_obvious_01` | `spelling` | `obvious` | True | True | 0.0833 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, obvious corruption (no distractor pair). |
| `spelling_tp_obvious_02` | `spelling` | `obvious` | True | True | 0.0833 | ✅ | One genuine misspelling ('Doeling' for 'Dowling') among long biography names, obvious corruption (no distractor pair). |
| `fd_fp_pageviews_vs_edits` | `functional_dependency` | `paper_example` | False | True | 0.1000 | ❌ | Two independent numeric-ish columns with no real dependency. |
| `fd_fp_unrelated_domain100_00` | `functional_dependency` | `clean` | False | False | 0.2500 | ✅ | Two independent columns drawn from a 0-100 integer domain -- no real dependency, not a data error. |
| `fd_fp_unrelated_domain250_01` | `functional_dependency` | `clean` | False | True | 0.0714 | ❌ | Two independent columns drawn from a 0-250 integer domain -- no real dependency, not a data error. |
| `fd_fp_unrelated_domain450_02` | `functional_dependency` | `clean` | False | True | 0.2000 | ❌ | Two independent columns drawn from a 0-450 integer domain -- no real dependency, not a data error. |
| `fd_fp_unrelated_domain700_03` | `functional_dependency` | `clean` | False | True | 0.2000 | ❌ | Two independent columns drawn from a 0-700 integer domain -- no real dependency, not a data error. |
| `fd_tp_country_code_violation_paper_example` | `functional_dependency` | `paper_example` | True | True | 0.0588 | ✅ | ISO code -> country name table (a hard functional dependency on Wikipedia) with one injected violating row. |
| `fd_tp_subtle_00` | `functional_dependency` | `subtle` | True | True | 0.0588 | ✅ | ISO code -> country name table with subtle corruption (1 injected violating rows). |
| `fd_tp_subtle_01` | `functional_dependency` | `subtle` | True | True | 0.0588 | ✅ | ISO code -> country name table with subtle corruption (1 injected violating rows). |
| `fd_tp_subtle_02` | `functional_dependency` | `subtle` | True | True | 0.0588 | ✅ | ISO code -> country name table with subtle corruption (1 injected violating rows). |
| `fd_tp_moderate_00` | `functional_dependency` | `moderate` | True | True | 0.0588 | ✅ | ISO code -> country name table with moderate corruption (4 injected violating rows). |
| `fd_tp_moderate_01` | `functional_dependency` | `moderate` | True | True | 0.0588 | ✅ | ISO code -> country name table with moderate corruption (4 injected violating rows). |
| `fd_tp_moderate_02` | `functional_dependency` | `moderate` | True | True | 0.0588 | ✅ | ISO code -> country name table with moderate corruption (4 injected violating rows). |
| `fd_tp_obvious_00` | `functional_dependency` | `obvious` | True | False | 1.0000 | ❌ | ISO code -> country name table with obvious corruption (10 injected violating rows). |
| `fd_tp_obvious_01` | `functional_dependency` | `obvious` | True | False | 1.0000 | ❌ | ISO code -> country name table with obvious corruption (10 injected violating rows). |
| `fd_tp_obvious_02` | `functional_dependency` | `obvious` | True | False | 1.0000 | ❌ | ISO code -> country name table with obvious corruption (10 injected violating rows). |

---

_Regenerate this file (and the charts above) from a results JSON with:_

```bash
uv run python benchmarks/generate_report.py
```

