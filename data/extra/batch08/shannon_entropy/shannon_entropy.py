import math
def ent(s):
    c = {}
    for ch in s: c[ch] = c.get(ch, 0) + 1
    h = 0.0
    for ch in c: p = c[ch] / len(s); h -= p * math.log(p) / math.log(2.0)
    return h
for s in ["aaaaaaaa", "abababab", "abcdabcd", "mississippi", "the quick brown fox", "0110100110010110"]:
    h = ent(s); print(f"{s:<20} {h:.3f} bits per char, at least {h * len(s):.1f} bits")
