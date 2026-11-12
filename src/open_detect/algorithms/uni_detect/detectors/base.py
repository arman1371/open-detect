"""Shared detection template implementing Uni-Detect's Definition 4 end-to-end.

Every concrete detector (``uniqueness.py``, ``numeric_outlier.py``,
``spelling.py``, ``functional_dependency.py``) only has to implement
:meth:`BaseDetector.extract_candidates` -- computing, per target column (or
column-pair), the perturbation outcome and feature bucket. This base class
owns the shared plumbing: scoring candidates against the corpus
(``corpus/store.py``), applying the significance threshold, and producing a
ranked, explainable result set.

Target tables are profiled with the *same*
:class:`~open_detect.algorithms.uni_detect.corpus.ingestion.CorpusIngestor` used to build the
background corpus -- scoring a table for errors and adding it to the corpus
are the same "read this table's columns" operation, just followed by a
different aggregation.
"""

from __future__ import annotations

import hashlib
import json
from abc import ABC, abstractmethod
from contextlib import suppress
from typing import TYPE_CHECKING, Any, Literal

from pyspark import StorageLevel

from open_detect.algorithms.uni_detect.config import UniDetectConfig
from open_detect.algorithms.uni_detect.core.enums import ErrorType
from open_detect.algorithms.uni_detect.corpus.ingestion import CorpusIngestor
from open_detect.algorithms.uni_detect.corpus.store import CorpusStatsStore
from open_detect.algorithms.uni_detect.failures import FailureTracker
from open_detect.algorithms.uni_detect.spark_utils import (
    ARROW_MAX_RECORDS_PER_BATCH,
    ARROW_MAX_RECORDS_PER_BATCH_KEY,
    scoped_conf,
)
from open_detect.algorithms.uni_detect.strategies import get_spec
from open_detect.logging_utils import get_logger, log_duration

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
        self._failure_tracker: FailureTracker | None = None
        self._persisted: list[DataFrame] = []
        self.ingestor = CorpusIngestor(
            spark,
            max_values_per_column=config.max_mpd_block_size * 200,
            max_fd_column_pairs_per_table=config.max_fd_column_pairs_per_table,
        )

    @abstractmethod
    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        """Return a DataFrame with the columns in :data:`CANDIDATE_COLUMNS`."""

    def _new_failure_tracker(self) -> FailureTracker:
        """Create the accumulator-backed tracker an ``extract_candidates`` run reports into."""
        self._failure_tracker = FailureTracker(
            self.spark.sparkContext,
            f"extract_candidates[{self.error_type.value}]",
            self.config.max_failure_ratio,
        )
        return self._failure_tracker

    def detect(self, table_names: Sequence[str]) -> DataFrame:
        """Run the full Definition-4 pipeline for ``table_names`` and rank results.

        Returns a DataFrame with columns: ``candidate_id``, ``error_type``,
        ``table_id``, ``column_names``, ``row_ids``, ``lr_ratio``,
        ``surprisal``, ``is_significant``, ``support``, ``evidence_json``.

        The returned DataFrame is **persisted** (``MEMORY_AND_DISK``) and
        materialized once, before ``candidates`` is released, so every later
        action (``.count()``, ``.show()``, ``.write``) reuses the cached frame
        instead of re-running ingestion + scoring.  Call :meth:`release` (or
        ``unpersist()`` the frame yourself) when done to free the memory.

        Ordering is **not** guaranteed by this method -- the per-detector
        ``orderBy`` was removed because it is redundant with the global sort in
        ``pipeline.UniDetect.detect``.  Direct callers that need a specific
        order must sort the returned frame themselves.

        .. note::

            The result is persisted, not just collected.  ``collect()`` alone
            would return a list of rows and force the caller to rebuild a
            DataFrame from scratch -- re-triggering the schema inference and
            losing the cache.  Returning the persisted frame keeps the
            materialized data available for downstream actions without
            re-executing the scoring stage.
        """
        from pyspark.sql import functions as F

        spec = get_spec(self.error_type)
        # Use scoped_conf to ensure ARROW_MAX_RECORDS_PER_BATCH stays active
        # through the entire pipeline: extract_candidates (mapInPandas),
        # candidate materialization (count), scoring (batch_score join),
        # and result materialization. This protects against OOM on array-heavy
        # workloads where a single Arrow batch can balloon to ~10^9 strings.
        candidates = None
        result = None
        try:
            with (
                log_duration(logger, f"detect[{self.error_type.value}]"),
                scoped_conf(
                    self.spark,
                    **{ARROW_MAX_RECORDS_PER_BATCH_KEY: str(ARROW_MAX_RECORDS_PER_BATCH)},
                ),
            ):
                candidates = self.extract_candidates(table_names)
                candidates.persist(StorageLevel.MEMORY_AND_DISK)
                n = candidates.count()
                if self._failure_tracker is not None:
                    self._failure_tracker.check()
                if n == 0:
                    logger.info(
                        "No candidates extracted for %s over %d table(s)",
                        self.error_type.value,
                        len(table_names),
                    )
                    logger.debug("Tables scanned: %s", list(table_names))
                    # Return a persisted empty result so downstream actions (count, collect,
                    # write) don't re-execute the scoring stage, and the frame can be
                    # released via release() like any other result.
                    result = self._track(self._empty_result().persist(StorageLevel.MEMORY_AND_DISK))
                    result.count()
                    return result

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
                )
                # Materialize once while ``candidates`` is still cached, then
                # release the inputs.  The persisted result survives on its own,
                # so downstream actions never re-execute the scoring stage.
                result = self._track(result.persist(StorageLevel.MEMORY_AND_DISK))
                result.count()
                return result
        except Exception:
            # On failure, clean up any frames that were tracked/persisted during this call.
            if result is not None:
                with suppress(Exception):
                    result.unpersist()
            raise
        finally:
            # Always release the candidate frame
            if candidates is not None:
                with suppress(Exception):
                    candidates.unpersist()

    def _empty_result(self) -> DataFrame:
        from open_detect.algorithms.uni_detect.detectors.schema import DETECTION_RESULT_SCHEMA

        return self.spark.createDataFrame([], schema=DETECTION_RESULT_SCHEMA)

    # ------------------------------------------------------------------
    # Result lifecycle: persisted frames released by callers (req 2)
    # ------------------------------------------------------------------
    def _track(self, frame: DataFrame) -> DataFrame:
        """Register a persisted result frame for later release."""
        self._persisted.append(frame)
        return frame

    def release(self) -> None:
        """Unpersist every result frame produced by this detector's ``detect()`` calls.

        Safe to call when nothing has been tracked; safe to call repeatedly.
        """
        for frame in self._persisted:
            with suppress(Exception):
                frame.unpersist()
        self._persisted.clear()


RedactMode = Literal["none", "hash", "drop"]

#: Evidence keys whose values are raw cell values from the scanned tables.
RAW_VALUE_EVIDENCE_KEYS = frozenset(
    {"duplicate_values", "violating_examples", "outlier_value", "pair"}
)


def _hash_value(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return [_hash_value(v) for v in value]
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()[:16]


def redact_evidence(evidence: dict[str, Any], mode: RedactMode) -> dict[str, Any]:
    """Drop or SHA-256-hash the raw cell values in ``evidence`` (other keys are kept).

    Hashes are unsalted so equal values stay comparable across runs; low-entropy
    values can therefore be recovered by dictionary attack -- use ``"drop"`` when
    that matters.
    """
    if mode == "none":
        return evidence
    if mode == "drop":
        return {k: v for k, v in evidence.items() if k not in RAW_VALUE_EVIDENCE_KEYS}
    return {k: _hash_value(v) if k in RAW_VALUE_EVIDENCE_KEYS else v for k, v in evidence.items()}


def make_evidence_json(evidence: dict, redact: RedactMode = "none") -> str:
    return json.dumps(redact_evidence(evidence, redact), default=str)
