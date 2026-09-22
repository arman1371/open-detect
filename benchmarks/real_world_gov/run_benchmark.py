"""Runs the real_world_gov benchmark for every available registered algorithm
(see ``README.md``) and scores each one's detections on the 5 datasets'
*dirty* tables against ``clean_changes.csv``'s cell-level ground truth:

- **uni_detect** -- builds corpus statistics from the *clean* tables, then
  scores the dirty tables against that corpus (Spark/Delta; requires JDK 17).
- **raha** -- scores each dirty table directly against its own *clean* table
  via :class:`~unidetect.algorithms.raha.GroundTruthLabeler` (pandas; no
  Spark/JDK dependency at all).

Usage::

    uv run python benchmarks/real_world_gov/run_benchmark.py
    uv run python benchmarks/real_world_gov/run_benchmark.py --update-baseline

Writes ``results/latest.json`` and, when a baseline exists, prints a
version-over-version comparison (also appended to ``$GITHUB_STEP_SUMMARY``
when running in GitHub Actions). Requires JDK 17 locally for the
``uni_detect`` half -- see this benchmark's ``README.md`` and the top-level
``README.md``'s "JDK version" note for why; ``raha`` runs regardless.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

BENCHMARK_DIR = Path(__file__).parent
REPO_ROOT = BENCHMARK_DIR.parent.parent

sys.path.insert(0, str(REPO_ROOT / "benchmarks"))
sys.path.insert(0, str(BENCHMARK_DIR))
from dataset_utils import DATASETS, dataset_paths, load_changes, load_csv  # noqa: E402

from common.metrics import confusion_metrics  # noqa: E402
from common.spark_session import SparkUnavailable, git_commit, spark_session  # noqa: E402

RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"
LATEST_FILE = RESULTS_DIR / "latest.json"

TEST_CATALOG = "spark_catalog"
TEST_SCHEMA = "unidetect_benchmark_real"

#: The paper's own labeling-budget default (Section 6.1); see ``README.md``
#: for why this benchmark keeps it rather than tuning it per dataset.
RAHA_LABELING_BUDGET = 20


def _build_config(uc_location):
    from unidetect.config import UniDetectConfig

    return UniDetectConfig(
        location=uc_location,
        # Same values as benchmarks/run_benchmark.py's wiki_subset config,
        # for the same reason: this benchmark's background corpus is a
        # handful of small real tables, not the paper's web-scale crawl.
        epsilon=0.05,
        alpha=0.2,
        max_mpd_block_size=200,
        max_fd_column_pairs_per_table=200,
        prevalence_edges=(2, 5, 20, 100, 1000),
    )


def _register_table(spark, fqn: str, header: list[str], rows: list[list]):
    df = spark.createDataFrame([tuple(row) for row in rows], schema=header)
    df.write.format("delta").mode("overwrite").saveAsTable(fqn)


def _dataset_frames() -> dict[str, dict]:
    """Load every dataset's clean/dirty CSVs + ground truth once, shared by both algorithms."""
    frames: dict[str, dict] = {}
    for name in DATASETS:
        clean_path, dirty_path, changes_path = dataset_paths(name)
        clean_header, clean_rows = load_csv(clean_path)
        dirty_header, dirty_rows = load_csv(dirty_path)
        assert clean_header == dirty_header
        frames[name] = {
            "header": clean_header,
            "clean_rows": clean_rows,
            "dirty_rows": dirty_rows,
            "error_counts": load_changes(changes_path),
        }
    return frames


