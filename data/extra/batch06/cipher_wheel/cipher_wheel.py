def ap(t, k, d):
    o = ""; i = 0
    for c in t:
        if c.islower(): o += chr((ord(c) - 97 + d * (ord(k[i % len(k)]) - 97) + 26) % 26 + 97); i += 1
        else: o += c
    return o
for m in ["attack at dawn", "meet me by the old mill, at nine.", "the quick brown fox"]:
    e = ap(m, "lemon", 1); print(e); print(f"  back: {'true' if ap(e, 'lemon', -1) == m else 'false'}")
