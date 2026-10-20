"""Deprecated: moved to :mod:`open_detect.algorithms.uni_detect.core.enums`. Removal in 0.5.0."""

import warnings

from open_detect.algorithms.uni_detect.core.enums import *  # noqa: F401,F403

warnings.warn(
    "open_detect.core.enums is deprecated; import from open_detect.algorithms.uni_detect.core.enums instead. "
    "This shim will be removed in 0.5.0.",
    DeprecationWarning,
    stacklevel=2,
)
