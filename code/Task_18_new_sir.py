import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# SIR model of flu spreading through a campus of 10,000 people
N = 10000
beta = 0.30       # infections per infected person per day
gamma = 0.10      # recovery rate (about 10 days to recover)

def sir(t, y):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

y0 = [N - 10, 10, 0]
t_eval = np.linspace(0, 120, 400)
sol = solve_ivp(sir, (0, 120), y0, t_eval=t_eval, rtol=1e-8, atol=1e-8)

S, I, R = sol.y
peak = np.argmax(I)
print("Solver success:", sol.success)
print(f"Basic reproduction number R0 = {beta/gamma:.1f}")
print(f"Peak infections: {I[peak]:,.0f} people on day {sol.t[peak]:.0f}")
print(f"Total ever infected by day 120: {R[-1] + I[-1]:,.0f} ({(R[-1] + I[-1])/N:.1%})")

plt.plot(sol.t, S, label="Susceptible")
plt.plot(sol.t, I, label="Infected")
plt.plot(sol.t, R, label="Recovered")
plt.xlabel("Day")
plt.ylabel("People")
plt.title("SIR epidemic on a campus of 10,000")
plt.legend()
plt.grid(True)
plt.show()
