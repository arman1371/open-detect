# Concepts

## The registry

Algorithms are looked up by name through a small registry in `open_detect.algorithms`.

```python
from open_detect.algorithms import get_algorithm, get_algorithm_class, list_algorithms

list_algorithms()                       # ['auto_validate', 'raha', 'uni_detect']
cls = get_algorithm_class("raha")       # the class, not an instance
algo = get_algorithm("raha")            # cls(*args, **kwargs)
algo = get_algorithm("auto_validate", config)   # extra arguments go to the constructor
```

Registration is **lazy**. Requesting `raha` imports scikit-learn; requesting `uni_detect`
imports PySpark; requesting neither imports neither. Asking for an unknown name raises
[`UnknownAlgorithmError`](reference/exceptions.md), which lists what is available.

Third-party packages can add algorithms without touching this repository, using a Python entry
point. See [Writing your own algorithm](guides/writing-an-algorithm.md).

## One contract: `detect()`

Every algorithm subclasses `ErrorDetectionAlgorithm` and implements a single method:

```python
def detect(self, data, *, table_id="table", **kwargs) -> AlgorithmResult: ...
```

What `data` is depends on the algorithm, deliberately:

| Algorithm | `data` | Why |
|---|---|---|
| `raha` | `pandas.DataFrame` | Scores one in-memory table |
| `auto_validate` | `pandas.DataFrame` | Scores one in-memory table against a pre-built index |
| `uni_detect` | sequence of Unity Catalog table names | Scores governed tables with Spark; the data never leaves the cluster |

Forcing these into one input type would distort at least one paper's operating model. Only the
output is unified.

## The shared result schema

`detect()` always returns an `AlgorithmResult`: the algorithm's name plus a tuple of
`CellResult`, one per (table, row, column) cell the algorithm reported on.

| Field | Type | Meaning |
|---|---|---|
| `table_id` | `str` | The table identifier you passed (or the source table, for Uni-Detect) |
| `row_index` | any | The row's index label in the input |
| `column_name` | `str` | The column |
| `algorithm` | `str` | Registry name of the algorithm that produced the cell |
| `is_error` | `bool` | The normalized verdict, comparable across algorithms |
| `score` | `float` | Algorithm-specific confidence, for ranking **within** one algorithm |
| `evidence` | `dict` | Algorithm-specific explanation of the verdict |

!!! warning "Do not compare raw `score` values across algorithms"
    Raha's score is a classifier probability in `[0, 1]`. Auto-Validate's is `1 - FPR` for flagged
    cells and `0.0` otherwise. Uni-Detect's is an unbounded surprisal. Use `is_error` to compare
    algorithms and `score` to rank within one.

Working with a result:

```python
result.errors()          # tuple[CellResult, ...] with is_error == True
result.to_pandas()       # DataFrame with the columns above
len(result)              # number of cells reported
for cell in result: ... # iterate every CellResult

from open_detect.algorithms import AlgorithmResult
combined = AlgorithmResult.union([raha_result, av_result], algorithm="ensemble")
```

See [Comparing algorithms](guides/comparing-algorithms.md) for a worked example.

## Configuration objects

Each algorithm has its own frozen dataclass of knobs, validated on construction. Invalid values
raise `ConfigurationError` immediately rather than failing deep inside a run.

| Algorithm | Config | Most-used settings |
|---|---|---|
| Raha | `RahaConfig` | `labeling_budget`, `conflict_resolution`, `classifier_factory`, `random_state` |
| Auto-Validate | `AutoValidateConfig` | `variant`, `r`, `m`, `tau`, `theta` |
| Uni-Detect | `UniDetectConfig` | `location`, `alpha`, `epsilon` |

Configs are immutable. To change one setting, build a new config, or use
`dataclasses.replace(config, alpha=0.01)`.

## Errors

All exceptions raised by the library derive from `OpenDetectError`, so you can catch broadly
(`except OpenDetectError`) or narrowly (`ConfigurationError`, `IndexNotBuiltError`,
`CorpusNotFoundError`, ...). See the [reference](reference/exceptions.md).
