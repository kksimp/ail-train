import re
t = "The rain fell on the town. The town slept, and the rain fell on; rain on the roofs, rain on the river, and the river rose."; S = {"the", "on", "and", "a"}; c = {}
for r in t.split(" "):
    w = "".join(ch for ch in r.lower() if ch.isalpha())
    if w and w not in S: c[w] = c.get(w, 0) + 1
for w in sorted(c, key=lambda w: (-c[w], w))[:5]: print(f"{w}: {c[w]}")
print(f"{len(c)} distinct words")
