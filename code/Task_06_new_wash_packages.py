import numpy as np

# Unknowns: number of Basic (x), Full (y) and Interior (z) washes in a day
# Each row is one resource:  water (litres), soap (ml), labour (minutes)
A = np.array([
    [30.0, 80.0, 50.0],    # water per wash
    [20.0, 60.0, 30.0],    # soap per wash
    [10.0, 40.0, 20.0]     # labour per wash
])
# Totals recorded at closing time
b = np.array([1650.0, 1150.0, 700.0])

solution = np.linalg.solve(A, b)
print("Basic, Full, Interior washes:", np.round(solution, 2))
print("Residual norm:", np.linalg.norm(b - A @ solution))
print("Condition number of A:", round(np.linalg.cond(A), 1))
