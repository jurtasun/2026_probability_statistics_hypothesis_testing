# Import libraries
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



# =========================
# Linear example
# =========================

# Generate data
np.random.seed(0)
x_points = np.linspace(0, 10, 100)
y_points = 2.5 * x_points + 3.5 + np.random.normal(0, 3, size=x_points.shape)

# Store fit coefficients
coeffs_lin = np.polyfit(x_points, y_points, 1)
fit_fn_lin = np.poly1d(coeffs_lin)

# Plot figure
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.scatter(x_points, y_points, color='firebrick', alpha=0.7, label="Sampling data")
ax.plot(x_points, fit_fn_lin(x_points), color='gray', lw=2,
        label=f"Fit: y(x) = {coeffs_lin[0]:.2f}x + {coeffs_lin[1]:.2f}")

for spine in ax.spines.values():
    spine.set_visible(False)

ax.annotate("", xy=(10.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, max(y_points)+5), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax.set_xlim(-0.5, 11)
ax.set_ylim(min(y_points)-5, max(y_points)+5)
ax.text(10.7, min(y_points)-5.5, r"$x$", fontsize=14, ha='right', va='top')
ax.text(-0.3, max(y_points)+5, r"$y$", fontsize=14, ha='left', va='bottom')
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Legend inside plot
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.05, 1))
plt.tight_layout()
plt.show()

fig.savefig("linear1.png", dpi=300, bbox_inches='tight')
fig.savefig("linear1.pdf", bbox_inches='tight')



# =========================
# Quadratic example
# =========================

# Generate data
np.random.seed(1)
x_points_q = np.linspace(0, 10, 100)
y_points_q = 1.2 * x_points_q**2 - 3 * x_points_q + 4 + np.random.normal(0, 6, size=x_points_q.shape)

# Store fit coefficients
coeffs_quad = np.polyfit(x_points_q, y_points_q, 2)
fit_fn_quad = np.poly1d(coeffs_quad)

# Plot figure
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.scatter(x_points_q, y_points_q, color='firebrick', alpha=0.7, label="Sampling data")
ax.plot(x_points_q, fit_fn_quad(x_points_q), color='gray', lw=2,
        label=f"Fit: y(x) = {coeffs_quad[0]:.2f}x² + {coeffs_quad[1]:.2f}x + {coeffs_quad[2]:.2f}")

for spine in ax.spines.values():
    spine.set_visible(False)

ax.annotate("", xy=(10.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, max(y_points_q)+5), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax.set_xlim(-0.5, 11)
ax.set_ylim(min(y_points_q)-10, max(y_points_q)+10)
ax.text(10.7, min(y_points_q)-10.5, r"$x$", fontsize=14, ha='right', va='top')
ax.text(-0.3, max(y_points_q)+10, r"$y$", fontsize=14, ha='left', va='bottom')
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Legend inside plot
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.05, 1))
plt.tight_layout()
plt.show()

fig.savefig("quadratic1.png", dpi=300, bbox_inches='tight')
fig.savefig("quadratic1.pdf", bbox_inches='tight')



# =========================
# Higher-degree "jiggly" example
# =========================

# Generate data
np.random.seed(2)
x_points_h = np.linspace(0, 10, 150)

# Stronger oscillations
y_points_h = 0.02 * x_points_h**4 - 0.3 * x_points_h**3 + 2 * x_points_h**2 \
             - 5 * x_points_h + 10 + 10*np.sin(1.5*x_points_h) \
             + np.random.normal(0, 3, size=x_points_h.shape)

deg = 5

# Store fit coefficients
coeffs_high = np.polyfit(x_points_h, y_points_h, deg)
fit_fn_high = np.poly1d(coeffs_high)

# Plot figure
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.scatter(x_points_h, y_points_h, color='firebrick', alpha=0.7, label="Sampling data")
ax.plot(x_points_h, fit_fn_high(x_points_h), color='gray', lw=2,
        label=f"Fit: degree-{deg} polynomial")

for spine in ax.spines.values():
    spine.set_visible(False)

ax.annotate("", xy=(10.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, max(y_points_h)+10), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax.set_xlim(-0.5, 11)
ax.set_ylim(min(y_points_h)-15, max(y_points_h)+15)
ax.text(10.7, min(y_points_h)-15.5, r"$x$", fontsize=14, ha='right', va='top')
ax.text(-0.3, max(y_points_h)+15, r"$y$", fontsize=14, ha='left', va='bottom')
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Legend inside plot
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.05, 1))
plt.tight_layout()
plt.show()

fig.savefig("polynomial1.png", dpi=300, bbox_inches='tight')
fig.savefig("polynomial1.pdf", bbox_inches='tight')



# =========================
# Random/no apparent dependency example
# =========================

# Generate data
np.random.seed(3)
x_points_r = np.linspace(0, 10, 100)
y_points_r = np.abs(np.random.normal(5, 5, size=x_points_r.shape))  # All positive y values

# Plot figure
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.scatter(x_points_r, y_points_r, color='firebrick', alpha=0.7, label="Random data")

for spine in ax.spines.values():
    spine.set_visible(False)

ax.annotate("", xy=(10.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, max(y_points_r)+5), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax.set_xlim(-0.5, 11)
ax.set_ylim(0, max(y_points_r)+5)  # Ensure y-axis starts at 0
ax.text(10.7, -0.5, r"$x$", fontsize=14, ha='right', va='top')
ax.text(-0.3, max(y_points_r)+5, r"$y$", fontsize=14, ha='left', va='bottom')
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Legend slightly right from y-axis
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.05, 1))

plt.tight_layout()
plt.show()

fig.savefig("random1.png", dpi=300, bbox_inches='tight')
fig.savefig("random1.pdf", bbox_inches='tight')


