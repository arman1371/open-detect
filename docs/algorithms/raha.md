# Raha

**Semi-supervised error detection for a single table.** Mahdavi et al., SIGMOD 2019.

Raha needs no background corpus, no declared constraints, and no tuning. It needs the dirty table
and a small labeling budget, 20 tuples by default.

## How it works

1. **Run many detectors.** Outlier, pattern-violation and rule-violation strategies run at many
   parameter settings. Each cell gets a feature vector: which strategies flagged it.
2. **Cluster.** Cells of each column are clustered by feature similarity.
3. **Sample tuples to label.** One tuple per iteration is chosen so that the clusters it touches
   are as yet unlabeled.
4. **Propagate labels.** A label on one cell spreads to the rest of its cluster.
5. **Classify.** One classifier per column learns from the labeled cells and predicts the rest.

## Install

```bash
pip install "open-detect[raha]"
```

## Usage

```python
import pandas as pd
from open_detect.algorithms.raha import RahaConfig, RahaDetector, GroundTruthLabeler

dirty = pd.read_csv("dirty.csv")
detector = RahaDetector(RahaConfig(labeling_budget=20))

result = detector.detect(dirty, table_id="my_table", labeler=GroundTruthLabeler(pd.read_csv("clean.csv")))
for cell in result.errors():
    print(cell.table_id, cell.row_index, cell.column_name, cell.score, cell.evidence["source"])
```

Through the registry it is the same thing:

```python
from open_detect.algorithms import get_algorithm
raha = get_algorithm("raha")                       # default RahaConfig
raha = get_algorithm("raha", RahaConfig(labeling_budget=10))
```

### Who answers the labeling questions?

Raha asks a `Labeler` "is each cell of this tuple dirty?". Three are included:

| Labeler | Use it for |
|---|---|
| `CallableLabeler(fn)` | **Real data.** Wrap a function that asks a person (CLI, web form, chat). See [Custom labelers](../guides/custom-labelers.md). |
| `GroundTruthLabeler(clean_df)` | Evaluation and benchmarks, when a clean copy of the table exists |
| `HeuristicLabeler` | Used automatically when you omit `labeler`. No human needed, but strictly weaker: a cell counts as dirty because most strategies already flagged it, so it adds little new information. |

### Reading the output

Every cell of the table is returned. `evidence["source"]` says where the verdict came from:

- `"user_label"`: the labeler answered for this cell directly. `score` is `1.0` or `0.0`.
- `"propagated"`: the cell shares a cluster with a labeled cell and inherited its label.
- `"classifier"`: the per-column classifier predicted it. `score` is its probability.

`evidence["fired_strategies"]` lists the detection strategies that flagged the cell, which is
usually the quickest way to see *why* a value looks wrong.

## Configuration

See [`RahaConfig`](../reference/raha.md#open_detect.algorithms.raha.config.RahaConfig) for the full list.

| Setting | Default | Notes |
|---|---|---|
| `labeling_budget` | `20` | Tuples the labeler is asked about. Also sets clusters per column to `labeling_budget + 1`. |
| `conflict_resolution` | `"majority"` | `"homogeneity"` only propagates through clusters whose labels agree. |
| `classifier_factory` | `GradientBoostingClassifier` | Any zero-argument callable returning an unfitted scikit-learn classifier. |
| `max_pattern_characters` | `128` | Caps the per-character pattern strategies on free-text columns. |
| `random_state` | `0` | Seeds clustering and tuple sampling for reproducible runs. |

```python
from sklearn.ensemble import RandomForestClassifier

config = RahaConfig(
    labeling_budget=15,
    conflict_resolution="homogeneity",
    classifier_factory=lambda: RandomForestClassifier(n_estimators=200),
)
```

## Scope

Not implemented: knowledge-base violation detection (it needs a live external knowledge base such
as DBpedia, which does not suit a library meant to run on private data) and the historical
strategy-filtering speed-up (Section 5 of the paper, an optimization rather than part of the
detection result).
