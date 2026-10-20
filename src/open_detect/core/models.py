"""Deprecated: moved to :mod:`open_detect.algorithms.uni_detect.core.models`. Removal in 0.5.0."""

import warnings

from open_detect.algorithms.uni_detect.core.models import *  # noqa: F401,F403

warnings.warn(
    "open_detect.core.models is deprecated; import from open_detect.algorithms.uni_detect.core.models instead. "
    "This shim will be removed in 0.5.0.",
    DeprecationWarning,
    stacklevel=2,
)
