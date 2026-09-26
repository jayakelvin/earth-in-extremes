"""Plot the preliminary IMD reference track for Cyclonic Storm Senyar.

The figure is a visual quality-control product. It combines the extracted
positions with the reported wind and central-pressure series; it does not
interpolate the track or add operational-advisory positions.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib as mpl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator
import pandas as pd


CASE_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = CASE_ROOT / "data" / "processed" / "imd_senyar_track_preliminary.csv"
DEFAULT_OUTPUT_DIR = CASE_ROOT / "figures"

FONT_REGULAR = Path(r"C:\Windows\Fonts\LEELAWAD.TTF")
FONT_BOLD = Path(r"C:\Windows\Fonts\LEELAWDB.TTF")

LAND = "#ece8df"
OCEAN = "#f7fafb"
COAST = "#4a4a4a"
GRID = "#c9ced1"
INK = "#202124"
MUTED = "#666a70"
GRADE_STYLE = {
    "D": {"label": "Depression", "color": "#0072B2", "marker": "o"},
    "DD": {"label": "Deep depression", "color": "#E69F00", "marker": "s"},
    "CS": {"label": "Cyclonic storm", "color": "#D55E00", "marker": "D"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def configure_style() -> None:
    """Apply a compact journal-style configuration using Leelawadee."""
    for font_path in (FONT_REGULAR, FONT_BOLD):
        if not font_path.exists():
            raise FileNotFoundError(f"Required Leelawadee font not found: {font_path}")
        fontManager.addfont(font_path)

    font_name = FontProperties(fname=FONT_REGULAR).get_name()
    mpl.rcParams.update(
        {
            "font.family": font_name,
            "font.size": 6.5,
            "axes.labelsize": 6.5,
            "axes.titlesize": 7.0,
            "axes.titleweight": "bold",
            "xtick.labelsize": 6.0,
            "ytick.labelsize": 6.0,
            "legend.fontsize": 6.0,
            "axes.linewidth": 0.55,
            "lines.linewidth": 1.0,
            "xtick.major.width": 0.5,
            "ytick.major.width": 0.5,
            "xtick.major.size": 2.5,
            "ytick.major.size": 2.5,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
            "savefig.facecolor": "white",
        }
    )


def load_track(path: Path) -> pd.DataFrame:
    track = pd.read_csv(path, parse_dates=["time_utc"])
    required = {
        "time_utc",
        "latitude_deg_n",
        "longitude_deg_e",
        "central_pressure_hpa",
        "maximum_sustained_wind_kt",
        "grade",
    }
    missing = required.difference(track.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    if track.empty:
        raise ValueError("The processed track is empty")
    if track["time_utc"].duplicated().any() or not track["time_utc"].is_monotonic_increasing:
        raise ValueError("Track timestamps must be unique and strictly increasing")
    unknown_grades = set(track["grade"].dropna()).difference(GRADE_STYLE)
    if unknown_grades:
        raise ValueError(f"Unsupported grade values: {', '.join(sorted(unknown_grades))}")
    return track


def panel_label(ax: mpl.axes.Axes, label: str) -> None:
    ax.text(
        -0.08,
        1.035,
        label,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8,
        fontweight="bold",
        color=INK,
    )


def plot_map(ax: mpl.axes.Axes, track: pd.DataFrame) -> None:
    transform = ccrs.PlateCarree()
    ax.set_extent([97.2, 101.35, 3.25, 5.70], crs=transform)
    ax.set_facecolor(OCEAN)
    ax.add_feature(cfeature.LAND.with_scale("10m"), facecolor=LAND, edgecolor="none", zorder=0)
    ax.add_feature(cfeature.COASTLINE.with_scale("10m"), edgecolor=COAST, linewidth=0.55, zorder=2)
    ax.add_feature(
        cfeature.BORDERS.with_scale("10m"),
        edgecolor="#888888",
        linewidth=0.35,
        linestyle=(0, (2, 1.5)),
        zorder=2,
    )

    gridlines = ax.gridlines(
        crs=transform,
        draw_labels=True,
        xlocs=[98, 99, 100, 101],
        ylocs=[3.5, 4.0, 4.5, 5.0, 5.5],
        linewidth=0.35,
        color=GRID,
        alpha=0.85,
        linestyle=(0, (1, 2)),
    )
    gridlines.top_labels = False
    gridlines.right_labels = False
    gridlines.xlabel_style = {"size": 6, "color": MUTED}
    gridlines.ylabel_style = {"size": 6, "color": MUTED}
    gridlines.xpadding = 2
    gridlines.ypadding = 2

    ax.plot(
        track["longitude_deg_e"],
        track["latitude_deg_n"],
        color=INK,
        linewidth=1.0,
        zorder=4,
        transform=transform,
    )

    for grade, style in GRADE_STYLE.items():
        points = track.loc[track["grade"] == grade]
        ax.scatter(
            points["longitude_deg_e"],
            points["latitude_deg_n"],
            s=23,
            marker=style["marker"],
            facecolor=style["color"],
            edgecolor="white",
            linewidth=0.45,
            zorder=5,
            transform=transform,
        )

    # IMD workbook narrative row 271: landfall near 4.900 N, 97.750 E,
    # between 02:00 and 03:00 UTC on 26 November 2025.
    ax.scatter(
        [97.75],
        [4.90],
        s=48,
        marker="X",
        facecolor="white",
        edgecolor=INK,
        linewidth=0.8,
        zorder=6,
        transform=transform,
    )
    ax.annotate(
        "Landfall\n26 Nov, 02–03 UTC",
        xy=(97.75, 4.90),
        xytext=(18, 11),
        textcoords="offset points",
        fontsize=6,
        color=INK,
        ha="left",
        va="bottom",
        arrowprops={"arrowstyle": "-", "color": MUTED, "lw": 0.5},
        zorder=7,
    )

    first = track.iloc[0]
    last = track.iloc[-1]
    ax.annotate(
        "Start\n25 Nov, 03 UTC",
        xy=(first["longitude_deg_e"], first["latitude_deg_n"]),
        xytext=(-7, 12),
        textcoords="offset points",
        fontsize=6,
        ha="right",
        va="bottom",
        color=INK,
    )
    ax.annotate(
        "Last position\n27 Nov, 15 UTC",
        xy=(last["longitude_deg_e"], last["latitude_deg_n"]),
        xytext=(-5, 12),
        textcoords="offset points",
        fontsize=6,
        ha="right",
        va="bottom",
        color=INK,
    )

    ax.text(
        0.02,
        0.025,
        "SUMATRA",
        transform=ax.transAxes,
        fontsize=6,
        fontweight="bold",
        color="#77736b",
        rotation=22,
        ha="left",
        va="bottom",
    )
    ax.text(
        0.77,
        0.51,
        "MALAY\nPENINSULA",
        transform=ax.transAxes,
        fontsize=6,
        fontweight="bold",
        color="#77736b",
        ha="center",
        va="center",
    )
    ax.text(
        0.55,
        0.72,
        "Strait of Malacca",
        transform=ax.transAxes,
        fontsize=6,
        fontstyle="italic",
        color="#65727a",
        rotation=-30,
        ha="center",
        va="center",
    )

    handles = [
        Line2D(
            [],
            [],
            linestyle="none",
            marker=style["marker"],
            markersize=4.5,
            markerfacecolor=style["color"],
            markeredgecolor="white",
            markeredgewidth=0.45,
            label=style["label"],
        )
        for style in GRADE_STYLE.values()
    ]
    handles.append(
        Line2D(
            [],
            [],
            linestyle="none",
            marker="X",
            markersize=5,
            markerfacecolor="white",
            markeredgecolor=INK,
            markeredgewidth=0.8,
            label="Reported landfall",
        )
    )
    ax.legend(
        handles=handles,
        loc="upper right",
        frameon=False,
        handletextpad=0.45,
        labelspacing=0.35,
        borderaxespad=0.55,
    )
    ax.set_title("Track and classification", loc="left", pad=5)
    panel_label(ax, "a")


def style_time_axis(ax: mpl.axes.Axes, track: pd.DataFrame) -> None:
    ax.set_xlim(track["time_utc"].iloc[0], track["time_utc"].iloc[-1])
    ax.xaxis.set_major_locator(mdates.HourLocator(byhour=[0, 12]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b\n%H UTC"))
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color=GRID, linewidth=0.35, linestyle=(0, (1, 2)))
    ax.tick_params(colors=MUTED, labelcolor=INK)


def plot_series(
    ax: mpl.axes.Axes,
    track: pd.DataFrame,
    column: str,
    ylabel: str,
    title: str,
    label: str,
) -> None:
    style_time_axis(ax, track)
    ax.plot(track["time_utc"], track[column], color=INK, linewidth=1.0, zorder=2)
    for grade, style in GRADE_STYLE.items():
        points = track.loc[track["grade"] == grade]
        ax.scatter(
            points["time_utc"],
            points[column],
            s=20,
            marker=style["marker"],
            facecolor=style["color"],
            edgecolor="white",
            linewidth=0.4,
            zorder=3,
        )
    ax.set_ylabel(ylabel, color=INK)
    ax.set_title(title, loc="left", pad=5)
    panel_label(ax, label)


def build_figure(track: pd.DataFrame) -> mpl.figure.Figure:
    projection = ccrs.PlateCarree()
    fig = plt.figure(figsize=(183 / 25.4, 126 / 25.4), constrained_layout=False)
    grid = fig.add_gridspec(
        2,
        2,
        width_ratios=[1.65, 1.0],
        height_ratios=[1, 1],
        left=0.065,
        right=0.985,
        bottom=0.13,
        top=0.965,
        wspace=0.28,
        hspace=0.48,
    )
    map_ax = fig.add_subplot(grid[:, 0], projection=projection)
    wind_ax = fig.add_subplot(grid[0, 1])
    pressure_ax = fig.add_subplot(grid[1, 1])

    plot_map(map_ax, track)
    plot_series(
        wind_ax,
        track,
        "maximum_sustained_wind_kt",
        "Maximum sustained wind (kt)",
        "Intensity",
        "b",
    )
    wind_ax.set_ylim(17, 43)
    wind_ax.yaxis.set_major_locator(MultipleLocator(5))

    plot_series(
        pressure_ax,
        track,
        "central_pressure_hpa",
        "Central pressure (hPa)",
        "Central pressure",
        "c",
    )
    pressure_ax.set_ylim(1006, 997)
    pressure_ax.yaxis.set_major_locator(MultipleLocator(2))
    pressure_ax.set_xlabel("Time (UTC)")

    fig.text(
        0.065,
        0.035,
        "Data: IMD preliminary 2025 best-track workbook. Basemap: Natural Earth 10 m. Values are reported, not interpolated; wind uses the IMD 3-min convention.",
        ha="left",
        va="bottom",
        fontsize=5.5,
        color=MUTED,
    )
    return fig


def main() -> None:
    args = parse_args()
    configure_style()
    track = load_track(args.input)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    figure = build_figure(track)
    output_stem = args.output_dir / "imd_senyar_track_qc"
    figure.savefig(output_stem.with_suffix(".pdf"))
    figure.savefig(output_stem.with_suffix(".svg"))
    figure.savefig(output_stem.with_suffix(".png"), dpi=600)
    plt.close(figure)


if __name__ == "__main__":
    main()
