import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


text_style = dict(horizontalalignment='right', verticalalignment='center', fontsize=12, fontfamily='monospace')
marker_style = dict(linestyle=':', color='0.8', markersize=10, markerfacecolor="black", markeredgecolor="black")

def format_axes(ax):
    ax.margins(0.2)
    ax.set_axis_off()
    ax.invert_yaxis()

def split_list(a_list):
    i_half = len(a_list) // 2
    return a_list[:i_half], a_list[i_half:]

fig, axs = plt.subplots(ncols=2)

fig.suptitle('Marcadores com preechimento', fontsize=12, y=0.86)

for ax, markers in zip(axs, split_list(Line2D.filled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot([y] * 3, marker=marker, **marker_style)
    format_axes(ax)

plt.savefig('ex03.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)