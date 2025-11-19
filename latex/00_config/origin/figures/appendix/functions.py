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

# Function and points
f = lambda x: x**2
x = np.linspace(0, 4, 1000)
x_0 = 2
y_0 = f(x_0)
h = 0.7
x_1 = x_0 + h
y_1 = f(x_1)



# --- Plot 1: function highlighting one point ---

# Prepare plot and layout
fig1, ax1 = plt.subplots(figsize=(7, 4.5))

for offset in np.linspace(-0.008, 0.008, 5):
    ax1.plot(x, f(x) + offset, color='black', lw=1.5, alpha=0.1)
for offset in np.linspace(-0.004, 0.004, 3):
    ax1.plot(x, f(x) + offset, color='black', lw=1.0, alpha=0.15)
ax1.plot(x, f(x), color='black', lw=1.7, alpha=0.3)
ax1.scatter(x_0, y_0, color='firebrick', zorder=5)

# Prepare axes and dashed delimiters
ax1.plot([x_0, x_0], [0, y_0], color='firebrick', linestyle='--', linewidth=1.5)
ax1.plot([0, x_0], [y_0, y_0], color='firebrick', linestyle='--', linewidth=1.5)

for spine in ax1.spines.values():
    spine.set_visible(False)

ax1.annotate("", xy=(4.2, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax1.annotate("", xy=(0, 18), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax1.set_xticks([x_0])
ax1.set_yticks([y_0])
ax1.set_xticklabels([r"$x_0$"], fontsize=13)
ax1.set_yticklabels([r"$f(x_0)$"], fontsize=13)

for label in ax1.get_yticklabels():
    label.set_horizontalalignment('right')
    label.set_x(-0.03)

# Add labels and plot
ax1.set_xlim(-0.5, 4.5)
ax1.set_ylim(-1, 18)
ax1.text(4.25, -1.2, r"$x$", fontsize=14, ha='right', va='top')
ax1.text(-0.3, 18, r"$f(x)$", fontsize=14, ha='left', va='bottom')
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.tick_params(axis='both', direction='in', length=4, width=1)
plt.tight_layout()

# Save figure
fig1.savefig("functions_point_1.png", dpi=300, bbox_inches='tight')
fig1.savefig("functions_point_1.pdf", bbox_inches='tight')
plt.show()



# --- Plot 2: function highlighting two points ---

# Prepare plot and layout
fig2, ax2 = plt.subplots(figsize=(7, 4.5))

for offset in np.linspace(-0.008, 0.008, 5):
    ax2.plot(x, f(x) + offset, color='black', lw=1.5, alpha=0.1)
for offset in np.linspace(-0.004, 0.004, 3):
    ax2.plot(x, f(x) + offset, color='black', lw=1.0, alpha=0.15)
ax2.plot(x, f(x), color='black', lw=1.7, alpha=0.3)
ax2.scatter([x_0, x_1], [y_0, y_1], color='firebrick', zorder=5)

# Prepare axes and dashed delimiters
ax2.plot([x_0, x_0], [0, y_0], color='firebrick', linestyle='--', linewidth=1.5)
ax2.plot([0, x_0], [y_0, y_0], color='firebrick', linestyle='--', linewidth=1.5)
ax2.plot([x_1, x_1], [0, y_1], color='firebrick', linestyle='--', linewidth=1.5)
ax2.plot([0, x_1], [y_1, y_1], color='firebrick', linestyle='--', linewidth=1.5)

for spine in ax2.spines.values():
    spine.set_visible(False)

ax2.annotate("", xy=(4.2, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax2.annotate("", xy=(0, 18), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax2.set_xticks([x_0, x_1])
ax2.set_yticks([y_0, y_1])
ax2.set_xticklabels([r"$x_0$", r"$x_0 + \Delta x$"], fontsize=13)
ax2.set_yticklabels([r"$f(x_0)$", r"$f(x_0 + \Delta x)$"], fontsize=13)

for label in ax2.get_yticklabels():
    label.set_horizontalalignment('right')
    label.set_x(-0.03)

# Add labels and plot
ax2.set_xlim(-0.5, 4.5)
ax2.set_ylim(-1, 18)
ax2.text(4.25, -1.2, r"$x$", fontsize=14, ha='right', va='top')
ax2.text(-0.3, 18, r"$f(x)$", fontsize=14, ha='left', va='bottom')
ax2.grid(True, linestyle='--', alpha=0.3)
ax2.tick_params(axis='both', direction='in', length=4, width=1)
plt.tight_layout()

# Save figure
fig2.savefig("functions_point_2.png", dpi=300, bbox_inches='tight')
fig2.savefig("functions_point_2.pdf", bbox_inches='tight')
plt.show()



# --- Plot 3: function with shadowed area representing increment ---

# Prepare plot and layout
fig3, ax3 = plt.subplots(figsize=(7, 4.5))

for offset in np.linspace(-0.008, 0.008, 5):
    ax3.plot(x, f(x) + offset, color='black', lw=1.5, alpha=0.1)
for offset in np.linspace(-0.004, 0.004, 3):
    ax3.plot(x, f(x) + offset, color='black', lw=1.0, alpha=0.15)
ax3.plot(x, f(x), color='black', lw=1.7, alpha=0.3)
ax3.scatter([x_0, x_1], [y_0, y_1], color='firebrick', zorder=5)

# Prepare axes and dashed delimiters
ax3.plot([x_0, x_0], [0, y_0], color='firebrick', linestyle='--', linewidth=1.5)
ax3.plot([0, x_0], [y_0, y_0], color='firebrick', linestyle='--', linewidth=1.5)
ax3.plot([x_1, x_1], [0, y_1], color='firebrick', linestyle='--', linewidth=1.5)
ax3.plot([0, x_1], [y_1, y_1], color='firebrick', linestyle='--', linewidth=1.5)

# Coordinates for the lower triangle vertices:
# (x_0, y_0), (x_1, y_0), (x_1, y_1)
triangle_x = [x_0, x_1, x_1]
triangle_y = [y_0, y_0, y_1]

# Fill the lower triangle
ax3.fill(triangle_x, triangle_y, color='firebrick', alpha=0.15)

for spine in ax3.spines.values():
    spine.set_visible(False)

ax3.annotate("", xy=(4.2, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax3.annotate("", xy=(0, 18), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

ax3.set_xticks([x_0, x_1])
ax3.set_yticks([y_0, y_1])
ax3.set_xticklabels([r"$x_0$", r"$x_0 + \Delta x$"], fontsize=13)
ax3.set_yticklabels([r"$f(x_0)$", r"$f(x_0 + \Delta x)$"], fontsize=13)

for label in ax3.get_yticklabels():
    label.set_horizontalalignment('right')
    label.set_x(-0.03)

ax3.set_xlim(-0.5, 4.5)
ax3.set_ylim(-1, 18)
ax3.text(4.25, -1.2, r"$x$", fontsize=14, ha='right', va='top')
ax3.text(-0.3, 18, r"$f(x)$", fontsize=14, ha='left', va='bottom')
ax3.grid(True, linestyle='--', alpha=0.3)
ax3.tick_params(axis='both', direction='in', length=4, width=1)

# Add the difference quotient as text next to the plot (top-right corner)
ax3.text(2.8, 5.5, 
         r"$\frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$",
         fontsize=14, color='#B22222', va='center', ha='left')

plt.tight_layout()

# Save figure
fig3.savefig("functions_point_2_shadow.png", dpi=300, bbox_inches='tight')
fig3.savefig("functions_point_2_shadow.pdf", bbox_inches='tight')
plt.show()
