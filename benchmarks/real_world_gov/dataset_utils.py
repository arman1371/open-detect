"""Shared helpers for reading the real_world_gov benchmark's checked-in CSVs.

Every dataset directory under ``data/<dataset>/`` follows the Matelda /
"raha-style" error-detection benchmark convention (see ``README.md``):

- ``clean.csv``   -- ground-truth values.
- ``dirty.csv``   -- the same table with real, historically-injected errors;
  same row order and column count as ``clean.csv``, but ``dirty.csv``'s
  header carries a SQL-type-hint suffix on non-text columns (e.g.
  ``"zipcode(long)"``) that ``clean.csv``'s header does not.
- ``clean_changes.csv`` -- ground truth: one row per corrupted *cell*,
  formatted ``"<row>.<column>",<dirty_value>,<clean_value>`` where
  ``<row>`` is a 1-based data-row index (row 0 would be the header) and
  ``<column>`` matches ``clean.csv``'s (un-suffixed) header.

Both ``run_benchmark.py`` (the Spark-based, CI-facing implementation) and
the pure-Python provenance harness documented in ``README.md`` import this
module so the two never disagree on how a dataset's columns are named or
which cells are ground-truth errors.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

#: The 5 datasets this benchmark evaluates, in the deterministic order
#: `select_datasets.py` selected them (see that script / README.md for the
#: full selection methodology).
DATASETS: tuple[str, ...] = tuple(sorted(p.name for p in DATA_DIR.iterdir() if p.is_dir()))

_TYPE_SUFFIX_RE = re.compile(r"\([^()]*\)\s*$")


def canonical_column(name: str) -> str:
    """Strip ``dirty.csv``'s SQL-type-hint suffix (e.g. ``"zip(double precision)"``).

    ``clean.csv`` never has this suffix, so stripping it is what makes the
    two files' headers -- and ``clean_changes.csv``'s column references --
    comparable.
    """
    return _TYPE_SUFFIX_RE.sub("", name).strip()


def load_csv(path: Path) -> tuple[list[str], list[list[str | None]]]:
    """Read a CSV into (canonical header, rows), treating ``""`` cells as null."""
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = [canonical_column(c) for c in next(reader)]
        rows = [[v if v != "" else None for v in row] for row in reader]
    return header, rows


def load_changes(path: Path) -> dict[str, int]:
    """Map ``column -> number of injected cell errors`` from a ``clean_changes.csv``."""
    counts: dict[str, int] = {}
    if not path.exists():
        return counts
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        for row in reader:
            if not row:
                continue
            _row_index, column = row[0].split(".", 1)
            counts[column] = counts.get(column, 0) + 1
    return counts


def dataset_paths(dataset: str) -> tuple[Path, Path, Path]:
    d = DATA_DIR / dataset
    return d / "clean.csv", d / "dirty.csv", d / "clean_changes.csv"
