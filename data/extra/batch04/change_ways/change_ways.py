def ways(a, cs):
    w = [0] * (a + 1); w[0] = 1
    for c in cs:
        for v in range(c, a + 1): w[v] += w[v - c]
    return w[a]
C = [1, 2, 5, 10, 20, 50, 100, 200]
for a in [5, 10, 50, 100, 200]: print(f"{a}: {ways(a, C)} ways")
out = []
def lw(a, cs, f, u):
    if a == 0: out.append("+".join(map(str, u))); return
    for i in range(f, len(cs)):
        if cs[i] <= a: lw(a - cs[i], cs, i, u + [cs[i]])
lw(10, [10, 5, 2, 1], 0, [])
print(f"10 as {len(out)}: {', '.join(out[:6])} ...")
