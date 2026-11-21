swims = [("Mon", "free", 40, 1500), ("Tue", "breast", 24, 1080), ("Wed", "free", 60, 2190), ("Thu", "back", 20, 900), ("Fri", "free", 32, 1120), ("Sat", "breast", 30, 1305)]

def mmss(s):
    return f"{s // 60}:{s % 60:02d}"

best = {}
metres = 0
for day, stroke, lengths, secs in swims:
    m = lengths * 25
    p = secs * 100 // m
    metres += m
    if p < best.get(stroke, 100000):
        best[stroke] = p
    print(f"{day} {stroke:<6} {m:>4} m in {mmss(secs):>5}, {mmss(p)} per 100 m")
for stroke, p in best.items():
    print(f"best {stroke}: {mmss(p)} per 100 m")
print(f"week: {metres // 1000}.{metres % 1000 // 10:02d} km")
