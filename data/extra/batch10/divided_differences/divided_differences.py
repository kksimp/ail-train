import math

def table(xs, ys):
    coef = ys[:]
    n = len(xs)
    for level in range(1, n):
        i = n - 1
        while i >= level:
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - level])
            i -= 1
    return coef

def newton_eval(xs, coef, x):
    result = coef[-1]
    i = len(coef) - 2
    while i >= 0:
        result = result * (x - xs[i]) + coef[i]
        i -= 1
    return result

xs = [1.0, 4.0, 9.0]
ys = [1.0, 2.0, 3.0]
for extra in [16.0, 25.0, 36.0]:
    coef = table(xs, ys)
    shown = ", ".join(f"{c:.6f}" for c in coef)
    row = [f"p({x:.0f}) = {newton_eval(xs, coef, x):.4f} vs {math.sqrt(x):.4f}" for x in [2.0, 6.0, 12.0]]
    print(f"{len(xs)} points, coefficients [{shown}]")
    print(f"    {'; '.join(row)}")
    xs.append(extra)
    ys.append(math.sqrt(extra))
