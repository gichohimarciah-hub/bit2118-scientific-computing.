import numpy as np
from scipy.integrate import simpson

# Water flow rate (litres per minute) measured hourly while the car wash is open
hours = np.arange(8, 18, dtype=float)                    # 8:00 to 17:00
flow_lpm = np.array([12, 20, 28, 35, 42, 38, 30, 33, 36, 18], dtype=float)

minutes = hours * 60                                     # integrate over minutes
litres_trap = np.trapezoid(flow_lpm, minutes)
litres_simp = simpson(flow_lpm, x=minutes)

price_per_litre = 0.15       # assumed tariff: KES 150 per cubic metre

print(f"Water used (trapezoidal): {litres_trap:,.0f} L")
print(f"Water used (Simpson):     {litres_simp:,.0f} L")
print(f"Difference: {abs(litres_trap - litres_simp):,.0f} L")
print(f"Daily water bill (Simpson): KES {litres_simp * price_per_litre:,.2f}")
