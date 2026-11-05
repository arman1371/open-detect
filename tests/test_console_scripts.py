"""Console-script entry-point contract tests.

The wheel installs four console scripts for the two Uni-Detect jobs: a primary
name and a backward-compatible alias per phase. Databricks ``python_wheel_tasks``
reference the alias names, so both names must resolve to the *same* callable
through ``importlib.metadata`` (not merely import successfully).

These tests read the installed entry-point metadata, so they only pass against
a real installed distribution -- running them from a source checkout without
installing the package first raises ``PackageNotFoundError`` (which is itself
the expected signal that the metadata is missing).
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, entry_points

PRIMARY_BUILD = "open_detect_build_corpus"
ALIAS_BUILD = "build_corpus_statistics_job"
PRIMARY_DETECT = "open_detect_run_detection"
ALIAS_DETECT = "run_detection_job"


def _console_scripts() -> dict[str, str]:
    """Map entry-point name -> target ``module:attr`` for console scripts."""
    try:
        eps = entry_points(group="console_scripts")
    except Exception as exc:  # pragma: no cover - defensive, mirrors production lookup
        raise PackageNotFoundError("open-detect") from exc
    return {ep.name: ep.value for ep in eps}


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
    assert (
        scripts[PRIMARY_BUILD]
        == "open_detect.algorithms.uni_detect.jobs.build_corpus_statistics:main"
    )
    assert scripts[PRIMARY_DETECT] == "open_detect.algorithms.uni_detect.jobs.run_detection:main"
