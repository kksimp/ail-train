skus = [("BRG-10", 1200, 450), ("MTR-22", 85, 21000), ("SCR-04", 50000, 3), ("BLT-08", 9000, 55), ("PMP-31", 40, 38000), ("GSK-12", 6000, 40), ("VLV-17", 300, 2900), ("FLT-05", 2200, 310), ("WSH-01", 80000, 1), ("CPL-09", 700, 640)]
ranked = sorted(skus, key=lambda s: -(s[1] * s[2]))
grand = sum(s[1] * s[2] for s in skus)
running = 0
counts = {"A": 0, "B": 0, "C": 0}
for code, units, cost in ranked:
    value = units * cost
    before = running * 100 // grand
    running += value
    cls = "A" if before < 80 else "B" if before < 95 else "C"
    counts[cls] += 1
    pct = running * 1000 // grand
    print(f"{code} {value:>9,} cumulative {pct // 10:>3}.{pct % 10}% class {cls}")
for cls, n in counts.items():
    print(f"class {cls}: {n} items")
