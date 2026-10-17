# Installation

`open-detect` requires **Python 3.10 or newer**. The core install is small (`numpy`,
`pandas`); `rapidfuzz` is no longer a core dependency. It is only needed by
Uni-Detect (`uni_detect` extra) and is not imported unless that algorithm is used.

Each algorithm's heavier dependencies are optional extras, so installing the
library never forces Spark or scikit-learn on you.

## Pick your extra

| You want | Install |
|---|---|
| (none) | `pip install open-detect` (just numpy + pandas) |
| Raha | `pip install "open-detect[raha]"` (adds scikit-learn, scipy) |
| Auto-Validate | `pip install "open-detect[auto_validate]"` (adds scipy) |
| Uni-Detect | `pip install "open-detect[uni_detect]"` (adds pyspark, pyarrow, numpy<2, rapidfuzz) |
| Spark (alias) | `pip install "open-detect[spark]"` (same as Uni-Detect) |
| Everything | `pip install "open-detect[all]"` (Uni-Detect + Raha + Auto-Validate) |

=== "pip"

    ```bash
    pip install "open-detect[raha,auto_validate]"
    ```

=== "uv"

    ```bash
    uv add "open-detect[raha,auto_validate]"
    ```

!!! note "Behaviour change"
    `rapidfuzz` is no longer a core dependency. The core
    install (`pip install open-detect`) now needs only `numpy` + `pandas`. Use the
    `uni_detect` extra (or the `spark` alias) to install Uni-Detect, which adds `rapidfuzz`
    plus `pyspark`, `pyarrow`, and `numpy<2`.

!!! note "New primary script names"
    The wheel now installs console scripts `open_detect_build_corpus` and
    `open_detect_run_detection`. The old names `build_corpus_statistics_job`
    and `run_detection_job` are kept as backward-compatible aliases
    (Databricks python_wheel_tasks reference entry-point names). See README
    and [databricks-jobs.md](https://github.com/arman1371/open-detect/blob/main/docs/guides/databricks-jobs.md) for examples.

!!! note "Databricks"
    On a Databricks cluster, Spark and Delta are already provided. Install the plain package
    (`pip install open-detect`) and do not add the `uni_detect` / `spark` extra; it would shadow the runtime's
    own PySpark.

!!! warning "Uni-Detect extra pins"
    The `uni_detect` / `spark` extras pin `pyspark>=3.5,<4.0`, `pyarrow<15` and `numpy<2` because PySpark 3.5's
    Arrow serialization is only tested against that range. If your environment needs NumPy 2,
    use Raha or Auto-Validate, which have no such constraint.

!!! warning "Local Spark needs JDK 17"
    For local Uni-Detect runs, use **JDK 17**. The Arrow version bundled with PySpark 3.5 does
    not work under JDK 21 or newer. This is a PySpark limitation, not a `open-detect` one.

## Installing from source

The project uses [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/arman1371/open-detect
cd open-detect
uv sync          # runtime + dev dependencies, including pyspark and delta-spark
```

## Check it works

```python
>>> import open_detect
>>> open_detect.__version__  # read from the installed package metadata
'x.y.z'
>>> from open_detect.algorithms import list_algorithms
>>> list_algorithms()
['auto_validate', 'raha', 'uni_detect']
```

`list_algorithms()` only reads the registry; it does not import an algorithm's dependencies.
They are imported the first time you request that algorithm with `get_algorithm`.
