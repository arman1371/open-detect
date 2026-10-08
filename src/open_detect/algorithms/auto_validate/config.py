"""Tunable knobs for the Auto-Validate algorithm.

Parameter names and defaults follow paper-spec Section 6.2 (the paper's own
reviewer response, O3). The paper has no ``alpha``/``beta``/``epsilon``.
"""

from __future__ import annotations

from dataclasses import dataclass

from open_detect.exceptions import ConfigurationError

#: The four optimization variants of Auto-Validate (paper Sections 2-4).
VARIANTS: frozenset[str] = frozenset({"fmdv", "fmdv_v", "fmdv_h", "fmdv_vh"})


@dataclass(frozen=True)
class AutoValidateConfig:
    """Configuration for :class:`~open_detect.algorithms.auto_validate.detector.AutoValidateAlgorithm`.

    Parameters
    ----------
    variant:
        Which optimization problem to solve per column. ``"fmdv"`` is the
        basic problem (Eqns 5-7); ``"fmdv_v"`` adds vertical cuts (Eqns 8-11);
        ``"fmdv_h"`` adds horizontal cuts with tolerance ``theta``
        (Eqns 12-16); ``"fmdv_vh"`` is the paper's best-performing
        combination of both.
    r:
        FPR threshold ``r`` (Eqns 6, 9, 14). The paper recommends ``0.05``
        and reports insensitivity for ``r >= 0.02``.
    m:
        Coverage threshold ``m`` (Eqns 7, 10, 15): the number of corpus columns
        that must match a pattern before it is trusted. The paper recommends
        ``100``, calibrated against a 7.2M-column corpus; small corpora must
        override this explicitly.
    tau:
        Token limit. Offline (Sec 2.4) it caps how many tokens a value may
        have to be indexed; in FMDV-V (Def. 2) it caps the width of a vertical
        segment. The paper recommends ``8``.
    theta:
        FMDV-H tolerance (Eqn 16): the fraction of query-column values a
        pattern is allowed to fail to match. **The paper gives no numeric
        default** -- ``0.1`` is this library's choice, not the paper's.
    drift_significance:
        Two-tailed significance level for the column-level drift test
        (Sec 4). The paper states ``0.01``.
    """

    variant: str = "fmdv_vh"
    r: float = 0.05
    m: int = 100
    tau: int = 8
    theta: float = 0.1
    drift_significance: float = 0.01

    def __post_init__(self) -> None:
        if self.variant not in VARIANTS:
            raise ConfigurationError(
                f"variant must be one of {sorted(VARIANTS)}, got {self.variant!r}"
            )
        for name in ("r", "theta", "drift_significance"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ConfigurationError(f"{name} must be in [0, 1], got {value}")
        if self.m < 1:
            raise ConfigurationError(f"m must be >= 1, got {self.m}")
        if self.tau < 1:
            raise ConfigurationError(f"tau must be >= 1, got {self.tau}")

    @property
    def uses_vertical_cuts(self) -> bool:
        """Whether the variant may split a query column into token segments."""
        return self.variant in ("fmdv_v", "fmdv_vh")

    @property
    def uses_horizontal_cuts(self) -> bool:
        """Whether the variant tolerates non-conforming values in the query column."""
        return self.variant in ("fmdv_h", "fmdv_vh")
