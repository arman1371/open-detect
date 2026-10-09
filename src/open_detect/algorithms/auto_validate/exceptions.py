"""Exceptions raised by the Auto-Validate algorithm."""

from __future__ import annotations

from open_detect.exceptions import OpenDetectError


class IndexNotBuiltError(OpenDetectError):
    """Raised when an Auto-Validate query runs before the offline index exists.

    The corpus ``T`` is a required input: FPR_T and Cov_T are defined only
    relative to it, so there is deliberately no corpus-free fallback.
    """
