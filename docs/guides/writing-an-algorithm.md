# Writing your own algorithm

Adding an algorithm means implementing one class and registering it by name. Once registered it
works with `get_algorithm`, `list_algorithms`, and the comparison tools in
[Comparing algorithms](comparing-algorithms.md).

## 1. Implement `ErrorDetectionAlgorithm`

Set a unique `name` (the registry key) and implement `detect()`, returning an `AlgorithmResult`.
Your constructor and your `data` type are yours to define.

```python
import pandas as pd
from open_detect.algorithms import AlgorithmResult, CellResult, ErrorDetectionAlgorithm


class NegativeValues(ErrorDetectionAlgorithm):
    """Flags negative numbers in numeric columns."""

    name = "negative_values"

    def __init__(self, tolerance: float = 0.0) -> None:
        self.tolerance = tolerance

    def detect(self, data: pd.DataFrame, *, table_id: str = "table", **kwargs) -> AlgorithmResult:
        cells = []
        for column in data.select_dtypes("number").columns:
            for row_index, value in data[column].items():
                bad = bool(value < -self.tolerance)
                cells.append(
                    CellResult(
                        table_id=table_id,
                        row_index=row_index,
                        column_name=column,
                        algorithm=self.name,
                        is_error=bad,
                        score=1.0 if bad else 0.0,
                        evidence={"value": float(value)},
                    )
                )
        return AlgorithmResult(algorithm=self.name, cells=tuple(cells))
```

Guidelines for `detect()`:

- Return **one `CellResult` per cell you assessed**, not only the flagged ones, so consumers can
  tell "checked and fine" from "never looked".
- Make `is_error` the honest binary verdict. Use `score` for ranking within your algorithm, and
  document its scale.
- Put human-readable reasoning in `evidence` (a plain dict).
- Raise exceptions derived from `OpenDetectError` for configuration and usage problems.

## 2. Register it

### In your own code

=== "Decorator"

    ```python
    from open_detect.algorithms import register_algorithm

    @register_algorithm("negative_values")
    class NegativeValues(ErrorDetectionAlgorithm): ...
    ```

=== "Lazy factory"

    Use this when your algorithm has heavy optional dependencies. They are only imported when the
    algorithm is first requested.

    ```python
    from open_detect.algorithms import register_lazy

    def _load():
        from my_package.algo import NegativeValues
        return NegativeValues

    register_lazy("negative_values", _load)
    ```

Then:

```python
from open_detect.algorithms import get_algorithm

algo = get_algorithm("negative_values", tolerance=0.5)
result = algo.detect(pd.DataFrame({"x": [1, -2, 3]}), table_id="demo")
result.errors()
```

Registering a name that already exists overwrites it, which is useful in tests and for swapping
in your own variant of a built-in.

### As a plugin package (no changes to `open-detect`)

Declare a Python entry point in the `open_detect.algorithms` group in **your** package's
`pyproject.toml`:

```toml
[project.entry-points."open_detect.algorithms"]
negative_values = "my_package.algo:NegativeValues"
```

After `pip install my-package`, `"negative_values"` appears in `list_algorithms()` and
`get_algorithm("negative_values")` works. Built-in names win: a plugin cannot silently replace
`raha`, `auto_validate` or `uni_detect`.

## 3. Test it

```python
def test_negative_values_flags_only_negatives():
    result = NegativeValues().detect(pd.DataFrame({"x": [1, -2, 3]}), table_id="t")
    assert [c.row_index for c in result.errors()] == [1]
    assert len(result) == 3
```
