def so(k): return sum(ord(c) for c in k) % 11
T = [""] * 11
for p in ["AB12", "CD34", "BA21", "EF56", "GH78", "DC43", "XY99", "ZZ01"]:
    i = so(p); pr = 1
    while T[i] != "": i = (i + 1) % 11; pr += 1
    T[i] = p; print(f"{p}: home {so(p)}, stored at {i} after {pr} probe(s)")
for i, t in enumerate(T): print(f"  {i:>2} {t if t else '-'}")
for w in ["DC43", "QQ00"]:
    i = so(w); s = 1
    while T[i] != "" and T[i] != w: i = (i + 1) % 11; s += 1
    print(f"lookup {w}: {'found at ' + str(i) if T[i] == w else 'absent'} in {s} step(s)")
