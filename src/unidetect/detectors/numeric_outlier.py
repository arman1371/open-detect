"""Numeric-outlier detector (paper Section 3.1)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from unidetect.core.enums import ErrorType
from unidetect.detectors.base import BaseDetector
from unidetect.detectors.schema import CANDIDATE_SCHEMA

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame


class NumericOutlierDetector(BaseDetector):
    error_type = ErrorType.NUMERIC_OUTLIER

    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        import pandas as pd

        cfg = self.config
        min_rows = 5

        def compute(batches):
            from unidetect.detectors.base import make_evidence_json
            from unidetect.featurization import build_outlier_bucket
            from unidetect.perturbation import perturb_numeric_outlier

            for batch in batches:
                rows: list[dict] = []
                for tid, col, n, vals in zip(
                    batch["table_id"],
                    batch["column_name"],
                    batch["num_rows"],
                    batch["values"],
                    strict=True,
                ):
                    numeric_vals: list[float] = []
                    original_index_map: list[int] = []
                    for i, v in enumerate(vals):
                        if v is None:
                            continue
                        try:
                            numeric_vals.append(float(v))
                            original_index_map.append(i)
                        except (TypeError, ValueError):
                            continue
                    if len(numeric_vals) < min_rows:
                        continue
                    try:
                        outcome = perturb_numeric_outlier(numeric_vals, epsilon=cfg.epsilon)
                        bucket = build_outlier_bucket(
                            values=numeric_vals,
                            num_rows=int(n),
                            row_count_edges=cfg.row_count_edges,
                        )
                    except Exception:  # noqa: BLE001
                        continue

                    dropped_original = [original_index_map[i] for i in outcome.dropped_indices]
                    rows.append(
                        {
                            "candidate_id": f"{tid}::{col}::outlier",
                            "table_id": tid,
                            "column_names": [col],
                            "row_ids": [str(i) for i in dropped_original],
                            "feature_bucket": bucket.as_key(),
                            "theta_before": outcome.theta_before,
                            "theta_after": outcome.theta_after,
                            "evidence_json": make_evidence_json(outcome.evidence),
                        }
                    )
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        columns_df = self.ingestor.ingest_columns(table_names)
        return columns_df.select("table_id", "column_name", "num_rows", "values").mapInPandas(
            compute, schema=CANDIDATE_SCHEMA
        )
