## Review Complete: OPE-194 (PR #106)

**Verdict: APPROVED**

### Summary
Reviewed the fix for OPE-92 batch_score weight computation bug. All changes are correct and well-tested. Submitted approval comment on PR #106.

### Changes Verified

1. **builder.py**: `_aggregate_scored_rows` correctly computes `weight = count` (number of original corpus rows per group). Output schema uses `LongType` for weight column. Pre-aggregation at builder level: one row per corpus row with weight=1.

2. **store.py**: `batch_score` uses pre-aggregated weight with `F.sum("weight")` for numerator/denominator. `bucket_support` correctly uses `F.sum(F.col("weight")).cast("long")` (not count of groups). Candidate deduplication by `(feature_bucket, theta1, theta2)` before scoring. Left-semi join pattern to restrict corpus to relevant buckets.

3. **schema.py**: `CORPUS_STATS_SCHEMA` includes `weight` as `LongType` (non-nullable).

4. **Backward Compatibility**: `CorpusStatsBuilder.write()` backfills legacy partitions with `weight=1` using additive schema evolution. `CorpusStatsStore.load()` adds `weight=1` column for tables built before OPE-92.

5. **Tests**: 9 unit tests passing. Covers: weighted sum equivalence (INCREASING/DECREASING), bucket_support semantics, candidate deduplication, backward compatibility.

6. **CI**: Timeout increased from 30 to 60 minutes for test job.

### Test Results
- All 733 tests pass (37 skipped - Spark integration tests)
- Lint (ruff): PASS
- Type-check (mypy): Pre-existing issues only (no new issues from this PR)

### Mathematical Equivalence Verified
The fix correctly maintains mathematical equivalence:
- Builder outputs one row per corpus row with `weight=1`
- Global pre-aggregation in `batch_score` sums weights: `sum(weight) = original row count`
- Weighted LR ratio formula: `(sum(numerator_weights) + α) / (sum(denominator_weights) + α)`
- This matches the original per-row counting semantics exactly

The PR is ready to merge. This unblocks OPE-92.