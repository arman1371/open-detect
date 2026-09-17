"""Functional-dependency violation detector (paper Section 3.4)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from unidetect.core.enums import ErrorType
from unidetect.detectors.base import BaseDetector
from unidetect.detectors.schema import CANDIDATE_SCHEMA

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame


class FunctionalDependencyDetector(BaseDetector):
    error_type = ErrorType.FUNCTIONAL_DEPENDENCY

    def extract_candidates(self, table_names: Sequence[str]) -> DataFrame:
        import pandas as pd

        cfg = self.config
        token_map = self.store.load_token_stats_map()
        broadcast_tdf = self.spark.sparkContext.broadcast(token_map)
        min_rows = 5

        def compute(batches):
            from unidetect.detectors.base import make_evidence_json
            from unidetect.featurization import build_functional_dependency_bucket
            from unidetect.perturbation import perturb_functional_dependency

            tdf = broadcast_tdf.value
            for batch in batches:
                rows: list[dict] = []
                for tid, lhs_col, rhs_col, rhs_idx, n, lhs_vals, rhs_vals in zip(
                    batch["table_id"],
                    batch["lhs_column"],
                    batch["rhs_column"],
                    batch["rhs_column_index"],
                    batch["num_rows"],
                    batch["lhs_values"],
                    batch["rhs_values"],
                    strict=True,
                ):
                    lhs_vals, rhs_vals = list(lhs_vals), list(rhs_vals)
                    if len(lhs_vals) < min_rows:
                        continue
                    try:
                        outcome = perturb_functional_dependency(
                            lhs_vals, rhs_vals, epsilon=cfg.epsilon
                        )
                        if not outcome.dropped_indices:
                            continue
                        bucket = build_functional_dependency_bucket(
                            rhs_values=rhs_vals,
                            num_rows=int(n),
                            rhs_column_index=int(rhs_idx),
                            token_document_frequency=tdf,
                            row_count_edges=cfg.row_count_edges,
                            prevalence_edges=cfg.prevalence_edges,
                        )
                    except Exception:  # noqa: BLE001
                        continue

                    rows.append(
                        {
                            "candidate_id": f"{tid}::{lhs_col}->{rhs_col}::fd",
                            "table_id": tid,
                            "column_names": [lhs_col, rhs_col],
                            "row_ids": [str(i) for i in outcome.dropped_indices],
                            "feature_bucket": bucket.as_key(),
                            "theta_before": outcome.theta_before,
                            "theta_after": outcome.theta_after,
                            "evidence_json": make_evidence_json(
                                {
                                    "lhs_column": lhs_col,
                                    "rhs_column": rhs_col,
                                    "violating_examples": [
                                        (lhs_vals[i], rhs_vals[i])
                                        for i in outcome.dropped_indices[:10]
                                    ],
                                    **outcome.evidence,
                                }
                            ),
                        }
                    )
                yield pd.DataFrame(rows, columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        pairs_df = self.ingestor.ingest_column_pairs(table_names)
        return pairs_df.select(
            "table_id",
            "lhs_column",
            "rhs_column",
            "rhs_column_index",
            "num_rows",
            "lhs_values",
            "rhs_values",
        ).mapInPandas(compute, schema=CANDIDATE_SCHEMA)
