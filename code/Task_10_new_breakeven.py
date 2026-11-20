import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Daily profit of a car wash as a function of cars washed (n)
# Assumptions: price KES 600 per car; variable cost KES 150 per car, rising by
# KES 0.5 for every extra car (water pressure, extra staff); fixed cost KES 6,000 per day
def profit(n):
    return 600*n - (150*n + 0.5*n**2) - 6000

# Bisection on a bracket where the sign changes
sol = root_scalar(profit, bracket=[1, 100], method="bisect", xtol=1e-10)

# Fixed-point form: n = (6000 + 0.5 n^2) / 450
def g(n):
    return (6000 + 0.5*n**2) / 450

n = 20.0
history = [n]
for _ in range(200):
    n_new = g(n)
    history.append(n_new)
    if abs(n_new - n) < 1e-10:
        break
    n = n_new

print(f"Break-even (bisection): {sol.root:.4f} cars per day, {sol.iterations} iterations")
print(f"Break-even (fixed point): {history[-1]:.4f} cars per day, {len(history)-1} iterations")
print("Cars needed in practice:", int(np.ceil(sol.root)))

x = np.linspace(1, 60, 300)
plt.plot(x, profit(x))
plt.axhline(0, linewidth=0.8)
plt.axvline(sol.root, linestyle="--")
plt.xlabel("Cars washed per day")
plt.ylabel("Profit (KES)")
plt.title("Break-even point of the car wash")
plt.grid(True)
plt.show()
