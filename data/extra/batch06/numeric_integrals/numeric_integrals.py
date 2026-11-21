import math
def tr(f, a, b, n):
    h = (b - a) / n; s = (f(a) + f(b)) / 2.0
    for i in range(1, n): s += f(a + h * i)
    return s * h
def si(f, a, b, n):
    h = (b - a) / n; s = f(a) + f(b)
    for i in range(1, n): s += (4.0 if i % 2 == 1 else 2.0) * f(a + h * i)
    return s * h / 3.0
for l, f, a, b, e in [("x^3 on 0..2", lambda x: x * x * x, 0.0, 2.0, 4.0), ("1/x on 1..3", lambda x: 1.0 / x, 1.0, 3.0, 1.0986122886681098), ("sin on 0..pi", math.sin, 0.0, 3.141592653589793, 2.0)]:
    for n in [4, 16]: t = tr(f, a, b, n); s = si(f, a, b, n); print(f"{l}, n={n}: trapezoid {t:.6f} (err {abs(t - e):.6f}), simpson {s:.6f}")
