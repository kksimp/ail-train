ws = ["listen", "silent", "enlist", "stone", "notes", "onset", "tones", "lemon", "melon", "apple", "inlets", "solo"]
g = {}
for w in ws: g.setdefault("".join(sorted(w.lower())), []).append(w)
for k, v in g.items():
    if len(v) > 1: print(f"{k}: {' '.join(v)}")
print(f"largest: {max(len(v) for v in g.values())} words")
