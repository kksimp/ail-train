def npv(r, fl): return sum(fl[t] / (1.0 + r) ** t for t in range(len(fl)))
def irr(fl):
    lo, hi = 0.0, 1.0
    for k in range(100):
        mid = (lo + hi) / 2.0
        if npv(mid, fl) > 0.0: lo = mid
        else: hi = mid
    return (lo + hi) / 2.0
for n, fl in [("solar roof", [-12000.0] + [1500.0] * 10), ("food truck", [-40000.0, 9000.0, 14000.0, 16000.0, 16000.0]), ("new oven", [-5000.0, 2500.0, 2500.0, 2500.0]), ("vending", [-3000.0, 900.0, 900.0, 900.0, 900.0])]:
    print(f"{n:<10} NPV at 10% {npv(0.1, fl):>9.2f}, IRR {irr(fl) * 100.0:.2f}%")
