W = ["listen", "silent", "enlist", "google", "gooegl", "cat", "act", "tac", "dog", "god", "bird", "inlets"]; g = {}
for w in W: g.setdefault("".join(sorted(w)), []).append(w)
ks = sorted([k for k in g if len(g[k]) > 1], key=lambda k: (-len(g[k]), k))
for k in ks: print(f"{k}: {' '.join(g[k])}")
print(f"{len(ks)} groups")
