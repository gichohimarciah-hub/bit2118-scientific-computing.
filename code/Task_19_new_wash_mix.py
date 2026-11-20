import numpy as np
from scipy.optimize import minimize

# x = Basic washes, y = Full washes per day
# Profit per wash: Basic KES 300, Full KES 700
# Water: 40 L and 90 L per wash, limit 3,000 L
# Labour: 15 min and 40 min per wash, limit 1,200 min (two workers, 10 hours)
def neg_profit(z):
    x, y = z
    return -(300*x + 700*y)

constraints = [
    {"type": "ineq", "fun": lambda z: 3000 - (40*z[0] + 90*z[1])},
    {"type": "ineq", "fun": lambda z: 1200 - (15*z[0] + 40*z[1])}
]
bounds = [(0, None), (0, None)]

sol = minimize(neg_profit, x0=[10, 10], method="SLSQP", bounds=bounds, constraints=constraints)
x, y = sol.x
print("Success:", sol.success)
print(f"Basic washes: {x:.2f}, Full washes: {y:.2f}")
print(f"Maximum daily profit: KES {-sol.fun:,.2f}")
print(f"Water used: {40*x + 90*y:.1f} L of 3000 L")
print(f"Labour used: {15*x + 40*y:.1f} min of 1200 min")

# Whole-number check
best = max(((300*a + 700*b, a, b) for a in range(0, 81) for b in range(0, 34)
            if 40*a + 90*b <= 3000 and 15*a + 40*b <= 1200))
print("Best whole-number plan (profit, basic, full):", best)
