from math import gcd
def gr(a, b):
    out = []
    while a > 0:
        d = (b + a - 1) // a; out.append(d); a, b = a * d - b, b * d
        if a > 0:
            g = gcd(a, b); a //= g; b //= g
    return out
for a, b in [(2, 3), (3, 4), (4, 13), (5, 6), (7, 15), (4, 17)]:
    print(f"{a}/{b} = " + " + ".join(f"1/{d}" for d in gr(a, b)))
l = max(range(1, 20), key=lambda n: (len(gr(n, 20)), -n))
print(f"most parts for n/20: {l}/20 with {len(gr(l, 20))}")
