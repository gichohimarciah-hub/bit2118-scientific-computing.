import numpy as np
import math
from decimal import Decimal

# Adding KES 0.10 one million times should give exactly KES 100,000
total = 0.0
for _ in range(1_000_000):
    total += 0.10

exact = 100000.0
print(f"Naive running total: {total:.10f}")
print(f"Absolute error: {abs(total - exact):.10f}")
print(f"Relative error: {abs(total - exact) / exact:.3e}")
print("Equal to 100000 exactly?", total == exact)
print("Close to 100000 (tolerance)?", np.isclose(total, exact))

# More accurate summation methods
print("math.fsum result:", math.fsum([0.10] * 1_000_000))
print("Decimal result:  ", sum(Decimal("0.10") for _ in range(1_000_000)))

# Cheap trick for money: work in whole cents (integers)
cents = sum(10 for _ in range(1_000_000))
print("Integer cents result (KES):", cents / 100)
