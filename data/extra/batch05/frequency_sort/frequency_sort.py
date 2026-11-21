from collections import Counter
for w in ["tree", "banana", "mississippi", "abracadabra", "letter"]:
    c = Counter(w); print(f"{w} -> " + "".join(k * c[k] for k in sorted(c, key=lambda k: (-c[k], k))))
