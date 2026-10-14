"""Verify the ``spark`` marker is auto-applied by ``tests/conftest.py``."""

from __future__ import annotations

from pathlib import Path

import pytest

pytest_plugins = ["pytester"]

_CONFTEST = Path(__file__).with_name("conftest.py")

# Stubs replace the real session-scoped ``spark`` fixture so no JVM is started;
# ``uc_location`` still comes from the real conftest and depends on ``spark``.
_SAMPLE_TESTS = """
import pytest

@pytest.fixture(scope="session")
def spark():
    return object()

def test_direct(spark):
    pass

def test_transitive(uc_location):
    pass

def test_plain():
    pass
"""


@pytest.fixture
def sample(pytester: pytest.Pytester) -> pytest.Pytester:
    pytester.makeconftest(_CONFTEST.read_text())
    pytester.makepyfile(test_sample=_SAMPLE_TESTS)
    return pytester


def test_spark_marker_applied_to_direct_and_transitive_users(sample: pytest.Pytester) -> None:
    result = sample.runpytest("-m", "spark", "-v")
    result.assert_outcomes(passed=2)
    result.stdout.fnmatch_lines(["*test_direct*PASSED*", "*test_transitive*PASSED*"])
    result.stdout.no_fnmatch_line("*test_plain*")


def test_spark_marker_not_applied_to_plain_tests(sample: pytest.Pytester) -> None:
    result = sample.runpytest("-m", "not spark", "-v")
    result.assert_outcomes(passed=1)
    result.stdout.fnmatch_lines(["*test_plain*PASSED*"])
