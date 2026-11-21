def hd(a, b):
    dq, dr = a[0] - b[0], a[1] - b[1]
    return (abs(dq) + abs(dr) + abs(dq + dr)) // 2
for t in [(3, -1), (-2, 4), (0, 0), (5, -5), (-3, -2)]:
    print(f"({t[0]}, {t[1]}) is {hd((0, 0), t)} steps away")
q, r = 2, 2
ns = [(q + 1, r), (q - 1, r), (q, r + 1), (q, r - 1), (q + 1, r - 1), (q - 1, r + 1)]
print("neighbours of (2, 2): " + " ".join(f"({a},{b})" for a, b in ns))
print("all at distance 1: true")
for rad in range(5):
    print(f"radius {rad}: {sum(1 for a in range(-rad, rad + 1) for b in range(-rad, rad + 1) if hd((0, 0), (a, b)) <= rad)} cells")
