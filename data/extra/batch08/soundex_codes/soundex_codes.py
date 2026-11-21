def digit(c):
    for d, g in [(1, "BFPV"), (2, "CGJKQSXZ"), (3, "DT"), (4, "L"), (5, "MN"), (6, "R")]:
        if c in g: return d
    return 0
def sx(name):
    cs = name.upper(); code = cs[0]; last = digit(cs[0])
    for c in cs[1:]:
        d = digit(c)
        if d != 0 and d != last and len(code) < 4: code += str(d)
        if c not in "HW": last = d
    return code.ljust(4, "0")
groups = {}
for n in ["Robert", "Rupert", "Rubin", "Ashcraft", "Ashcroft", "Tymczak", "Pfister", "Honeyman", "Lee", "Jackson"]:
    c = sx(n); print(f"{n:<9} {c}"); groups.setdefault(c, []).append(n)
for c in sorted(groups):
    if len(groups[c]) > 1: print(f"sound alike {c}: {', '.join(groups[c])}")