def run_uni_detect(frames: dict[str, dict]) -> tuple[list[dict], dict, float]:
    """Score every dataset's dirty table with Uni-Detect. Returns (targets, metrics, duration_seconds)."""
    from unidetect.config import UnityCatalogLocation
    from unidetect.core.enums import ErrorType
    from unidetect.pipeline import UniDetect

    uc_location = UnityCatalogLocation(catalog=TEST_CATALOG, schema=TEST_SCHEMA)
    config = _build_config(uc_location)

    start = time.perf_counter()
    with spark_session(TEST_CATALOG, TEST_SCHEMA) as spark:
        ud = UniDetect(config, spark=spark)

        clean_fqns: dict[str, str] = {}
        dirty_fqns: dict[str, str] = {}
        for name, frame in frames.items():
            clean_fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.clean_{name}".replace("-", "_").replace(
                ".", "_"
            )
            dirty_fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.dirty_{name}".replace("-", "_").replace(
                ".", "_"
            )
            _register_table(spark, clean_fqn, frame["header"], frame["clean_rows"])
            _register_table(spark, dirty_fqn, frame["header"], frame["dirty_rows"])
            clean_fqns[name] = clean_fqn
            dirty_fqns[name] = dirty_fqn

        # Offline: learn "what these clean government tables typically look
        # like" from the clean versions. create_schema=False: the namespace
        # is already created above by spark_session()'s own `CREATE
        # NAMESPACE`; ensure_schema_exists() issues `CREATE CATALOG`, a
        # Unity-Catalog-only DDL statement a local, non-Unity-Catalog
        # `spark_catalog` doesn't support.
        ud.build_corpus_statistics(
            list(clean_fqns.values()), error_types=list(ErrorType), create_schema=False
        )

        # Online: score the dirty (really-corrupted) versions against it.
        detections = ud.detect(list(dirty_fqns.values()), error_types=list(ErrorType)).toPandas()

        fqn_to_dataset = {fqn: name for name, fqn in dirty_fqns.items()}

        # (dataset, column) -> the best (lowest lr_ratio) detection that
        # touched that column, across every error type and every candidate
        # (single-column ones directly, FD pairs via either side).
        per_column: dict[tuple[str, str], dict] = {}
        for _, row in detections.iterrows():
            dataset = fqn_to_dataset[row["table_id"]]
            for col in row["column_names"]:
                key = (dataset, col)
                existing = per_column.get(key)
                if existing is None or row["lr_ratio"] < existing["lr_ratio"]:
                    per_column[key] = row

        targets: list[dict] = []
        for name, frame in frames.items():
            for col in frame["header"]:
                hit = per_column.get((name, col))
                error_count = frame["error_counts"].get(col, 0)
                targets.append(
                    {
                        "id": f"{name}::{col}",
                        "dataset": name,
                        "column": col,
                        "num_rows": len(frame["clean_rows"]),
                        "error_count": error_count,
                        "expected_significant": error_count > 0,
                        "predicted_significant": bool(hit is not None and hit["is_significant"]),
                        "lr_ratio": float(hit["lr_ratio"]) if hit is not None else None,
                        "matched_error_type": hit["error_type"] if hit is not None else None,
                    }
                )
    duration = time.perf_counter() - start

    overall = confusion_metrics(targets)
    by_dataset = {
        name: confusion_metrics([t for t in targets if t["dataset"] == name]) for name in DATASETS
    }
    return targets, {"overall": overall, "by_dataset": by_dataset}, duration


