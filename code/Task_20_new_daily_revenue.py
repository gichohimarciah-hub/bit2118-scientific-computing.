import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
N = 50_000                      # simulated days

# Cars per day vary randomly (Poisson, mean 30). Each car buys Basic, Full or Interior.
prices = np.array([300, 700, 500])
probabilities = [0.6, 0.3, 0.1]
daily_cost = 12000              # assumed wages, rent, water and soap per day

cars = rng.poisson(30, N)
revenue = np.zeros(N)
for day in range(N):
    choices = rng.choice(prices, size=cars[day], p=probabilities)
    revenue[day] = choices.sum()

loss = revenue < daily_cost
print(f"Average daily revenue: KES {revenue.mean():,.0f}")
print(f"Probability of a loss-making day: {loss.mean():.2%}")
print(f"5th percentile of revenue: KES {np.percentile(revenue, 5):,.0f}")
print(f"95th percentile of revenue: KES {np.percentile(revenue, 95):,.0f}")

plt.hist(revenue, bins=50)
plt.axvline(daily_cost, linestyle="--")
plt.xlabel("Daily revenue (KES)")
plt.ylabel("Number of simulated days")
plt.title("Monte Carlo simulation of daily car-wash revenue")
plt.grid(True)
plt.show()
