"""Column-level distributional drift test (paper Section 5.4).

Given a training column with inferred pattern h and a test column, compute
the fraction of non-conforming values in each (theta_train, theta_test) and
run a two-tailed Fisher's exact test on the 2×2 contingency table of
(conforming, non-conforming) counts.  Return a DriftResult.

``scipy`` is imported lazily inside this module so it never appears on the
algorithm's import path.  The optional extra ``auto_validate`` in
``pyproject.toml`` pulls it in when requested.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from unidetect.algorithms.auto_validate.config import AutoValidateConfig
from unidetect.algorithms.auto_validate.fmdv import InferredPattern
from unidetect.algorithms.auto_validate.hierarchy import matches


@dataclass(frozen=True, slots=True)
class DriftResult:
    """Result of a column-level drift test."""

    theta_train: float
    theta_test: float
    p_value: float
    drifted: bool


def check_drift(
    train: pd.Series,
    test: pd.Series,
    pattern: InferredPattern,
    significance: float | None = None,
    config: AutoValidateConfig | None = None,
) -> DriftResult:
    """Two-tailed Fisher's exact test on conforming vs. non-conforming counts.

    Parameters
    ----------
    train, test:
        Columns of string values (nulls and blanks are dropped).
    pattern:
        The inferred validation pattern for the column domain.
    significance:
        Two-tailed significance level. Defaults to
        ``config.drift_significance`` (0.01).
    config:
        Used only for the default significance when ``significance`` is
        omitted.
    """
    config = config or AutoValidateConfig()
    if significance is None:
        significance = config.drift_significance

    return _fisher_two_tailed(train, test, pattern, significance)


def _fisher_two_tailed(
    train: pd.Series, test: pd.Series, pattern: InferredPattern, significance: float
) -> DriftResult:
    """Run the Fisher exact test; return DriftResult directly."""
    from scipy.stats import fisher_exact

    train_clean = _clean_series(train)
    test_clean = _clean_series(test)

    n_train = len(train_clean)
    n_test = len(test_clean)
    if n_train == 0 or n_test == 0:
        return DriftResult(theta_train=0.0, theta_test=0.0, p_value=1.0, drifted=False)

    pat = pattern.pattern
    pat_str = pat if isinstance(pat, str) else pat[0]

    conform_train = sum(1 for v in train_clean if matches(pat_str, v))
    noncon_train = n_train - conform_train
    conform_test = sum(1 for v in test_clean if matches(pat_str, v))
    noncon_test = n_test - conform_test

    oddsratio, p_value = fisher_exact(
        [[conform_train, noncon_train], [conform_test, noncon_test]],
        alternative="two-sided",
    )
    theta_train = 1.0 - conform_train / n_train if n_train else 0.0
    theta_test = 1.0 - conform_test / n_test if n_test else 0.0
    return DriftResult(
        theta_train=theta_train,
        theta_test=theta_test,
        p_value=float(p_value),
        drifted=bool(p_value < significance),
    )


def _clean_series(values: pd.Series) -> list[str]:
    """Drop nulls and blanks, str()-convert, preserve order."""
    out: list[str] = []
    for v in values:
        if v is None:
            continue
        try:
            if pd.isna(v):
                continue
        except (TypeError, ValueError):
            pass
        text = v if isinstance(v, str) else str(v)
        if text:
            out.append(text)
    return out