def run_raha(frames: dict[str, dict]) -> tuple[list[dict], dict, dict, float]:
    """Score every dataset's dirty table with Raha.

    Returns ``(targets, column_metrics, cell_metrics, duration_seconds)``.
    ``column_metrics`` reduces Raha's cell-level verdicts to the same
    per-column granularity Uni-Detect produces (any flagged cell -> column
    flagged), for the apples-to-apples comparison table. ``cell_metrics`` is
    Raha's *native* granularity -- precision/recall/F1 over every individual
    (row, column) cell against ``clean_changes.csv``, the same granularity
    the paper's own Table 5 reports (Section 6) -- and is the more
    informative number for judging Raha specifically: the column-level
    reduction is a much coarser task (one true positive among dozens of
    rows is enough to call a whole column "predicted significant"), and
    columns in this benchmark's real, historically-corrupted data often have
    a double-digit-percent error rate, so a perfect column-level score does
    not by itself mean every cell was classified correctly.

    Each dataset gets its own :class:`~unidetect.algorithms.raha.RahaDetector`
    run (Raha trains one classifier per column of a single table, so there is
    no cross-dataset "corpus" phase the way Uni-Detect has). Labels come from
    :class:`~unidetect.algorithms.raha.GroundTruthLabeler` against the
    dataset's own ``clean.csv`` -- the same "raha-style" clean/dirty pairing
    this benchmark's data already ships in, and the natural way to answer "how
    does Raha do with the labeling budget its own paper evaluates it at"
    without a human in the loop for a CI benchmark.
    """
    import pandas as pd

    from unidetect.algorithms.raha import GroundTruthLabeler, RahaConfig, RahaDetector
    from unidetect.algorithms.raha.strategies import NULL_SENTINEL, normalize_to_str

    targets: list[dict] = []
    cell_rows: list[dict] = []
    start = time.perf_counter()
    for name, frame in frames.items():
        header = frame["header"]
        clean_df = pd.DataFrame(frame["clean_rows"], columns=header)
        dirty_df = pd.DataFrame(frame["dirty_rows"], columns=header)

        detector = RahaDetector(RahaConfig(labeling_budget=RAHA_LABELING_BUDGET, random_state=0))
        result = detector.detect(dirty_df, table_id=name, labeler=GroundTruthLabeler(clean_df))

        dirty_norm = normalize_to_str(dirty_df)
        clean_norm = normalize_to_str(clean_df)
        by_column: dict[str, list] = defaultdict(list)
        for cell in result:
            by_column[cell.column_name].append(cell)
            expected = dirty_norm.loc[cell.row_index, cell.column_name] != clean_norm.get(
                cell.column_name, {}
            ).get(cell.row_index, NULL_SENTINEL)
            cell_rows.append(
                {
                    "dataset": name,
                    "expected_significant": bool(expected),
                    "predicted_significant": cell.is_error,
                }
            )

        for col in header:
            cells = by_column.get(col, [])
            error_count = frame["error_counts"].get(col, 0)
            targets.append(
                {
                    "id": f"{name}::{col}",
                    "dataset": name,
                    "column": col,
                    "num_rows": len(frame["clean_rows"]),
                    "error_count": error_count,
                    "expected_significant": error_count > 0,
                    "predicted_significant": any(c.is_error for c in cells),
                    "score": max((c.score for c in cells), default=0.0),
                }
            )
    duration = time.perf_counter() - start

    column_overall = confusion_metrics(targets)
    column_by_dataset = {
        name: confusion_metrics([t for t in targets if t["dataset"] == name]) for name in DATASETS
    }
    cell_overall = confusion_metrics(cell_rows)
    cell_by_dataset = {
        name: confusion_metrics([r for r in cell_rows if r["dataset"] == name]) for name in DATASETS
    }
    return (
        targets,
        {"overall": column_overall, "by_dataset": column_by_dataset},
        {"overall": cell_overall, "by_dataset": cell_by_dataset},
        duration,
    )


