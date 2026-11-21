std = [b * m for m in [1, 10, 100, 1000] for b in [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]]
for s in [5000, 9000, 12000]:
    for c, fv in [("red", 2000), ("green", 3100), ("blue", 3300), ("white", 3200)]:
        d = s - fv; ex = (d + 19) // 20; pick = min(r for r in std if r >= ex); ma = d / pick; mw = d * ma / 1000.0
        print(f"{s // 1000:>2} V {c:<5}: needs {ex:>4} ohm, use {pick:>4}, {ma:.1f} mA, {mw:.1f} mW")
