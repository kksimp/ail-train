import math

def cost(kind, x):
    if kind == 0:
        return (x - 2.0) * (x - 2.0) + 1.0
    if kind == 1:
        return 2.0 * 3.141592653589793 * x * x + 2.0 * 330.0 / x
    return math.exp(x) - 3.0 * x

def minimise(kind, lo, hi):
    inv = (math.sqrt(5.0) - 1.0) / 2.0
    c = hi - inv * (hi - lo)
    d = lo + inv * (hi - lo)
    fc = cost(kind, c)
    fd = cost(kind, d)
    steps = 0
    while hi - lo > 0.00000001:
        if fc < fd:
            hi = d
            d = c
            fd = fc
            c = hi - inv * (hi - lo)
            fc = cost(kind, c)
        else:
            lo = c
            c = d
            fc = fd
            d = lo + inv * (hi - lo)
            fd = cost(kind, d)
        steps += 1
    x = (lo + hi) / 2.0
    return [x, cost(kind, x), float(steps)]

names = ["(x - 2)^2 + 1 on [0, 5]", "tin of 330 ml: surface by radius (cm) on [1, 10]", "e^x - 3x on [0, 3]"]
ranges = [[0.0, 5.0], [1.0, 10.0], [0.0, 3.0]]
for k in range(3):
    r = minimise(k, ranges[k][0], ranges[k][1])
    print(f"{names[k]}: minimum at {r[0]:.6f} value {r[1]:.6f} after {int(r[2])} steps")
pi = 3.141592653589793
exact = math.cbrt(330.0 / (2.0 * pi))
print(f"tin radius by calculus {exact:.6f}, height {330.0 / (pi * exact * exact):.6f}; e^x - 3x by calculus at ln 3 = {math.log(3.0):.6f}")
