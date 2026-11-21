import math
def cheb(n):
    ts = [[1], [0, 1]]
    for k in range(1, n):
        nx = [0] + [2 * c for c in ts[k]]
        prev = ts[k - 1]
        for i in range(len(prev)):
            nx[i] -= prev[i]
        ts.append(nx)
    return ts
def show(p):
    parts = []
    for i in range(len(p) - 1, -1, -1):
        c = p[i]
        if c != 0:
            pw = "" if i == 0 else ("x" if i == 1 else f"x^{i}")
            num = "" if abs(c) == 1 and i > 0 else f"{abs(c)}"
            sign = (" - " if c < 0 else " + ") if parts else ("-" if c < 0 else "")
            parts.append(f"{sign}{num}{pw}")
    return "".join(parts)
def runge(x):
    return 1.0 / (1.0 + 25.0 * x * x)
def interp(xs, x):
    total = 0.0
    for i in range(len(xs)):
        term = runge(xs[i])
        for j in range(len(xs)):
            if j != i:
                term = term * (x - xs[j]) / (xs[i] - xs[j])
        total += term
    return total
def max_err(xs):
    worst = 0.0
    for i in range(201):
        x = (i - 100) / 100.0
        worst = max(worst, abs(interp(xs, x) - runge(x)))
    return worst
ts = cheb(6)
for n in range(len(ts)):
    print(f"T{n}(x) = {show(ts[n])}")
n = 11
even = [(2 * k - 10) / 10.0 for k in range(n)]
nodes = [math.cos((2 * k + 1) * 3.141592653589793 / (2 * n)) for k in range(n)]
print(f"11 even points:     largest error {max_err(even):.3f}")
print(f"11 Chebyshev nodes: largest error {max_err(nodes):.3f}")
