from math import gcd

found = []
for n in range(10, 100):
    for d in range(n + 1, 100):
        if n % 10 == 0 and d % 10 == 0:
            continue
        nd = [n // 10, n % 10]
        dd = [d // 10, d % 10]
        for i in range(2):
            for j in range(2):
                if nd[i] == dd[j] and dd[1 - j] != 0:
                    a = nd[1 - i]
                    b = dd[1 - j]
                    if n * b == d * a:
                        found.append((n, d))
                        print(f"{n}/{d} = {a}/{b} after striking the {nd[i]}s")
pn, pd = 1, 1
for n, d in found:
    pn, pd = pn * n, pd * d
    g = gcd(pn, pd)
    pn, pd = pn // g, pd // g
print(f"product of the {len(found)} fractions: {pn}/{pd}")
