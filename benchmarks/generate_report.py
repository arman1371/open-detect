"""Renders a benchmark results JSON (see ``run_benchmark.py``) as a
human-readable Markdown report with SVG charts, so people can see the
WIKI-subset benchmark results at a glance without reading raw JSON.

Usage::

    uv run python benchmarks/generate_report.py
    uv run python benchmarks/generate_report.py --input benchmarks/results/latest.json

Defaults to rendering ``benchmarks/results/baseline.json`` (the checked-in
reference run) into ``benchmarks/results/REPORT.md`` and
``benchmarks/results/charts/*.svg``. Pure stdlib -- no plotting library
required.
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Callable
from pathlib import Path

BENCHMARK_DIR = Path(__file__).parent
RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"

ERROR_TYPES = [
    "uniqueness",
    "numeric_outlier",
    "spelling",
    "functional_dependency",
]

#: Display order for severity levels, easiest-to-call to hardest. Kept in
#: sync with ``run_benchmark.py::SEVERITIES`` and ``generate_dataset.py``.
SEVERITIES = ["paper_example", "obvious", "moderate", "subtle", "clean"]

SEVERITY_LABELS = {
    "paper_example": "paper example",
    "obvious": "obvious corruption",
    "moderate": "moderate corruption",
    "subtle": "subtle corruption",
    "clean": "clean (no injection)",
}

# Colors are the validated categorical/chrome slots from the dataviz skill's
# reference palette (light mode) -- see benchmarks/README.md.
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
SURFACE = "#fcfcfb"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
YELLOW = "#eda100"
FONT = "system-ui, -apple-system, 'Segoe UI', sans-serif"


def _nice_ceiling(value: float) -> float:
    if value <= 0:
        return 1.0
    step = 0.1 if value <= 1 else (0.5 if value <= 5 else 1.0)
    return math.ceil(value / step) * step


def _rounded_top_rect(x: float, y: float, w: float, h: float, r: float) -> str:
    """A bar path rounded at the top (far end from the baseline) only."""
    r = min(r, w / 2, h) if h > 0 else 0
    if r <= 0:
        return f"M {x},{y} h {w} v {h} h {-w} Z"
    return (
        f"M {x},{y + r} "
        f"Q {x},{y} {x + r},{y} "
        f"L {x + w - r},{y} "
        f"Q {x + w},{y} {x + w},{y + r} "
        f"L {x + w},{y + h} "
        f"L {x},{y + h} Z"
    )


def grouped_bar_chart(
    groups: list[str],
    series: dict[str, list[float]],
    colors: dict[str, str],
    title: str,
    subtitle: str | None = None,
    value_fmt: Callable[[float], str] = lambda v: f"{v:.2f}",
    y_max: float | None = None,
    width: int = 720,
) -> str:
    n_groups = len(groups)
    n_series = len(series)
    all_values = [v for vals in series.values() for v in vals]
    y_max = y_max if y_max is not None else _nice_ceiling(max(all_values, default=1.0))

    has_legend = n_series > 1
    margin_left = 44
    margin_right = 20
    margin_top = 54 if subtitle else 40
    margin_bottom = 56 + (24 if has_legend else 0)
    height = 380
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom

    group_w = plot_w / n_groups
    group_pad = group_w * 0.22
    bars_w = group_w - group_pad
    bar_gap = 3.0
    bar_w = (bars_w - bar_gap * (n_series - 1)) / n_series

    parts: list[str] = []
    parts.append(
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="{FONT}" role="img" aria-label="{title}">'
    )
    parts.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{SURFACE}"/>')
    parts.append(
        f'<text x="{margin_left}" y="24" font-size="15" font-weight="600" fill="{INK}">'
        f"{title}</text>"
    )
    if subtitle:
        parts.append(
            f'<text x="{margin_left}" y="40" font-size="11.5" fill="{MUTED}">{subtitle}</text>'
        )

    # Gridlines + y-axis ticks (5 bands).
    n_ticks = 5
    for i in range(n_ticks + 1):
        frac = i / n_ticks
        gy = margin_top + plot_h - frac * plot_h
        val = frac * y_max
        parts.append(
            f'<line x1="{margin_left}" y1="{gy:.1f}" x2="{margin_left + plot_w}" '
            f'y2="{gy:.1f}" stroke="{GRID}" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{margin_left - 8}" y="{gy + 3.5:.1f}" font-size="10.5" '
            f'fill="{MUTED}" text-anchor="end">{val:.2f}</text>'
        )

    # Baseline / axis.
    baseline_y = margin_top + plot_h
    parts.append(
        f'<line x1="{margin_left}" y1="{baseline_y:.1f}" x2="{margin_left + plot_w}" '
        f'y2="{baseline_y:.1f}" stroke="{AXIS}" stroke-width="1.25"/>'
    )

    for gi, group in enumerate(groups):
        group_x0 = margin_left + gi * group_w + group_pad / 2
        for si, (name, values) in enumerate(series.items()):
            val = values[gi]
            bar_h = 0.0 if y_max == 0 else (val / y_max) * plot_h
            bx = group_x0 + si * (bar_w + bar_gap)
            by = baseline_y - bar_h
            color = colors[name]
            path = _rounded_top_rect(bx, by, bar_w, bar_h, r=4)
            parts.append(f'<path d="{path}" fill="{color}"/>')
            label_y = by - 5
            parts.append(
                f'<text x="{bx + bar_w / 2:.1f}" y="{label_y:.1f}" font-size="10.5" '
                f'fill="{INK_SECONDARY}" text-anchor="middle">{value_fmt(val)}</text>'
            )
        # Category label.
        parts.append(
            f'<text x="{group_x0 + bars_w / 2:.1f}" y="{baseline_y + 18:.1f}" '
            f'font-size="11" fill="{INK_SECONDARY}" text-anchor="middle">{group}</text>'
        )

    if has_legend:
        legend_y = height - 16
        # Center the legend row.
        item_widths = [14 + 6 + 7 * len(name) + 18 for name in series]
        total_w = sum(item_widths)
        lx = margin_left + max(0, (plot_w - total_w) / 2)
        for (name, _), iw in zip(series.items(), item_widths, strict=True):
            parts.append(
                f'<rect x="{lx:.1f}" y="{legend_y - 10:.1f}" width="11" height="11" '
                f'rx="2.5" fill="{colors[name]}"/>'
            )
            parts.append(
                f'<text x="{lx + 17:.1f}" y="{legend_y - 1:.1f}" font-size="11" '
                f'fill="{INK_SECONDARY}">{name}</text>'
            )
            lx += iw

    parts.append("</svg>")
    return "\n".join(parts)


def _overall_metrics_chart(results: dict) -> str:
    overall = results["metrics"]["overall"]
    groups = ["Precision", "Recall", "F1", "Accuracy"]
    keys = ["precision", "recall", "f1", "accuracy"]
    colors = {"score": BLUE}
    series = {"score": [overall[k] for k in keys]}
    return grouped_bar_chart(
        groups,
        series,
        colors,
        title="Overall metrics",
        subtitle=f"n = {overall['n']} evaluation targets",
        y_max=1.0,
    )


def _f1_by_error_type_chart(results: dict) -> str:
    by_type = results["metrics"]["by_error_type"]
    groups = ["overall"] + ERROR_TYPES
    values = [results["metrics"]["overall"]["f1"]] + [
        by_type.get(et, {}).get("f1", 0.0) for et in ERROR_TYPES
    ]
    return grouped_bar_chart(
        groups,
        {"F1": values},
        {"F1": AQUA},
        title="F1 score by error type",
        y_max=1.0,
    )


def _severity_chart(results: dict) -> str:
    # Precision/recall are degenerate for severity tiers that are entirely
    # one ground-truth class ("obvious"/"moderate"/"subtle" contain only
    # true-positive targets; "clean" contains only true-negative targets),
    # so plotting them per severity would show a meaningless 0/1 artifact
    # rather than a real precision or recall measurement. Accuracy is
    # well-defined in every tier -- it reduces to recall on a pure-TP tier
    # and to the true-negative rate on the pure-FP "clean" tier -- so it's
    # the one metric that is comparable across the whole severity axis.
    by_severity = results["metrics"].get("by_severity", {})
    groups = [s for s in SEVERITIES if s in by_severity]
    return grouped_bar_chart(
        [SEVERITY_LABELS.get(s, s) for s in groups],
        {"Accuracy": [by_severity[s]["accuracy"] for s in groups]},
        {"Accuracy": AQUA},
        title="Accuracy by corruption severity",
        subtitle="How detection holds up as injected errors get harder to spot "
        "(or, for 'clean', how often genuinely clean data is left alone)",
        y_max=1.0,
    )


def _ranking_chart(results: dict) -> str:
    ranking = results["metrics"]["ranking"]
    groups = [et for et in ERROR_TYPES if et in ranking]
    tp_vals = [ranking[et]["true_positive_lr_ratio"] for et in groups]
    fp_vals = [ranking[et]["false_positive_lr_ratio"] for et in groups]
    return grouped_bar_chart(
        groups,
        {"true error (lower = more surprising)": tp_vals, "false positive": fp_vals},
        {
            "true error (lower = more surprising)": BLUE,
            "false positive": ORANGE,
        },
        title="Detection ranking: lr_ratio",
        subtitle="A correctly ranked pair has a shorter blue bar than orange",
        value_fmt=lambda v: f"{v:.3f}",
    )


def _fmt_pct(value: float) -> str:
    return f"{value:.3f}"


def _metrics_table_row(label: str, m: dict) -> str:
    return (
        f"| {label} | {m['n']} | {_fmt_pct(m['precision'])} | {_fmt_pct(m['recall'])} | "
        f"{_fmt_pct(m['f1'])} | {_fmt_pct(m['accuracy'])} |"
    )


def render_markdown(results: dict) -> str:
    overall = results["metrics"]["overall"]
    by_type = results["metrics"]["by_error_type"]
    ranking = results["metrics"]["ranking"]

    lines: list[str] = []
    lines.append("# WIKI-subset benchmark results")
    lines.append("")
    lines.append(
        "Human-readable view of the checked-in benchmark run. "
        "See [benchmarks/README.md](../README.md) for how this benchmark works "
        "and how to regenerate this file."
    )
    lines.append("")
    lines.append(f"**Generated at:** {results.get('generated_at', 'unknown')}  ")
    lines.append(f"**Commit:** `{results.get('git_commit', 'unknown')}`  ")
    lines.append(f"**Dataset:** {results.get('dataset', 'unknown')}")
    lines.append("")

    lines.append("## Overall")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Targets evaluated | {overall['n']} |")
    lines.append(f"| Precision | {_fmt_pct(overall['precision'])} |")
    lines.append(f"| Recall | {_fmt_pct(overall['recall'])} |")
    lines.append(f"| F1 | {_fmt_pct(overall['f1'])} |")
    lines.append(f"| Accuracy | {_fmt_pct(overall['accuracy'])} |")
    lines.append("")
    lines.append("![Overall metrics](charts/overall_metrics.svg)")
    lines.append("")

    lines.append("## By error type")
    lines.append("")
    lines.append("| Error type | n | Precision | Recall | F1 | Accuracy |")
    lines.append("|---|---|---|---|---|---|")
    lines.append(_metrics_table_row("**overall**", overall))
    for et in ERROR_TYPES:
        if et in by_type:
            lines.append(_metrics_table_row(f"`{et}`", by_type[et]))
    lines.append("")
    lines.append("![F1 by error type](charts/f1_by_error_type.svg)")
    lines.append("")

    by_severity = results["metrics"].get("by_severity", {})
    if by_severity:
        lines.append("## By corruption severity")
        lines.append("")
        lines.append(
            "How detection holds up as injected errors get harder to spot. "
            "`paper_example` are the paper's own canonical worked examples "
            "(a mix of true- and false-positive shapes); `obvious`/`moderate`/`subtle` "
            "are true-positive targets with graded, programmatically-injected "
            "corruption; `clean` are false-positive shapes with no injected error at "
            "all. Precision/recall are not shown here because most of these tiers are "
            "single-class by construction (see [benchmarks/README.md](../README.md)) "
            "-- accuracy is the one metric that is meaningful across all of them."
        )
        lines.append("")
        lines.append("| Severity | n | TP | FP | FN | TN | Accuracy |")
        lines.append("|---|---|---|---|---|---|---|")
        for severity in SEVERITIES:
            if severity not in by_severity:
                continue
            m = by_severity[severity]
            lines.append(
                f"| `{severity}` | {m['n']} | {m['true_positive']} | {m['false_positive']} | "
                f"{m['false_negative']} | {m['true_negative']} | {_fmt_pct(m['accuracy'])} |"
            )
        lines.append("")
        lines.append("![Accuracy by corruption severity](charts/severity_accuracy.svg)")
        lines.append("")

    lines.append("## Ranking correctness")
    lines.append("")
    lines.append(
        "For each error type: is the true-positive (genuine error) target scored "
        "as *more surprising* (lower `lr_ratio`) than the false-positive target? "
        "This is the paper's central claim."
    )
    lines.append("")
    lines.append("| Error type | TP lr_ratio | FP lr_ratio | Correctly ranked |")
    lines.append("|---|---|---|---|")
    for et in ERROR_TYPES:
        if et in ranking:
            info = ranking[et]
            mark = "✅" if info["correctly_ranked"] else "❌"
            lines.append(
                f"| `{et}` | {info['true_positive_lr_ratio']:.4f} | "
                f"{info['false_positive_lr_ratio']:.4f} | {mark} |"
            )
    lines.append("")
    lines.append("![Detection ranking](charts/ranking_lr_ratio.svg)")
    lines.append("")

    lines.append("## Evaluation targets")
    lines.append("")
    lines.append(
        "| Target | Error type | Severity | Expected | Predicted | lr_ratio | Result | "
        "Description |"
    )
    lines.append("|---|---|---|---|---|---|---|---|")
    for t in results["targets"]:
        result_mark = "✅" if t["predicted_significant"] == t["expected_significant"] else "❌"
        lr = f"{t['lr_ratio']:.4f}" if t.get("lr_ratio") is not None else "n/a"
        lines.append(
            f"| `{t['id']}` | `{t['error_type']}` | `{t.get('severity', 'unknown')}` | "
            f"{t['expected_significant']} | {t['predicted_significant']} | {lr} | "
            f"{result_mark} | {t['description']} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("_Regenerate this file (and the charts above) from a results JSON with:_")
    lines.append("")
    lines.append("```bash")
    lines.append("uv run python benchmarks/generate_report.py")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def write_report(results: dict, output_dir: Path) -> None:
    charts_dir = output_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    (charts_dir / "overall_metrics.svg").write_text(_overall_metrics_chart(results) + "\n")
    (charts_dir / "f1_by_error_type.svg").write_text(_f1_by_error_type_chart(results) + "\n")
    if results["metrics"].get("by_severity"):
        (charts_dir / "severity_accuracy.svg").write_text(_severity_chart(results) + "\n")
    (charts_dir / "ranking_lr_ratio.svg").write_text(_ranking_chart(results) + "\n")

    (output_dir / "REPORT.md").write_text(render_markdown(results) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default=str(BASELINE_FILE),
        help="Path to a benchmark results JSON (default: benchmarks/results/baseline.json).",
    )
    parser.add_argument(
        "--output-dir",
        default=str(RESULTS_DIR),
        help="Directory to write REPORT.md and charts/ into (default: benchmarks/results).",
    )
    args = parser.parse_args()

    results = json.loads(Path(args.input).read_text())
    output_dir = Path(args.output_dir)
    write_report(results, output_dir)
    print(f"Wrote {output_dir / 'REPORT.md'} and {output_dir / 'charts'}/*.svg")


if __name__ == "__main__":
    main()
