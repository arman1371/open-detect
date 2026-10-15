"""Numeric-outlier detector (paper Section 3.1)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.detectors.base import BaseDetector, make_evidence_json
from open_detect.algorithms.uni_detect.detectors.schema import CANDIDATE_SCHEMA
from open_detect.algorithms.uni_detect.failures import FailureCounts
from open_detect.algorithms.uni_detect.featurization import build_outlier_bucket
from open_detect.algorithms.uni_detect.metrics.base import require_min_size
from open_detect.algorithms.uni_detect.metrics.outliers import finite_floats
from open_detect.algorithms.uni_detect.perturbation import perturb_numeric_outlier
from open_detect.algorithms.uni_detect.strategies import get_spec
from open_detect.core.enums import ErrorType

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame

    from open_detect.algorithms.uni_detect.config import UniDetectConfig


def _score_column(numeric_vals, numeric_row_ids, num_rows, cfg: UniDetectConfig):
    """Return ``(outcome, bucket)`` for one column's parsed numeric values and their row ids."""
    require_min_size(numeric_vals, 2, "perturb_numeric_outlier")
    outcome = perturb_numeric_outlier(numeric_vals, epsilon=cfg.epsilon, row_ids=numeric_row_ids)
    bucket = build_outlier_bucket(
        values=numeric_vals, num_rows=num_rows, row_count_edges=cfg.row_count_edges
    )
    return outcome, bucket


def _candidate_row(tid, col, outcome, bucket) -> dict:
    return {
        "candidate_id": f"{tid}::{col}::outlier",
        "table_id": tid,
        "column_names": [col],
        "row_ids": [str(i) for i in outcome.dropped_indices],
        "feature_bucket": bucket.as_key(),
        "theta_before": outcome.theta_before,
        "theta_after": outcome.theta_after,
        "evidence_json": make_evidence_json(outcome.evidence),
    }


class NumericOutlierDetector(BaseDetector):
    error_type = ErrorType.NUMERIC_OUTLIER

    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        import pandas as pd

        cfg = self.config
        min_rows = get_spec(self.error_type).min_rows
        tracker = self._new_failure_tracker()

        def compute(batches):
            for batch in batches:
                counts = FailureCounts()
                rows: list[dict] = []
                for tid, col, n, vals, rids in zip(
                    batch["table_id"],
                    batch["column_name"],
                    batch["num_rows"],
                    batch["values"],
                    batch["row_ids"],
                    strict=True,
                ):
                    numeric_vals, positions = finite_floats(vals)
                    if len(numeric_vals) < min_rows:
                        continue
                    numeric_rids = [int(rids[p]) for p in positions]
                    scored = counts.attempt(_score_column, numeric_vals, numeric_rids, int(n), cfg)
                    if scored is None:
                        continue
                    outcome, bucket = scored
                    rows.append(_candidate_row(tid, col, outcome, bucket))
                tracker.flush(counts)
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        columns_df = self.ingestor.ingest_columns(table_names, include_row_ids=True)
        return columns_df.select(
            "table_id", "column_name", "num_rows", "values", "row_ids"
        ).mapInPandas(compute, schema=CANDIDATE_SCHEMA)
