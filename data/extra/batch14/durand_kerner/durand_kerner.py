def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def div(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)
def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])
def ev(p, z):
    acc = (0.0, 0.0)
    for c in p:
        m = mul(acc, z)
        acc = (m[0] + c, m[1])
    return acc
def tidy(v):
    return 0.0 if abs(v) < 0.00005 else v
def text(z):
    r, i = tidy(z[0]), tidy(z[1])
    if i < 0.0:
        return f"{r:.4f} - {-i:.4f}i"
    return f"{r:.4f} + {i:.4f}i"
def roots(p):
    n = len(p) - 1
    seed = (0.4, 0.9)
    zs = [(1.0, 0.0)]
    for k in range(1, n):
        zs.append(mul(zs[k - 1], seed))
    for rnd in range(200):
        for i in range(n):
            den = (1.0, 0.0)
            for j in range(n):
                if j != i:
                    den = mul(den, sub(zs[i], zs[j]))
            zs[i] = sub(zs[i], div(ev(p, zs[i]), den))
    return zs
polys = [("x^3 - 3x^2 + 3x - 5", [1.0, -3.0, 3.0, -5.0]), ("x^4 + 1", [1.0, 0.0, 0.0, 0.0, 1.0]), ("x^3 - 1", [1.0, 0.0, 0.0, -1.0]), ("x^4 - 10x^2 + 9", [1.0, 0.0, -10.0, 0.0, 9.0])]
for name, p in polys:
    print(f"{name}: " + ", ".join(text(z) for z in roots(p)))
