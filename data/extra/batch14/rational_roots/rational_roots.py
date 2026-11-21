from math import gcd
def divisors(n):
    return [d for d in range(1, abs(n) + 1) if n % d == 0]
def is_root(a, p, q):
    n = len(a) - 1
    return sum(a[i] * p ** (n - i) * q ** i for i in range(len(a))) == 0
polys = [("2x^3 - 3x^2 - 11x + 6", [2, -3, -11, 6]), ("6x^3 - 11x^2 + 6x - 1", [6, -11, 6, -1]), ("x^3 - 2", [1, 0, 0, -2]), ("4x^4 - 17x^2 + 4", [4, 0, -17, 0, 4])]
for name, a in polys:
    tried = 0
    roots = []
    for q in divisors(a[0]):
        for p in divisors(a[-1]):
            for s in [1, -1]:
                if gcd(p, q) == 1:
                    tried += 1
                    if is_root(a, s * p, q):
                        roots.append((s * p, q))
    roots.sort(key=lambda r: r[0] / r[1])
    shown = [f"{n}" if d == 1 else f"{n}/{d}" for n, d in roots]
    text = ", ".join(shown) if shown else "none"
    print(f"{name}: {tried} candidates, rational roots {text}")
