def chi(c):
    e = sum(c) / len(c); return sum((x - e) * (x - e) / e for x in c)
for n, c in [("red", [22, 17, 21, 19, 23, 18]), ("blue", [12, 15, 18, 20, 24, 31]), ("green", [20, 20, 20, 20, 20, 20]), ("white", [27, 14, 16, 25, 13, 25])]:
    s = 0.0
    for x in c: d = x - sum(c) / len(c); s += d * d / (sum(c) / len(c))
    print(f"{n:<5} {' '.join(str(x) for x in c)}: chi-square {s:>5.2f}, {'looks loaded' if s > 11.07 else 'consistent with fair'}")
