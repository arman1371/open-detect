"""Uniqueness-violation detector (paper Section 3.3)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.core.enums import ErrorType
from open_detect.algorithms.uni_detect.detectors.base import BaseDetector
from open_detect.algorithms.uni_detect.detectors.schema import CANDIDATE_SCHEMA
from open_detect.algorithms.uni_detect.failures import FailureCounts
from open_detect.algorithms.uni_detect.featurization import build_uniqueness_bucket
from open_detect.algorithms.uni_detect.perturbation import perturb_uniqueness
from open_detect.algorithms.uni_detect.strategies import get_spec

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame

    from open_detect.algorithms.uni_detect.config import UniDetectConfig


def _score_column(vals, num_rows, column_index, token_document_frequency, cfg: UniDetectConfig):
    """Return ``(outcome, bucket)``, or ``None`` when there is nothing to flag."""
    outcome = perturb_uniqueness(vals, epsilon=cfg.epsilon)
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
            from open_detect.algorithms.uni_detect.detectors.base import make_evidence_json

            tdf = broadcast_tdf.value
            for batch in batches:
                counts = FailureCounts()
                rows: list[dict] = []
                for tid, col, idx, n, vals in zip(
                    batch["table_id"],
                    batch["column_name"],
                    batch["column_index"],
                    batch["num_rows"],
                    batch["values"],
                    strict=True,
                ):
                    vals = list(vals)
                    if len(vals) < min_rows:
                        continue
                    scored = counts.attempt(_score_column, vals, int(n), int(idx), tdf, cfg)
                    if scored is None:
                        continue
                    outcome, bucket = scored

                    rows.append(
                        {
                            "candidate_id": f"{tid}::{col}::uniqueness",
                            "table_id": tid,
                            "column_names": [col],
                            "row_ids": [str(i) for i in outcome.dropped_indices],
                            "feature_bucket": bucket.as_key(),
                            "theta_before": outcome.theta_before,
                            "theta_after": outcome.theta_after,
                            "evidence_json": make_evidence_json(
                                {
                                    "duplicate_values": [vals[i] for i in outcome.dropped_indices][
                                        :10
                                    ],
                                    **outcome.evidence,
                                },
                                cfg.redact_evidence,
                            ),
                        }
                    )
                tracker.flush(counts)
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        columns_df = self.ingestor.ingest_columns(table_names)
        return columns_df.select(
            "table_id", "column_name", "column_index", "num_rows", "values"
        ).mapInPandas(compute, schema=CANDIDATE_SCHEMA)
