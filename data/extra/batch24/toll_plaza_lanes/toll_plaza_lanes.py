def mean_waits(cars, tag_lanes, cash_lanes):
    free = [[0] * tag_lanes, [0] * cash_lanes]
    waits = [0, 0]; counts = [0, 0]
    for t, kind in cars:
        lanes = free[kind]
        best = 0
        for i in range(1, len(lanes)):
            if lanes[i] < lanes[best]: best = i
        start = max(lanes[best], t)
        lanes[best] = start + (3 if kind == 0 else 14)
        waits[kind] += start - t
        counts[kind] += 1
    return [waits[0] / counts[0], waits[1] / counts[1]]
cars = []
seed = 31; t = 0
for i in range(60):
    seed = (seed * 75 + 74) % 65537
    t += seed % 5
    kind = 1 if seed % 3 == 0 else 0
    cars.append([t, kind])
cash = sum(1 for c in cars if c[1] == 1)
print(f"{len(cars)} cars in {t} seconds, {cash} paying cash")
for plan in [[2, 2], [3, 1]]:
    w = mean_waits(cars, plan[0], plan[1])
    print(f"{plan[0]} tag + {plan[1]} cash lanes: tag wait {w[0]:.2f} s, cash wait {w[1]:.2f} s")
