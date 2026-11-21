def cost_of(pallets, plan):
    inbound = [5, 15, 25, 35]
    outbound = [10, 20, 30, 40]
    total = 0
    for t in range(4):
        door = inbound[plan[t]]
        for o in range(4):
            total += pallets[t][o] * (abs(door - outbound[o]) + 10)
    return total

pallets = [[12, 0, 3, 5], [0, 8, 10, 2], [4, 4, 0, 14], [9, 1, 1, 0]]
plain = cost_of(pallets, [0, 1, 2, 3])
best = plain
best_plan = [0, 1, 2, 3]
tried = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if len({a, b, c, d}) < 4:
                    continue
                tried += 1
                plan = [a, b, c, d]
                got = cost_of(pallets, plan)
                if got < best:
                    best = got
                    best_plan = plan
print(f"tried {tried} plans")
print(f"trailers at doors 1-4 in order: {plain} pallet-metres")
for t in range(4):
    print(f"trailer {t + 1} -> receiving door {best_plan[t] + 1}")
print(f"best plan: {best} pallet-metres, saving {plain - best}")
