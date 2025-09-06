import numpy as np
import matplotlib.pyplot as plt

# import from local package
from signal_ICT_ShivkumarPaun_92510133008 import unitary_signals, trigonometric_signals, operations

def demo():
    # -----------------------------
    # Signal Parameters
    # -----------------------------
    n = np.arange(0, 30)          # Discrete indices
    t = np.linspace(0, 1, 500)    # Continuous time vector
    t_exp = np.linspace(0, 1, 100)

    # -----------------------------
    # 1. Unitary Signals
    # -----------------------------
    step = unitary_signals.unit_step(n)
    impulse = unitary_signals.unit_impulse(n)
    ramp = unitary_signals.ramp_signal(n)

    # -----------------------------
    # 2. Trigonometric Signals
    # -----------------------------
    sine = trigonometric_signals.sine_wave(2, 5, 0, t)
    cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
    exp_signal = trigonometric_signals.exponential_signal(1, 2, t_exp)

    # -----------------------------
    # 3. Operations
    # -----------------------------
    shifted_sine = operations.time_shift(sine, 5)
    k = 2
    scaled_signal = operations.time_scale(sine, k)
    scaled_time = t[::k]
    added = operations.signal_addition(step, ramp)
    product = operations.signal_multiplication(sine, cosine)

    # -----------------------------
    # 10 Separate Graphs
    # -----------------------------
    

    # 7. Time-shifted Sine
    plt.figure(figsize=(8,4))
    plt.plot(t, sine, label="Original Sine")
    plt.plot(t, shifted_sine, linestyle="--", label="Shifted +5 samples")
    plt.title("Time Shift of Sine Wave")
    plt.xlabel("Time (s)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 8. Time-scaled Sine
    plt.figure(figsize=(8,4))
    plt.plot(t, sine, label="Original Sine")
    plt.plot(scaled_time, scaled_signal, label=f"Scaled k={k}")
    plt.title("Time Scaling of Sine Wave")
    plt.xlabel("Time (s)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 9. Step + Ramp Addition
    plt.figure(figsize=(8,4))
    plt.stem(n[:len(added)], added)
    plt.title("Signal Addition: Step + Ramp")
    plt.xlabel("n")
    plt.grid(True)
    plt.show()

    # 10. Sine × Cosine Multiplication
    plt.figure(figsize=(8,4))
    plt.plot(t[:len(product)], product)
    plt.title("Signal Multiplication: Sine × Cosine")
    plt.xlabel("Time (s)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    demo()
