import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Cars washed per month over the first eight months of a new branch
months = np.arange(1, 9, dtype=float)
cars = np.array([210, 228, 251, 270, 298, 320, 352, 380], dtype=float)

# Exponential growth model: cars = a * exp(b * month)
def model(t, a, b):
    return a * np.exp(b * t)

(a, b), cov = curve_fit(model, months, cars, p0=[200, 0.05])
fitted = model(months, a, b)
rmse = np.sqrt(np.mean((cars - fitted)**2))

print(f"Fitted model: cars = {a:.2f} * exp({b:.4f} * month)")
print(f"Monthly growth rate: {np.exp(b) - 1:.2%}")
print(f"RMSE: {rmse:.2f} cars")
print(f"Forecast for month 12: {model(12, a, b):.0f} cars")

x = np.linspace(1, 12, 200)
plt.scatter(months, cars, label="Recorded")
plt.plot(x, model(x, a, b), label="Fitted curve")
plt.xlabel("Month")
plt.ylabel("Cars washed")
plt.title("Branch growth: exponential curve fit")
plt.legend()
plt.grid(True)
plt.show()
