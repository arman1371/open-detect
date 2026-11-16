---
name: project_ope89_cache_lifecycle
description: OPE-89 fix implementation status and next steps
metadata:
  type: project
---

# OPE-89: Fix Spark Cache Lifecycle in Uni-Detect

## Status
✅ **Implementation complete** - All tests pass (37 passed, 8 skipped without Spark)
✅ **PR #102 created and ready for review**

## Progress

### Completed Work
1. **Core Fix**: Fixed cache lifecycle in `BaseDetector.detect()` and `pipeline.UniDetect.detect()`:
   - `detect()` persists candidates with `MEMORY_AND_DISK` and returns persisted result
   - Added `release()` method on `BaseDetector` and `UniDetect` to free cached frames
   - Per-detector `orderBy("lr_ratio")` removed (redundant with global sort)
   - Empty-candidates early return also persists/unpersists

2. **Validation Fix**: Fixed `_check_expected_type` in `validation.py`:
   - Uses `get_origin()` to handle parameterized `Sequence[str]` in isinstance checks
   - Restored missing test cases for parameterized and bare Sequence types

3. **Test Coverage**: Added comprehensive cache-lifecycle tests:
   - Pure-Python tests for cache contract (persist/unpersist behavior)
   - Spark-backed tests (skipped without Java) to verify no re-execution

4. **PR Created**: PR #102 created with 42 commits, 10,226 additions, 533 deletions
   - 3 existing comments on the PR
   - Merge state: "dirty" (due to uncommitted graphify output files)

### Related Work
- OPE-86: Merged (PR #99 on main)
- OPE-87: Baseline merged (PR #80 on main)

## Blockers
- None - Implementation is complete

## Next Steps
1. ✅ PR #102 created - ready for CodeReviewer review
2. Assign to CodeReviewer for code review
3. Merge PR to main branch after approval

## Related Issues
- OPE-87: Baseline: benchmark timings, Spark job counts, detections snapshot (merged)
- OPE-86: StringDtype and list-like nulls (merged)
- OPE-81: Tighten tooling: strict mypy + extended ruff rules
- OPE-83: Raha labeler correctness
- OPE-86 distinct verdicts (merged)