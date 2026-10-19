"""Turn a set of Unity Catalog tables into the canonical corpus representation.

The paper's corpus ``T`` is 100M+ tables scraped from the web. The natural
Databricks/Unity-Catalog analogue -- and the one this library targets -- is
the set of tables an organization already has registered in Unity Catalog
(a whole catalog, a set of schemas, or an explicit allow-list). For most
enterprises this is thousands to millions of governed tables spanning many
domains, which plays the same statistical role T does in the paper: a large
background sample of "what clean tables look like" to reason against.

:class:`CorpusIngestor` bounds how many values are materialized per column
(avoiding driver-side collection and unbounded executor memory use on wide
or skewed tables), and writes the canonical ``corpus_columns`` /
``corpus_column_pairs`` representations that every metric/featurization
function in this package consumes.

Every source row is first given a stable, dense ordinal (``0..num_rows-1`` in scan
order) *before* nulls are dropped or values are sampled. Oversized tables are sampled
by ordering on a seeded hash of that ordinal, so the sample is deterministic, and
detection ingests the ordinals alongside the values (``include_row_ids=True``) so a
reported cell can be traced back to its source row.
"""

from __future__ import annotations

import hashlib
import heapq
from collections.abc import Sequence
from itertools import permutations
from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.corpus.schema import (
    CORPUS_COLUMNS_SCHEMA,
    CORPUS_PAIRS_SCHEMA,
    INGESTED_COLUMNS_WITH_ROW_IDS_SCHEMA,
    INGESTED_PAIRS_WITH_ROW_IDS_SCHEMA,
    TOKEN_STATS_SCHEMA,
)
from open_detect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)

_ROW_ID = "__row_id"
_MONOTONIC_ID = "__mid"
_PARTITION_ID = "__pid"
_PARTITION_OFFSET = "__offset"
#: ``monotonically_increasing_id`` packs the partition index above bit 33.
_PARTITION_SHIFT = 33
_WITHIN_PARTITION_MASK = (1 << _PARTITION_SHIFT) - 1


def select_fd_column_pairs(
    table_id: str, column_names: Sequence[str], max_pairs: int
) -> list[tuple[int, int]]:
    """Pick the ordered ``(lhs_idx, rhs_idx)`` candidate pairs for one table.

    Both directions (A->B and B->A) are candidates. When there are more than
    ``max_pairs`` the survivors are those with the smallest stable hash of
    ``(table_id, lhs_name, rhs_name)``, so the selection depends only on the
    table and its column *names* -- not on column order -- and is identical
    across runs and processes (``hashlib``, unlike ``hash()``, is unsalted).
    """

    def sort_key(pair: tuple[int, int]) -> tuple[bytes, int, int]:
        lhs, rhs = pair
        digest = hashlib.sha256(
            f"{table_id}\x00{column_names[lhs]}\x00{column_names[rhs]}".encode()
        ).digest()
        return digest, lhs, rhs

    candidates = permutations(range(len(column_names)), 2)
    return heapq.nsmallest(max_pairs, candidates, key=sort_key)


