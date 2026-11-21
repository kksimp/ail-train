t = [(36, "3.5"), (37, "4"), (38, "5"), (39, "6"), (40, "6.5"), (41, "7.5"), (42, "8"), (43, "9"), (44, "9.5"), (45, "10.5")]
def uk(e):
    b = t[0]
    for r in t:
        if abs(r[0] - e) < abs(b[0] - e): b = r
    return b[1]
for e in [36, 41, 47, 30]: print(f"EU {e} -> UK {uk(e)}")
c = {}
for e in [42, 41, 42, 39, 44, 42, 38, 41, 43, 42, 40, 41]: c[uk(e)] = c.get(uk(e), 0) + 1
for s, n in sorted(c.items(), key=lambda kv: -kv[1])[:3]: print(f"UK {s}: {n} pairs")
