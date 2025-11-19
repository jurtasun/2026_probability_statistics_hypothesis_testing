import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

def gaussian(t, sigma=0.2):
    return np.exp(-t**2 / (2*sigma**2))

def square_pulse(t, width=1):
    return np.where(np.abs(t) <= width/2, 1, 0)

def sinc_function(t):
    return np.sinc(t/np.pi)

t = np.linspace(-10, 10, 1000)
freq = np.fft.fftfreq(len(t), d=(t[1]-t[0]))
freq = np.fft.fftshift(freq)

gauss = gaussian(t)
pulse = square_pulse(t)
sinc = sinc_function(t)

gauss_ft = np.abs(np.fft.fftshift(np.fft.fft(gauss)))
pulse_ft = np.abs(np.fft.fftshift(np.fft.fft(pulse)))
sinc_ft = np.abs(np.fft.fftshift(np.fft.fft(sinc)))

signals = [gauss_ft, pulse_ft, sinc_ft]
titles = ["Gaussian FT", "Square Pulse FT", "Sinc FT"]

for i in range(3):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    y_ft = signals[i]

    ax.plot(freq, y_ft, color='firebrick', lw=2)
    ax.set_xlim(freq.min(), freq.max())
    ax.set_ylim(0, y_ft.max()*1.1)

    # ax.set_title(titles[i], fontsize=14)

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
    ax.annotate("", xy=(xlim[1]*1.05, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
    ax.annotate("", xy=(0, ylim[1]*1.3), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

    ax.grid(True, linestyle='--', alpha=0.3)
    ax.tick_params(axis='both', direction='in', length=4, width=1)

    plt.tight_layout()
    filename = f"fourier_transform_{i+1}.png"
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
