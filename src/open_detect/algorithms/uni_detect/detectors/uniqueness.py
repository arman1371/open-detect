"""Uniqueness-violation detector (paper Section 3.3)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.detectors.base import BaseDetector, make_evidence_json
from open_detect.algorithms.uni_detect.detectors.schema import CANDIDATE_SCHEMA
from open_detect.algorithms.uni_detect.failures import FailureCounts
from open_detect.algorithms.uni_detect.featurization import build_uniqueness_bucket
from open_detect.algorithms.uni_detect.perturbation import perturb_uniqueness
from open_detect.algorithms.uni_detect.strategies import get_spec
from open_detect.core.enums import ErrorType

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame

    from open_detect.algorithms.uni_detect.config import UniDetectConfig


def _score_column(
    vals, row_ids, num_rows, column_index, token_document_frequency, cfg: UniDetectConfig
):
    """Return ``(outcome, bucket)``, or ``None`` when there is nothing to flag."""
    outcome = perturb_uniqueness(vals, epsilon=cfg.epsilon, row_ids=row_ids)
    if not outcome.dropped_indices:
        return None
    bucket = build_uniqueness_bucket(
        values=vals,
        num_rows=num_rows,
        column_index=column_index,
        token_document_frequency=token_document_frequency,
        row_count_edges=cfg.row_count_edges,
        prevalence_edges=cfg.prevalence_edges,
    )
    return outcome, bucket


def _candidate_row(tid, col, vals, row_ids, outcome, bucket) -> dict:
    value_by_row = dict(zip(row_ids, vals, strict=True))
    return {
        "candidate_id": f"{tid}::{col}::uniqueness",
        "table_id": tid,
        "column_names": [col],
        "row_ids": [str(i) for i in outcome.dropped_indices],
        "feature_bucket": bucket.as_key(),
        "theta_before": outcome.theta_before,
        "theta_after": outcome.theta_after,
        "evidence_json": make_evidence_json(
            {
                "duplicate_values": [value_by_row[i] for i in outcome.dropped_indices][:10],
                **outcome.evidence,
            }
        ),
    }


class UniquenessDetector(BaseDetector):
    error_type = ErrorType.UNIQUENESS

    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        import pandas as pd

        cfg = self.config
        token_map = self.store.load_token_stats_map()
        broadcast_tdf = self.spark.sparkContext.broadcast(token_map)
        min_rows = get_spec(self.error_type).min_rows
        tracker = self._new_failure_tracker()

        def compute(batches):
            tdf = broadcast_tdf.value
            for batch in batches:
                counts = FailureCounts()
                rows: list[dict] = []
                for tid, col, idx, n, vals, rids in zip(
                    batch["table_id"],
                    batch["column_name"],
                    batch["column_index"],
                    batch["num_rows"],
                    batch["values"],
                    batch["row_ids"],
                    strict=True,
                ):
                    vals, rids = list(vals), [int(r) for r in rids]
                    if len(vals) < min_rows:
                        continue
                    scored = counts.attempt(
                        _score_column, vals, rids, int(n), int(idx), tdf, cfg
                    )
                    if scored is None:
                        continue
                    outcome, bucket = scored
                    rows.append(_candidate_row(tid, col, vals, rids, outcome, bucket))
                tracker.flush(counts)
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        columns_df = self.ingestor.ingest_columns(table_names, include_row_ids=True)
        return columns_df.select(
            "table_id", "column_name", "column_index", "num_rows", "values", "row_ids"
        ).mapInPandas(compute, schema=CANDIDATE_SCHEMA)
