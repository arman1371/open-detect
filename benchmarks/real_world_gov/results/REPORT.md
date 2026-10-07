# real_world_gov benchmark results

Human-readable view of the checked-in benchmark run. See [README.md](README.md) for how this benchmark works, where its 5 datasets came from, and how to regenerate this file.

**Generated at:** 2026-10-06T22:16:12.191491+00:00  
**Commit:** `5976e33`  
**Source:** https://github.com/LUH-DBS/Matelda/tree/main/datasets/DGov_NTR

## Algorithm comparison

Every algorithm below scores the same set of (dataset, column) targets against the same `clean_changes.csv` ground truth (see [README.md](README.md) for how each algorithm's per-column verdict is derived), so the comparison is apples-to-apples on effectiveness. Duration is each algorithm's own wall-clock time to go from loaded data to predictions (see README for exactly what is/isn't included, and why one algorithm's duration may be unmeasured in a given run).

| Algorithm | n | Precision | Recall | F1 | Accuracy | Duration (s) |
|---|---|---|---|---|---|---|
| `raha` | 47 | 1.000 | 1.000 | 1.000 | 1.000 | 5.68 |
| `auto_validate` | 47 | 1.000 | 0.265 | 0.419 | 0.468 | 153.33 |
| `uni_detect` | 47 | 0.800 | 0.824 | 0.812 | 0.723 | 484.07 |

![F1 by algorithm](charts/algorithm_f1_comparison.svg)

![Duration by algorithm](charts/algorithm_duration_comparison.svg)

## `raha`

**Duration:** 5.68s  

| Metric | Value |
|---|---|
| Columns evaluated | 47 |
| Precision | 1.000 |
| Recall | 1.000 |
| F1 | 1.000 |
| Accuracy | 1.000 |

![F1 by dataset (raha)](charts/f1_by_dataset_raha.svg)

### By dataset (column-level)

Column-level: a column is "predicted significant" if *any* of its cells was flagged -- the same granularity Uni-Detect's own output has, used for the apples-to-apples comparison above. See "Cell-level" below for Raha's native, per-cell granularity (the same one the paper's own Table 5 reports).

| Dataset | n | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|
| **overall** | 47 | 1.000 | 1.000 | 1.000 | 1.000 |
| `Hate_Crimes` | 13 | 1.000 | 1.000 | 1.000 | 1.000 |
| `Illicit-drug-use.g8_2014_0731_0900` | 7 | 1.000 | 1.000 | 1.000 | 1.000 |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | 6 | 1.000 | 1.000 | 1.000 | 1.000 |
| `adult-depression-lghc-indicator-24` | 8 | 1.000 | 1.000 | 1.000 | 1.000 |
| `oklahoma-public-school-district-directory-january-2016` | 13 | 1.000 | 1.000 | 1.000 | 1.000 |

### By dataset (cell-level)

Precision/recall/F1 over every individual `(row, column)` cell against `clean_changes.csv` -- Raha's native evaluation granularity, and typically a more informative number than the column-level reduction above, since a real, historically-corrupted column in this benchmark often has a double-digit-percent error rate: getting the column-level call right only requires flagging *one* of many erroneous cells.

| Dataset | n | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|
| **overall** | 11472 | 0.585 | 0.475 | 0.524 | 0.888 |
| `Hate_Crimes` | 546 | 0.845 | 0.789 | 0.816 | 0.951 |
| `Illicit-drug-use.g8_2014_0731_0900` | 2184 | 0.787 | 0.802 | 0.795 | 0.922 |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | 252 | 0.688 | 0.917 | 0.786 | 0.976 |
| `adult-depression-lghc-indicator-24` | 1288 | 0.829 | 0.953 | 0.886 | 0.976 |
| `oklahoma-public-school-district-directory-january-2016` | 7202 | 0.332 | 0.214 | 0.260 | 0.855 |

### Evaluated columns (column-level)

| Dataset | Column | Rows | Errors | Expected | Predicted | Score | Result |
|---|---|---|---|---|---|---|---|
| `Hate_Crimes` | `casenumber` | 42 | 7 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `datevalue` | 42 | 3 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `weekday` | 42 | 10 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `victims` | 42 | 6 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `victimrace` | 42 | 5 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `victimgender` | 42 | 3 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `victimtype` | 42 | 12 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `offenders` | 42 | 1 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `offenderrace` | 42 | 6 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `offendergender` | 42 | 8 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `offense` | 42 | 3 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `locationtype` | 42 | 5 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `motivation` | 42 | 7 | True | True | 1.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `sexraceethnicity` | 312 | 146 | True | True | 1.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `sex` | 312 | 126 | True | True | 1.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `raceethnicity` | 312 | 95 | True | True | 1.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `yearvalue` | 312 | 0 | False | False | 0.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `percentage` | 312 | 0 | False | False | 0.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `standarderroronpercentage` | 312 | 0 | False | False | 0.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `noteonpercent` | 312 | 43 | True | True | 1.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `yearvalue` | 42 | 0 | False | False | 0.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `sourcevalue` | 42 | 2 | True | True | 1.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `question` | 42 | 1 | True | True | 1.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `prevalence` | 42 | 0 | False | False | 0.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `lowerninefiveconfidenceinterval` | 42 | 9 | True | True | 1.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `upperninefiveconfidenceinterval` | 42 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `yearvalue` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `strata` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `strataname` | 161 | 127 | True | True | 1.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `frequency` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `weightedfrequency` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `percentvalue` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `lowerninefivecl` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `upperninefivecl` | 161 | 0 | False | False | 0.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `countyname` | 554 | 68 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `code` | 554 | 128 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `districtname` | 554 | 51 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `city` | 554 | 60 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `address` | 554 | 71 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `statevalue` | 554 | 62 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `zip` | 554 | 1 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `phone` | 554 | 122 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `fax` | 554 | 64 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `websiteurl` | 554 | 63 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `superintendent` | 554 | 61 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `superintendentemail` | 554 | 60 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `boardpresident` | 554 | 65 | True | True | 1.000 | ✅ |

## `auto_validate`

**Duration:** 153.33s  
(build_index + detect; m and tau overridden from corpus size (see README))  

| Metric | Value |
|---|---|
| Columns evaluated | 47 |
| Precision | 1.000 |
| Recall | 0.265 |
| F1 | 0.419 |
| Accuracy | 0.468 |

![F1 by dataset (auto_validate)](charts/f1_by_dataset_auto_validate.svg)

### By dataset (column-level)

Column-level: a column is "predicted significant" if *any* of its cells was flagged -- the same granularity Uni-Detect's own output has, used for the apples-to-apples comparison above. See "Cell-level" below for Auto-Validate's native, per-cell granularity (the same one the paper's own Table 5 reports).

| Dataset | n | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|
| **overall** | 47 | 1.000 | 0.265 | 0.419 | 0.468 |
| `Hate_Crimes` | 13 | 1.000 | 0.308 | 0.471 | 0.308 |
| `Illicit-drug-use.g8_2014_0731_0900` | 7 | 0.000 | 0.000 | 0.000 | 0.429 |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | 6 | 0.000 | 0.000 | 0.000 | 0.500 |
| `adult-depression-lghc-indicator-24` | 8 | 0.000 | 0.000 | 0.000 | 0.875 |
| `oklahoma-public-school-district-directory-january-2016` | 13 | 1.000 | 0.385 | 0.556 | 0.385 |

### By dataset (cell-level)

Precision/recall/F1 over every individual `(row, column)` cell against `clean_changes.csv` -- Auto-Validate's native evaluation granularity, and typically a more informative number than the column-level reduction above, since a real, historically-corrupted column in this benchmark often has a double-digit-percent error rate: getting the column-level call right only requires flagging *one* of many erroneous cells.

| Dataset | n | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|
| **overall** | 11467 | 0.145 | 0.232 | 0.178 | 0.724 |
| `Hate_Crimes` | 541 | 0.058 | 0.127 | 0.080 | 0.616 |
| `Illicit-drug-use.g8_2014_0731_0900` | 2184 | 0.000 | 0.000 | 0.000 | 0.812 |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | 252 | 0.000 | 0.000 | 0.000 | 0.952 |
| `adult-depression-lghc-indicator-24` | 1288 | 0.000 | 0.000 | 0.000 | 0.901 |
| `oklahoma-public-school-district-directory-january-2016` | 7202 | 0.151 | 0.388 | 0.217 | 0.666 |

### Evaluated columns (column-level)

| Dataset | Column | Rows | Errors | Expected | Predicted | Score | Result |
|---|---|---|---|---|---|---|---|
| `Hate_Crimes` | `casenumber` | 42 | 7 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `datevalue` | 42 | 3 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `weekday` | 42 | 10 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `victims` | 42 | 6 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `victimrace` | 42 | 5 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `victimgender` | 42 | 3 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `victimtype` | 42 | 12 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `offenders` | 42 | 1 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `offenderrace` | 42 | 6 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `offendergender` | 42 | 8 | True | True | 1.000 | ✅ |
| `Hate_Crimes` | `offense` | 42 | 3 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `locationtype` | 42 | 5 | True | False | 0.000 | ❌ |
| `Hate_Crimes` | `motivation` | 42 | 7 | True | False | 0.000 | ❌ |
| `Illicit-drug-use.g8_2014_0731_0900` | `sexraceethnicity` | 312 | 146 | True | False | 0.000 | ❌ |
| `Illicit-drug-use.g8_2014_0731_0900` | `sex` | 312 | 126 | True | False | 0.000 | ❌ |
| `Illicit-drug-use.g8_2014_0731_0900` | `raceethnicity` | 312 | 95 | True | False | 0.000 | ❌ |
| `Illicit-drug-use.g8_2014_0731_0900` | `yearvalue` | 312 | 0 | False | False | 0.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `percentage` | 312 | 0 | False | False | 0.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `standarderroronpercentage` | 312 | 0 | False | False | 0.000 | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `noteonpercent` | 312 | 43 | True | False | 0.000 | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `yearvalue` | 42 | 0 | False | False | 0.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `sourcevalue` | 42 | 2 | True | False | 0.000 | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `question` | 42 | 1 | True | False | 0.000 | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `prevalence` | 42 | 0 | False | False | 0.000 | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `lowerninefiveconfidenceinterval` | 42 | 9 | True | False | 0.000 | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `upperninefiveconfidenceinterval` | 42 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `yearvalue` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `strata` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `strataname` | 161 | 127 | True | False | 0.000 | ❌ |
| `adult-depression-lghc-indicator-24` | `frequency` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `weightedfrequency` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `percentvalue` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `lowerninefivecl` | 161 | 0 | False | False | 0.000 | ✅ |
| `adult-depression-lghc-indicator-24` | `upperninefivecl` | 161 | 0 | False | False | 0.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `countyname` | 554 | 68 | True | False | 0.000 | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `code` | 554 | 128 | True | True | 0.930 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `districtname` | 554 | 51 | True | False | 0.000 | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `city` | 554 | 60 | True | False | 0.000 | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `address` | 554 | 71 | True | True | 0.825 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `statevalue` | 554 | 62 | True | False | 0.000 | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `zip` | 554 | 1 | True | False | 0.000 | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `phone` | 554 | 122 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `fax` | 554 | 64 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `websiteurl` | 554 | 63 | True | True | 1.000 | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `superintendent` | 554 | 61 | True | False | 0.000 | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `superintendentemail` | 554 | 60 | True | False | 0.000 | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `boardpresident` | 554 | 65 | True | False | 0.000 | ❌ |

## `uni_detect`

**Duration:** 484.07s  

| Metric | Value |
|---|---|
| Columns evaluated | 47 |
| Precision | 0.800 |
| Recall | 0.824 |
| F1 | 0.812 |
| Accuracy | 0.723 |

![F1 by dataset (uni_detect)](charts/f1_by_dataset_uni_detect.svg)

### By dataset (column-level)

| Dataset | n | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|
| **overall** | 47 | 0.800 | 0.824 | 0.812 | 0.723 |
| `Hate_Crimes` | 13 | 1.000 | 0.846 | 0.917 | 0.846 |
| `Illicit-drug-use.g8_2014_0731_0900` | 7 | 0.500 | 0.750 | 0.600 | 0.429 |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | 6 | 0.500 | 0.333 | 0.400 | 0.500 |
| `adult-depression-lghc-indicator-24` | 8 | 0.250 | 1.000 | 0.400 | 0.625 |
| `oklahoma-public-school-district-directory-january-2016` | 13 | 1.000 | 0.923 | 0.960 | 0.923 |

### Evaluated columns (column-level)

| Dataset | Column | Rows | Errors | Expected | Predicted | lr_ratio | Matched via | Result |
|---|---|---|---|---|---|---|---|---|
| `Hate_Crimes` | `casenumber` | 42 | 7 | True | True | 0.0294 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `datevalue` | 42 | 3 | True | True | 0.0294 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `weekday` | 42 | 10 | True | True | 0.0357 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `victims` | 42 | 6 | True | True | 0.0370 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `victimrace` | 42 | 5 | True | True | 0.0370 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `victimgender` | 42 | 3 | True | True | 0.0370 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `victimtype` | 42 | 12 | True | True | 0.0370 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `offenders` | 42 | 1 | True | True | 0.1250 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `offenderrace` | 42 | 6 | True | False | 0.5000 | `uniqueness` | ❌ |
| `Hate_Crimes` | `offendergender` | 42 | 8 | True | False | 0.5000 | `uniqueness` | ❌ |
| `Hate_Crimes` | `offense` | 42 | 3 | True | True | 0.0294 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `locationtype` | 42 | 5 | True | True | 0.0357 | `functional_dependency` | ✅ |
| `Hate_Crimes` | `motivation` | 42 | 7 | True | True | 0.0294 | `functional_dependency` | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `sexraceethnicity` | 312 | 146 | True | True | 0.1250 | `functional_dependency` | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `sex` | 312 | 126 | True | True | 0.1250 | `functional_dependency` | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `raceethnicity` | 312 | 95 | True | True | 0.1111 | `functional_dependency` | ✅ |
| `Illicit-drug-use.g8_2014_0731_0900` | `yearvalue` | 312 | 0 | False | True | 0.1429 | `functional_dependency` | ❌ |
| `Illicit-drug-use.g8_2014_0731_0900` | `percentage` | 312 | 0 | False | True | 0.1250 | `functional_dependency` | ❌ |
| `Illicit-drug-use.g8_2014_0731_0900` | `standarderroronpercentage` | 312 | 0 | False | True | 0.1111 | `functional_dependency` | ❌ |
| `Illicit-drug-use.g8_2014_0731_0900` | `noteonpercent` | 312 | 43 | True | False | 0.5000 | `uniqueness` | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `yearvalue` | 42 | 0 | False | False | 0.5000 | `functional_dependency` | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `sourcevalue` | 42 | 2 | True | False | 0.2500 | `functional_dependency` | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `question` | 42 | 1 | True | False | 0.2500 | `functional_dependency` | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `prevalence` | 42 | 0 | False | True | 0.2000 | `functional_dependency` | ❌ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `lowerninefiveconfidenceinterval` | 42 | 9 | True | True | 0.2000 | `functional_dependency` | ✅ |
| `Pregnancy_Risk_Assessment_Monitoring_System__PRAMS_` | `upperninefiveconfidenceinterval` | 42 | 0 | False | False | 0.2500 | `functional_dependency` | ✅ |
| `adult-depression-lghc-indicator-24` | `yearvalue` | 161 | 0 | False | False | 0.5000 | `numeric_outlier` | ✅ |
| `adult-depression-lghc-indicator-24` | `strata` | 161 | 0 | False | False | 0.3750 | `functional_dependency` | ✅ |
| `adult-depression-lghc-indicator-24` | `strataname` | 161 | 127 | True | True | 0.1250 | `functional_dependency` | ✅ |
| `adult-depression-lghc-indicator-24` | `frequency` | 161 | 0 | False | True | 0.1429 | `functional_dependency` | ❌ |
| `adult-depression-lghc-indicator-24` | `weightedfrequency` | 161 | 0 | False | True | 0.1667 | `functional_dependency` | ❌ |
| `adult-depression-lghc-indicator-24` | `percentvalue` | 161 | 0 | False | True | 0.1250 | `functional_dependency` | ❌ |
| `adult-depression-lghc-indicator-24` | `lowerninefivecl` | 161 | 0 | False | False | 0.2500 | `functional_dependency` | ✅ |
| `adult-depression-lghc-indicator-24` | `upperninefivecl` | 161 | 0 | False | False | 0.2500 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `countyname` | 554 | 68 | True | True | 0.1429 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `code` | 554 | 128 | True | True | 0.0769 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `districtname` | 554 | 51 | True | True | 0.1667 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `city` | 554 | 60 | True | True | 0.0769 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `address` | 554 | 71 | True | False | 0.2500 | `spelling` | ❌ |
| `oklahoma-public-school-district-directory-january-2016` | `statevalue` | 554 | 62 | True | True | 0.1667 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `zip` | 554 | 1 | True | True | 0.0769 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `phone` | 554 | 122 | True | True | 0.0769 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `fax` | 554 | 64 | True | True | 0.2000 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `websiteurl` | 554 | 63 | True | True | 0.1176 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `superintendent` | 554 | 61 | True | True | 0.0769 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `superintendentemail` | 554 | 60 | True | True | 0.0769 | `functional_dependency` | ✅ |
| `oklahoma-public-school-district-directory-january-2016` | `boardpresident` | 554 | 65 | True | True | 0.0769 | `functional_dependency` | ✅ |

---

_Regenerate this file (and the charts above) from a results JSON with:_

```bash
uv run python benchmarks/real_world_gov/generate_report.py
```

