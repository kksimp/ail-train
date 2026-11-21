import math

def reduce(x):
    tau = 6.283185307179586
    r = x
    while r > 3.141592653589793:
        r -= tau
    while r < -3.141592653589793:
        r += tau
    return r

def series(x, start):
    term = 1.0 if start == 0 else x
    total = term
    k = start
    terms = 1
    while abs(term) > 0.0000000000000001:
        term = -term * x * x / float((k + 1) * (k + 2))
        total += term
        k += 2
        terms += 1
    return [total, float(terms)]

for deg in [0.0, 30.0, 45.0, 90.0, 135.0, 300.0, 1000.0]:
    x = reduce(deg * 3.141592653589793 / 180.0)
    s = series(x, 1)
    c = series(x, 0)
    raw = deg * 3.141592653589793 / 180.0
    close = abs(s[0] - math.sin(raw)) < 0.000000000001 and abs(c[0] - math.cos(raw)) < 0.000000000001
    print(f"{deg:>6.1f} deg: sin {s[0]:>9.6f} ({int(s[1]):>2} terms), cos {c[0]:>9.6f} ({int(c[1]):>2} terms), matches built-in: {str(close).lower()}")
