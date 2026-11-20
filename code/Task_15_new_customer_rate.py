import numpy as np
import matplotlib.pyplot as plt

# Cumulative cars washed, recorded at each hour from 8:00 to 16:00
hours = np.arange(8, 17, dtype=float)
cumulative = np.array([0, 6, 15, 29, 47, 64, 78, 89, 95], dtype=float)

# Rate of cars per hour with central differences inside, one-sided at the ends
rate = np.zeros_like(cumulative)
rate[0] = (cumulative[1] - cumulative[0]) / (hours[1] - hours[0])
for i in range(1, len(hours) - 1):
    rate[i] = (cumulative[i+1] - cumulative[i-1]) / (hours[i+1] - hours[i-1])
rate[-1] = (cumulative[-1] - cumulative[-2]) / (hours[-1] - hours[-2])

# Compare with NumPy's built-in gradient
check = np.gradient(cumulative, hours)

for h, r, c in zip(hours, rate, check):
    print(f"{h:4.0f}:00  rate = {r:5.2f} cars/hour   np.gradient = {c:5.2f}")
print("Largest difference from np.gradient:", np.max(np.abs(rate - check)))
print(f"Peak rate: {rate.max():.1f} cars/hour at {hours[np.argmax(rate)]:.0f}:00")

plt.plot(hours, rate, marker="o")
plt.xlabel("Hour of day")
plt.ylabel("Cars per hour")
plt.title("Customer arrival rate from cumulative counts")
plt.grid(True)
plt.show()
