def spot(s):
    h = 0
    for c in s: h = (h * 31 + ord(c)) % 360
    return h
def ring(nodes): return sorted([(spot(f"{n}-{v}"), n) for n in nodes for v in range(3)])
def owner(pts, key):
    k = spot(key)
    for p, n in pts:
        if p >= k: return n
    return pts[0][1]
b4 = ring(["alpha", "beta", "gamma"]); af = ring(["alpha", "gamma"]); moved = 0
keys = ["user:17", "cart:9", "img:cat", "img:dog", "session:a1", "session:b2", "video:42", "doc:7"]
for k in keys:
    a = owner(b4, k); b = owner(af, k); moved += a != b
    print(f"{k:<10} at {spot(k):>3}: {a} -> {b}{'' if a == b else ' (moved)'}")
print(f"{moved} of {len(keys)} keys moved when beta left")
