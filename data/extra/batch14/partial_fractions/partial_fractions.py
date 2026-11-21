from math import gcd
def make(n, d):
    g = gcd(n, d)
    s = -1 if d < 0 else 1
    return (s * n // g, s * d // g)
def plus(a, b):
    return make(a[0] * b[1] + b[0] * a[1], a[1] * b[1])
def text(f):
    return f"{f[0]}" if f[1] == 1 else f"{f[0]}/{f[1]}"
def ev(c, x):
    t = 0
    for k in c:
        t = t * x + k
    return t
def factor(r):
    return "x" if r == 0 else (f"(x + {-r})" if r < 0 else f"(x - {r})")
cases = [("3x + 5", [3, 5], [1, -1]), ("x^2 + 1", [1, 0, 1], [0, 1, 2]), ("5", [5], [-1, -2, -3]), ("2x^2 - x + 4", [2, -1, 4], [3, -1, 2])]
for name, num, roots in cases:
    terms = []
    total = make(0, 1)
    den10 = 1
    for i in range(len(roots)):
        d = 1
        for j in range(len(roots)):
            if j != i:
                d *= roots[i] - roots[j]
        a = make(ev(num, roots[i]), d)
        mag = make(abs(a[0]), a[1])
        body = f"{text(mag)}/{factor(roots[i])}" if a[1] == 1 else f"({text(mag)})/{factor(roots[i])}"
        sign = ("-" if a[0] < 0 else "") if not terms else (" - " if a[0] < 0 else " + ")
        terms.append(f"{sign}{body}")
        total = plus(total, make(a[0], a[1] * (10 - roots[i])))
        den10 *= 10 - roots[i]
    lhs = make(ev(num, 10), den10)
    print(f"({name}) / {''.join(factor(r) for r in roots)} = {''.join(terms)}")
    print(f"    at x = 10: {text(lhs)} vs {text(total)}")
