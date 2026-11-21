import json
rows = [("north", "tea", 120), ("south", "tea", 80), ("east", "jam", 45), ("north", "jam", 60), ("west", "tea", 200), ("south", "oats", 35), ("east", "oats", 30), ("north", "oats", 90), ("west", "jam", 15), ("south", "jam", 25)]
min_total = 100
groups = []
for region, product, amount in rows:
    found = False
    for g in groups:
        if g[0] == region:
            g[1] += 1
            g[2] += amount
            found = True
    if not found:
        groups.append([region, 1, amount])
kept = sorted([g for g in groups if g[2] > min_total], key=lambda g: -g[2])
print("region  count  sum    avg")
for g in kept:
    avg = g[2] / g[1]
    print(f"{g[0]:<7} {g[1]:>5} {g[2]:>4} {avg:>6.1f}")
dropped = [g[0] for g in groups if g[2] <= min_total]
print(f"{len(groups)} groups, {len(kept)} with sum over {min_total}; dropped {json.dumps(dropped)}")
