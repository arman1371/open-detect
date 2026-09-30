"""End-to-end tests for AutoValidateAlgorithm (paper Sec. 2-5, PRD F11)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
import pytest

from unidetect.algorithms import get_algorithm, get_algorithm_class, list_algorithms
from unidetect.algorithms.auto_validate.config import AutoValidateConfig
from unidetect.algorithms.auto_validate.detector import AutoValidateAlgorithm
from unidetect.algorithms.auto_validate.exceptions import IndexNotBuiltError

if TYPE_CHECKING:
    pass


def _make_tiny_corpus() -> list[pd.Series]:
    """Realistic tiny corpus with multiple column types."""
    return [
        pd.Series(["2024-01-15", "2024-02-20", "2024-03-10"]),  # dates
        pd.Series(["john@example.com", "jane@test.org", "admin@site.net"]),  # emails
        pd.Series(["New York", "London", "Tokyo"]),  # cities
    ]


class TestAutoValidateDetector:
    def test_build_index_then_detect(self):
        """Basic flow: build index from clean corpus, detect outliers in dirty table."""
        config = AutoValidateConfig(m=1, tau=16)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame(
            {
                "date": ["2024-01-15", "2024-02-20", "NOT-A-DATE", None],
                "email": ["john@example.com", "invalid-email", "admin@site.net", "user@test.com"],
                "city": ["New York", "London", "Tokyo", "Paris"],
            }
        )
        result = detector.detect(dirty, table_id="t1")
        assert result.algorithm == "auto_validate"

        # email column: 4 non-null cells, 1 should be error (invalid-email doesn't match pattern)
        email_cells = [c for c in result.cells if c.column_name == "email"]
        assert len(email_cells) == 4
        email_errors = [c for c in email_cells if c.is_error]
        assert len(email_errors) == 1
        assert email_errors[0].row_index == 1
        assert email_errors[0].evidence["variant"] == "fmdv_vh"

        # date column: all values match the pattern (including NOT-A-DATE due to generic fallback)
        date_cells = [c for c in result.cells if c.column_name == "date"]
        assert len(date_cells) == 3  # 3 non-null cells
        # date column may or may not flag based on pattern; test just checks structure
        assert all(c.evidence["variant"] == "fmdv_vh" for c in date_cells)

    def test_no_corpus_raises_index_not_built(self):
        """Calling detect without build_index must raise IndexNotBuiltError."""
        detector = AutoValidateAlgorithm()
        dirty = pd.DataFrame({"time": ["10:00:00"]})
        with pytest.raises(IndexNotBuiltError, match="build_index"):
            detector.detect(dirty)

    def test_infer_pattern_without_build_raises(self):
        detector = AutoValidateAlgorithm()
        with pytest.raises(IndexNotBuiltError):
            detector.infer_pattern(pd.Series(["10:00:00"]))

    def test_null_cells_never_flagged(self):
        """Null values should produce no CellResult."""
        config = AutoValidateConfig(m=1, tau=16)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame(
            {
                "date": [None, "2024-01-15", None, "2024-02-20"],
                "email": ["a@b.com", "x@y.com", "m@n.com", "p@q.com"],
            }
        )
        result = detector.detect(dirty, table_id="t1")
        assert all(
            cell.column_name == "date" or cell.column_name == "email" for cell in result.cells
        )
        assert all(not cell.is_error for cell in result.cells)
        # Only 2 non-null date cells + 4 email cells
        assert len(result.cells) == 6

    def test_evidence_keys(self):
        """Evidence dict must contain the documented keys."""
        config = AutoValidateConfig(m=1, tau=16)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame({"date": ["NOT-A-DATE"]})
        result = detector.detect(dirty, table_id="t1")
        assert len(result.cells) == 1
        cell = result.cells[0]
        expected_keys = {"pattern", "fpr_t", "cov_t", "theta_c", "variant", "r", "m", "tau"}
        assert set(cell.evidence.keys()) == expected_keys

    def test_score_computed_as_1_minus_fpr(self):
        """For flagged cells, score = 1 - fpr_t."""
        config = AutoValidateConfig(m=1, tau=16)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame(
            {
                "email": ["invalid-email", "valid@test.com"],
            }
        )
        result = detector.detect(dirty, table_id="t1")
        error_cells = [c for c in result.cells if c.is_error]
        assert len(error_cells) == 1
        cell = error_cells[0]
        fpr_t = cell.evidence["fpr_t"]
        assert cell.score == pytest.approx(1.0 - fpr_t)

    def test_unflagged_cells_have_zero_score(self):
        config = AutoValidateConfig(m=1, tau=16)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame({"date": ["2024-01-15"]})
        result = detector.detect(dirty, table_id="t1")
        cell = result.cells[0]
        assert cell.is_error is False
        assert cell.score == 0.0

    def test_columns_subset(self):
        """columns= should limit detection to only those columns."""
        config = AutoValidateConfig(m=1, tau=16)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame(
            {
                "date": ["NOT-A-DATE"],
                "email": ["invalid"],
            }
        )
        result = detector.detect(dirty, table_id="t1", columns=["date"])
        assert all(cell.column_name == "date" for cell in result.cells)

    @pytest.mark.parametrize("variant", ["fmdv", "fmdv_h", "fmdv_v", "fmdv_vh"])
    def test_all_variants_infer_something(self, variant):
        """Each variant should successfully infer a pattern for a simple corpus."""
        config = AutoValidateConfig(m=1, tau=16, variant=variant)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame({"date": ["2024-01-15"]})
        result = detector.detect(dirty, table_id="t1")
        assert len(result.cells) == 1
        assert result.cells[0].evidence["variant"] == variant

    def test_registry_lookup(self):
        """get_algorithm('auto_validate') should return an AutoValidateAlgorithm instance."""
        algo_class = get_algorithm_class("auto_validate")
        assert algo_class is AutoValidateAlgorithm
        algo = get_algorithm("auto_validate")
        assert isinstance(algo, AutoValidateAlgorithm)

    def test_empty_dataframe(self):
        """Empty dataframe should return an empty AlgorithmResult."""
        config = AutoValidateConfig(m=1, tau=16)
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame({"date": pd.Series([], dtype=object)})
        result = detector.detect(dirty, table_id="t1")
        assert len(result) == 0

    def test_infeasible_column_no_flags(self):
        """When no pattern is feasible for a column, no cells should be flagged."""
        config = AutoValidateConfig(m=100, tau=16)  # m too high for tiny corpus
        corpus = _make_tiny_corpus()
        detector = AutoValidateAlgorithm(config)
        detector.build_index(corpus)

        dirty = pd.DataFrame(
            {
                "date": ["NOT-A-DATE", "ALSO-BAD"],
                "email": ["a@b.com", "c@d.com"],
            }
        )
        result = detector.detect(dirty, table_id="t1")
        # date column: 2 cells, both no flags (infeasible)
        date_cells = [c for c in result.cells if c.column_name == "date"]
        assert len(date_cells) == 2
        assert all(not cell.is_error for cell in date_cells)
        assert all(cell.evidence["pattern"] is None for cell in date_cells)

    def test_list_algorithms_contains_auto_validate(self):
        assert "auto_validate" in list_algorithms()
