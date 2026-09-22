"""Unit tests for the unidetect.algorithms registry and base contract."""

from __future__ import annotations

import pytest

from unidetect.algorithms import list_algorithms, registry
from unidetect.algorithms.base import AlgorithmResult, CellResult
from unidetect.algorithms.registry import (
    UnknownAlgorithmError,
    get_algorithm,
    get_algorithm_class,
    register_lazy,
)


def test_builtin_algorithms_are_registered():
    assert {"raha", "uni_detect"} <= set(list_algorithms())


def test_unknown_algorithm_raises():
    with pytest.raises(UnknownAlgorithmError, match="unknown"):
        get_algorithm_class("unknown")


def test_get_algorithm_constructs_with_args():
    from unidetect.algorithms.raha import RahaConfig, RahaDetector

    config = RahaConfig(labeling_budget=5)
    algo = get_algorithm("raha", config)
    assert isinstance(algo, RahaDetector)
    assert algo.config.labeling_budget == 5


def test_register_lazy_overrides_existing_name():
    class Dummy:
        name = "dummy"

    register_lazy("dummy", lambda: Dummy)
    try:
        assert get_algorithm_class("dummy") is Dummy
        assert "dummy" in list_algorithms()
    finally:
        registry._registry.pop("dummy", None)


def test_register_lazy_is_lazy():
    calls = []

    def factory():
        calls.append(1)
        return object

    register_lazy("lazy_probe", factory)
    try:
        assert calls == []  # registering must not import/construct anything
        get_algorithm_class("lazy_probe")
        assert calls == [1]
    finally:
        registry._registry.pop("lazy_probe", None)


class TestAlgorithmResult:
    def test_errors_filters_to_flagged_cells(self):
        result = AlgorithmResult(
            algorithm="test",
            cells=(
                CellResult("t", 0, "a", "test", True, 0.9),
                CellResult("t", 1, "a", "test", False, 0.1),
            ),
        )
        assert result.errors() == (result.cells[0],)
        assert len(result) == 2

    def test_to_pandas_has_shared_schema(self):
        result = AlgorithmResult(
            algorithm="test", cells=(CellResult("t", 0, "a", "test", True, 0.9, {"x": 1}),)
        )
        frame = result.to_pandas()
        assert frame.loc[0, "is_error"]
        assert frame.loc[0, "evidence"] == {"x": 1}

    def test_union_combines_multiple_results(self):
        a = AlgorithmResult("a", (CellResult("t", 0, "a", "a", True, 1.0),))
        b = AlgorithmResult("b", (CellResult("t", 1, "b", "b", False, 0.0),))
        combined = AlgorithmResult.union([a, b])
        assert len(combined) == 2
        assert combined.algorithm == "ensemble"
