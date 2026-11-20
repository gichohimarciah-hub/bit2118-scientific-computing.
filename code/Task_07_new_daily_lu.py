import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Same resource matrix as the package problem, reused for five different days
A = np.array([
    [30.0, 80.0, 50.0],
    [20.0, 60.0, 30.0],
    [10.0, 40.0, 20.0]
])

daily_totals = {
    "Monday":    np.array([1650.0, 1150.0,  700.0]),
    "Tuesday":   np.array([1710.0, 1200.0,  750.0]),
    "Wednesday": np.array([1590.0, 1100.0,  650.0]),
    "Thursday":  np.array([2600.0, 1800.0, 1100.0]),
    "Friday":    np.array([3250.0, 2260.0, 1390.0])
}

lu, piv = lu_factor(A)        # factor once

for day, b in daily_totals.items():
    x = lu_solve((lu, piv), b)
    print(f"{day:<10} Basic={x[0]:6.2f}  Full={x[1]:6.2f}  Interior={x[2]:6.2f}  "
          f"residual={np.linalg.norm(b - A @ x):.1e}")
