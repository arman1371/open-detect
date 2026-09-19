"""Unit tests for strategies.py (no Spark required)."""

from __future__ import annotations

from unidetect.core.enums import ComparisonDirection, ErrorType
from unidetect.strategies import all_specs, get_spec


class TestGetSpec:
    def test_uniqueness_is_increasing(self):
        spec = get_spec(ErrorType.UNIQUENESS)
        assert spec.error_type is ErrorType.UNIQUENESS
        assert spec.direction is ComparisonDirection.INCREASING
        assert spec.min_rows == 5

    def test_functional_dependency_is_increasing(self):
        spec = get_spec(ErrorType.FUNCTIONAL_DEPENDENCY)
        assert spec.direction is ComparisonDirection.INCREASING

    def test_numeric_outlier_is_decreasing(self):
        spec = get_spec(ErrorType.NUMERIC_OUTLIER)
        assert spec.direction is ComparisonDirection.DECREASING

    def test_spelling_is_increasing(self):
        spec = get_spec(ErrorType.SPELLING)
        assert spec.direction is ComparisonDirection.INCREASING
        assert spec.min_rows == 3

    def test_every_spec_has_a_description(self):
        for error_type in ErrorType:
            assert get_spec(error_type).description


class TestAllSpecs:
    def test_returns_one_spec_per_error_type(self):
        specs = all_specs()
        assert len(specs) == len(ErrorType)
        assert {s.error_type for s in specs} == set(ErrorType)

    def test_returns_a_tuple(self):
        assert isinstance(all_specs(), tuple)
