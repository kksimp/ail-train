def od(P, C):
    ind = {c: 0 for c in C}
    for a, b in P: ind[b] += 1
    dn = []
    while len(dn) < len(C):
        r = sorted(c for c in C if ind[c] == 0 and c not in dn)
        if not r: return None
        p = r[0]; dn.append(p)
        for a, b in P:
            if a == p: ind[b] -= 1
    return dn
print(" -> ".join(od([("intro", "algebra"), ("algebra", "calculus"), ("calculus", "mechanics"), ("physics", "mechanics"), ("algebra", "stats"), ("intro", "physics")], ["algebra", "calculus", "physics", "stats", "mechanics", "intro"])))
o = od([("a", "b"), ("b", "c"), ("c", "a")], ["a", "b", "c", "d"]); print(" -> ".join(o) if o else "cycle: no valid order")
