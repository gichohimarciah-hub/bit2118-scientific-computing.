import numpy as np

# Rows = branches, columns = number of washes sold: [Basic, Full, Interior]
sales = np.array([
    [40, 15, 10],    # Branch 1
    [25, 30,  5],    # Branch 2
    [35, 10, 20]     # Branch 3
])

# Assumed prices in KES for Basic, Full, Interior
prices = np.array([300, 700, 500])

revenue_per_branch = sales @ prices
print("Revenue per branch (KES):", revenue_per_branch)
print("Total revenue (KES):", revenue_per_branch.sum())

# Next week: every service sold is expected to grow 10% at branch 1, 20% at branch 2, 5% at branch 3
growth = np.diag([1.10, 1.20, 1.05])
next_week = growth @ sales
print("Projected sales next week:\n", next_week)
print("Projected revenue (KES):", next_week @ prices)

# Determinant and inverse of a square sales matrix
print("Determinant of sales matrix:", round(np.linalg.det(sales), 2))
print("Inverse exists:", abs(np.linalg.det(sales)) > 1e-9)
