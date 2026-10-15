"""Save and diff Uni-Detect detections snapshots.

A snapshot is a CSV of a ``UniDetect.detect()`` result restricted to the
columns that define *what was detected*: ``candidate_id``, ``error_type``,
``table_id``, ``column_names``, ``row_ids`` (both JSON-encoded lists),
``lr_ratio`` and ``is_significant``.

:func:`diff_snapshots` matches rows by ``(error_type, table_id, candidate_id)``
-- so row order, and the order of tied ``lr_ratio`` rows in particular, is
irrelevant -- requires exact equality of ids, ``column_names``, ``row_ids`` and
``is_significant``, and compares ``lr_ratio`` within a tolerance (default
``1e-9``).

Command line (exits non-zero when the snapshots differ)::

    python benchmarks/common/snapshot.py diff BASELINE NEW [--tol 1e-9]

``BASELINE``/``NEW`` are CSV files or directories containing ``detections.csv``.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any

import pandas as pd

SNAPSHOT_FILENAME = "detections.csv"
SNAPSHOT_COLUMNS = (
    "candidate_id",
    "error_type",
    "table_id",
    "column_names",
    "row_ids",
    "lr_ratio",
    "is_significant",
)
KEY_COLUMNS = ("error_type", "table_id", "candidate_id")
DEFAULT_TOLERANCE = 1e-9
_MAX_REPORTED = 20


def _as_json_list(value: Any) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "[]"
    return json.dumps([str(v) for v in value])


def normalize(detections: pd.DataFrame) -> pd.DataFrame:
    """Project ``detections`` onto :data:`SNAPSHOT_COLUMNS` in a canonical, sorted form."""
    missing = [c for c in SNAPSHOT_COLUMNS if c not in detections.columns]
    if missing:
        raise ValueError(f"detections is missing snapshot columns: {missing}")
    frame = detections.loc[:, list(SNAPSHOT_COLUMNS)].copy()
    for col in ("column_names", "row_ids"):
        frame[col] = [v if isinstance(v, str) else _as_json_list(v) for v in frame[col]]
    frame["lr_ratio"] = frame["lr_ratio"].astype("float64")
    frame["is_significant"] = frame["is_significant"].astype(bool)
    return frame.sort_values(
        [*KEY_COLUMNS, "column_names", "row_ids", "lr_ratio"], kind="mergesort"
    ).reset_index(drop=True)


def save_snapshot(detections: pd.DataFrame, path: Path) -> Path:
    """Write ``detections`` (one or more concatenated ``detect()`` results) to ``path``."""
    target = path / SNAPSHOT_FILENAME if path.suffix == "" else path
    target.parent.mkdir(parents=True, exist_ok=True)
    normalize(detections).to_csv(target, index=False, float_format="%.17g")
    return target


def load_snapshot(path: Path) -> pd.DataFrame:
    source = path / SNAPSHOT_FILENAME if path.is_dir() else path
    frame = pd.read_csv(
        source,
        dtype={
            "candidate_id": "string",
            "error_type": "string",
            "table_id": "string",
            "column_names": "string",
            "row_ids": "string",
        },
        keep_default_na=False,
        na_values=["nan", "NaN"],
    )
    return normalize(frame)


def _lr_equal(a: float, b: float, tol: float) -> bool:
    if math.isnan(a) or math.isnan(b):
        return math.isnan(a) and math.isnan(b)
    return math.isclose(a, b, rel_tol=0.0, abs_tol=tol)


def diff_snapshots(
    baseline: pd.DataFrame, new: pd.DataFrame, tol: float = DEFAULT_TOLERANCE
) -> list[str]:
    """Return human-readable differences (empty list means the snapshots match)."""
    base = normalize(baseline)
    cur = normalize(new)
    problems: list[str] = []

    for name, frame in (("baseline", base), ("new", cur)):
        dupes = int(frame.duplicated(subset=list(KEY_COLUMNS)).sum())
        if dupes:
            problems.append(
                f"{name} has {dupes} duplicate (error_type, table_id, candidate_id) keys"
            )

    base_keys = set(map(tuple, base.loc[:, list(KEY_COLUMNS)].itertuples(index=False)))
    cur_keys = set(map(tuple, cur.loc[:, list(KEY_COLUMNS)].itertuples(index=False)))
    problems.extend(_list_keys("only in baseline", base_keys - cur_keys))
    problems.extend(_list_keys("only in new", cur_keys - base_keys))

    merged = base.merge(
        cur, on=list(KEY_COLUMNS), how="inner", suffixes=("_base", "_new"), validate="m:m"
    )
    changed = 0
    for row in merged.itertuples(index=False):
        row_dict = row._asdict()
        label = f"{row_dict['error_type']}/{row_dict['table_id']}/{row_dict['candidate_id']}"
        reasons = []
        for col in ("column_names", "row_ids", "is_significant"):
            if row_dict[f"{col}_base"] != row_dict[f"{col}_new"]:
                reasons.append(f"{col}: {row_dict[f'{col}_base']!r} -> {row_dict[f'{col}_new']!r}")
        if not _lr_equal(row_dict["lr_ratio_base"], row_dict["lr_ratio_new"], tol):
            reasons.append(
                f"lr_ratio: {row_dict['lr_ratio_base']!r} -> {row_dict['lr_ratio_new']!r}"
            )
        if reasons:
            changed += 1
            if changed <= _MAX_REPORTED:
                problems.append(f"changed {label}: " + "; ".join(reasons))
    if changed > _MAX_REPORTED:
        problems.append(f"... and {changed - _MAX_REPORTED} more changed rows")
    return problems


def _list_keys(prefix: str, keys: Iterable[tuple[str, ...]]) -> list[str]:
    ordered = sorted(keys)
    if not ordered:
        return []
    lines = [f"{len(ordered)} candidates {prefix}:"]
    lines.extend(f"  {'/'.join(key)}" for key in ordered[:_MAX_REPORTED])
    if len(ordered) > _MAX_REPORTED:
        lines.append(f"  ... and {len(ordered) - _MAX_REPORTED} more")
    return lines


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    diff = sub.add_parser("diff", help="Diff two detections snapshots; exit 1 on any difference.")
    diff.add_argument("baseline", type=Path)
    diff.add_argument("new", type=Path)
    diff.add_argument("--tol", type=float, default=DEFAULT_TOLERANCE)
    args = parser.parse_args(argv)

    problems = diff_snapshots(load_snapshot(args.baseline), load_snapshot(args.new), args.tol)
    if problems:
        print(f"Snapshots DIFFER ({args.baseline} vs {args.new}):")
        print("\n".join(problems))
        return 1
    print(f"Snapshots match ({args.baseline} vs {args.new}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
