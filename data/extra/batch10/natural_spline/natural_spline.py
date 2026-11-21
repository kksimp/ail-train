import math

def curvatures(xs, ys):
    n = len(xs)
    a = [0.0] * n
    b = [1.0] * n
    c = [0.0] * n
    d = [0.0] * n
    for i in range(1, n - 1):
        h0 = xs[i] - xs[i - 1]
        h1 = xs[i + 1] - xs[i]
        a[i] = h0
        b[i] = 2.0 * (h0 + h1)
        c[i] = h1
        d[i] = 6.0 * ((ys[i + 1] - ys[i]) / h1 - (ys[i] - ys[i - 1]) / h0)
    for i in range(1, n):
        w = a[i] / b[i - 1]
        b[i] -= w * c[i - 1]
        d[i] -= w * d[i - 1]
    m = [0.0] * n
    m[n - 1] = d[n - 1] / b[n - 1]
    i = n - 2
    while i >= 0:
        m[i] = (d[i] - c[i] * m[i + 1]) / b[i]
        i -= 1
    return m

def spline_at(xs, ys, m, x):
    k = 0
    while k < len(xs) - 2 and x > xs[k + 1]:
        k += 1
    h = xs[k + 1] - xs[k]
    t1 = xs[k + 1] - x
    t0 = x - xs[k]
    return m[k] * t1 * t1 * t1 / (6.0 * h) + m[k + 1] * t0 * t0 * t0 / (6.0 * h) + (ys[k] / h - m[k] * h / 6.0) * t1 + (ys[k + 1] / h - m[k + 1] * h / 6.0) * t0

pi = 3.141592653589793
xs = [0.0, 0.7, 1.4, 2.1, 2.8, 3.5]
ys = [math.sin(v) for v in xs]
m = curvatures(xs, ys)
print(f"curvatures at the knots: {', '.join(f'{v:.4f}' for v in m)}")
for x in [0.35, 1.0, pi / 2.0, 2.5, 3.2]:
    s = spline_at(xs, ys, m, x)
    print(f"x {x:.3f}: spline {s:.5f}, sin {math.sin(x):.5f}, error {abs(s - math.sin(x)):.5f}")
