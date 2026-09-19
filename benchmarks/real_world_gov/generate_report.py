"""Renders a real_world_gov results JSON (see ``run_benchmark.py``) as a
human-readable Markdown report with SVG charts.

Usage::

    uv run python benchmarks/real_world_gov/generate_report.py
    uv run python benchmarks/real_world_gov/generate_report.py --input results/latest.json

Defaults to rendering ``results/baseline.json`` into ``results/REPORT.md``
and ``results/charts/*.svg``. Pure stdlib -- no plotting library required.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BENCHMARK_DIR = Path(__file__).parent
RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"

sys.path.insert(0, str(BENCHMARK_DIR.parent))
from common.charts import AQUA, BLUE, grouped_bar_chart  # noqa: E402


def _overall_metrics_chart(results: dict) -> str:
    overall = results["metrics"]["overall"]
    groups = ["Precision", "Recall", "F1", "Accuracy"]
    keys = ["precision", "recall", "f1", "accuracy"]
    return grouped_bar_chart(
        groups,
        {"score": [overall[k] for k in keys]},
        {"score": BLUE},
        title="Overall metrics",
        subtitle=f"n = {overall['n']} evaluated columns across {len(results['datasets_used'])} datasets",
        y_max=1.0,
    )


def _by_dataset_chart(results: dict) -> str:
    by_dataset = results["metrics"]["by_dataset"]
    datasets = results["datasets_used"]
    return grouped_bar_chart(
        [_short_name(d) for d in datasets],
        {"F1": [by_dataset.get(d, {}).get("f1", 0.0) for d in datasets]},
        {"F1": AQUA},
        title="F1 score by dataset",
        y_max=1.0,
        width=760,
    )


def _short_name(dataset: str) -> str:
    # Keep chart x-axis labels readable; full names are in the tables below.
    return dataset if len(dataset) <= 24 else dataset[:21] + "..."


def _fmt_pct(value: float) -> str:
    return f"{value:.3f}"


def _metrics_table_row(label: str, m: dict) -> str:
    return (
        f"| {label} | {m['n']} | {_fmt_pct(m['precision'])} | {_fmt_pct(m['recall'])} | "
        f"{_fmt_pct(m['f1'])} | {_fmt_pct(m['accuracy'])} |"
    )


def render_markdown(results: dict) -> str:
    overall = results["metrics"]["overall"]
    by_dataset = results["metrics"]["by_dataset"]
    datasets = results["datasets_used"]

    lines: list[str] = []
    lines.append("# real_world_gov benchmark results")
    lines.append("")
    lines.append(
        "Human-readable view of the checked-in benchmark run. "
        "See [README.md](README.md) for how this benchmark works, where its "
        "5 datasets came from, and how to regenerate this file."
    )
    lines.append("")
    lines.append(f"**Generated at:** {results.get('generated_at', 'unknown')}  ")
    lines.append(f"**Commit:** `{results.get('git_commit', 'unknown')}`  ")
    lines.append(f"**Source:** {results.get('source', 'unknown')}")
    lines.append("")

    lines.append("## Overall")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Columns evaluated | {overall['n']} |")
    lines.append(f"| Datasets | {len(datasets)} |")
    lines.append(f"| Precision | {_fmt_pct(overall['precision'])} |")
    lines.append(f"| Recall | {_fmt_pct(overall['recall'])} |")
    lines.append(f"| F1 | {_fmt_pct(overall['f1'])} |")
    lines.append(f"| Accuracy | {_fmt_pct(overall['accuracy'])} |")
    lines.append("")
    lines.append("![Overall metrics](charts/overall_metrics.svg)")
    lines.append("")

    lines.append("## By dataset")
    lines.append("")
    lines.append(
        "One row per source dataset (see [README.md](README.md) for what each one is and "
        "a link to its place in the source repository)."
    )
    lines.append("")
    lines.append("| Dataset | n | Precision | Recall | F1 | Accuracy |")
    lines.append("|---|---|---|---|---|---|")
    lines.append(_metrics_table_row("**overall**", overall))
    for name in datasets:
        if name in by_dataset:
            lines.append(_metrics_table_row(f"`{name}`", by_dataset[name]))
    lines.append("")
    lines.append("![F1 by dataset](charts/f1_by_dataset.svg)")
    lines.append("")

    lines.append("## Evaluated columns")
    lines.append("")
    lines.append(
        "One row per column of one of the 5 dirty tables. `Errors` is how many cells "
        "`clean_changes.csv` records as corrupted in that column; `Expected` is "
        "`Errors > 0`. `Matched via` is which of the four error-type detectors "
        "produced the column's best (lowest `lr_ratio`) candidate, if any."
    )
    lines.append("")
    lines.append(
        "| Dataset | Column | Rows | Errors | Expected | Predicted | lr_ratio | Matched via | Result |"
    )
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for t in results["targets"]:
        result_mark = "✅" if t["predicted_significant"] == t["expected_significant"] else "❌"
        lr = f"{t['lr_ratio']:.4f}" if t.get("lr_ratio") is not None else "n/a"
        matched = t.get("matched_error_type") or "n/a"
        lines.append(
            f"| `{t['dataset']}` | `{t['column']}` | {t['num_rows']} | {t['error_count']} | "
            f"{t['expected_significant']} | {t['predicted_significant']} | {lr} | `{matched}` | "
            f"{result_mark} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("_Regenerate this file (and the charts above) from a results JSON with:_")
    lines.append("")
    lines.append("```bash")
    lines.append("uv run python benchmarks/real_world_gov/generate_report.py")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def write_report(results: dict, output_dir: Path) -> None:
    charts_dir = output_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    (charts_dir / "overall_metrics.svg").write_text(_overall_metrics_chart(results) + "\n")
    (charts_dir / "f1_by_dataset.svg").write_text(_by_dataset_chart(results) + "\n")

    (output_dir / "REPORT.md").write_text(render_markdown(results) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default=str(BASELINE_FILE),
        help="Path to a benchmark results JSON (default: results/baseline.json).",
    )
    parser.add_argument(
        "--output-dir",
        default=str(RESULTS_DIR),
        help="Directory to write REPORT.md and charts/ into (default: results).",
    )
    args = parser.parse_args()

    results = json.loads(Path(args.input).read_text())
    output_dir = Path(args.output_dir)
    write_report(results, output_dir)
    print(f"Wrote {output_dir / 'REPORT.md'} and {output_dir / 'charts'}/*.svg")


if __name__ == "__main__":
    main()
