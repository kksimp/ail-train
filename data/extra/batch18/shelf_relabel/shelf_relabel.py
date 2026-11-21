rises = {"dairy": 8, "bakery": 5, "household": 3}
items = [["milk 2l", "dairy", 145], ["cheddar", "dairy", 329], ["bloomer", "bakery", 180], ["bin bags", "household", 210], ["bananas", "fruit", 99]]
old = [p[2] for p in items]
for it in items:
    pct = rises.get(it[1], 0)
    if pct > 0:
        r = it[2] + (it[2] * pct + 99) // 100; it[2] = (r // 100) * 100 + 99
for i, p in enumerate(items): print(f"{p[0]:<9} {old[i]:>4} -> {p[2]:>4} (+{p[2] - old[i]})")
print(f"{sum(1 for p in items if rises.get(p[1], 0) == 0)} items kept their price")