class CorpusIngestor:
    """Builds ``corpus_columns``, ``corpus_column_pairs`` and ``token_stats``.

    Parameters
    ----------
    spark:
        An active, Unity-Catalog-enabled :class:`SparkSession`.
    max_values_per_column:
        Upper bound on how many (stringified) values are materialized per
        corpus column. Uses ``DataFrame.limit`` *before* aggregation, so cost
        is bounded regardless of the source table's true size.
    max_fd_column_pairs_per_table:
        Caps the number of ordered LHS/RHS candidate pairs generated per
        table, avoiding an O(columns^2) blow-up on very wide tables. Over the
        cap, pairs are sampled deterministically (see
        :func:`select_fd_column_pairs`).
    sample_seed:
        Seed of the hash that orders rows when a column (or pair) has more than
        ``max_values_per_column`` non-null values; the same table always yields
        the same sample.
    """

    def __init__(
        self,
        spark: SparkSession,
        max_values_per_column: int = 20_000,
        max_fd_column_pairs_per_table: int = 200,
        sample_seed: int = 0,
    ) -> None:
        self.spark = spark
        self.max_values_per_column = max_values_per_column
        self.max_fd_column_pairs_per_table = max_fd_column_pairs_per_table
        self.sample_seed = sample_seed

    def _with_row_ordinals(self, df: DataFrame) -> tuple[DataFrame, int]:
        """Return ``df`` with a dense ``__row_id`` ordinal column, and its row count.

        ``monotonically_increasing_id`` is unique but sparse (partition index in the
        high bits); one cheap per-partition count job turns it into a dense
        ``0..n-1`` ordinal -- the same job also yields the table's row count. The
        ordinal is stable as long as the table's scan partitioning is (i.e. the table is
        not modified between the count and the sampling jobs).
        """
        from pyspark.sql import functions as F

        tagged = df.withColumn(_MONOTONIC_ID, F.monotonically_increasing_id())
        partition_of = F.shiftright(F.col(_MONOTONIC_ID), _PARTITION_SHIFT)
        counts = tagged.groupBy(partition_of.alias(_PARTITION_ID)).count().collect()
        num_rows = sum(int(r["count"]) for r in counts)
        if num_rows == 0:
            return tagged, 0

        offsets: list[tuple[int, int]] = []
        running = 0
        for r in sorted(counts, key=lambda r: r[_PARTITION_ID]):
            offsets.append((int(r[_PARTITION_ID]), running))
            running += int(r["count"])
        offsets_df = self.spark.createDataFrame(
            offsets, schema=f"{_PARTITION_ID} long, {_PARTITION_OFFSET} long"
        )
        with_ordinals = (
            tagged.withColumn(_PARTITION_ID, partition_of)
            .join(F.broadcast(offsets_df), on=_PARTITION_ID)
            .withColumn(
                _ROW_ID,
                F.col(_MONOTONIC_ID).bitwiseAND(F.lit(_WITHIN_PARTITION_MASK))
                + F.col(_PARTITION_OFFSET),
            )
        )
        return with_ordinals, num_rows

    def _sample(self, df: DataFrame, num_rows: int) -> DataFrame:
        """Cap ``df`` (which has ``__row_id``) at ``max_values_per_column`` rows.

        Tables within the cap are kept whole; larger ones are ordered by a seeded hash
        of the row ordinal, so the sample is reproducible. Skipping the sort when it
        is not needed keeps the common small-table path a plain scan.
        """
        from pyspark.sql import functions as F

        if num_rows <= self.max_values_per_column:
            return df
        return df.orderBy(F.xxhash64(F.lit(self.sample_seed), F.col(_ROW_ID)), _ROW_ID).limit(
            self.max_values_per_column
        )

    def ingest_columns(
        self, table_names: Sequence[str], include_row_ids: bool = False
    ) -> DataFrame:
        """Build the ``corpus_columns`` DataFrame from a list of UC table FQNs.

        Each source table is scanned once for its per-partition row counts and
        once per column for its sampled non-null values; all per-column
        aggregations are lazy Spark transformations unioned together, so the
        only action taken here (besides the row counts) is whatever the
        caller triggers downstream (e.g. a Delta write).

        With ``include_row_ids=True`` the result has an extra ``row_ids``
        ``array<bigint>`` column parallel to ``values``: the source row ordinal
        (0-based, scan order) of each sampled value. Both arrays are ordered by
        ascending row id.
        """
        from functools import reduce

        per_column_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_columns({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    frames = self._per_table_column_frames(fqn, include_row_ids)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                per_column_frames.extend(frames)

        if not per_column_frames:
            return self.spark.createDataFrame(
                [],
                schema=(
                    INGESTED_COLUMNS_WITH_ROW_IDS_SCHEMA if include_row_ids else CORPUS_COLUMNS_SCHEMA
                ),
            )
        return reduce(lambda a, b: a.unionByName(b), per_column_frames)

    def _per_table_column_frames(self, fqn: str, include_row_ids: bool) -> list[DataFrame]:
        from pyspark.sql import functions as F

        source = self.spark.table(fqn)
        df, num_rows = self._with_row_ordinals(source)
        if num_rows == 0:
            return []

        frames: list[DataFrame] = []
        for idx, field in enumerate(source.schema.fields):
            col = field.name
            # Ordinals were assigned above, before nulls are dropped, so they index the
            # source table rather than the filtered/sampled list.
            non_null = df.select(
                F.col(_ROW_ID), F.col(f"`{col}`").cast("string").alias("v")
            ).where(F.col("v").isNotNull())
            sampled = self._sample(non_null, num_rows)
            pairs = F.sort_array(F.collect_list(F.struct(_ROW_ID, "v")))
            per_col = sampled.agg(pairs.alias("pairs")).select(
                F.lit(fqn).alias("table_id"),
                F.lit(col).alias("column_name"),
                F.lit(idx).alias("column_index"),
                F.lit(num_rows).alias("num_rows"),
                F.col("pairs.v").alias("values"),
                *([F.col(f"pairs.{_ROW_ID}").alias("row_ids")] if include_row_ids else []),
            )
            frames.append(per_col)
        return frames

    def ingest_column_pairs(
        self, table_names: Sequence[str], include_row_ids: bool = False
    ) -> DataFrame:
        """Build the ``corpus_column_pairs`` DataFrame used for FD statistics.

        With ``include_row_ids=True`` the result has an extra ``row_ids``
        ``array<bigint>`` column parallel to ``lhs_values``/``rhs_values`` holding each
        sampled pair's source row ordinal (see :meth:`ingest_columns`).
        """
        from functools import reduce

        per_pair_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_column_pairs({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    frames = self._per_table_pair_frames(fqn, include_row_ids)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                per_pair_frames.extend(frames)

        if not per_pair_frames:
            return self.spark.createDataFrame(
                [],
                schema=(
                    INGESTED_PAIRS_WITH_ROW_IDS_SCHEMA if include_row_ids else CORPUS_PAIRS_SCHEMA
                ),
            )
        return reduce(lambda a, b: a.unionByName(b), per_pair_frames)

    def _per_table_pair_frames(self, fqn: str, include_row_ids: bool) -> list[DataFrame]:
        from pyspark.sql import functions as F

        source = self.spark.table(fqn)
        columns = [f.name for f in source.schema.fields]
        if len(columns) < 2:
            return []
        df, num_rows = self._with_row_ordinals(source)
        if num_rows == 0:
            return []

        pairs = select_fd_column_pairs(fqn, columns, self.max_fd_column_pairs_per_table)
        frames: list[DataFrame] = []
        for lhs_idx, rhs_idx in pairs:
            lhs_col, rhs_col = columns[lhs_idx], columns[rhs_idx]
            # Collect (row id, lhs, rhs) as one struct, keeping only rows where both
            # sides are non-null: collecting the columns independently drops
            # nulls independently, leaving arrays of different lengths whose
            # positions no longer refer to the same rows.
            non_null = df.select(
                F.col(_ROW_ID),
                F.col(f"`{lhs_col}`").cast("string").alias("lhs"),
                F.col(f"`{rhs_col}`").cast("string").alias("rhs"),
            ).where(F.col("lhs").isNotNull() & F.col("rhs").isNotNull())
            sampled = self._sample(non_null, num_rows)
            collected = F.sort_array(F.collect_list(F.struct(_ROW_ID, "lhs", "rhs")))
            per_pair = sampled.agg(collected.alias("pairs")).select(
                F.lit(fqn).alias("table_id"),
                F.lit(lhs_col).alias("lhs_column"),
                F.lit(rhs_col).alias("rhs_column"),
                F.lit(rhs_idx).alias("rhs_column_index"),
                F.lit(num_rows).alias("num_rows"),
                F.col("pairs.lhs").alias("lhs_values"),
                F.col("pairs.rhs").alias("rhs_values"),
                *([F.col(f"pairs.{_ROW_ID}").alias("row_ids")] if include_row_ids else []),
            )
            frames.append(per_pair)
        return frames

    def build_token_stats(self, corpus_columns: DataFrame) -> DataFrame:
        """Global token -> distinct-table document-frequency (``Prev(C)`` input).

        A token's document frequency is the number of *distinct tables* (not
        rows/values) it appears in, matching the paper's ``Prev`` definition
        (Sec. 3.3: "the number of times the tokens in C occur in other
        tables").
        """
        from pyspark.sql import functions as F

        from open_detect.text_utils import tokenize

        tokenize_udf = F.udf(lambda s: tokenize(s) if s else [], "array<string>")

        exploded = (
            corpus_columns.select("table_id", F.explode("values").alias("value"))
            .where(F.col("value").isNotNull())
            .select("table_id", F.explode(tokenize_udf(F.lower(F.col("value")))).alias("token"))
            .dropDuplicates(["table_id", "token"])
        )
        return exploded.groupBy("token").agg(F.count("*").alias("doc_frequency"))

    @staticmethod
    def token_stats_schema():
        return TOKEN_STATS_SCHEMA
