# Auto-Validate Architecture

Song & He, SIGMOD 2021.

## Code map

| Algorithm / Eqn | Paper section | Code |
|---|---|---|
| Generalization hierarchy, tokenizer | Sec 2.1 | `hierarchy.py` (`tokenize`, `matches`, `generalize`, `token_count`, `generality_weight`) |
| `P(v)`, Algorithm 1 (GeneratePatterns) | Sec 2.1, Alg 1 | `patterns.py` (`iter_patterns`, `patterns_of`, `sorted_patterns`) |
| Impurity `Imp_D(h)` (Eqn 1), FPR_D = Imp_D (Eqns 2-3) | Sec 2.4, Def 1, 2, 3 | `metrics.py` (`impurity`, `fpr_column`) |
| Corpus FPR_T (Eqn 4), Cov_T, tau-pruned index | Sec 2.4 | `index.py` (`PatternIndex`, `build_pattern_index`, `clean_column`, `indexable_values`) |
| FMDV (Eqns 5-7) | Sec 2 | `fmdv.py::fmdv` |
| FMDV-H (Eqns 12-16) | Sec 4 | `fmdv.py::fmdv_h` |
| FMDV-V (Eqns 8-11) | Sec 3 | `fmdv_v.py::fmdv_v` |
| FMDV-VH (paper-spec §5.5) | Sec 4 | `fmdv_v.py::fmdv_vh` |
| Drift test (Sec 4) | Sec 5.4 | `drift.py::check_drift` |
| Detector, registry | — | `detector.py::AutoValidateAlgorithm` |

## Config

`AutoValidateConfig` (`config.py`): `variant="fmdv_vh"`, `r=0.05`, `m=100`,
`tau=8`, `theta=0.1`, `drift_significance=0.01`.  The paper has no
`alpha`/`beta`/`epsilon`.  `m=100` is the paper's recommendation for a
7.2M-column corpus; small corpora must override explicitly.

## Public API

- `build_pattern_index(corpus, config)` — offline scan of `T`.
- `fmdv(values, index, config)` — Eqn 5-7: `min FPR_T(h)` over
  `H(C)=∩P(v)\{" .* "}` s.t. `FPR_T(h)<=r` and `Cov_T(h)>=m`.
- `fmdv_h(values, index, config)` — Eqn 12-16: same but hypothesis space is
  `∪P(v)\{" .* "}` with `(1-theta)|C|` coverage on the query column.
- `fmdv_v(values, index, config)` — Eqn 8-11: vertical cuts via DP.
- `fmdv_vh(values, index, config)` — FMDV-H per segment, then FMDV-V.
- `check_drift(train, test, pattern, significance)` — two-tailed Fisher's
  exact test on non-conforming counts (column-level alert only).
- `InferredPattern(pattern, fpr_t, cov_t, theta_c, variant)` — result of any
  variant.
- `DriftResult(theta_train, theta_test, p_value, drifted)` — drift test result.
- `AutoValidateAlgorithm` — end-to-end detector registered as `"auto_validate"`.

### Detector API

`AutoValidateAlgorithm(ErrorDetectionAlgorithm)` implements:

- `__init__(config=None)` — accepts an `AutoValidateConfig` instance.
- `build_index(corpus: Iterable[Series|DataFrame]) -> PatternIndex` — builds
  the offline index and stores it on `self._index`.
- `infer_pattern(column: Series) -> tuple[str|None, float, int, float, str|None]`
  — returns `(pattern, fpr_t, cov_t, theta_c, reason)` where `reason` is
  ``None`` on success or an explanation string on infeasibility.
- `detect(data: DataFrame, *, table_id="table", columns=None, **kw) -> AlgorithmResult`
  — scans the dirty table, infers a pattern per column, produces one
  `CellResult` per non-null cell. `is_error = (value not in L(pattern))`.
  Evidence keys: `pattern`, `fpr_t`, `cov_t`, `theta_c`, `variant`, `r`, `m`, `tau`.
  Infeasible columns produce cells with `pattern=None, reason="no_feasible_pattern"`.
- `IndexNotBuiltError` — raised when `detect` or `infer_pattern` is called
  before `build_index`.

