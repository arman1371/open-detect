"""Benchmark infrastructure shared across benchmarks.

This package makes the ``benchmarks/common/`` module importable from tests and
other code outside the benchmarks directory (e.g., test_cache_lifecycle.py
which does ``sys.path.insert(0, str(benchmarks_dir))`` and then imports
``benchmarks.common.spark_jobs``).
"""
