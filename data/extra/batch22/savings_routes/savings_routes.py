def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def route_len(pts, route):
    total = 0
    at = 0
    for c in route:
        total += dist(pts[at], pts[c])
        at = c
    return total + dist(pts[at], pts[0])

pts = [[0, 0], [4, 0], [5, 3], [0, 6], [-3, 4], [-4, -2], [2, -5]]
loads = [0, 4, 3, 5, 2, 6, 3]
routes = [[c] for c in range(7)]
owner = list(range(7))
savings = []
for i in range(1, 7):
    for j in range(i + 1, 7):
        savings.append([dist(pts[0], pts[i]) + dist(pts[0], pts[j]) - dist(pts[i], pts[j]), i, j])
for s, i, j in sorted(savings, key=lambda x: (-x[0], x[1], x[2])):
    ri = owner[i]
    rj = owner[j]
    if s <= 0 or ri == rj or loads[ri] + loads[rj] > 10:
        continue
    a = routes[ri][::-1] if routes[ri][0] == i else routes[ri]
    b = routes[rj] if routes[rj][0] == j else routes[rj][::-1]
    if a[-1] != i or b[0] != j:
        continue
    joined = a + b
    routes[ri] = joined
    routes[rj] = []
    loads[ri] += loads[rj]
    loads[rj] = 0
    for c in joined:
        owner[c] = ri
    print(f"join {i} and {j} (saves {s}): {joined}")
total = 0
for r in range(1, 7):
    if routes[r]:
        n = route_len(pts, routes[r])
        total += n
        print(f"route {routes[r]}: load {loads[r]}, length {n}")
separate = sum(2 * dist(pts[0], pts[c]) for c in range(1, 7))
print(f"total {total} against {separate} for one trip per customer")
