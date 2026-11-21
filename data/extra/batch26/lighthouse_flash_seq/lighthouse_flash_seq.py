def fl(g, p):
    s = 0
    while True:
        for k in range(g): yield s + k * 2
        s += p
def upto(gen, lim):
    out = []
    for t in gen:
        if t >= lim: break
        out.append(t)
    return out
a = upto(fl(3, 15), 60); b = upto(fl(2, 10), 60)
strip = lambda on, n: "".join("*" if t in on else "." for t in range(n))
print(f"Fl(3) 15s  {strip(a, 30)}")
print(f"Fl(2) 10s  {strip(b, 30)}")
print(f"flash together at {[t for t in a if t in b]}")
print(f"flashes per minute: {len(a)} and {len(b)}")
g = fl(3, 15); l = [next(g) for _ in range(8)][5:]
print(f"sixth to eighth flash of the first light: {l}")
