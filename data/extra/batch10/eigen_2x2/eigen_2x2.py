import math

def spectrum(m):
    t = m[0][0] + m[1][1]
    d = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    disc = t * t - 4.0 * d
    if disc > 0.0:
        r = math.sqrt(disc)
        return ("real", (t + r) / 2.0, (t - r) / 2.0)
    if disc == 0.0:
        return ("rep", t / 2.0, 0.0)
    return ("cx", t / 2.0, math.sqrt(-disc) / 2.0)

def vector_for(m, lam):
    x = m[0][1] if m[0][1] != 0.0 else lam - m[1][1]
    y = lam - m[0][0] if m[0][1] != 0.0 else m[1][0]
    n = math.sqrt(x * x + y * y)
    return f"({x / n:.4f}, {y / n:.4f})"

mats = [[[2.0, 1.0], [1.0, 2.0]], [[1.0, 2.0], [3.0, 4.0]], [[1.0, 1.0], [1.0, 0.0]], [[4.0, 1.0], [0.0, 4.0]], [[0.0, -1.0], [1.0, 0.0]], [[3.0, -2.0], [4.0, -1.0]]]
for m in mats:
    print(f"{m}:")
    kind, a, b = spectrum(m)
    if kind == "real":
        print(f"    {a:.4f} with {vector_for(m, a)}, {b:.4f} with {vector_for(m, b)}")
    elif kind == "rep":
        print(f"    {a:.4f} twice")
    else:
        print(f"    {a:.4f} +- {b:.4f}i")
