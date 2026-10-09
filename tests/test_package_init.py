"""Unit tests for the top-level package's lazy ``__getattr__`` (no Spark required)."""

from __future__ import annotations

import pytest

import open_detect


def test_lazy_import_resolves_open_detect_class():
    from open_detect.pipeline import UniDetect

    assert open_detect.UniDetect is UniDetect


def test_lazy_import_resolves_algorithm_registry_functions():
    from open_detect.algorithms import get_algorithm, list_algorithms

    assert open_detect.get_algorithm is get_algorithm
    assert open_detect.list_algorithms is list_algorithms


def test_lazy_import_raises_for_unknown_attribute():
    with pytest.raises(AttributeError, match="unknown_attribute"):
        _ = open_detect.unknown_attribute
