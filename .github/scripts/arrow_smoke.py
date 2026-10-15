"""Exercise the PySpark <-> Arrow paths open_detect relies on, with whatever pyarrow/numpy is installed.

Used by the caps-spike workflow. Fails (non-zero exit) on the first broken path.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pyarrow as pa
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T

print(f"pyspark={pyspark.__version__} pyarrow={pa.__version__} numpy={np.__version__}")

spark = (
    SparkSession.builder.master("local[2]")
    .appName("caps-spike")
    .config("spark.sql.shuffle.partitions", "2")
    .config("spark.sql.execution.arrow.pyspark.enabled", "true")
    .config("spark.ui.enabled", "false")
    .getOrCreate()
)

pdf = pd.DataFrame({"id": [1, 2, 3], "tags": [["a", "b"], ["c"], []], "x": [1.0, 2.5, None]})
sdf = spark.createDataFrame(
    pdf,
    schema=T.StructType(
        [
            T.StructField("id", T.LongType()),
            T.StructField("tags", T.ArrayType(T.StringType())),
            T.StructField("x", T.DoubleType()),
        ]
    ),
)

# Spark -> pandas via Arrow, including the array-typed column ("Expected Array, got ChunkedArray").
out = sdf.toPandas()
assert len(out) == 3, out


@F.pandas_udf(T.ArrayType(T.StringType()))
def upper_tags(s: pd.Series) -> pd.Series:
    return s.apply(lambda v: [t.upper() for t in v])


res = sdf.select("id", upper_tags("tags").alias("tags")).orderBy("id").toPandas()
assert [list(v) for v in res["tags"]] == [["A", "B"], ["C"], []], res


def add_one(it):
    for batch in it:
        batch["x"] = batch["x"] + 1
        yield batch


mapped = sdf.select("id", "x").mapInPandas(add_one, schema="id long, x double").orderBy("id")
got = mapped.toPandas()["x"].tolist()
assert got[0] == 2.0 and got[1] == 3.5 and np.isnan(got[2]), got

print("arrow smoke OK")
spark.stop()
