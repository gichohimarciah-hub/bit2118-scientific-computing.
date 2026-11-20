from scipy.optimize import root_scalar

# Buying a second pressure washer: cost now, extra cash inflow each year (KES)
cash_flows = [-85000, 30000, 32000, 35000, 28000]
hurdle_rate = 0.12      # assumed minimum acceptable return

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)

print(f"IRR (Newton-Raphson): {newton.root:.4%}  in {newton.iterations} iterations")
print(f"IRR (Secant):         {secant.root:.4%}  in {secant.iterations} iterations")
print(f"NPV at the {hurdle_rate:.0%} hurdle rate: KES {npv(hurdle_rate):,.2f}")
print("Buy the machine?", "Yes" if newton.root > hurdle_rate else "No")
