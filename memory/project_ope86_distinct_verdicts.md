# OPE-86: Per-distinct-value verdicts in Auto-Validate (P-10, AV part)

## Overview
Implements performance improvement: compute pattern verdict once per distinct non-null value and broadcast to every cell instead of re-running `_value_matches` per cell.

## Changes Made
- **`src/open_detect/algorithms/auto_validate/detector.py`**:
  - Added `_value_text()` — canonical text representation used by `_value_matches` for caching. Returns `None` for null values.
  - Added `_distinct_value_verdicts()` — computes `{text: is_error}` map once per distinct text representation in the series.
  - Refactored `detect()` to use the verdict cache instead of per-cell pattern matching.
  - Enhanced `_value_matches()` to handle `fmdv_vh` ordered segments (list of sequences) correctly.

## Technical Details
- **Before**: Per-cell `_value_matches` call + per-cell `pd.isna` → O(n) pattern matching
- **After**: One pass to build verdict cache (O(distinct)), then O(n) dictionary lookups
- Values like `1`, `1.0`, `True` get distinct verdicts (different string representations)
- Unhashable values (lists, dicts, numpy arrays) fall back to per-cell resolution

## Verification
- `tests/algorithms/auto_validate/` — 176 tests pass
- `tests/algorithms/auto_validate/test_ope86_distinct_verdicts.py` — 7 acceptance tests pass
- `ruff`/`black` clean on changed files
- Non-Spark test suite passes

## Related
- OPE-89: Cache lifecycle fix
- OPE-162: Verdict cache optimization
- OPE-133: GitHub lifecycle (push branch + open PR)

## Current State
- Branch `chore/ope-86-distinct-verdicts` pushed to GitHub
- PR #94 open against `main`
- All CI passing (test, lint, type-check, build, docs)
- Ready for CodeReviewer review