"""Adapter registering :class:`unidetect.pipeline.UniDetect` as the ``"uni_detect"`` algorithm.

Uni-Detect and Raha have fundamentally different operating models (see
``unidetect/algorithms/base.py``): Uni-Detect scores Unity Catalog tables
against a background corpus that must already be built via
``UniDetect.build_corpus_statistics``, using Spark throughout. This adapter
does not re-implement any of that -- it only flattens Uni-Detect's Spark
``detect()`` output into the shared, algorithm-agnostic
:class:`~unidetect.algorithms.base.AlgorithmResult` schema, so its results
can be compared or unioned with another algorithm's (e.g. Raha's) output.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from unidetect.algorithms.base import AlgorithmResult, CellResult, ErrorDetectionAlgorithm
from unidetect.config import UniDetectConfig

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import SparkSession

    from unidetect.core.enums import ErrorType


class UniDetectAlgorithm(ErrorDetectionAlgorithm):
    """Registered as ``"uni_detect"`` in :mod:`unidetect.algorithms`.

    Construct with a :class:`~unidetect.config.UniDetectConfig` pointing at a
    Unity Catalog location whose corpus statistics have already been built,
    e.g. ``get_algorithm("uni_detect", config)``.
    """

    name = "uni_detect"

    def __init__(self, config: UniDetectConfig, spark: SparkSession | None = None) -> None:
        from unidetect.pipeline import UniDetect

        self.config = config
        self._pipeline = UniDetect(config, spark=spark)

    def detect(
        self,
        data: Sequence[str],
        *,
        table_id: str = "table",
        error_types: Sequence[ErrorType] | None = None,
        **kwargs: Any,
    ) -> AlgorithmResult:
        """Score the Unity Catalog tables named in ``data``.

        ``table_id`` is ignored -- Uni-Detect can score several tables in one
        call, and each result cell already carries its own source
        ``table_id``. A detection spanning multiple columns and/or rows (a
        functional-dependency violation, a duplicate-value group) is
        expanded into one :class:`~unidetect.algorithms.base.CellResult` per
        (column, row) it covers, all sharing the same evidence.
        """
        spark_result = self._pipeline.detect(list(data), error_types=error_types)
        cells: list[CellResult] = []
        for row in spark_result.collect():
            evidence = {
                "lr_ratio": row["lr_ratio"],
                "support": row["support"],
                "error_type": row["error_type"],
                "evidence_json": row["evidence_json"],
            }
            for column_name in row["column_names"] or ():
                for row_id in row["row_ids"] or (None,):
                    cells.append(
                        CellResult(
                            table_id=row["table_id"],
                            row_index=row_id,
                            column_name=column_name,
                            algorithm=self.name,
                            is_error=bool(row["is_significant"]),
                            score=float(row["surprisal"]),
                            evidence=evidence,
                        )
                    )
        return AlgorithmResult(algorithm=self.name, cells=tuple(cells))
