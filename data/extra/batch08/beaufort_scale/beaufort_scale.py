lim = [1, 6, 12, 20, 29, 39, 50, 62, 75, 89, 103, 118]
names = ["calm", "light air", "light breeze", "gentle breeze", "moderate breeze", "fresh breeze", "strong breeze", "near gale", "gale", "strong gale", "storm", "violent storm", "hurricane force"]
worst = 0
for d, k in [("Mon", 0), ("Tue", 4), ("Wed", 15), ("Thu", 28), ("Fri", 45), ("Sat", 70), ("Sun", 95), ("gust", 130)]:
    f = sum(1 for l in lim if k >= l); worst = max(worst, f); print(f"{d:<4} {k:>3} km/h: force {f:>2}, {names[f]}")
print(f"highest force {worst}: {names[worst]}")
