# CHANGELOG

<!-- version list -->

## Unreleased

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
