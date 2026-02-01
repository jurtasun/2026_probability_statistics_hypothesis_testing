import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Turn off axes
ax.axis("off")

# Box positions: (x, y, width, height)
boxes = {
    "Fisher":        (0.1, 0.55, 0.35, 0.25),
    "NeymanPearson": (0.55, 0.55, 0.35, 0.25),
    "Bayesian":      (0.1, 0.15, 0.35, 0.25),
    "Popper":        (0.55, 0.15, 0.35, 0.25),
}

# Text for each box
texts = {
    "Fisher": (
        "Fisherian significance testing\n\n"
        "Primary question:\n"
        "• Is the data surprising under H₀?\n\n"
        "Key concept:\n"
        "• p-value as evidence\n\n"
        "No decision rule\n"
        "No Type II error"
    ),
    "NeymanPearson": (
        "Neyman–Pearson testing\n\n"
        "Primary question:\n"
        "• What decision rule controls error?\n\n"
        "Key concepts:\n"
        "• Type I error (α)\n"
        "• Type II error (β)\n"
        "• Power"
    ),
    "Bayesian": (
        "Bayesian inference\n\n"
        "Primary question:\n"
        "• How should beliefs change?\n\n"
        "Key concepts:\n"
        "• Prior → Posterior\n"
        "• Bayes factor\n"
        "• Expected loss"
    ),
    "Popper": (
        "Popperian falsification\n\n"
        "Primary question:\n"
        "• Has the theory survived a severe test?\n\n"
        "Key concepts:\n"
        "• Risky predictions\n"
        "• Refutation, not confirmation"
    ),
}

# Draw boxes
for key, (x, y, w, h) in boxes.items():
    rect = plt.Rectangle((x, y), w, h, fill=False)
    ax.add_patch(rect)
    ax.text(
        x + w / 2,
        y + h / 2,
        texts[key],
        ha="center",
        va="center",
        wrap=True
    )

# Title
plt.title(
    "Conceptual frameworks of hypothesis testing\n"
    "Different questions answered by different approaches",
    pad=20
)

fig.savefig("approaches.png", dpi=300, bbox_inches='tight')
fig.savefig("approaches.pdf", bbox_inches='tight')
plt.show()
