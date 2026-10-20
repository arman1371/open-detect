"""Deprecated: moved to :mod:`open_detect.algorithms.uni_detect.core`. Removal in 0.5.0."""

import warnings
from typing import Any


def __getattr__(name: str) -> Any:
    from open_detect.algorithms.uni_detect import core as _new

    if name.startswith("__") or not hasattr(_new, name):
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    warnings.warn(
        f"open_detect.core.{name} is deprecated; import it from "
        "open_detect.algorithms.uni_detect.core instead. "
        "This shim will be removed in 0.5.0.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(_new, name)
