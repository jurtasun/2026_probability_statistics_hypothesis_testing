import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

def square_wave(x):
    return np.where(np.sin(x) >= 0, 1, -1)

def fourier_series_square(x, N):
    s = np.zeros_like(x)
    for k in range(1, N+1, 2):
        s += (4/np.pi) * (1/k) * np.sin(k*x)
    return s

x = np.linspace(-np.pi, np.pi, 1000)
terms_list = [1, 3, 7]

for i, N in enumerate(terms_list, start=1):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    y = fourier_series_square(x, N)
    ax.plot(x, y, color='firebrick', lw=2)
    ax.plot(x, square_wave(x), color='black', lw=1, alpha=0.3, linestyle='--')

    # ax.set_title(f"{N} Terms", fontsize=14)
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-1.5, 1.5)

    for spine in ax.spines.values():
        spine.set_visible(False)

    # Dashed black rectangle border matching axes
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax.plot([xlim[0], xlim[1]], [ylim[0], ylim[0]], 'k--', lw=1)
    ax.plot([xlim[0], xlim[1]], [ylim[1], ylim[1]], 'k--', lw=1)
    ax.plot([xlim[0], xlim[0]], [ylim[0], ylim[1]], 'k--', lw=1)
    ax.plot([xlim[1], xlim[1]], [ylim[0], ylim[1]], 'k--', lw=1)

    # Axes arrows
    ax.annotate("", xy=(np.pi*1.05, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
    ax.annotate("", xy=(0, 1.7), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

    ax.set_xticks([-np.pi, 0, np.pi])
    ax.set_xticklabels([r"$-\pi$", r"$0$", r"$\pi$"], fontsize=13)
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels([r"$-1$", r"$0$", r"$1$"], fontsize=13)

    ax.grid(True, linestyle='--', alpha=0.3)
    ax.tick_params(axis='both', direction='in', length=4, width=1)

    plt.tight_layout()
    filename = f"fourier_series_{i}.png"
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
