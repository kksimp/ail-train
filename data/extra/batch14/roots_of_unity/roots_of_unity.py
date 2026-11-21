import math
def tidy(v):
    return 0.0 if abs(v) < 0.0005 else v
def text(re, im):
    r, i = tidy(re), tidy(im)
    if i < 0.0:
        return f"{r:.3f} - {-i:.3f}i"
    return f"{r:.3f} + {i:.3f}i"
def root(k, n):
    a = 2.0 * 3.141592653589793 * k / n
    return [math.cos(a), math.sin(a)]
n = 6
sre = sim = 0.0
for k in range(n):
    z = root(k, n)
    kind = "primitive" if math.gcd(k, n) == 1 else "not primitive"
    print(f"k = {k}: {text(z[0], z[1])} ({kind})")
    sre += z[0]
    sim += z[1]
print(f"sum of the 6 roots: {text(sre, sim)}")
for m in [5, 8]:
    pre, pim = 1.0, 0.0
    for k in range(m):
        z = root(k, m)
        nre = pre * z[0] - pim * z[1]
        pim = pre * z[1] + pim * z[0]
        pre = nre
    print(f"product of the {m} roots: {text(pre, pim)}")
counts = [len([k for k in range(1, m + 1) if math.gcd(k, m) == 1]) for m in range(1, 13)]
print(f"primitive roots for n = 1..12: [{', '.join(map(str, counts))}]")
