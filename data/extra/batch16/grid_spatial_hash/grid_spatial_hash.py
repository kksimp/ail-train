seed = 7
xs = []
ys = []
for i in range(40):
    seed = (seed * 1103515245 + 12345) % 2147483648
    xs.append((seed // 65536) % 100)
    seed = (seed * 1103515245 + 12345) % 2147483648
    ys.append((seed // 65536) % 100)
cell = 10
grid = {}
for i in range(len(xs)):
    grid.setdefault((xs[i] // cell) * 100 + ys[i] // cell, []).append(i)
print(f"{len(xs)} points in {len(grid)} occupied cells")
for q in [[50, 50, 12], [5, 95, 15], [80, 20, 9], [33, 66, 20]]:
    reach = (q[2] + cell - 1) // cell
    found = []
    measured = 0
    for cx in range(q[0] // cell - reach, q[0] // cell + reach + 1):
        for cy in range(q[1] // cell - reach, q[1] // cell + reach + 1):
            for i in grid.get(cx * 100 + cy, []):
                measured += 1
                dx = xs[i] - q[0]
                dy = ys[i] - q[1]
                if dx * dx + dy * dy <= q[2] * q[2]:
                    found.append(i)
    full = [i for i in range(len(xs)) if (xs[i] - q[0]) ** 2 + (ys[i] - q[1]) ** 2 <= q[2] * q[2]]
    agree = "true" if sorted(found) == full else "false"
    print(f"around ({q[0]}, {q[1]}) r {q[2]}: {sorted(found)} measured {measured} of {len(xs)}, matches scan {agree}")
