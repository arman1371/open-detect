"""Unit tests for algorithms/uni_detect_algorithm.py (the adapter, not the pipeline).

``UniDetect.detect`` itself (the Spark pipeline) is already covered by
``test_corpus_and_detectors.py``; this module mocks it out -- the same
pattern ``test_run_detection_job.py`` uses -- since all the adapter owns is
flattening Uni-Detect's Spark output rows into the shared
:class:`~unidetect.algorithms.base.AlgorithmResult` schema.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from unidetect.algorithms import get_algorithm
from unidetect.algorithms.uni_detect_algorithm import UniDetectAlgorithm
from unidetect.config import UniDetectConfig, UnityCatalogLocation


def _config() -> UniDetectConfig:
    return UniDetectConfig(location=UnityCatalogLocation(catalog="main", schema="dq"))


def _row(**kwargs):
    # A plain dict already supports the bracket access UniDetectAlgorithm
    # uses on a pyspark Row (`row["column_names"]`).
    return kwargs


class TestUniDetectAlgorithm:
    def test_flattens_multi_column_multi_row_detection(self):
        with patch("unidetect.pipeline.UniDetect") as mock_cls:
            mock_pipeline = mock_cls.return_value
            mock_pipeline.detect.return_value.collect.return_value = [
                _row(
                    table_id="main.sales.orders",
                    column_names=["customer_id", "customer_name"],
                    row_ids=["1", "2"],
                    lr_ratio=0.01,
                    surprisal=4.6,
                    is_significant=True,
                    support=100,
                    error_type="functional_dependency",
                    evidence_json="{}",
                )
            ]
            algo = UniDetectAlgorithm(_config(), spark=MagicMock())
            result = algo.detect(["main.sales.orders"])

        assert len(result) == 4  # 2 columns x 2 row ids, cross product
        assert {c.column_name for c in result} == {"customer_id", "customer_name"}
        assert {c.row_index for c in result} == {"1", "2"}
        assert all(c.table_id == "main.sales.orders" for c in result)
        assert all(c.algorithm == "uni_detect" for c in result)
        assert all(c.is_error for c in result)
        assert all(c.score == 4.6 for c in result)
        assert all(c.evidence["lr_ratio"] == 0.01 for c in result)

    def test_single_column_single_row_detection(self):
        with patch("unidetect.pipeline.UniDetect") as mock_cls:
            mock_pipeline = mock_cls.return_value
            mock_pipeline.detect.return_value.collect.return_value = [
                _row(
                    table_id="t",
                    column_names=["amount"],
                    row_ids=["42"],
                    lr_ratio=0.2,
                    surprisal=1.6,
                    is_significant=False,
                    support=10,
                    error_type="numeric_outlier",
                    evidence_json="{}",
                )
            ]
            algo = UniDetectAlgorithm(_config(), spark=MagicMock())
            result = algo.detect(["t"])

        assert len(result) == 1
        cell = result.cells[0]
        assert cell.column_name == "amount"
        assert cell.row_index == "42"
        assert cell.is_error is False

    def test_registered_under_uni_detect(self):
        with patch("unidetect.pipeline.UniDetect"):
            algo = get_algorithm("uni_detect", _config(), MagicMock())
        assert isinstance(algo, UniDetectAlgorithm)
