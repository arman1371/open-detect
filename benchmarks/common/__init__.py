"""Shared infrastructure for every benchmark under ``benchmarks/``.

This package exists so that adding a new benchmark (see
``benchmarks/real_world_gov/`` for the second one, after
``benchmarks/wiki_subset/``) means writing the benchmark-specific data and
scoring logic only -- the local-Spark-session bootstrap, confusion-matrix
math, and Markdown/SVG report rendering are all one implementation shared by
every benchmark, not copy-pasted per benchmark.

A new benchmark typically needs:

- ``data/`` (or an equivalent) with its corpus/eval inputs.
- ``run_benchmark.py`` using :func:`common.spark_session.spark_session` and
  :func:`common.metrics.confusion_metrics`, writing a results JSON shaped
  like ``{"generated_at", "git_commit", "dataset", ..., "metrics": {...}}``.
- ``generate_report.py`` using :mod:`common.charts` to render that JSON as
  ``results/REPORT.md`` + ``results/charts/*.svg``.
- A ``results/`` directory with a checked-in ``baseline.json``.

See ``benchmarks/README.md`` for the full list of benchmarks and how they
relate to each other.
"""
