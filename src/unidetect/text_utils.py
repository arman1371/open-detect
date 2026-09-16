"""Tokenization and data-type inference shared by featurization and corpus ingestion."""

from __future__ import annotations

import re
from collections.abc import Sequence

from unidetect.core.enums import ColumnDataType

_TOKEN_RE = re.compile(r"[A-Za-z0-9]+")
_INT_RE = re.compile(r"^[+-]?\d+$")
_FLOAT_RE = re.compile(r"^[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?$")
_ALPHANUMERIC_MIX_RE = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9\-_./]+$")


def tokenize(value: str) -> list[str]:
    """Split a value into alphanumeric tokens, discarding punctuation/whitespace."""
    return _TOKEN_RE.findall(value)


def is_integer_like(value: str) -> bool:
    return bool(_INT_RE.match(value.strip()))


def is_float_like(value: str) -> bool:
    return bool(_FLOAT_RE.match(value.strip()))


def is_mixed_alphanumeric(value: str) -> bool:
    """True for values like 'ICAO123', 'SKU-9981', 'AB12CD34' -- typical ID/code strings."""
    return bool(_ALPHANUMERIC_MIX_RE.match(value.strip()))


def infer_column_data_type(values: Sequence[object], sample_size: int = 200) -> ColumnDataType:
    """Classify a column into the coarse types used for featurization (paper Fig. 5).

    Sampling keeps this cheap on very large columns; a small, consistent
    sample is sufficient because we only need a coarse majority-vote type,
    not a strict schema.
    """
    sample = [str(v) for v in values[:sample_size] if v is not None]
    if not sample:
        return ColumnDataType.UNKNOWN

    counts = {
        ColumnDataType.INTEGER: 0,
        ColumnDataType.FLOAT: 0,
        ColumnDataType.MIXED_ALPHANUMERIC: 0,
        ColumnDataType.STRING: 0,
    }
    for v in sample:
        if is_integer_like(v):
            counts[ColumnDataType.INTEGER] += 1
        elif is_float_like(v):
            counts[ColumnDataType.FLOAT] += 1
        elif is_mixed_alphanumeric(v):
            counts[ColumnDataType.MIXED_ALPHANUMERIC] += 1
        else:
            counts[ColumnDataType.STRING] += 1

    majority_type, majority_count = max(counts.items(), key=lambda kv: kv[1])
    if majority_count / len(sample) < 0.6:
        # No clear majority: treat as string, the most permissive bucket.
        return ColumnDataType.STRING
    return majority_type
