"""Runs the WIKI-subset benchmark for every available registered algorithm
(see ``README.md``): builds corpus statistics from ``data/corpus`` and
scores the labeled targets in ``data/eval/targets.json`` against their known
ground truth.

- **uni_detect** -- builds corpus statistics from ``data/corpus``, then
  scores each target against it (Spark/Delta; requires JDK 17).
- **raha** -- scores each target directly, using the target's own
  ``injected_row_indices`` ground truth (see ``generate_dataset.py``) via a
  local ``KnownIndexLabeler`` (pandas; no Spark/JDK dependency at all).

Usage::

    uv run python benchmarks/wiki_subset/run_benchmark.py
    uv run python benchmarks/wiki_subset/run_benchmark.py --update-baseline

Writes ``results/latest.json`` and, when a baseline exists, prints a
version-over-version comparison (also appended to ``$GITHUB_STEP_SUMMARY``
when running in GitHub Actions).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BENCHMARK_DIR = Path(__file__).parent
REPO_ROOT = BENCHMARK_DIR.parent.parent

sys.path.insert(0, str(BENCHMARK_DIR.parent))
from common.comparison import comparison_table_markdown  # noqa: E402
from common.metrics import confusion_metrics  # noqa: E402
from common.spark_session import SparkUnavailable, git_commit, spark_session  # noqa: E402

DATA_DIR = BENCHMARK_DIR / "data"
CORPUS_DIR = DATA_DIR / "corpus"
TARGETS_FILE = DATA_DIR / "eval" / "targets.json"
RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"
LATEST_FILE = RESULTS_DIR / "latest.json"

TEST_CATALOG = "spark_catalog"
TEST_SCHEMA = "unidetect_benchmark"

ERROR_TYPES = [
    "uniqueness",
    "numeric_outlier",
    "spelling",
    "functional_dependency",
]

#: Corruption-severity levels a target can be tagged with (see
#: ``generate_dataset.py``): the three graded true-positive levels, plus
#: "paper_example" (the paper's own canonical worked examples) and "clean"
#: (a false-positive shape with no injected error at all). Order here is
#: display order, roughly easiest-to-detect/reject to hardest.
SEVERITIES = ["paper_example", "obvious", "moderate", "subtle", "clean"]

#: The paper's own labeling-budget default (Section 6.1); RahaDetector caps
#: it at each target's own row count, so this is effectively "as many labels
#: as the table has, up to 20" -- full supervision on the smallest targets.
RAHA_LABELING_BUDGET = 20


def _load_corpus_tables(spark, error_type: str) -> list[str]:
    import csv as csv_module

    fqns: list[str] = []
    category_dir = CORPUS_DIR / error_type
    for csv_path in sorted(category_dir.glob("*.csv")):
        with csv_path.open(newline="", encoding="utf-8") as fh:
            reader = csv_module.reader(fh)
            header = next(reader)
            rows = [tuple(row) for row in reader]
        table_name = csv_path.stem
        fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.corpus_{error_type}_{table_name}"
        df = spark.createDataFrame(rows, schema=header)
        if error_type == "numeric_outlier":
            from pyspark.sql import functions as F

            df = df.withColumn(header[0], F.col(header[0]).cast("double"))
        df.write.format("delta").mode("overwrite").saveAsTable(fqn)
        fqns.append(fqn)
    return fqns


def _load_targets(spark) -> list[dict]:
    targets = json.loads(TARGETS_FILE.read_text())
    for target in targets:
        fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.target_{target['id']}"
        df = spark.createDataFrame([tuple(r) for r in target["rows"]], schema=target["columns"])
        if target["error_type"] == "numeric_outlier":
            from pyspark.sql import functions as F

            col = target["columns"][0]
            df = df.withColumn(col, F.col(col).cast("double"))
        df.write.format("delta").mode("overwrite").saveAsTable(fqn)
        target["_fqn"] = fqn
    return targets


def _build_config(uc_location):
    from unidetect.config import UniDetectConfig

    return UniDetectConfig(
        location=uc_location,
        epsilon=0.05,
        alpha=0.2,
        max_mpd_block_size=200,
        max_fd_column_pairs_per_table=10,
        # Scaled down from the web-scale defaults to match this benchmark's
        # tens-of-tables corpus, the same reasoning
        # ``tests/test_corpus_and_detectors.py::config`` documents.
        prevalence_edges=(2, 5, 20, 100, 1000),
    )


def run_uni_detect() -> tuple[list[dict], dict, float]:
    """Score every eval target with Uni-Detect. Returns (targets, metrics, duration_seconds)."""
    from unidetect.config import UnityCatalogLocation
    from unidetect.core.enums import ErrorType
    from unidetect.pipeline import UniDetect

    uc_location = UnityCatalogLocation(catalog=TEST_CATALOG, schema=TEST_SCHEMA)
    config = _build_config(uc_location)

    start = time.perf_counter()
    with spark_session(TEST_CATALOG, TEST_SCHEMA) as spark:
        ud = UniDetect(config, spark=spark)
        targets = _load_targets(spark)

        for error_type in ERROR_TYPES:
            corpus_tables = _load_corpus_tables(spark, error_type)
            ud.build_corpus_statistics(
                corpus_tables,
                error_types=[ErrorType(error_type)],
                create_schema=False,
            )

        target_rows: list[dict] = []
        for error_type in ERROR_TYPES:
            type_targets = [t for t in targets if t["error_type"] == error_type]
            if not type_targets:
                continue
            fqns = [t["_fqn"] for t in type_targets]
            result = ud.detect(fqns, error_types=[ErrorType(error_type)]).toPandas()
            for target in type_targets:
                rows = result[result["table_id"] == target["_fqn"]]
                predicted_significant = (
                    bool(rows["is_significant"].any()) if not rows.empty else False
                )
                lr_ratio = float(rows["lr_ratio"].min()) if not rows.empty else None
                target_rows.append(
                    {
                        "id": target["id"],
                        "error_type": error_type,
                        "severity": target.get("severity", "unknown"),
                        "description": target["description"],
                        "expected_significant": target["expected_significant"],
                        "predicted_significant": predicted_significant,
                        "lr_ratio": lr_ratio,
                    }
                )
    duration = time.perf_counter() - start

    overall = confusion_metrics(target_rows)
    by_type = {
        error_type: confusion_metrics([r for r in target_rows if r["error_type"] == error_type])
        for error_type in ERROR_TYPES
    }
    by_severity = {
        severity: confusion_metrics([r for r in target_rows if r["severity"] == severity])
        for severity in SEVERITIES
        if any(r["severity"] == severity for r in target_rows)
    }

    ranking: dict[str, dict] = {}
    for error_type in ERROR_TYPES:
        # Restricted to `severity == "paper_example"`: this check exists to
        # verify the paper's own central claim (a genuine error is *always*
        # scored as more surprising than a superficially-anomalous
        # non-error) on its own canonical worked example pair. Taking the
        # min lr_ratio across *all* severities -- including the
        # deliberately adversarial "clean" false-positive variants added
        # for the broader precision/recall sweep -- would conflate that
        # narrow claim with the much harder question of whether ranking
        # holds against every hand-picked hard case, which is what
        # `by_severity` and `by_error_type` above already measure.
        type_rows = [
            r
            for r in target_rows
            if r["error_type"] == error_type and r["severity"] == "paper_example"
        ]
        tp_rows = [r for r in type_rows if r["expected_significant"] and r["lr_ratio"] is not None]
        fp_rows = [
            r for r in type_rows if not r["expected_significant"] and r["lr_ratio"] is not None
        ]
        if tp_rows and fp_rows:
            tp_ratio = min(r["lr_ratio"] for r in tp_rows)
            fp_ratio = min(r["lr_ratio"] for r in fp_rows)
            ranking[error_type] = {
                "true_positive_lr_ratio": tp_ratio,
                "false_positive_lr_ratio": fp_ratio,
                "correctly_ranked": tp_ratio < fp_ratio,
            }

    return (
        target_rows,
        {
            "overall": overall,
            "by_error_type": by_type,
            "by_severity": by_severity,
            "ranking": ranking,
        },
        duration,
    )


def run_raha() -> tuple[list[dict], dict, dict, float]:
    """Score every eval target with Raha.

    Returns ``(targets, column_metrics, cell_metrics, duration_seconds)``,
    the same shape ``real_world_gov/run_benchmark.py::run_raha`` returns, for
    the same reason: ``column_metrics`` reduces to "was *any* cell of this
    target flagged" -- the same whole-target verdict Uni-Detect's own output
    is -- for the apples-to-apples comparison table, while ``cell_metrics``
    is Raha's native per-cell granularity (the paper's own Table 5
    granularity), scored against ``generate_dataset.py``'s own
    ``injected_row_indices`` ground truth via a local
    :class:`KnownIndexLabeler` rather than a diff against a separate clean
    table (these synthetic targets have no such counterpart -- the generator
    already knows exactly what it injected, so this labeler just exposes
    that same information through Raha's ``Labeler`` interface).
    """
    import pandas as pd

    from unidetect.algorithms.raha import RahaConfig, RahaDetector
    from unidetect.algorithms.raha.labeling import Labeler

    class KnownIndexLabeler(Labeler):
        def __init__(self, target_column: str, injected_indices: set[int]) -> None:
            self._target_column = target_column
            self._injected_indices = injected_indices

        def label_tuple(self, df, row_index):
            is_error = row_index in self._injected_indices
            return {col: (is_error if col == self._target_column else False) for col in df.columns}

    targets = json.loads(TARGETS_FILE.read_text())
    target_rows: list[dict] = []
    cell_rows: list[dict] = []
    start = time.perf_counter()
    for target in targets:
        df = pd.DataFrame(target["rows"], columns=target["columns"])
        # The FD targets' two columns are `[lhs, rhs]`; only the RHS is ever
        # corrupted (see generate_dataset.py's `_target` docstring). Every
        # other error type has exactly one column, so `columns[-1]` is that
        # column too.
        target_column = target["columns"][-1]
        injected = set(target["injected_row_indices"])

        detector = RahaDetector(RahaConfig(labeling_budget=RAHA_LABELING_BUDGET, random_state=0))
        result = detector.detect(
            df, table_id=target["id"], labeler=KnownIndexLabeler(target_column, injected)
        )

        target_rows.append(
            {
                "id": target["id"],
                "error_type": target["error_type"],
                "severity": target.get("severity", "unknown"),
                "description": target["description"],
                "expected_significant": target["expected_significant"],
                "predicted_significant": any(cell.is_error for cell in result),
                "score": max((cell.score for cell in result), default=0.0),
            }
        )
        for cell in result:
            expected = cell.column_name == target_column and cell.row_index in injected
            cell_rows.append(
                {
                    "error_type": target["error_type"],
                    "severity": target.get("severity", "unknown"),
                    "expected_significant": expected,
                    "predicted_significant": cell.is_error,
                }
            )
    duration = time.perf_counter() - start

    def _metrics(rows: list[dict]) -> dict:
        return {
            "overall": confusion_metrics(rows),
            "by_error_type": {
                et: confusion_metrics([r for r in rows if r["error_type"] == et])
                for et in ERROR_TYPES
            },
            "by_severity": {
                s: confusion_metrics([r for r in rows if r["severity"] == s])
                for s in SEVERITIES
                if any(r["severity"] == s for r in rows)
            },
        }

    return target_rows, _metrics(target_rows), _metrics(cell_rows), duration


def run() -> dict:
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
        raha_targets, raha_column_metrics, raha_cell_metrics, raha_duration = run_raha()
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
            ud_targets, ud_metrics, ud_duration = run_uni_detect()
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
        "dataset": "wiki_subset",
        "algorithms": algorithms,
    }


def _print_comparison(current: dict, baseline: dict | None) -> str:
    lines = ["## WIKI-subset benchmark results", ""]
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
        for error_type in ERROR_TYPES:
            cur = entry["metrics"]["by_error_type"].get(error_type, {})
            base = base_entry["metrics"]["by_error_type"].get(error_type) if base_entry else None
            _row(error_type, cur, base)

        if algo_name == "uni_detect":
            lines.append("")
            lines.append("| Error type | correctly ranked (TP more surprising than FP) |")
            lines.append("|---|---|")
            for error_type, info in entry["metrics"]["ranking"].items():
                lines.append(f"| {error_type} | {'yes' if info['correctly_ranked'] else 'NO'} |")

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
            "Regenerated results/REPORT.md and results/charts/ "
            "-- remember to `git add` them alongside baseline.json"
        )


if __name__ == "__main__":
    main()
