"""Spelling-error detector (paper Section 3.2)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.core.enums import ErrorType
from open_detect.algorithms.uni_detect.detectors.base import (
    BaseDetector,
    make_evidence_json,
)
from open_detect.algorithms.uni_detect.detectors.schema import CANDIDATE_SCHEMA
from open_detect.algorithms.uni_detect.failures import FailureCounts
from open_detect.algorithms.uni_detect.featurization import build_spelling_bucket
from open_detect.algorithms.uni_detect.perturbation import perturb_spelling
from open_detect.algorithms.uni_detect.strategies import get_spec

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame

    from open_detect.algorithms.uni_detect.config import UniDetectConfig


def _drop_nulls(vals: Sequence[object]) -> tuple[list[object], list[int]]:
    """Return non-null values plus each one's 0-based position in ``vals``."""
    positions = [i for i, v in enumerate(vals) if v is not None]
    return [vals[i] for i in positions], positions


def _original_row_ids(dropped_indices: Sequence[int], positions: Sequence[int]) -> list[str]:
    """Map indices into the null-dropped list back to original row ids (order preserved)."""
    return [str(positions[i]) for i in dropped_indices]


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


def _build_row(tid, col, vals, outcome, bucket, cfg: UniDetectConfig) -> dict:
    """Build one candidate row from the perturbation outcome for a column.

    Maps ``outcome.dropped_indices`` (which index into the null-dropped list) back to
    original 0-based row positions via ``_drop_nulls`` / ``_original_row_ids``.
    """
    _, orig_positions = _drop_nulls(vals)
    row_ids = _original_row_ids(outcome.dropped_indices, orig_positions)
    return {
        "candidate_id": f"{tid}::{col}::spelling::{row_ids[0]}",
        "table_id": tid,
        "column_names": [col],
        "row_ids": row_ids,
        "feature_bucket": bucket.as_key(),
        "theta_before": outcome.theta_before,
        "theta_after": outcome.theta_after,
        "evidence_json": make_evidence_json(outcome.evidence, cfg.redact_evidence),
    }


class SpellingDetector(BaseDetector):
    error_type = ErrorType.SPELLING

    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        import pandas as pd

        cfg = self.config
        min_rows = get_spec(self.error_type).min_rows
        tracker = self._new_failure_tracker()

        def compute(batches):
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
                    rows.append(_build_row(tid, col, vals, outcome, bucket, cfg))
                tracker.flush(counts)
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        columns_df = self.ingestor.ingest_columns(table_names)
        return columns_df.select("table_id", "column_name", "num_rows", "values").mapInPandas(
            compute, schema=CANDIDATE_SCHEMA
        )
