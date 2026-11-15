"""Turn a set of Unity Catalog tables into the canonical corpus representation.

The paper's corpus ``T`` is 100M+ tables scraped from the web. The natural
Databricks/Unity-Catalog analogue -- and the one this library targets -- is
the set of tables an organization already has registered in Unity Catalog
(a whole catalog, a set of schemas, or an explicit allow-list). For most
enterprises this is thousands to millions of governed tables spanning many
domains, which plays the same statistical role T does in the paper: a large
background sample of "what clean tables look like" to reason against.

:class:`CorpusIngestor` reads each source table *once*, using Spark's own
``limit`` push-down to bound how many values are materialized per column
(avoiding driver-side collection and unbounded executor memory use on wide
or skewed tables), and writes the canonical ``corpus_columns`` /
``corpus_column_pairs`` representations that every metric/featurization
function in this package consumes.
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
    TOKEN_STATS_SCHEMA,
)
from open_detect.algorithms.uni_detect.text_utils import infer_column_data_type
from open_detect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)


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
    """

    def __init__(
        self,
        spark: SparkSession,
        max_values_per_column: int = 20_000,
        max_fd_column_pairs_per_table: int = 200,
    ) -> None:
        self.spark = spark
        self.max_values_per_column = max_values_per_column
        self.max_fd_column_pairs_per_table = max_fd_column_pairs_per_table

    def ingest_columns(self, table_names: Sequence[str]) -> DataFrame:
        """Build the ``corpus_columns`` DataFrame from a list of UC table FQNs.

        Each source table is scanned ONCE: all per-column value arrays are
        computed in a single ``agg(collect_list(...))`` call, and the column
        rows are derived from that frame. This avoids O(columns) scans per table.
        """
        per_table_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_columns({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    frame = self._per_table_column_frame(fqn)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                if frame is not None:
                    per_table_frames.append(frame)

        if not per_table_frames:
            return self.spark.createDataFrame([], schema=CORPUS_COLUMNS_SCHEMA)
        # Use balanced union to avoid left-deep reduce(unionByName) plan blow-up
        return self._balanced_union(per_table_frames)

    def _per_table_column_frame(self, fqn: str) -> DataFrame | None:
        from pyspark.sql import functions as F

        df = self.spark.table(fqn)
        fields = df.schema.fields
        if not fields:
            return None

        # Single scan: collect every column's values in one ``agg`` call.
        # ``array_sort(collect_list(...))`` + ``slice`` reproduces the baseline
        # ``orderBy(value).limit(max_values_per_column)`` semantics (the N
        # smallest stringified values, in sorted order) without a per-column
        # scan, a window rank column, or a driver-side collect.
        col_names = [f.name for f in fields]
        cast_df = df.select(*[F.col(f"`{c}`").cast("string").alias(c) for c in col_names])
        agg_exprs = [
            F.slice(
                F.array_sort(F.collect_list(F.col(c))),
                1,
                self.max_values_per_column,
            ).alias(f"values_{idx}")
            for idx, c in enumerate(col_names)
        ]
        all_values_row = cast_df.agg(*agg_exprs).first()
        if all_values_row is None:
            return None

        num_rows = df.count()
        if num_rows == 0:
            return None

        # Build per-column rows from the single-scan result
        rows = []
        for idx, field in enumerate(fields):
            col_name = field.name
            values = all_values_row[f"values_{idx}"] or []
            # Infer column data type for P-14 tagging
            col_type = infer_column_data_type(values)
            rows.append(
                (
                    fqn,  # table_id
                    col_name,  # column_name
                    idx,  # column_index
                    num_rows,  # num_rows
                    values,  # values
                    col_type.value,  # column_data_type
                )
            )

        return self.spark.createDataFrame(rows, schema=CORPUS_COLUMNS_SCHEMA)

    def _balanced_union(self, frames: list[DataFrame]) -> DataFrame:
        """Combine DataFrames with a balanced union tree to avoid left-deep plans."""
        if len(frames) == 1:
            return frames[0]
        mid = len(frames) // 2
        left = self._balanced_union(frames[:mid])
        right = self._balanced_union(frames[mid:])
        return left.unionByName(right)

    def ingest_column_pairs(self, table_names: Sequence[str]) -> DataFrame:
        """Build the ``corpus_column_pairs`` DataFrame used for FD statistics.

        Uses the same single-scan frame via explode/arrays_zip; no per-pair scans.
        """
        from functools import reduce

        per_pair_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_column_pairs({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    frames = self._per_table_pair_frames(fqn)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                per_pair_frames.extend(frames)

        if not per_pair_frames:
            return self.spark.createDataFrame([], schema=CORPUS_PAIRS_SCHEMA)
        return reduce(lambda a, b: a.unionByName(b), per_pair_frames)

    def _per_table_pair_frames(self, fqn: str) -> list[DataFrame]:
        from pyspark.sql import functions as F

        df = self.spark.table(fqn)
        columns = [f.name for f in df.schema.fields]
        if len(columns) < 2:
            return []

        num_rows = df.count()
        if num_rows == 0:
            return []

        pairs = select_fd_column_pairs(fqn, columns, self.max_fd_column_pairs_per_table)
        if not pairs:
            return []

        # Single scan: collect every selected pair's (lhs, rhs) values at once.
        # Each pair is collected independently -- nulls are dropped *per pair*
        # (a row with a null lhs/rhs is dropped for that pair but kept for others),
        # matching the baseline per-pair ``where(lhs.isNotNull() & rhs.isNotNull())``
        # semantics. A global null filter would misalign the arrays across pairs.
        pair_exprs = [
            F.struct(
                F.col(f"`{columns[lhs_idx]}`").cast("string").alias("lhs"),
                F.col(f"`{columns[rhs_idx]}`").cast("string").alias("rhs"),
            ).alias(f"pair_{lhs_idx}_{rhs_idx}")
            for lhs_idx, rhs_idx in pairs
        ]

        # Order by first pair for deterministic selection, then limit rows
        first_lhs, first_rhs = pairs[0]
        ordered_df = (
            df.select(*pair_exprs)
            .orderBy(f"pair_{first_lhs}_{first_rhs}.lhs", f"pair_{first_lhs}_{first_rhs}.rhs")
            .limit(self.max_values_per_column)
        )

        all_pairs_row = ordered_df.first()
        if all_pairs_row is None:
            return []

        frames: list[DataFrame] = []
        for lhs_idx, rhs_idx in pairs:
            lhs_col, rhs_col = columns[lhs_idx], columns[rhs_idx]
            pair_data = all_pairs_row[f"pair_{lhs_idx}_{rhs_idx}"] or []
            # Filter nulls: keep only rows where both lhs and rhs are non-null
            lhs_values = [
                p["lhs"] for p in pair_data if p["lhs"] is not None and p["rhs"] is not None
            ]
            rhs_values = [
                p["rhs"] for p in pair_data if p["lhs"] is not None and p["rhs"] is not None
            ]

            frames.append(
                self.spark.createDataFrame(
                    [(fqn, lhs_col, rhs_col, rhs_idx, num_rows, lhs_values, rhs_values)],
                    schema=CORPUS_PAIRS_SCHEMA,
                )
            )
        return frames

    def build_token_stats(self, corpus_columns: DataFrame) -> DataFrame:
        """Global token -> distinct-table document-frequency (``Prev(C)`` input).

        A token's document frequency is the number of *distinct tables* (not
        rows/values) it appears in, matching the paper's ``Prev`` definition
        (Sec. 3.3: "the number of times the tokens in C occur in other
        tables").
        """
        from pyspark.sql import functions as F

        from open_detect.algorithms.uni_detect.text_utils import tokenize

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
