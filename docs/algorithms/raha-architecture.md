# Raha (Mahdavi et al., SIGMOD 2019)

## 8. Code map

Raha's Algorithm 1 maps onto `src/open_detect/algorithms/raha/` module-by-step:

| Algorithm 1 step | Paper section | Code |
|---|---|---|
| Line 1: configure strategies | Section 4.1 | `strategies.py` (`histogram_outlier_strategies`, `gaussian_outlier_strategies`, `pattern_character_strategies`, `fd_violation_strategies`) |
| Line 2: generate feature vectors | Section 4.2 | `features.py` (`build_column_features`, `build_all_features`) |
| Lines 3-11: cluster + sample tuples | Section 4.3 | `clustering.py` (`cluster_column`, `sample_tuple`) |
| Line 9: label a tuple | Appendix C | `labeling.py` (`Labeler` and its implementations) |
| Lines 12-14: propagate labels | Section 4.4 | `labeling.py::propagate_labels` |
| Lines 15-16: train + predict per column | Section 4.4 | `classifier.py::train_and_predict` |
| Whole algorithm | Section 3-4 | `detector.py::RahaDetector.detect` |

## 9. Strategy families and what each feature means

A "feature" of a cell's feature vector is one strategy's binary verdict on
that cell (Definition 1). Three of the paper's four families are
implemented, each producing a parameter grid rather than one fixed
threshold, per Section 4.1:

- **Histogram outlier (`s_tf`)** -- flags a cell whose value is rare in its
  column (relative frequency below a threshold), at 9 thresholds
  (`0.1, ..., 0.9`).
- **Gaussian outlier (`s_dist`)** -- flags a numeric cell far from its
  column's mean in standard deviations, at 9 thresholds following the
  paper's 68-95-99.7 rule (`1, 1.3, ..., 3`). Only generated for columns
  that are mostly numeric.
- **Pattern violation (bag-of-characters, `s_ch`)** -- one strategy per
  distinct character in the column, flagging cells that contain it (e.g. a
  stray `-` in a digit-only column), capped at the most frequent
  `max_pattern_characters` to bound the feature space on free-text columns.
- **Rule/FD violation (`s_{a->a'}`)** -- for every other column `a`, flags
  cells of the target column `a'` whose `a`-group contains more than one
  distinct `a'` value, following Section 4.1's formal `j = index of a'`
  assignment (see the fidelity note in `strategies.py` about the paper's own
  inconsistent illustrative example).

`features.py` drops constant features per column (Section 4.2's
post-processing step) before assembling the matrix Raha clusters on.

## 10. Clustering, sampling, and labeling

`RahaDetector.detect` runs Algorithm 1's `while |L| < labels_budget` loop
directly: each iteration re-clusters every column at `k` (starting at 2,
incrementing by 1 per iteration -- Section 4.3), draws one tuple via the
softmax rule of Equation 3 (`clustering.py::sample_tuple`, favoring
under-labeled clusters), and asks the configured `Labeler` to label it.

`Labeler` (`labeling.py`) is the paper's Appendix-C human-labeling step made
pluggable:

- `GroundTruthLabeler` -- compares against a known-clean table; for
  evaluation/benchmarking.
- `CallableLabeler` -- wraps any function, e.g. a real UI or CLI prompt; the
  paper's actual intended use.
- `HeuristicLabeler` -- a documented deviation from the paper: a no-human
  fallback (majority vote of a cell's own fired strategies) so the pipeline
  can still run with zero interaction. Strictly weaker than a real label,
  since it mostly reinforces what the strategies already say; see its
  docstring.

After sampling, `propagate_labels` implements Section 4.4's cluster-based
label propagation with both conflict-resolution policies the paper
describes (`"homogeneity"`: skip clusters with contradicting labels;
`"majority"`: resolve them by vote, ties going to "dirty" as the
conservative choice for a class-imbalanced task) -- user labels always
override propagated ones for their own cell.

## 11. Classification and cell-level output

`classifier.py::train_and_predict` fits one classifier per column
(`RahaConfig.classifier_factory`, defaulting to `GradientBoostingClassifier`
per the paper's Section 6.1 setup) on the propagated labels and predicts
every remaining cell's `P(dirty)`. Degenerate cases (no labels, a
single-class label set, or a column with no informative features -- none of
which a real scikit-learn classifier can fit) fall back to the labeled
rows' majority vote rather than raising.

`RahaDetector.detect` then assembles the final `AlgorithmResult`: a directly
labeled or propagated cell keeps that exact label (`score` 1.0/0.0), while
every other cell gets the classifier's prediction and probability, each
tagged with `evidence.source` (`"user_label"` / `"propagated"` /
`"classifier"`) and `evidence.fired_strategies` (which strategies flagged
that specific cell) for explainability, in the same spirit as Uni-Detect's
`evidence_json` (Section 7 above).

## 12. Deviations from a literal reading of the paper, and why

1. **Histogram outlier normalization.** The published `s_tf` formula
   normalizes by `sum_i' TF(d[i',j])`, which algebraically is `sum_v
   count(v)^2`, not the column size. Plugging that literal denominator into
   the paper's own worked example (Section 2.2) does not reproduce the
   stated result; the natural reading -- relative frequency `count(v) /
   |d|` -- reproduces it exactly, and is what `strategies.py` implements.
   Same class of PDF-math-extraction artifact as Uni-Detect's FD formula
   (Section 6.2 above).

2. **Knowledge-base violation detection is omitted** (Section 9 above).

3. **Historical strategy filtering (paper Section 5) is not implemented.**
   It is a runtime optimization -- pruning strategies unlikely to help based
   on similarity to previously cleaned columns -- not part of the core
   detection result, and requires a corpus of historical cleaned datasets
   this library has no equivalent source for today. `RahaConfig` and the
   strategy functions are structured so this could be added later as a
   pre-filtering step over `features.py`'s strategy dict, without changing
   the clustering/labeling/classification pipeline.

4. **Bag-of-characters strategies are capped** (`max_pattern_characters`,
   default 128) rather than one-per-distinct-character unboundedly, since a
   free-text column can have an effectively unbounded character vocabulary;
   the most frequent characters are kept on the assumption that a rare
   character is already exposed by the histogram outlier strategies on the
   whole value.