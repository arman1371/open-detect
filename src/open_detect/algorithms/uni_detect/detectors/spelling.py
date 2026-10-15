"""Spelling-error detector (paper Section 3.2)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.detectors.base import BaseDetector
from open_detect.algorithms.uni_detect.detectors.schema import CANDIDATE_SCHEMA
from open_detect.algorithms.uni_detect.failures import FailureCounts
from open_detect.algorithms.uni_detect.featurization import build_spelling_bucket
from open_detect.algorithms.uni_detect.perturbation import perturb_spelling
from open_detect.algorithms.uni_detect.strategies import get_spec
from open_detect.core.enums import ErrorType

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame

    from open_detect.algorithms.uni_detect.config import UniDetectConfig


def _score_column(clean_vals, num_rows, cfg: UniDetectConfig):
    """Return ``(outcome, bucket)`` for one column's non-null values."""
    outcome = perturb_spelling(
        clean_vals, epsilon=cfg.epsilon, max_block_size=cfg.max_mpd_block_size
    )
    avg_len = outcome.evidence.get("avg_differing_token_length", 0.0)
    bucket = build_spelling_bucket(
        values=clean_vals,
        num_rows=num_rows,
        avg_differing_token_length=avg_len,
        row_count_edges=cfg.row_count_edges,
        token_length_edges=cfg.token_length_edges,
    )
    return outcome, bucket


class SpellingDetector(BaseDetector):
    error_type = ErrorType.SPELLING

    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        import pandas as pd

        cfg = self.config
        min_rows = get_spec(self.error_type).min_rows
        tracker = self._new_failure_tracker()

        def compute(batches):
            from open_detect.algorithms.uni_detect.detectors.base import make_evidence_json

            for batch in batches:
                counts = FailureCounts()
                rows: list[dict] = []
                for tid, col, n, vals in zip(
                    batch["table_id"],
                    batch["column_name"],
                    batch["num_rows"],
                    batch["values"],
                    strict=True,
                ):
                    clean_vals = [v for v in vals if v is not None]
                    if len(clean_vals) < min_rows:
                        continue
                    scored = counts.attempt(_score_column, clean_vals, int(n), cfg)
                    if scored is None:
                        continue
                    outcome, bucket = scored

                    rows.append(
                        {
                            "candidate_id": f"{tid}::{col}::spelling::{outcome.dropped_indices[0]}",
                            "table_id": tid,
                            "column_names": [col],
                            "row_ids": [str(i) for i in outcome.dropped_indices],
                            "feature_bucket": bucket.as_key(),
                            "theta_before": outcome.theta_before,
                            "theta_after": outcome.theta_after,
                            "evidence_json": make_evidence_json(outcome.evidence),
                        }
                    )
                tracker.flush(counts)
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        columns_df = self.ingestor.ingest_columns(table_names)
        return columns_df.select("table_id", "column_name", "num_rows", "values").mapInPandas(
            compute, schema=CANDIDATE_SCHEMA
        )
