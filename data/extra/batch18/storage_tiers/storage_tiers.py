tiers = [("hot", 20, 0, 1), ("cool", 10, 10, 1), ("archive", 2, 90, 6)]
total = 0
for name, gb, months, reads in [("backups", 500, 12, 0), ("logs", 50, 2, 200), ("photos", 200, 3, 40), ("scratch", 30, 1, 10)]:
    costs = [gb * max(months, mm) * pm + reads * pr for _, pm, pr, mm in tiers]
    best = 0
    for i in range(1, 3):
        if costs[i] < costs[best]: best = i
    total += costs[best]
    print(f"{name:<8} {' / '.join(str(c) for c in costs)} -> {tiers[best][0]}")
print(f"cheapest plan costs {total} cents")
