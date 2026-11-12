# OPE-86 / PR #96 — Copilot Review Fixes

All 5 Copilot review comments on PR #96 addressed and resolved.

## Fixes Applied

| # | File | Change |
|---|------|--------|
| 1 | `benchmarks/common/spark_session.py:_host_memory_bytes()` | Clamp cgroup-v1 unlimited sentinel to physical RAM (`min(cgroup_limit, physical_ram)`) |
| 2 | `benchmarks/common/spark_session.py:_cap_driver_memory()` | Raise `SparkUnavailable` when budget cannot support 1g minimum heap; also guard against 1g floor exceeding cgroup budget |
| 3 | `src/open_detect/algorithms/auto_validate/detector.py:_matches_segments()` | Match concatenated ordered FMDV-VH segment pattern against whole value instead of each segment against whole value |
| 4 | `src/open_detect/algorithms/auto_validate/detector.py:_value_text()` | Preserve empty string as verdict-cache key; only `None` represents actual null |
| 5 | `src/open_detect/validation.py:_validate_literal_value()` | Check `isinstance(value, str)` before Literal set membership to raise `ValidationError` instead of `TypeError` for unhashable inputs |

## Verification
- All 647 non-Spark tests pass
- Individual tests confirm each fix handles the reported edge case

## Resolution
Code fixes pushed to `chore/ope-86-distinct-verdicts-reopen`. PR #96 handed off to CodeReviewer.