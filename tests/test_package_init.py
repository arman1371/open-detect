"""Unit tests for the top-level package's lazy ``__getattr__`` (no Spark required)."""

from __future__ import annotations

import subprocess
import sys
from importlib.metadata import version

import pytest

import open_detect


def test_lazy_import_resolves_open_detect_class():
    from open_detect.algorithms.uni_detect.pipeline import UniDetect

    assert open_detect.UniDetect is UniDetect


def test_lazy_import_resolves_algorithm_registry_functions():
    from open_detect.algorithms import get_algorithm, list_algorithms

    assert open_detect.get_algorithm is get_algorithm
    assert open_detect.list_algorithms is list_algorithms


def test_lazy_import_raises_for_unknown_attribute():
    with pytest.raises(AttributeError, match="unknown_attribute"):
        _ = open_detect.unknown_attribute


def test_version_matches_installed_package_metadata():
    assert isinstance(open_detect.__version__, str)
    assert open_detect.__version__
    assert open_detect.__version__ == version("open-detect")


def test_import_open_detect_without_rapidfuzz():
    """`import open_detect` must work with rapidfuzz absent.

    `rapidfuzz` is a `uni_detect` extra, not a core dependency, and it is only
    used by :mod:`open_detect.algorithms.uni_detect.metrics.spelling`. Blocking
    the import via ``sys.modules['rapidfuzz'] = None`` simulates a core-only
    environment (the module is not installed at all) and pins the behaviour in a
    fresh interpreter so a future top-level rapidfuzz import is caught.
    """
    code = (
        "import sys\n"
        "sys.modules['rapidfuzz'] = None  # block the optional extra\n"
        "import open_detect\n"
        "assert open_detect.__version__\n"
        "from open_detect.algorithms import list_algorithms\n"
        "assert list_algorithms() == ['auto_validate', 'raha', 'uni_detect']\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
