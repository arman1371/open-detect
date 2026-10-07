# Installation

`unidetect` requires **Python 3.10 or newer**. The core install is small (`numpy`, `pandas`,
`rapidfuzz`); each algorithm's heavier dependencies are optional extras, so installing the
library never forces Spark or scikit-learn on you.

## Pick your extra

| You want | Install |
|---|---|
| Raha | `pip install "unidetect[raha]"` (adds scikit-learn, scipy) |
| Auto-Validate | `pip install "unidetect[auto_validate]"` (adds scipy) |
| Uni-Detect | `pip install "unidetect[spark]"` (adds pyspark, pyarrow) |
| Everything | `pip install "unidetect[raha,auto_validate,spark]"` |

=== "pip"

    ```bash
    pip install "unidetect[raha,auto_validate]"
    ```

=== "uv"

    ```bash
    uv add "unidetect[raha,auto_validate]"
    ```

!!! note "Databricks"
    On a Databricks cluster, Spark and Delta are already provided. Install the plain package
    (`pip install unidetect`) and do not add the `spark` extra; it would shadow the runtime's
    own PySpark.

!!! warning "Spark extra pins"
    The `spark` extra pins `pyspark>=3.5,<4.0`, `pyarrow<15` and `numpy<2` because PySpark 3.5's
    Arrow serialization is only tested against that range. If your environment needs NumPy 2,
    use Raha or Auto-Validate, which have no such constraint.

!!! warning "Local Spark needs JDK 17"
    For local Uni-Detect runs, use **JDK 17**. The Arrow version bundled with PySpark 3.5 does
    not work under JDK 21 or newer. This is a PySpark limitation, not a `unidetect` one.

## Installing from source

The project uses [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/arman1371/open-detect
cd open-detect
uv sync          # runtime + dev dependencies, including pyspark and delta-spark
```

## Check it works

```python
>>> import unidetect
>>> unidetect.__version__
'0.2.0'
>>> from unidetect.algorithms import list_algorithms
>>> list_algorithms()
['auto_validate', 'raha', 'uni_detect']
```

`list_algorithms()` only reads the registry; it does not import an algorithm's dependencies.
They are imported the first time you request that algorithm with `get_algorithm`.
