bs = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
def hat(x):
    h = 0
    for b in bs:
        if b[0] <= x < b[1] and b[2] > h: h = b[2]
    return h
edges = sorted(x for b in bs for x in (b[0], b[1]))
prev = 0; pts = []; area = 0
for i, x in enumerate(edges):
    h = hat(x)
    if h != prev: pts.append(f"({x}, {h})"); prev = h
    if i + 1 < len(edges): area += h * (edges[i + 1] - x)
print(f"roofline: {' '.join(pts)}")
print(f"area under roofline: {area}")
