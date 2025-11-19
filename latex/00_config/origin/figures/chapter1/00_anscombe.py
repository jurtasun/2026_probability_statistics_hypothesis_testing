

import numpy as np
import matplotlib.pyplot as plt

# Parameters for plot
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

# Common function to draw each subplot
def draw_subplot(ax, x, y, fit_fn=None, fit_label=None):
    ax.scatter(x, y, color='firebrick', alpha=0.7, label="Sampling data")
    if fit_fn is not None:
        ax.plot(x, fit_fn(x), color='gray', lw=2, label=fit_label)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.annotate("", xy=(max(x)+0.5, 0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
    ax.annotate("", xy=(0, max(y)+5), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

    ax.set_xlim(-0.5, max(x)+1)
    ax.set_ylim(0, max(y)+10)
    ax.text(max(x)+0.7, -1, r"$x$", fontsize=14, ha='right', va='top')
    ax.text(-0.3, max(y)+5, r"$y$", fontsize=14, ha='left', va='bottom')
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.tick_params(axis='both', direction='in', length=4, width=1)
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.05, 1))



# =========================
# Data for four plots
# =========================
np.random.seed(0)
x1 = np.linspace(0, 10, 100)
y1 = 2.5 * x1 + 3.5 + np.random.normal(0, 3, size=x1.shape)
coeffs1 = np.polyfit(x1, y1, 1)
fit1 = np.poly1d(coeffs1)

np.random.seed(1)
x2 = np.linspace(0, 10, 100)
y2 = 1.2 * x2**2 - 3 * x2 + 4 + np.random.normal(0, 6, size=x2.shape)
coeffs2 = np.polyfit(x2, y2, 2)
fit2 = np.poly1d(coeffs2)

np.random.seed(2)
x3 = np.linspace(0, 10, 150)
y3 = 0.02 * x3**4 - 0.3 * x3**3 + 2 * x3**2 - 5*x3 + 10 + 15*np.sin(1.5*x3) + np.random.normal(0,3,x3.shape)
deg3 = 5
coeffs3 = np.polyfit(x3, y3, deg3)
fit3 = np.poly1d(coeffs3)

np.random.seed(3)
x4 = np.linspace(0, 10, 100)
y4 = np.abs(np.random.normal(5, 5, size=x4.shape))  # Random positive data

# =========================
# Figure with 2x2 grid
# =========================
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
axes = axes.flatten()

draw_subplot(axes[0], x1, y1, fit1, f"Fit: y={coeffs1[0]:.2f}x+{coeffs1[1]:.2f}")
axes[0].set_title("Linear trend", fontsize=14)

draw_subplot(axes[1], x2, y2, fit2, f"Fit: y={coeffs2[0]:.2f}x²+{coeffs2[1]:.2f}x+{coeffs2[2]:.2f}")
axes[1].set_title("Quadratic trend", fontsize=14)

draw_subplot(axes[2], x3, y3, fit3, f"Fit: degree-{deg3} poly")
axes[2].set_title("High-degree polynomial", fontsize=14)

draw_subplot(axes[3], x4, y4)
axes[3].set_title("Random positive data", fontsize=14)

plt.tight_layout()
plt.show()
fig.savefig("anscombe.png", dpi=300, bbox_inches='tight')
fig.savefig("anscombe.pdf", bbox_inches='tight')
