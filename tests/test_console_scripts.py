"""Console-script entry-point contract tests.

The wheel installs four console scripts for the two Uni-Detect jobs: a primary
name and a backward-compatible alias per phase. Databricks ``python_wheel_tasks``
reference the alias names, so both names must resolve to the *same* callable
through ``importlib.metadata`` (not merely import successfully).

These tests read the installed entry-point metadata, so they only pass against
a real installed distribution. Running them from a source checkout without
installing the package first raises ``PackageNotFoundError`` (which is itself
the expected signal that the metadata is missing).
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, distribution, entry_points

PRIMARY_BUILD = "open_detect_build_corpus"
ALIAS_BUILD = "build_corpus_statistics_job"
PRIMARY_DETECT = "open_detect_run_detection"
ALIAS_DETECT = "run_detection_job"

# The targets the wheel's [project.scripts] must point at.
EXPECTED_BUILD_TARGET = "open_detect.algorithms.uni_detect.jobs.build_corpus_statistics:main"
EXPECTED_DETECT_TARGET = "open_detect.algorithms.uni_detect.jobs.run_detection:main"

# Every console script we care about targets a module under this package.
_TARGET_PREFIX = "open_detect.algorithms.uni_detect.jobs."


def _console_scripts() -> dict[str, str]:
    """Map entry-point name -> target ``module:attr`` for open-detect's scripts."""
    try:
        distribution("open-detect")
    except PackageNotFoundError as exc:
        raise AssertionError(
            "open-detect is not installed; run `uv sync` or `pip install -e .` first"
        ) from exc
    # Filter to our own scripts by target prefix rather than by distribution:
    # the `dist=` filter on entry_points() is unreliable for editable installs
    # (the per-entry-point distribution reference is often unset).
    eps = entry_points(group="console_scripts")
    return {ep.name: ep.value for ep in eps if ep.value.startswith(_TARGET_PREFIX)}


def test_all_four_console_scripts_are_declared():
    scripts = _console_scripts()
    for name in (PRIMARY_BUILD, ALIAS_BUILD, PRIMARY_DETECT, ALIAS_DETECT):
        assert name in scripts, f"console script {name!r} is missing from entry-point metadata"


def test_primary_and_alias_resolve_to_identical_callables():
    scripts = _console_scripts()
    assert scripts[PRIMARY_BUILD] == scripts[ALIAS_BUILD]
    assert scripts[PRIMARY_DETECT] == scripts[ALIAS_DETECT]


def test_console_script_targets_match_pyproject():
    """The entry-point targets must point at the jobs modules' ``main`` callables."""
    scripts = _console_scripts()
    assert scripts[PRIMARY_BUILD] == EXPECTED_BUILD_TARGET
    assert scripts[PRIMARY_DETECT] == EXPECTED_DETECT_TARGET
