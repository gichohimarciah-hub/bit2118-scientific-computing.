import numpy as np
import matplotlib.pyplot as plt

# Loan balance B (KES) with interest compounding continuously and a repayment stream:
# dB/dt = r*B - p
r = 0.015            # assumed 1.5% per month
p = 8000.0           # repayment per month
B0 = 200000.0
T = 24               # months

def exact(t):
    return (B0 - p/r) * np.exp(r*t) + p/r

def euler(h):
    t = np.arange(0, T + h, h)
    B = np.zeros_like(t)
    B[0] = B0
    for i in range(len(t) - 1):
        B[i+1] = B[i] + h * (r*B[i] - p)
    return t, B

for h in (4.0, 1.0, 0.25):
    t, B = euler(h)
    print(f"h = {h:<5} Euler balance after {T} months: {B[-1]:,.2f}  "
          f"error = {abs(B[-1] - exact(T)):,.2f}")
print(f"Exact balance: {exact(T):,.2f}")

t1, B1 = euler(1.0)
plt.plot(t1, B1, marker="o", label="Euler (h = 1)")
plt.plot(t1, exact(t1), label="Exact")
plt.xlabel("Month")
plt.ylabel("Loan balance (KES)")
plt.title("Loan repayment modelled with Euler's method")
plt.legend()
plt.grid(True)
plt.show()
