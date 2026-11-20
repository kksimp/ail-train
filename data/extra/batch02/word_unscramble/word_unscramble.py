words = ["listen", "silent", "enlist", "google", "stone", "tones", "notes", "onset", "banana", "inlets", "tinsel"]
idx = {}
for w in words: idx.setdefault("".join(sorted(w.lower())), []).append(w)
for s in ["tsilen", "otnes", "nabana", "xyz", "ELGOOG"]:
    f = idx.get("".join(sorted(s.lower())), [])
    print(f"{s}: {', '.join(f) if f else 'no match'}")
b = max(idx, key=lambda k: len(idx[k]))
print(f"largest family: {len(idx[b])} words ({b})")
