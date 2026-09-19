"""Pure-stdlib SVG bar-chart rendering shared by every benchmark's report.

Extracted from what used to be ``benchmarks/wiki_subset/generate_report.py``'s own
private chart code so a second (or third) benchmark's ``generate_report.py``
gets the same look (and the same validated color palette, see the dataviz
skill) without copy-pasting the SVG-generation code.
"""

from __future__ import annotations

import math
from collections.abc import Callable

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
