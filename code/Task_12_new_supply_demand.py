import numpy as np
from scipy.optimize import root

# Market for car-wash bookings: q = washes per week, p = price in KES
# Demand falls faster as the price rises:  p = 500 - 0.02 q^2
# Supply (capacity cost) rises with volume: p = 100 + 0.5 q
def equations(z):
    q, p = z
    return [
        p - (500 - 0.02*q**2),
        p - (100 + 0.5*q)
    ]

for guess in ([100.0, 150.0], [-100.0, 50.0]):
    sol = root(equations, guess)
    print("Initial guess:", guess)
    print(f"Solution: q = {sol.x[0]:.3f}, p = {sol.x[1]:.3f}")
    print("Residuals:", np.round(equations(sol.x), 10))
    print("Converged:", sol.success)
    print()

# Check with the polynomial 0.02 q^2 + 0.5 q - 400 = 0
print("np.roots check:", np.roots([0.02, 0.5, -400]))
