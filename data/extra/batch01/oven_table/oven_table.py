st = [(140, 1), (150, 2), (170, 3), (180, 4), (190, 5), (200, 6), (220, 7), (230, 8)]
fa = lambda c: c * 9.0 / 5.0 + 32.0
print(f"{'C':>4} {'F':>5} gas")
for c, m in st:
    print(f"{c:>4} {fa(c):>5.0f} {m:>3}")
for f in [350.0, 400.0, 275.0, 500.0]:
    best = min(st, key=lambda s: int(abs(fa(s[0]) - f) * 100.0))
    print(f"{f:.0f}F is closest to gas {best[1]} ({best[0]}C)")
