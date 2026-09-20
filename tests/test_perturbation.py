"""Unit tests for perturbation.py: the (before, after) metric readings that
feed the likelihood-ratio test.
"""

from __future__ import annotations

import pytest

from unidetect.perturbation import (
    perturb_functional_dependency,
    perturb_numeric_outlier,
    perturb_spelling,
    perturb_uniqueness,
)


class TestPerturbUniqueness:
    def test_paper_example_2(self):
        values = [f"id{i}" for i in range(98)] + ["dup", "dup"]
        outcome = perturb_uniqueness(values, epsilon=0.01)
        assert outcome.theta_before == pytest.approx(0.99)
        assert outcome.theta_after == pytest.approx(1.0)
        assert len(outcome.dropped_indices) == 1

    def test_no_duplicates_drops_nothing(self):
        outcome = perturb_uniqueness(["a", "b", "c", "d", "e"], epsilon=0.5)
        assert outcome.dropped_indices == ()
        assert outcome.theta_before == outcome.theta_after == 1.0


class TestPerturbNumericOutlier:
    def test_c_minus_drops_top_outlier_and_ratio_falls(self):
        c_minus = [43, 22, 9, 5, 0.76, 0.32, 0.30]
        outcome = perturb_numeric_outlier(c_minus, epsilon=0.5)
        assert outcome.theta_before == pytest.approx(8.1, abs=0.02)
        # Paper: removing "43" drops max-MAD to 7.4
        assert outcome.theta_after == pytest.approx(7.4, abs=0.1)
        assert outcome.evidence["outlier_value"] == pytest.approx(43.0)

    def test_c_plus_drops_the_true_outlier_more_dramatically(self):
        c_plus = [8011, 8.716, 9954, 11895, 13329, 11352, 11709]
        outcome = perturb_numeric_outlier(c_plus, epsilon=0.5)
        assert outcome.theta_before == pytest.approx(8.1, abs=0.02)
        # Paper: removing "8.716" drops max-MAD to 3.5
        assert outcome.theta_after == pytest.approx(3.5, abs=0.2)
        assert outcome.evidence["outlier_value"] == pytest.approx(8.716)

    def test_c_plus_after_is_lower_than_c_minus_after(self):
        # This is the crux of the paper's argument: even though before-scores
        # are identical, the *after* perturbation scores tell them apart.
        c_minus = [43, 22, 9, 5, 0.76, 0.32, 0.30]
        c_plus = [8011, 8.716, 9954, 11895, 13329, 11352, 11709]
        after_minus = perturb_numeric_outlier(c_minus, epsilon=0.5).theta_after
        after_plus = perturb_numeric_outlier(c_plus, epsilon=0.5).theta_after
        assert after_plus < after_minus


class TestPerturbSpelling:
    def test_paper_example_1(self):
        column = ["Kevin Doeling", "Kevin Dowling", "Alan Myerson", "Rob Morrow"]
        outcome = perturb_spelling(column, epsilon=0.5)
        assert outcome.theta_before == 1.0
        assert outcome.theta_after > outcome.theta_before
        assert set(outcome.evidence["pair"]) == {"Kevin Doeling", "Kevin Dowling"}

    def test_undefined_after_when_remaining_values_have_no_comparable_blocks(self):
        # One close pair (found via blocking) plus enough uniquely-blocked
        # values that, once the pair's first value is dropped, no block has
        # >= 2 members and the remainder exceeds max_block_size -- forcing
        # the internal re-scoring call to raise ValueError, which
        # perturb_spelling must translate into the "undefined after" sentinel.
        values = ["aa000", "aa001", "bb1", "cc22", "dd333", "ee4444", "ff55555"]
        outcome = perturb_spelling(values, epsilon=0.5, max_block_size=3)
        assert outcome.theta_before == 1.0
        assert outcome.theta_after == pytest.approx(1.0e9)


class TestPerturbFunctionalDependency:
    def test_repairs_minority_violation(self):
        lhs = ["1", "1", "2", "2", "3", "3"]
        rhs = ["x", "x", "y", "y", "z", "w"]
        outcome = perturb_functional_dependency(lhs, rhs, epsilon=0.5)
        assert outcome.theta_before == pytest.approx(4 / 6)
        assert outcome.theta_after == pytest.approx(1.0)
        assert outcome.dropped_indices == (5,)

    def test_no_violation_drops_nothing(self):
        lhs = ["1", "1", "2", "2"]
        rhs = ["x", "x", "y", "y"]
        outcome = perturb_functional_dependency(lhs, rhs, epsilon=0.5)
        assert outcome.dropped_indices == ()
        assert outcome.theta_before == outcome.theta_after == 1.0
