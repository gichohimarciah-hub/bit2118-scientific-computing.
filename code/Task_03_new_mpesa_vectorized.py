import numpy as np
import timeit

# One million simulated mobile-money transfers in KES
rng = np.random.default_rng(7)
amounts = rng.uniform(50, 20000, 1_000_000)

# Assumed fee rule: 1% of the amount, but never below KES 10 and never above KES 108
def loop_fees():
    fees = []
    for a in amounts:
        fee = 0.01 * a
        if fee < 10:
            fee = 10
        elif fee > 108:
            fee = 108
        fees.append(fee)
    return fees

def vector_fees():
    return np.clip(0.01 * amounts, 10, 108)

t_loop = timeit.timeit(loop_fees, number=1)
t_vec = timeit.timeit(vector_fees, number=3) / 3
fees = vector_fees()

print(f"Total fees collected: KES {fees.sum():,.2f}")
print(f"Average fee: KES {fees.mean():.2f}")
print(f"Share of transfers charged the KES 108 cap: {np.mean(fees == 108):.2%}")
print(f"Loop: {t_loop:.4f} s | Vectorized: {t_vec:.4f} s | Speed-up: {t_loop/t_vec:.0f}x")
