# Custom labelers (Raha)

Raha is semi-supervised: during `detect()` it picks tuples and asks a `Labeler` which of their
cells are dirty. The `Labeler` interface is how a person, a UI, or a rules engine plugs in.

## The simplest labeler: a function

`CallableLabeler` wraps a function `(df, row_index) -> {column_name: is_error}`:

```python
from unidetect.algorithms.raha import CallableLabeler, RahaConfig, RahaDetector

def ask_a_human(df, row_index):
    row = df.loc[row_index]
    print(f"\nRow {row_index}:")
    answers = {}
    for column, value in row.items():
        reply = input(f"  {column} = {value!r}  dirty? [y/N] ")
        answers[column] = reply.strip().lower() == "y"
    return answers

detector = RahaDetector(RahaConfig(labeling_budget=20))
result = detector.detect(df, table_id="orders", labeler=CallableLabeler(ask_a_human))
```

The function must return an entry for **every column** of the sampled row. `row_index` is the
DataFrame's own index label, so use `df.loc[row_index]`.

## Labeling with rules you already trust

When you know some constraints, a function can label from them. Raha still generalizes to errors
the rules do not cover:

```python
import pandas as pd

def label_from_rules(df, row_index):
    row = df.loc[row_index]
    return {
        "email": "@" not in str(row["email"]),
        "age": not (0 <= pd.to_numeric(row["age"], errors="coerce") <= 120),
        "name": False,
    }
```

## Writing a class

For anything stateful (a web session, a database connection) subclass `Labeler`:

```python
from unidetect.algorithms.raha import Labeler

class SlackLabeler(Labeler):
    def __init__(self, channel):
        self.channel = channel

    def label_tuple(self, df, row_index):
        return post_and_wait_for_reply(self.channel, df.loc[row_index])
```

## Choosing a budget

`labeling_budget` is the number of tuples you will be asked about (default 20, capped at the
number of rows). More labels generally means better recall, with diminishing returns. If
labeling is expensive, start at 10 to 20 and look at how much the result changes.

## Reproducibility

Tuple sampling is randomized. Fix `RahaConfig(random_state=...)` so reruns ask about the same
tuples, which matters when you cache human answers.
