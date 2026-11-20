import numpy as np
import matplotlib.pyplot as plt

# Steady-state temperatures at the four interior points of a small metal plate
# Layout:   p1  p2     Top edge = 100 C, left edge = 50 C,
#           p3  p4     right and bottom edges = 0 C
A = np.array([
    [ 4., -1., -1.,  0.],
    [-1.,  4.,  0., -1.],
    [-1.,  0.,  4., -1.],
    [ 0., -1., -1.,  4.]
])
b = np.array([150., 100., 50., 0.])      # boundary contributions

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        err = np.linalg.norm(x - old, ord=np.inf)
        errors.append(err)
        if err < tol:
            break
    return x, errors

x, errors = gauss_seidel(A, b)
print("Gauss-Seidel temperatures:", np.round(x, 4))
print("Direct solution:         ", np.round(np.linalg.solve(A, b), 4))
print("Iterations used:", len(errors))

plt.semilogy(errors, marker="o")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Gauss-Seidel convergence for the metal plate")
plt.grid(True)
plt.show()
