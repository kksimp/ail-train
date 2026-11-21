import math

def f(kind, x):
    if kind == 0:
        return x * x * x - 2.0 * x - 5.0
    if kind == 1:
        return x * x - 2.0
    if kind == 2:
        return x * x * x - 10.0
    return math.cos(x) - x

def df(kind, x):
    if kind == 0:
        return 3.0 * x * x - 2.0
    if kind == 1:
        return 2.0 * x
    if kind == 2:
        return 3.0 * x * x
    return -math.sin(x) - 1.0

def newton(kind, start, trail):
    x = start
    for _ in range(50):
        trail.append(x)
        nxt = x - f(kind, x) / df(kind, x)
        if abs(nxt - x) < 0.000000000001:
            return nxt
        x = nxt
    return x

names = ["x^3 - 2x - 5 = 0", "x^2 = 2", "x^3 = 10", "cos x = x"]
starts = [2.0, 1.0, 2.0, 1.0]
for k in range(4):
    trail = []
    root = newton(k, starts[k], trail)
    print(f"{names[k]:<17} root {root:.12f} after {len(trail)} steps, f(root) tiny: {str(abs(f(k, root)) < 0.000000001).lower()}")
trail = []
newton(0, 2.0, trail)
for i, x in enumerate(trail):
    print(f"    step {i}: {x:.15f}")
