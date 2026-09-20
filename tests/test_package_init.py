"""Unit tests for the top-level package's lazy ``__getattr__`` (no Spark required)."""

from __future__ import annotations

import pytest

import unidetect


def test_lazy_import_resolves_unidetect_class():
    from unidetect.pipeline import UniDetect

    assert unidetect.UniDetect is UniDetect


def test_lazy_import_raises_for_unknown_attribute():
    with pytest.raises(AttributeError, match="unknown_attribute"):
        _ = unidetect.unknown_attribute
