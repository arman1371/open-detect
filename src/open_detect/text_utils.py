"""Deprecated: moved to :mod:`open_detect.algorithms.uni_detect.text_utils`. Removal in 0.5.0."""

import warnings

from open_detect.algorithms.uni_detect.text_utils import *  # noqa: F401,F403

warnings.warn(
    "open_detect.text_utils is deprecated; import from open_detect.algorithms.uni_detect.text_utils instead. "
    "This shim will be removed in 0.5.0.",
    DeprecationWarning,
    stacklevel=2,
)
