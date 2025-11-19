import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 0
sigma = 1
size = 100

# Generate data and compute running mean
np.random.seed(42)
data = np.random.normal(loc=mu, scale=sigma, size=size)
running_mean = np.cumsum(data) / np.arange(1, size + 1)
trials = np.arange(1, size + 1)

# Plot
fig, ax = plt.subplots(figsize=(7, 4.5))

# Running mean line
ax.plot(trials, running_mean, color="#1f77b4", lw=1.7, alpha=0.8)

# Horizontal line for true mean
ax.axhline(mu, color='firebrick', linestyle='--', linewidth=1.5)

# Hide spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Axes arrows
ax.annotate("", xy=(size + size*0.05, mu), xytext=(0, mu),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, running_mean.max() + 0.5), xytext=(0, mu - 1.5),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Labels and text
ax.set_xlabel("Number of trials", fontsize=14, family='serif')
ax.set_ylabel("Running mean", fontsize=14, family='serif')
ax.text(size + size*0.07, mu, r"$\mu$", fontsize=14, ha='left', va='center', color='firebrick', family='serif')
ax.text(size / 3, running_mean.max() + 0.4, "Running mean", fontsize=14, ha='center', va='bottom', color="#1f77b4", family='serif')

# Limits and ticks
ax.set_xlim(0, size + size*0.1)
y_min = min(running_mean.min(), mu) - 1
y_max = max(running_mean.max(), mu) + 0.5
ax.set_ylim(y_min, y_max)
ax.tick_params(axis='both', direction='in', length=4, width=1)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
fig.savefig("lln_fancy.png", dpi=300, bbox_inches='tight')
fig.savefig("lln_fancy.pdf", bbox_inches='tight')
plt.show()
