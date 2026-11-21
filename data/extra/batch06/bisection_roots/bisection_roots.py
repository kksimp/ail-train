import math
def f(k, x): return x * x - 2.0 if k == 0 else x * x * x - x - 1.0 if k == 1 else math.cos(x) - x
for l, k, a0, b0 in [("x^2 - 2", 0, 0.0, 2.0), ("x^3 - x - 1", 1, 1.0, 2.0), ("cos x - x", 2, 0.0, 1.0), ("x^2 - 2 (bad bracket)", 0, 2.0, 3.0)]:
    a = a0; b = b0
    if f(k, a) * f(k, b) > 0.0: print(f"{l}: no sign change on [{a0:.1f}, {b0:.1f}]"); continue
    s = 0
    while b - a > 0.000000001:
        m = (a + b) / 2.0
        if f(k, a) * f(k, m) <= 0.0: b = m
        else: a = m
        s += 1
    print(f"{l}: root {(a + b) / 2.0:.8f} after {s} halvings")
