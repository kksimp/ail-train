vs = [("Mon", 2399), ("Tue", 1850), ("Sat", 7420), ("Tue", 999), ("Fri", 3110), ("Sun", 4500)]
p = 0
for i, (d, c) in enumerate(vs):
    b = c // 100; b = b * 2 if d == "Tue" else b
    e = b + (50 if (i + 1) % 5 == 0 else 0); p += e
    print(f"visit {i + 1} ({d}): +{e} -> {p}")
print(f"redeem {p // 100} x 100 points for {p // 100 * 5} euro off, {p % 100} points kept")
