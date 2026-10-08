# Quickstart

Every algorithm is reached the same way: look it up by name, call `detect()`, read an
`AlgorithmResult`.

```python
from open_detect.algorithms import get_algorithm, list_algorithms

list_algorithms()   # ['auto_validate', 'raha', 'uni_detect']
```

## Raha: find errors with a few labels

Raha needs only the dirty table. It samples tuples for you to label, and spreads those labels
through clusters of similar cells.

```bash
pip install "open-detect[raha]"
```

```python
import pandas as pd
from open_detect.algorithms.raha import GroundTruthLabeler, RahaConfig, RahaDetector

dirty = pd.DataFrame(
    {
        "Lord": ["Aragorn", "Sauron", "Gandalf", "Saruman", "Elrond", "Theoden", "Bilbo"],
        "Kingdom": ["Minas Tirith", "Mordor", "MISSING", "MISSING", "123", "Shire", "Shire"],
    }
)
clean = pd.DataFrame(
    {
        "Lord": ["Aragorn", "Sauron", "Gandalf", "Saruman", "Elrond", "Theoden", "Bilbo"],
        "Kingdom": ["Minas Tirith", "Mordor", "N/A", "Isengard", "Rivendell", "Rohan", "Shire"],
    }
)

detector = RahaDetector(RahaConfig(labeling_budget=6, random_state=0))
labeler = GroundTruthLabeler(clean)   # answers "is this cell dirty?" from a known-clean copy

result = detector.detect(dirty, table_id="lord_of_the_rings", labeler=labeler)

print(f"Scanned {len(result)} cells, flagged {len(result.errors())} as errors")
for cell in result.errors():
    print(cell.row_index, cell.column_name, round(cell.score, 2), cell.evidence["source"])
```

```text
Scanned 14 cells, flagged 4 as errors
2 Kingdom 1.0 user_label
3 Kingdom 1.0 classifier
4 Kingdom 1.0 user_label
5 Kingdom 1.0 user_label
```

`GroundTruthLabeler` is for evaluation. On real data you wire in a person with
[`CallableLabeler`](../guides/custom-labelers.md); if you omit `labeler`, Raha falls back to
`HeuristicLabeler`, which needs no human but is weaker.

## Auto-Validate: learn patterns from clean columns

Auto-Validate first indexes a corpus of **clean** columns, then infers a validation pattern for
each column of your table and flags cells that do not match.

```python
import pandas as pd
from open_detect.algorithms.auto_validate import AutoValidateAlgorithm, AutoValidateConfig

corpus = [  # columns known to be clean
    pd.Series(["2024-01-15", "2024-02-20", "2024-03-10"]),
    pd.Series(["john@example.com", "jane@test.org", "admin@site.net"]),
    pd.Series(["New York", "London", "Tokyo"]),
]

detector = AutoValidateAlgorithm(AutoValidateConfig(m=1, tau=16))  # (1)!
detector.build_index(corpus)

dirty = pd.DataFrame(
    {"email": ["john@example.com", "invalid-email", "admin@site.net", "user@test.com"]}
)
result = detector.detect(dirty, table_id="contacts")

for cell in result.errors():
    print(cell.row_index, dirty.loc[cell.row_index, cell.column_name])
```

1. `m` is the minimum number of corpus columns that must match a pattern before it is trusted.
   The default (`100`) assumes a corpus of millions of columns; a toy corpus needs a small `m`.

```text
1 invalid-email
```

## Uni-Detect: score tables in Unity Catalog

Uni-Detect compares your tables against statistics learned from a large corpus of tables, using
Spark and Delta Lake. It has an offline phase (build statistics once) and an online phase (scan).

```python
from open_detect import UniDetectConfig, UnityCatalogLocation
from open_detect.pipeline import UniDetect
from open_detect.catalog import list_tables_matching

config = UniDetectConfig(location=UnityCatalogLocation(catalog="main", schema="data_quality"))
ud = UniDetect(config)   # uses the active Databricks SparkSession

ud.build_corpus_statistics(list_tables_matching(spark, catalog="main"))   # offline, run weekly
detections = ud.detect(["main.sales.orders"])                             # online
detections.show()
```

See the [Uni-Detect guide](../algorithms/uni-detect.md) for the full walk-through, including a
fully local example you can run without Databricks.

## Reading results

All three return an [`AlgorithmResult`](../reference/algorithms.md):

```python
result.errors()      # tuple of CellResult flagged as errors
result.to_pandas()   # DataFrame: table_id, row_index, column_name, algorithm, is_error, score, evidence
len(result)          # number of cells the algorithm reported on
```

Next: [Concepts](../concepts.md).
