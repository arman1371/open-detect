# OPE-86 Status - Distinct Verdicts in Auto-Validate (P-10 AV)

## Implementation Status
- ✅ **Core optimization**: `_distinct_value_verdicts()` computes pattern verdict once per distinct value and broadcasts to all cells
- ✅ **Equivalence**: All 19 acceptance tests pass, verifying output matches per-cell baseline
- ✅ **Performance**: Cache reduces `_value_matches` calls from O(n) to O(distinct values)
- ✅ **Unhashable values**: Lists/dicts fall back to per-cell resolution
- ✅ **Type safety**: mpyy check passes, ruff check passes

## Test Results
- 19/19 OPE-86 specific tests pass
- 206/206 auto_validate tests pass
- 719/750 total tests pass (31 Spark/Java skipped)

## PR Status
- **PR #99** is open against `main` 
- **Copilot review**: 3 medium-severity comments, 1 addressed (ScoringJobCounter patch restoration)
- **Remaining**: 2 comments about Arrow batch limit restoration and adapter result unpersisting

## Recent Changes
- Fixed `benchmarks/common/spark_jobs.py`: `ScoringJobCounter.scope()` now restores `CorpusStatsStore.batch_score` after each scope exits, preventing patch persistence across nested/sequential scopes

## Code Review State
- CodeReviewer assignment needed after PR cleanup
- All non-Spark unit tests pass
- Manual verification of equivalence done against per-cell baseline
