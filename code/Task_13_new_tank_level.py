import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Water-tank level (litres) recorded every two hours
hours = np.array([6, 8, 10, 12, 14, 16, 18], dtype=float)
level = np.array([1000, 930, 820, 640, 560, 430, 380], dtype=float)

linear = interp1d(hours, level, kind="linear")
cubic = CubicSpline(hours, level)

for t in (11.0, 15.0):
    print(f"Level at {t:.0f}:00  linear = {float(linear(t)):.1f} L, cubic = {float(cubic(t)):.1f} L")

# When does the tank fall below 500 L? (search on a fine grid)
fine = np.linspace(6, 18, 1201)
below = fine[cubic(fine) < 500]
print(f"Cubic spline says the tank drops below 500 L at about {below[0]:.2f} h")

plt.scatter(hours, level, label="Measured")
plt.plot(fine, linear(fine), label="Linear")
plt.plot(fine, cubic(fine), label="Cubic spline")
plt.axhline(500, linestyle=":", linewidth=0.8)
plt.xlabel("Hour of day")
plt.ylabel("Tank level (L)")
plt.title("Water-tank level interpolation")
plt.legend()
plt.grid(True)
plt.show()
