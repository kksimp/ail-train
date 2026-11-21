def dg(c):
    for i, s in enumerate(["bfpv", "cgjkqsxz", "dt", "l", "mn", "r"]):
        if c in s: return i + 1
    return 0
def sx(n):
    cs = n.lower(); out = cs[0].upper(); last = dg(cs[0])
    for c in cs[1:]:
        d = dg(c)
        if d != 0 and d != last:
            out += str(d)
            if len(out) == 4: break
        if c not in "hw": last = d
    return out.ljust(4, "0")
ns = ["Robert", "Rupert", "Rubin", "Ashcraft", "Tymczak", "Pfister", "Lee", "Honeyman"]
for n in ns: print(f"{n:<9} {sx(n)}")
g = {}
for n in ns: g.setdefault(sx(n), []).append(n)
for k in sorted(g):
    if len(g[k]) > 1: print(f"{k}: {', '.join(g[k])}")
