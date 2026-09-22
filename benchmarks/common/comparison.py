"""Cross-algorithm comparison table + chart rendering.

Shared by every benchmark that scores more than one registered
``unidetect.algorithms`` algorithm against the same targets -- which is
possible at all only because every algorithm's result is normalized into the
same shape (see ``unidetect/algorithms/base.py::AlgorithmResult``). Each
benchmark's ``run_benchmark.py`` produces a results JSON with an
``"algorithms"`` map of ``{name: {"metrics": {"overall": {...}, ...},
"duration_seconds": float | None, "duration_note": str | None}}``; this
module turns that map into a single comparison table/chart pair instead of
every benchmark's ``generate_report.py`` reimplementing the same rendering.
"""

from __future__ import annotations

from collections.abc import Mapping


def comparison_table_markdown(algorithms: Mapping[str, Mapping[str, object]]) -> str:
    """One row per algorithm: n, precision, recall, F1, accuracy, wall-clock duration.

    An algorithm whose ``duration_seconds`` is ``None`` (not measured in this
    run's environment -- see ``duration_note``) shows "n/a" with a footnote
    rather than a fabricated number.
    """
    lines = [
        "| Algorithm | n | Precision | Recall | F1 | Accuracy | Duration (s) |",
        "|---|---|---|---|---|---|---|",
    ]
    notes: list[str] = []
    for name, entry in algorithms.items():
        m = entry["metrics"]["overall"]  # type: ignore[index]
        duration = entry.get("duration_seconds")
        if duration is None:
            note = entry.get("duration_note")
            marker = f"n/a[^{name}]" if note else "n/a"
            if note:
                notes.append(f"[^{name}]: {note}")
            duration_str = marker
        else:
            duration_str = f"{duration:.2f}"
        lines.append(
            f"| `{name}` | {m['n']} | {m['precision']:.3f} | {m['recall']:.3f} | "
            f"{m['f1']:.3f} | {m['accuracy']:.3f} | {duration_str} |"
        )
    text = "\n".join(lines)
    if notes:
        text += "\n\n" + "\n".join(notes)
    return text


def comparison_charts(
    algorithms: Mapping[str, Mapping[str, object]],
) -> tuple[str, str | None]:
    """Return ``(f1_chart_svg, duration_chart_svg)``.

    ``duration_chart_svg`` is ``None`` when no algorithm in ``algorithms`` has
    a measured duration, rather than a chart with fabricated zero bars.
    """
    from common.charts import AQUA, BLUE, grouped_bar_chart

    names = list(algorithms)
    f1_values = [algorithms[n]["metrics"]["overall"]["f1"] for n in names]  # type: ignore[index]
    f1_chart = grouped_bar_chart(
        [f"`{n}`" for n in names],
        {"F1": f1_values},
        {"F1": AQUA},
        title="F1 score by algorithm",
        y_max=1.0,
    )

    measured: dict[str, float] = {
        n: algorithms[n]["duration_seconds"]  # type: ignore[misc]
        for n in names
        if algorithms[n].get("duration_seconds") is not None
    }
    duration_chart = None
    if measured:
        duration_chart = grouped_bar_chart(
            [f"`{n}`" for n in measured],
            {"Duration (s)": list(measured.values())},
            {"Duration (s)": BLUE},
            title="Wall-clock duration by algorithm",
            subtitle="Lower is faster. Algorithms with no measured duration in this run are omitted.",
            value_fmt=lambda v: f"{v:.1f}s",
        )
    return f1_chart, duration_chart
