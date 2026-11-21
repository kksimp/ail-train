import math
def risk(w, s1, s2, rho):
    v = 1.0 - w
    return math.sqrt(w * w * s1 * s1 + v * v * s2 * s2 + 2.0 * w * v * rho * s1 * s2)
r1 = 8.0
s1 = 16.0
r2 = 4.0
s2 = 6.0
rho = 0.1
for pct in [0, 20, 40, 60, 80, 100]:
    w = float(pct) / 100.0
    ret = w * r1 + (1.0 - w) * r2
    print(f"{pct:>3}% shares: return {ret:.2f}%, risk {risk(w, s1, s2, rho):.2f}%")
best = (s2 * s2 - rho * s1 * s2) / (s1 * s1 + s2 * s2 - 2.0 * rho * s1 * s2)
print(f"least risk at {best * 100.0:.1f}% shares: {risk(best, s1, s2, rho):.2f}%")
