"""Java-free tests for ``benchmarks/common/snapshot.py`` (the detections-snapshot differ)."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "benchmarks"))
from common import snapshot  # noqa: E402


def _row(cid: str, lr: float, sig: bool = True, cols=("a",), rows=("1",)) -> dict:
    return {
        "candidate_id": cid,
        "error_type": "uniqueness",
        "table_id": "t",
        "column_names": list(cols),
        "row_ids": list(rows),
        "lr_ratio": lr,
        "is_significant": sig,
        # Extra detect() columns must be ignored by the snapshot.
        "surprisal": 1.0,
        "evidence_json": "{}",
    }


def _frame(*rows: dict) -> pd.DataFrame:
    return pd.DataFrame(list(rows))


def test_identical_snapshots_match() -> None:
    base = _frame(_row("c1", 0.01), _row("c2", 0.5, sig=False))
    assert snapshot.diff_snapshots(base, base.copy()) == []


def test_row_order_and_tie_order_are_irrelevant() -> None:
    base = _frame(_row("c1", 0.1), _row("c2", 0.1), _row("c3", 0.3, sig=False))
    shuffled = base.iloc[[2, 1, 0]].reset_index(drop=True)
    assert snapshot.diff_snapshots(base, shuffled) == []


def test_lr_ratio_within_tolerance_matches() -> None:
    base = _frame(_row("c1", 0.01))
    near = _frame(_row("c1", 0.01 + 5e-10))
    assert snapshot.diff_snapshots(base, near) == []


def test_lr_ratio_beyond_tolerance_differs() -> None:
    base = _frame(_row("c1", 0.01))
    far = _frame(_row("c1", 0.01 + 1e-6))
    problems = snapshot.diff_snapshots(base, far)
    assert len(problems) == 1
    assert "lr_ratio" in problems[0]


def test_flag_and_list_changes_are_exact() -> None:
    base = _frame(_row("c1", 0.01))
    assert snapshot.diff_snapshots(base, _frame(_row("c1", 0.01, sig=False)))
    assert snapshot.diff_snapshots(base, _frame(_row("c1", 0.01, rows=("2",))))
    assert snapshot.diff_snapshots(base, _frame(_row("c1", 0.01, cols=("b",))))


def test_added_and_removed_candidates_are_reported() -> None:
    base = _frame(_row("c1", 0.01), _row("gone", 0.2))
    new = _frame(_row("c1", 0.01), _row("fresh", 0.2))
    text = "\n".join(snapshot.diff_snapshots(base, new))
    assert "only in baseline" in text
    assert "gone" in text
    assert "only in new" in text
    assert "fresh" in text


def test_nan_and_inf_lr_ratio_compare_equal_to_themselves() -> None:
    base = _frame(_row("c1", float("nan")), _row("c2", float("inf"), sig=False))
    assert snapshot.diff_snapshots(base, base.copy()) == []
    assert snapshot.diff_snapshots(
        base, _frame(_row("c1", 0.1), _row("c2", float("inf"), sig=False))
    )


def test_save_load_roundtrip_and_cli_exit_codes(
    tmp_path: Path, capsys: pytest.CaptureFixture
) -> None:
    base = _frame(_row("c1", 0.1 + 0.2), _row("c2", 0.5, sig=False, cols=("a", "b"), rows=()))
    a = snapshot.save_snapshot(base, tmp_path / "a")
    b = snapshot.save_snapshot(base.iloc[::-1], tmp_path / "b")
    assert a.name == snapshot.SNAPSHOT_FILENAME
    assert snapshot.diff_snapshots(snapshot.load_snapshot(a), base) == []
    assert snapshot.main(["diff", str(tmp_path / "a"), str(b)]) == 0

    changed = base.copy()
    changed.loc[0, "is_significant"] = False
    c = snapshot.save_snapshot(changed, tmp_path / "c")
    assert snapshot.main(["diff", str(a), str(c)]) == 1
    assert "DIFFER" in capsys.readouterr().out


def test_missing_columns_rejected() -> None:
    with pytest.raises(ValueError, match="missing snapshot columns"):
        snapshot.normalize(pd.DataFrame({"candidate_id": ["c1"]}))


def test_empty_detections_roundtrip(tmp_path: Path) -> None:
    path = snapshot.save_snapshot(pd.DataFrame(), tmp_path / "empty")
    assert snapshot.load_snapshot(path).empty
    assert snapshot.main(["diff", str(path), str(path)]) == 0
