def child(a, b): return a + b if a.isupper() or not b.isupper() else b + a
def cross(p, q):
    c = {}
    for a in p:
        for b in q: k = child(a, b); c[k] = c.get(k, 0) + 1
    parts = [f"{k} {c[k]}/4" for k in sorted(c)]; dom = sum(c[k] for k in c if k[0].isupper())
    print(f"{p} x {q}: {', '.join(parts)}; dominant look {dom}/4")
def gam(p): return [x + y for x in p[0:2] for y in p[2:4]]
cross("Aa", "Aa"); cross("AA", "aa"); cross("Aa", "aa")
looks = {}
for g in gam("AaBb"):
    for h in gam("AaBb"):
        k = ("A_" if g[0].isupper() or h[0].isupper() else "aa") + ("B_" if g[1].isupper() or h[1].isupper() else "bb")
        looks[k] = looks.get(k, 0) + 1
print(f"AaBb x AaBb: {', '.join(f'{k} {looks[k]}' for k in ['A_B_', 'A_bb', 'aaB_', 'aabb'])} of 16")
