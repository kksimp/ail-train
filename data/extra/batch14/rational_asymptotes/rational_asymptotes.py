from math import gcd
def ev(p, x):
    t = 0
    for c in p:
        t = t * x + c
    return t
def ratio(a, b):
    g = gcd(a, b)
    s = -1 if b < 0 else 1
    n, d = s * a // g, s * b // g
    return f"y = {n}" if d == 1 else f"y = {n}/{d}"
def line(a, b):
    head = "x" if a == 1 else ("-x" if a == -1 else f"{a}x")
    tail = f" + {b}" if b > 0 else (f" - {-b}" if b < 0 else "")
    return f"y = {head}{tail}"
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
cases = [("(2x^2 + 1) / (x^2 - 4)", [2, 0, 1], [1, 0, -4]), ("(x^2 - 1) / (x^2 + 2x - 3)", [1, 0, -1], [1, 2, -3]), ("(x^3 + 2x) / (x^2 - 1)", [1, 0, 2, 0], [1, 0, -1]), ("(3x + 6) / (x^2 + 1)", [3, 6], [1, 0, 1]), ("(x^2 + x - 6) / (x - 2)", [1, 1, -6], [1, -2]), ("x^4 / (x - 1)", [1, 0, 0, 0, 0], [1, -1])]
for name, num, den in cases:
    vert, holes = [], []
    for x in range(-10, 11):
        if ev(den, x) == 0:
            (holes if ev(num, x) == 0 else vert).append(x)
    dn, dd = len(num) - 1, len(den) - 1
    asym = "no line: it grows faster than any line"
    if dn < dd:
        asym = "y = 0"
    elif dn == dd:
        asym = ratio(num[0], den[0])
    elif dn == dd + 1:
        asym = line(num[0], num[1] - num[0] * den[1])
    print(name)
    print(f"    vertical at {fl(vert)}, holes at {fl(holes)}, far away {asym}")
