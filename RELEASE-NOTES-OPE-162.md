# OpenDetect — OPE-162: Verdict Cache Optimization for Auto-Validate

**Release Date**: 2026-11-18  
**Version**: v0.3.1 (included in release v0.3.0)

---

## Improvements

### Auto-Validate: Per-Distinct-Value Verdict Caching
The Auto-Validate algorithm now computes pattern verdicts once per distinct text value instead of re-evaluating every cell. This reduces the detection complexity from O(rows) to O(distinct values) for columns with repeated data — a significant speedup on real-world tables where values like email domains, status codes, or categorical labels appear many times.

**What this means for you**: Faster error detection on columns with duplicate values. The algorithm internally caches the match result for each unique text representation and broadcasts it to all matching cells.

### Empty String Handling
Empty strings (`""`) in feasible columns are now correctly treated as non-null values that fail pattern matching and are emitted as error cells. Previously, empty strings were silently skipped or misclassified. This ensures data quality issues with missing-but-not-null fields are surfaced.

### Robust Type Handling
The verdict cache correctly distinguishes between values with different string representations:
- `1` (int), `1.0` (float), and `True` (bool) each get their own cached verdict
- Nulls (`None`, `pd.NA`, `NaN`) are excluded from caching and never flagged as errors
- Unhashable values (lists, dicts) fall back to per-cell evaluation

---

## Bug Fixes

- Fixed cache invariant: `_value_matches` is now called exactly once per distinct text value
- Fixed row alignment when the input DataFrame has a non-default index
- Fixed handling of `StringDtype` columns containing `pd.NA`
- Fixed list-like nulls (`[None]`) in the verdict cache

---

## Test Coverage

Added 19 new acceptance tests in `tests/auto_validate/test_ope86_distinct_verdicts.py` covering:
- Output equivalence against the per-cell reference implementation
- Cache invariant verification
- Empty string behavior on both feasible and infeasible columns
- Non-default index row alignment
- Mixed-type columns (integers, floats, booleans, strings, emails, `None`, `pd.NA`, lists)
- `StringDtype` columns with `pd.NA`
- List-like null values
- Unhashable values with string deduplication keying

All 176 auto_validate tests and 719 non-Spark tests pass.

---

## Migration Notes

No migration required. This is a purely internal optimization — the public API and output schema are unchanged. Existing corpora and detection results remain valid.

---

## Related Work

- **OPE-86**: Complete — verdict-cache optimization implementation (PR #99, merged to main)
- **OPE-162**: Complete — auto_validate verdict cache with empty string handling (this release)
- **OPE-133**: Complete — PR #99 review and merge
- **OPE-89**: In progress — cache lifecycle management (separate PR)