"""Uniqueness-violation detector (paper Section 3.3)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from unidetect.core.enums import ErrorType
from unidetect.detectors.base import BaseDetector
from unidetect.detectors.schema import CANDIDATE_SCHEMA

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame


class UniquenessDetector(BaseDetector):
    error_type = ErrorType.UNIQUENESS

    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        import pandas as pd

        cfg = self.config
        token_map = self.store.load_token_stats_map()
        broadcast_tdf = self.spark.sparkContext.broadcast(token_map)
        min_rows = 5

        def compute(batches):
            from unidetect.detectors.base import make_evidence_json
            from unidetect.featurization import build_uniqueness_bucket
            from unidetect.perturbation import perturb_uniqueness

            tdf = broadcast_tdf.value
            for batch in batches:
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
                    try:
                        outcome = perturb_uniqueness(vals, epsilon=cfg.epsilon)
                        if not outcome.dropped_indices:
                            continue
                        bucket = build_uniqueness_bucket(
                            values=vals,
                            num_rows=int(n),
                            column_index=int(idx),
                            token_document_frequency=tdf,
                            row_count_edges=cfg.row_count_edges,
                            prevalence_edges=cfg.prevalence_edges,
                        )
                    except Exception:  # noqa: BLE001
                        continue

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
                                }
                            ),
                        }
                    )
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        columns_df = self.ingestor.ingest_columns(table_names)
        return columns_df.select(
            "table_id", "column_name", "column_index", "num_rows", "values"
        ).mapInPandas(compute, schema=CANDIDATE_SCHEMA)
