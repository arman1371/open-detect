"""Auto-Validate: unsupervised data validation using data-lake-inferred patterns.

Implementation of:
    Jie Song, Yeye He. "Auto-Validate: Unsupervised Data Validation Using
    Data-Domain Patterns Inferred from Data Lakes." SIGMOD 2021.

The package is organized around the paper's own offline/online split:

- :mod:`~unidetect.algorithms.auto_validate.hierarchy` -- the generalization
  hierarchy and value tokenizer (Section 2.1).
- :mod:`~unidetect.algorithms.auto_validate.patterns` -- ``P(v)``, the patterns
  a value generalizes into (Section 2.1, Algorithm 1).
- :mod:`~unidetect.algorithms.auto_validate.metrics` -- impurity and per-column
  FPR (Eqns 1-3).
- :mod:`~unidetect.algorithms.auto_validate.index` -- the offline pattern index
  of ``FPR_T`` / ``Cov_T`` over the background corpus ``T`` (Eqn 4, Section 2.4).

The optimizer variants (FMDV, FMDV-H, FMDV-V, FMDV-VH) and the detector are
built on top of these in later modules.
"""

from __future__ import annotations

from unidetect.algorithms.auto_validate.config import VARIANTS, AutoValidateConfig
from unidetect.algorithms.auto_validate.exceptions import IndexNotBuiltError
from unidetect.algorithms.auto_validate.hierarchy import matches, token_count, tokenize
from unidetect.algorithms.auto_validate.index import PatternIndex, build_pattern_index
from unidetect.algorithms.auto_validate.metrics import fpr_column, impurity
from unidetect.algorithms.auto_validate.patterns import patterns_of, sorted_patterns

__all__ = [
    "VARIANTS",
    "AutoValidateConfig",
    "IndexNotBuiltError",
    "PatternIndex",
    "build_pattern_index",
    "fpr_column",
    "impurity",
    "matches",
    "patterns_of",
    "sorted_patterns",
    "token_count",
    "tokenize",
]
