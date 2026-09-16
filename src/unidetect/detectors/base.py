"""Shared detection template implementing Uni-Detect's Definition 4 end-to-end.

Every concrete detector (``uniqueness.py``, ``numeric_outlier.py``,
``spelling.py``, ``functional_dependency.py``) only has to implement
:meth:`BaseDetector.extract_candidates` -- computing, per target column (or
column-pair), the perturbation outcome and feature bucket. This base class
owns the shared plumbing: scoring candidates against the corpus
(``corpus/store.py``), applying the significance threshold, and producing a
ranked, explainable result set.

Target tables are profiled with the *same*
:class:`~unidetect.corpus.ingestion.CorpusIngestor` used to build the
background corpus -- scoring a table for errors and adding it to the corpus
are the same "read this table's columns" operation, just followed by a
different aggregation.
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from unidetect.config import UniDetectConfig
from unidetect.core.enums import ErrorType
from unidetect.corpus.ingestion import CorpusIngestor
from unidetect.corpus.store import CorpusStatsStore
from unidetect.logging_utils import get_logger, log_duration
from unidetect.strategies import get_spec

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)

#: Shared candidate schema every ``extract_candidates`` implementation must produce.
CANDIDATE_COLUMNS = (
    "candidate_id",
    "table_id",
    "column_names",  # array<string>
    "row_ids",  # array<string> (stringified indices/keys)
    "feature_bucket",
    "theta_before",
    "theta_after",
    "evidence_json",
)


class BaseDetector(ABC):
    """Template-method base class for a single error-type detector."""

    error_type: ErrorType

    def __init__(self, spark: SparkSession, config: UniDetectConfig) -> None:
        self.spark = spark
        self.config = config
        self.store = CorpusStatsStore(spark, config)
        self.ingestor = CorpusIngestor(
            spark,
            max_values_per_column=config.max_mpd_block_size * 200,
            max_fd_column_pairs_per_table=config.max_fd_column_pairs_per_table,
        )

    @abstractmethod
    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        """Return a DataFrame with the columns in :data:`CANDIDATE_COLUMNS`."""

    def detect(self, table_names: Sequence[str]) -> DataFrame:
        """Run the full Definition-4 pipeline for ``table_names`` and rank results.

        Returns a DataFrame sorted ascending by ``lr_ratio`` (most surprising
        first) with columns: ``candidate_id``, ``error_type``, ``table_id``,
        ``column_names``, ``row_ids``, ``lr_ratio``, ``surprisal``,
        ``is_significant``, ``support``, ``evidence_json``.
        """
        from pyspark.sql import functions as F

        spec = get_spec(self.error_type)
        with log_duration(logger, f"detect[{self.error_type.value}]"):
            candidates = self.extract_candidates(table_names)
            candidates.cache()
            try:
                n = candidates.count()
                if n == 0:
                    logger.info(
                        "No candidates extracted for %s over %s", self.error_type.value, table_names
                    )
                    return self._empty_result()

                scored = self.store.batch_score(candidates, self.error_type, spec.direction)
                joined = candidates.join(scored, on="candidate_id", how="inner")

                alpha = float(self.config.alpha)
                result = (
                    joined.withColumn("error_type", F.lit(self.error_type.value))
                    .withColumn("surprisal", -F.log(F.col("lr_ratio")))
                    .withColumn("is_significant", F.col("lr_ratio") <= F.lit(alpha))
                    .withColumnRenamed("bucket_support", "support")
                    .select(
                        "candidate_id",
                        "error_type",
                        "table_id",
                        "column_names",
                        "row_ids",
                        "lr_ratio",
                        "surprisal",
                        "is_significant",
                        "support",
                        "evidence_json",
                    )
                    .orderBy(F.col("lr_ratio").asc())
                )
                return result
            finally:
                candidates.unpersist()

    def _empty_result(self) -> DataFrame:
        from unidetect.detectors.schema import DETECTION_RESULT_SCHEMA

        return self.spark.createDataFrame([], schema=DETECTION_RESULT_SCHEMA)


def make_evidence_json(evidence: dict) -> str:
    return json.dumps(evidence, default=str)
