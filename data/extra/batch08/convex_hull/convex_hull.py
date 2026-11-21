def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def hull(points):
    pts = sorted(points); lower = []; upper = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
trees = [[0, 0], [4, 0], [4, 4], [0, 4], [2, 2], [1, 3], [3, 1], [2, 5], [5, 2], [2, -1], [1, 1], [3, 3]]
f = hull(trees)
print("fence posts: " + " ".join(f"({p[0]}, {p[1]})" for p in f))
print(f"{len(f)} on the fence, {len(trees) - len(f)} inside")