def run() -> dict:
    frames = _dataset_frames()
    algorithms: dict[str, dict] = {}

    try:
        import sklearn  # noqa: F401
    except ImportError:
        print(
            "scikit-learn not installed; skipping raha "
            "(run `uv sync` or `uv pip install unidetect[raha]` first).",
            file=sys.stderr,
        )
    else:
        raha_targets, raha_column_metrics, raha_cell_metrics, raha_duration = run_raha(frames)
        algorithms["raha"] = {
            "targets": raha_targets,
            "metrics": raha_column_metrics,
            "cell_metrics": raha_cell_metrics,
            "duration_seconds": raha_duration,
            "duration_note": None,
        }

    try:
        import delta  # noqa: F401
        import pyspark  # noqa: F401
    except ImportError:
        print(
            "pyspark/delta-spark not installed; skipping uni_detect "
            "(run `uv sync` or `uv sync --group dev` first).",
            file=sys.stderr,
        )
    else:
        try:
            ud_targets, ud_metrics, ud_duration = run_uni_detect(frames)
        except SparkUnavailable as exc:
            print(
                f"Could not start a local Delta-enabled Spark session; skipping uni_detect: {exc}"
            )
        else:
            algorithms["uni_detect"] = {
                "targets": ud_targets,
                "metrics": ud_metrics,
                "duration_seconds": ud_duration,
                "duration_note": None,
            }

    if not algorithms:
        raise RuntimeError("No algorithm could be run -- see the skip messages above.")

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_commit(REPO_ROOT),
        "dataset": "real_world_gov",
        "source": "https://github.com/LUH-DBS/Matelda/tree/main/datasets/DGov_NTR",
        "datasets_used": list(DATASETS),
        "algorithms": algorithms,
    }


def _print_comparison(current: dict, baseline: dict | None) -> str:
    from common.comparison import comparison_table_markdown

    lines = ["## real_world_gov benchmark results", ""]
    lines.append(f"Commit: `{current['git_commit']}`  ")
    if baseline:
        lines.append(f"Baseline commit: `{baseline.get('git_commit', 'unknown')}`")
    lines.append("")
    lines.append("### Algorithm comparison")
    lines.append("")
    lines.append(comparison_table_markdown(current["algorithms"]))
    lines.append("")

    header = "| Metric | Current | Baseline | Delta |" if baseline else "| Metric | Current |"
    sep = "|---|---|---|---|" if baseline else "|---|---|"

    def _row(label: str, cur_metrics: dict, base_metrics: dict | None) -> None:
        for key in ("precision", "recall", "f1", "accuracy"):
            cur_val = cur_metrics.get(key, 0.0)
            if baseline and base_metrics is not None:
                base_val = base_metrics.get(key, 0.0)
                delta = cur_val - base_val
                arrow = "▲" if delta > 1e-9 else ("▼" if delta < -1e-9 else "=")
                lines.append(
                    f"| {label} {key} | {cur_val:.3f} | {base_val:.3f} | {arrow} {delta:+.3f} |"
                )
            else:
                lines.append(f"| {label} {key} | {cur_val:.3f} |")

    for algo_name, entry in current["algorithms"].items():
        lines.append("")
        lines.append(f"### `{algo_name}`")
        lines.append("")
        lines.append(header)
        lines.append(sep)
        base_entry = baseline["algorithms"].get(algo_name) if baseline else None
        base_overall = base_entry["metrics"]["overall"] if base_entry else None
        _row("overall", entry["metrics"]["overall"], base_overall)
        for name in current["datasets_used"]:
            cur = entry["metrics"]["by_dataset"].get(name, {})
            base = base_entry["metrics"]["by_dataset"].get(name) if base_entry else None
            _row(name, cur, base)

    text = "\n".join(lines)
    print(text)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="Overwrite results/baseline.json with this run's results.",
    )
    args = parser.parse_args()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    results = run()

    LATEST_FILE.write_text(json.dumps(results, indent=2) + "\n")

    baseline = json.loads(BASELINE_FILE.read_text()) if BASELINE_FILE.exists() else None
    summary = _print_comparison(results, baseline)

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write(summary + "\n")

    if args.update_baseline:
        BASELINE_FILE.write_text(json.dumps(results, indent=2) + "\n")
        print(f"\nUpdated {BASELINE_FILE}")

        subprocess.run(
            [sys.executable, str(BENCHMARK_DIR / "generate_report.py")],
            cwd=REPO_ROOT,
            check=True,
        )
        print(
            "Regenerated results/REPORT.md and results/charts/ -- "
            "remember to `git add` them alongside baseline.json"
        )


if __name__ == "__main__":
    main()
