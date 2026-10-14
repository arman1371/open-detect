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

## v0.2.0 (2026-10-08)

Baseline release. This is the first version tracked by the automated release process;
everything before it is recorded only in the git history. Releases from `v0.3.0` onwards are
generated from [Conventional Commits](https://www.conventionalcommits.org/) by
[python-semantic-release](https://python-semantic-release.readthedocs.io/) (see
[Contributing](https://arman1371.github.io/open-detect/contributing/#commit-conventions-and-releases)).
