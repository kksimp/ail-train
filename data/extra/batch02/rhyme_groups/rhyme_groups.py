words = ["cat", "hat", "moon", "spoon", "tree", "sky", "bat", "noon", "free", "dog", "fly"]
e = lambda w: w if len(w) <= 2 else w[-2:]
g = {}
for w in words: g.setdefault(e(w), []).append(w)
for k, ws in g.items():
    if len(ws) >= 2: print(f"-{k}: {' '.join(ws)}")
print("no rhyme: " + " ".join(w for w in words if len(g[e(w)]) == 1))
print(f"groups: {len(g)}, rhyming groups: {sum(1 for v in g.values() if len(v) >= 2)}")
