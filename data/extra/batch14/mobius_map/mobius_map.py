import math
def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def add(a, b):
    return (a[0] + b[0], a[1] + b[1])
def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])
def div(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)
def apply(m, z):
    return div(add(mul(m[0], z), m[1]), add(mul(m[2], z), m[3]))
def compose(f, g):
    return [add(mul(f[0], g[0]), mul(f[1], g[2])), add(mul(f[0], g[1]), mul(f[1], g[3])), add(mul(f[2], g[0]), mul(f[3], g[2])), add(mul(f[2], g[1]), mul(f[3], g[3]))]
def tidy(v):
    return 0.0 if abs(v) < 0.00005 else v
def text(z):
    r, i = tidy(z[0]), tidy(z[1])
    if i < 0.0:
        return f"{r:.4f} - {-i:.4f}i"
    return f"{r:.4f} + {i:.4f}i"
def cross(a, b, c, d):
    return div(mul(sub(a, c), sub(b, d)), mul(sub(a, d), sub(b, c)))
one, zero, i = (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)
cay = [one, (0.0, -1.0), one, i]
for z in [i, zero, one, (0.0, 2.0), (-3.0, 0.5)]:
    w = apply(cay, z)
    size = math.sqrt(w[0] * w[0] + w[1] * w[1])
    print(f"{text(z)} -> {text(w)}, distance from centre {size:.4f}")
shift = [one, (2.0, 0.0), zero, one]
both = compose(cay, shift)
z = (1.0, 1.0)
print(f"Cayley after shift by 2, as one matrix: {text(apply(both, z))}, step by step: {text(apply(cay, apply(shift, z)))}")
a, b, c, d = (2.0, 1.0), (-1.0, 3.0), (0.5, 0.5), (4.0, 2.0)
before = cross(a, b, c, d)
after = cross(apply(cay, a), apply(cay, b), apply(cay, c), apply(cay, d))
print(f"cross ratio before {text(before)}, after {text(after)}")
