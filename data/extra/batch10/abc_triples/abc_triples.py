import math
from math import gcd

def radicals(limit):
    rad = [1] * (limit + 1)
    for p in range(2, limit + 1):
        if rad[p] == 1:
            for m in range(p, limit + 1, p):
                rad[m] *= p
    return rad

limit = 1000
rad = radicals(limit)
hits = []
for c in range(3, limit + 1):
    for a in range(1, (c + 1) // 2):
        b = c - a
        if gcd(a, b) == 1:
            r = rad[a] * rad[b] * rad[c]
            if r < c:
                hits.append([a, b, c, r])
print(f"{len(hits)} abc triples with c <= {limit}")
best = sorted(hits, key=lambda h: -(math.log(float(h[2])) / math.log(float(h[3]))))
for h in best[:6]:
    q = math.log(float(h[2])) / math.log(float(h[3]))
    print(f"{h[0]:>3} + {h[1]:>3} = {h[2]:>4}  rad {h[3]:>3}  quality {q:.4f}")
