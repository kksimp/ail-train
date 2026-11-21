def square(key):
    seen = []; 
    for c in (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper():
        d = "I" if c == "J" else c
        if d.isalpha() and d not in seen: seen.append(d)
    return seen
def enc(g, msg):
    L = ["I" if c == "J" else c for c in msg.upper() if c.isalpha()]; out = []; i = 0
    while i < len(L):
        a = L[i]; b = "X"
        if i + 1 < len(L) and L[i + 1] != a: b = L[i + 1]; i += 2
        else: i += 1
        pa = g.index(a); pb = g.index(b); ra, ca = divmod(pa, 5); rb, cb = divmod(pb, 5)
        if ra == rb: out += [g[ra * 5 + (ca + 1) % 5], g[rb * 5 + (cb + 1) % 5]]
        elif ca == cb: out += [g[((ra + 1) % 5) * 5 + ca], g[((rb + 1) % 5) * 5 + cb]]
        else: out += [g[ra * 5 + cb], g[rb * 5 + ca]]
    return "".join(out)
g = square("playfair example")
for r in range(5): print(" ".join(g[r * 5:r * 5 + 5]))
for m in ["Hide the gold in the tree stump", "Meet at noon", "Jazz"]: print(f"{m} -> {enc(g, m)}")
