# Comparing algorithms

Because every algorithm returns the same schema, running several and combining the results takes
a few lines. This is the payoff of the shared contract.

## Run two algorithms on the same table

```python
import pandas as pd
from unidetect.algorithms import AlgorithmResult, get_algorithm
from unidetect.algorithms.auto_validate import AutoValidateConfig

dirty = pd.DataFrame(
    {
        "email": ["john@example.com", "invalid-email", "admin@site.net", "user@test.com"],
        "city": ["New York", "London", "MISSING", "Tokyo"],
    }
)

raha = get_algorithm("raha")
av = get_algorithm("auto_validate", AutoValidateConfig(m=1, tau=16))
av.build_index([pd.Series(["john@example.com", "jane@test.org", "admin@site.net"])])

results = [
    raha.detect(dirty, table_id="contacts"),
    av.detect(dirty, table_id="contacts", columns=["email"]),
]
```

## Combine

```python
combined = AlgorithmResult.union(results, algorithm="ensemble")
df = combined.to_pandas()
```

`union` simply concatenates; each row still records the `algorithm` that produced it.

## Find the cells they agree on

```python
flags = (
    df[df.is_error]
    .groupby(["table_id", "row_index", "column_name"])["algorithm"]
    .agg(["nunique", lambda s: sorted(set(s))])
    .rename(columns={"nunique": "votes", "<lambda_0>": "algorithms"})
    .sort_values("votes", ascending=False)
)
print(flags)
```

Cells flagged by more than one algorithm are the best candidates to review first.

## Ranking caveat

`is_error` is comparable across algorithms; `score` is not. Raha's is a probability, Auto-Validate's
is `1 - FPR`, Uni-Detect's is an unbounded surprisal. Rank *within* an algorithm by `score`, and
combine *across* algorithms with votes on `is_error`, as above.

## Mixed inputs

Algorithms take different inputs, so a comparison pipeline passes each what it needs: the
DataFrame to Raha and Auto-Validate, table names to Uni-Detect. Only the results line up. If your
data lives in Unity Catalog, load a table into pandas for the single-table algorithms
(`spark.table(name).toPandas()` for tables small enough to fit) and pass the name to Uni-Detect.
