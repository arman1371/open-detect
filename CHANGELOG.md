# CHANGELOG

<!-- version list -->

## v0.2.7 (2026-10-18)

### Bug Fixes

- **uni-detect**: SpellingDetector reports original row positions (OPE-104)
  ([#48](https://github.com/arman1371/open-detect/pull/48),
  [`cc66bea`](https://github.com/arman1371/open-detect/commit/cc66beaaca976e13c0568ec4e6479c9b1c2f97aa))

### Documentation

- Fix ARCHITECTURE.md drift (S-M6) ([#21](https://github.com/arman1371/open-detect/pull/21),
  [`8ae637b`](https://github.com/arman1371/open-detect/commit/8ae637bf48873c5f5de6ab09ab601c6489b86520))

### Refactoring

- Hygiene batch for logging, asserts, evidence, plugins, pytest config (OPE-79)
  ([`5fa6346`](https://github.com/arman1371/open-detect/commit/5fa6346941941d233add062dcd2a9c116294c6cf))

- Unify library errors under OpenDetectError (ValidationError et al.) (OPE-75)
  ([#27](https://github.com/arman1371/open-detect/pull/27),
  [`3052b58`](https://github.com/arman1371/open-detect/commit/3052b589fa6f899f456e8fe0bb9b3873f7e759ae))

---

**Full Changelog**: [v0.2.6...v0.2.7](https://github.com/arman1371/open-detect/compare/v0.2.6...v0.2.7)


## v0.2.6 (2026-10-15)

### Bug Fixes

- **auto_validate**: Drift check against full vertical-cut pattern list (BUG-9)
  ([#26](https://github.com/arman1371/open-detect/pull/26),
  [`8899b60`](https://github.com/arman1371/open-detect/commit/8899b6047d819878694d107f1c0b5f7770481093))

---

**Full Changelog**: [v0.2.5...v0.2.6](https://github.com/arman1371/open-detect/compare/v0.2.5...v0.2.6)


## v0.2.5 (2026-10-15)

### Bug Fixes

- **uni-detect**: Spelling MPD dedupe, numeric non-finite handling, MPD blocking (OPE-71)
  ([#30](https://github.com/arman1371/open-detect/pull/30),
  [`1862498`](https://github.com/arman1371/open-detect/commit/1862498fb9ebdfd0ad43ac324bca1cb05ca49449))

---

**Full Changelog**: [v0.2.4...v0.2.5](https://github.com/arman1371/open-detect/compare/v0.2.4...v0.2.5)


## v0.2.4 (2026-10-15)

### Bug Fixes

- **auto-validate**: Rewrite FMDV-V segment DP, coarse signature, ceil off-by-one
  ([#28](https://github.com/arman1371/open-detect/pull/28),
  [`e5bcac1`](https://github.com/arman1371/open-detect/commit/e5bcac1c810f7c05ee5295587ed1dd4bc3c30bb9))

---

**Full Changelog**: [v0.2.3...v0.2.4](https://github.com/arman1371/open-detect/compare/v0.2.3...v0.2.4)


## v0.2.3 (2026-10-15)

### Bug Fixes

- **uni-detect**: Corpus FD pairs, null alignment and min_rows gating (OPE-73)
  ([#32](https://github.com/arman1371/open-detect/pull/32),
  [`fedf192`](https://github.com/arman1371/open-detect/commit/fedf19211a3e84f01443761cbce4f50a7eacf07d))

---

**Full Changelog**: [v0.2.2...v0.2.3](https://github.com/arman1371/open-detect/compare/v0.2.2...v0.2.3)


## v0.2.2 (2026-10-15)

### Bug Fixes

- **uni-detect**: Config validation + persisted epsilon/bucket config (OPE-72)
  ([#24](https://github.com/arman1371/open-detect/pull/24),
  [`43e9bde`](https://github.com/arman1371/open-detect/commit/43e9bde471ac9f820906597ddfcb7c3749aacdae))

---

**Full Changelog**: [v0.2.1...v0.2.2](https://github.com/arman1371/open-detect/compare/v0.2.1...v0.2.2)


## Unreleased

- **Corpus semantics change (spelling) -- rebuild existing corpora:** `min_pairwise_edit_distance`
  now computes MPD over *distinct* values, so exact duplicates no longer land in the MPD=0 bucket
  or get flagged as misspellings (columns with fewer than two distinct values are "not
  computable"). Spelling blocking was also widened (prefix and suffix keys, shifted length
  buckets, exhaustive comparison up to `max_mpd_block_size` distinct values), so it no longer
  misses distance-1 pairs such as `apple`/`ppple`; MPD values and thetas therefore differ from
  corpora built by earlier versions. Rebuild spelling corpora (`build_corpus_statistics`).
- **Fix (numeric outliers):** NaN, +/-inf and their string forms (`"nan"`, `"inf"`, `"-Infinity"`)
  are now filtered once before scoring, in both corpus building and detection. Previously a NaN
  shifted the dropped index onto the wrong element and `inf` was accepted as data. Numeric-outlier
  corpora built from columns containing such values should be rebuilt.
- **Corpus metadata format addition:** the corpus-statistics build now records its configuration
  (`epsilon`, `laplace_smoothing`, `max_mpd_block_size`, `max_fd_column_pairs_per_table`, and all
  bucket edge tuples, as JSON) as one Delta table property per error type
  (`open_detect.build_config.<error_type>`). Detection compares it with the active
  `UniDetectConfig` and raises `ConfigurationError` listing the differing fields; set
  `allow_corpus_config_mismatch=True` (`--allow-config-mismatch` on `run_detection`) to log and
  proceed. Corpora built before this change load with a warning and are not verified; rebuild them
  to record the configuration. `laplace_smoothing` is applied at scoring time, so a difference is
  only logged.
- `run_detection` gained `--epsilon` (default `0.01`, same as the build job).
- `UniDetectConfig` now rejects `laplace_smoothing <= 0`/NaN/inf (previously `0` was accepted and
  could cause 0/0 divisions) and empty, non-finite or non-strictly-increasing bucket edges.
- **Corpus semantics change (rebuild required) — OPE-73:**
  - FD column pairs are now *ordered* (both A->B and B->A are tested). Over
    `max_fd_column_pairs_per_table` they are sampled deterministically from a hash of
    `(table, lhs name, rhs name)`, so the choice no longer depends on column order. The pair arrays
    keep only rows where both columns are non-null, so LHS/RHS values are always row-aligned
    (previously nulls were dropped independently, which misaligned or silently skipped pairs).
  - The corpus build now skips columns/pairs with fewer values than `ErrorTypeSpec.min_rows`
    (spelling 3, others 5), the same minimums the detectors use (detectors now read them from the
    spec). Previously tiny columns polluted the low-row-count buckets.
  - A column counts as numeric for the outlier corpus only if at least 80%
    (`MIN_NUMERIC_FRACTION`) of its non-null values parse as finite numbers; `nan`/`inf` never
    count. Previously two numeric-looking values in a text column were enough.
  Existing corpora built before this change should be rebuilt.

## v0.2.1 (2026-10-14)

### Bug Fixes

- Count, narrow and gate executor-side swallowed exceptions (OPE-78)
  ([#25](https://github.com/arman1371/open-detect/pull/25),
  [`6bc2c9a`](https://github.com/arman1371/open-detect/commit/6bc2c9afc4a7e31ba8b18b68be8d6d45ea7ae76d))

### Refactoring

- Derive __version__ from package metadata ([#22](https://github.com/arman1371/open-detect/pull/22),
  [`f577401`](https://github.com/arman1371/open-detect/commit/f577401ae31ee316a49a5ef8a10040541bf905fa))

- Move Uni-Detect into algorithms/uni_detect/ and mirror layout in tests
  ([#17](https://github.com/arman1371/open-detect/pull/17),
  [`1cd3cf1`](https://github.com/arman1371/open-detect/commit/1cd3cf1f8570c84568f1ff9a76fa8796ef916be2))

---

**Full Changelog**: [v0.2.0...v0.2.1](https://github.com/arman1371/open-detect/compare/v0.2.0...v0.2.1)


## v0.2.0 (2026-10-08)

Baseline release. This is the first version tracked by the automated release process;
everything before it is recorded only in the git history. Releases from `v0.3.0` onwards are
generated from [Conventional Commits](https://www.conventionalcommits.org/) by
[python-semantic-release](https://python-semantic-release.readthedocs.io/) (see
[Contributing](https://arman1371.github.io/open-detect/contributing/#commit-conventions-and-releases)).
