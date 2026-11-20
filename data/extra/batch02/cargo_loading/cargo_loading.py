goods = [("rice", 50.0, 60.0), ("saffron", 2.0, 300.0), ("oil", 30.0, 90.0), ("sand", 100.0, 10.0)]
for cap in [10.0, 60.0, 120.0, 500.0]:
    room, tot, log = cap, 0.0, []
    for n, k, v in sorted(goods, key=lambda g: -int(g[2] / g[1] * 1000.0)):
        if room <= 0.0: break
        t = k if k <= room else room
        tot += v * t / k; room -= t
        log.append(f"{n} {t:.1f}kg")
    print(f"capacity {cap:.0f}: {tot:.2f} ({', '.join(log)})")
