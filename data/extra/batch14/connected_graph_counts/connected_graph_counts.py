from math import comb
g = [1]
c = [0]
for n in range(1, 10):
    g.append(1 << (n * (n - 1) // 2))
    cn = g[n]
    for k in range(1, n):
        cn -= comb(n - 1, k - 1) * c[k] * g[n - k]
    c.append(cn)
print("  n           graphs        connected  share")
for n in range(1, 10):
    share = c[n] / g[n]
    print(f"{n:>3} {g[n]:>16} {c[n]:>16}  {share:.3f}")
print("almost every large random graph is connected")
