def ec(k):
    c = 0
    for s, r in [(100, 18), (200, 26), (1000000, 34)]:
        u = min(k, s); c += u * r; k -= u
        if k == 0: break
    return c
for n, k, d in [("flat 1", 85, 30), ("flat 2", 240, 30), ("house", 610, 31), ("cottage", 300, 28)]:
    t = ec(k) + d * 45; print(f"{n:<8} {k:>4} kWh {d} days: {t // 100}.{t % 100:02}")
