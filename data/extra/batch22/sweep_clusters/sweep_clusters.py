import math
stops = [("A", 4.0, 1.0, 5), ("B", 2.0, 5.0, 4), ("C", -3.0, 4.0, 6), ("D", -5.0, -1.0, 3), ("E", -1.0, -4.0, 7), ("F", 3.0, -3.0, 5), ("G", 6.0, 3.0, 2), ("H", -2.0, 1.0, 4)]

def length(route):
    total = 0.0
    px = 0.0
    py = 0.0
    for s in route:
        total += math.hypot(s[1] - px, s[2] - py)
        px = s[1]
        py = s[2]
    return total + math.hypot(px, py)

order = sorted(stops, key=lambda s: math.atan2(s[2], s[1]))
routes = []
current = []
load = 0
for s in order:
    if load + s[3] > 15:
        routes.append(current)
        current = []
        load = 0
    current.append(s)
    load += s[3]
routes.append(current)
total = 0.0
for i, r in enumerate(routes):
    names = " ".join(s[0] for s in r)
    n = length(r)
    total += n
    weight = sum(s[3] for s in r)
    print(f"van {i + 1}: {names}, load {weight}, length {n:.2f}")
print(f"all vans {total:.2f}")