Registry: `_load_auto_validate()` → `register_lazy("auto_validate", ...)` in
`src/open_detect.algorithms/__init__.py`.  `open_detect.algorithms` import path
never imports scipy/pyspark/sklearn — those are lazy-loaded only when the
algorithm is actually constructed.

## Fidelity notes

1. **FMDV-H exact search vs. paper greedy.**  The paper says the decision
   version of FMDV-H is NP-hard (Thm 1) and uses a greedy.  The paper-spec
   description of the greedy is vague, so we implement an exact search over
   all candidate patterns in `∪P(v)`.  This solves Eqn 12-16 exactly; the
   greedy is omitted rather than approximated.
2. **Tie-breaking.**  The paper is silent.  We break ties by
   `(FPR_T ascending, impurity on C ascending, Cov_T descending, lexicographic
   pattern)`.  This favors general patterns with more corpus evidence and is
   deterministic.
3. **MSA approximation.**  Exact multi-sequence alignment (Carrillo & Lipman
   1988) is exponential.  We group values by coarse token-class signature
   (`<symbol>`, `<num>`, `<letter>` runs).  Within each group alignment is
   exact (same class sequence means positional alignment needs no gaps).
   This is exact when all values share one coarse signature (typical for
   homogeneous machine-generated data, per the paper's own assumption) and
   an approximation otherwise.
4. **FMDV-VH composition order.**  The paper (§5.5) says "horizontal first
   then vertical".  Our interpretation: partition values by coarse signature
   into vertical groups, then within each group apply FMDV-H (theta
   tolerance), then DP over token positions.  The per-group H-cut tolerates
   outliers before vertical segmentation.  A list pattern is one pattern per
   vertical segment, so at detection time `_value_matches` (`detector.py`)
   and the drift check (`drift.py`) share `hierarchy.matches_segments`: the
   value's tokens are split left to right into one slice per segment, every
   slice must match its segment's pattern, and the slices must consume every
   token.  A one-element list or plain string behaves exactly like
   `hierarchy.matches`.
5. **No corpus-free fallback.**  `fmdv`/`fmdv_h`/`fmdv_v`/`fmdv_vh` require
   a `PatternIndex`; without one, callers must raise `IndexNotBuiltError`.
   This follows from the paper's requirement that `T` be a background
   corpus of columns.
6. **Score definition (non-paper).**  The paper has no per-cell score
   (Section 6.4).  We set `score = 1 - FPR_T(h)` for flagged cells and
   `0.0` for unflagged cells — a ranking-only extension documented here.
7. **Drift test not wired into `detect`.**  `detect` does not call
   `check_drift` because a single-table scan has no "future" column to
   compare against.  This is a fidelity question for the independent
   reviewer (paper-spec §8.8).
8. **`P(v)` for T-side counting uses all values (weighted by multiplicity).**
   Impurity is computed over every value in the column, not distinct values
   only, consistent with Eqn 1.
9. **Pattern matching at detection time.**  `detect` uses `matches(pattern, value)`
   from `hierarchy.py` to determine `is_error`.  When the inferred pattern
   is generic (e.g. `<alphanum>+<symbol>+<alphanum>+<symbol>+<alphanum>+` for
   email-like input with low corpus diversity), the pattern may match non-email
   values too — this is inherent to the hierarchy's granularity, not a bug.
10. **Infeasible columns get no flags.**  When `infer_pattern` returns
    `(None, 0.0, 0, 0.0, "no_feasible_pattern")`, the detector produces one
    `CellResult` per non-null cell with `is_error=False` and evidence
    `{"pattern": None, "reason": "no_feasible_pattern", ...}`.  This avoids
    false positives when the corpus is too small or too diverse for any
    pattern to satisfy the `r`/`m` thresholds.

## Scope exclusions

- **Corpus-free mode**: undefined in the paper; omitted.
- **ML pattern profiler**: the paper uses a dedicated "profiler" tool; this
  library uses the mathematically defined hierarchy directly.
- **NL-content columns**: excluded by the paper (footnote on Section 2.1).
- **Multi-column constraints**: the basic algorithm is single-column.
- **Pattern unions**: unsupported in the paper's own profiler.
- **Spark implementation**: deferred.
- **Index persistence / parallel offline build**: speed-only, deferred.
- **Benchmarks**: deferred.