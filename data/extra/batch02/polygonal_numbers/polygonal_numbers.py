pg = lambda s, n: ((s - 2) * n * n - (s - 4) * n) // 2
def up(s, l):
    o = set(); n = 1
    while pg(s, n) < l: o.add(pg(s, n)); n += 1
    return o
for s, lab in [(3, "triangular"), (4, "square"), (5, "pentagonal"), (6, "hexagonal")]:
    print(f"{lab:<11} " + " ".join(str(pg(s, n)) for n in range(1, 9)))
L = 100000000
tri, pen = up(3, L), up(5, L)
print(f"triangular, pentagonal and hexagonal below {L}: {[h for h in sorted(up(6, L)) if h in tri and h in pen]}")
print(f"square and triangular below 100000: {[s for s in sorted(up(4, 100000)) if s in tri]}")
