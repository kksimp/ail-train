import math

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def d2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def hull(pts):
    ps = sorted(pts, key=lambda p: (p[0], p[1]))
    lower = []
    for p in ps:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(ps):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

pts = [[0, 0], [7, 2], [3, 9], [10, 10], [12, 4], [5, 5], [2, 3], [9, 1], [1, 7], [6, 12], [11, 8], [4, 2]]
h = hull(pts)
n = len(h)
print(f"hull: {h}")
best = 0
pair = [0, 0]
j = 1
steps = 0
for i in range(n):
    k = (i + 1) % n
    while abs(cross(h[i], h[k], h[(j + 1) % n])) > abs(cross(h[i], h[k], h[j])):
        j = (j + 1) % n
        steps += 1
    for cand in [i, k]:
        if d2(h[cand], h[j]) > best:
            best = d2(h[cand], h[j])
            pair = [cand, j]
brute = max(d2(a, b) for a in pts for b in pts)
dist = math.sqrt(float(best))
print(f"farthest pair {h[pair[0]]} and {h[pair[1]]}, squared distance {best}, distance {dist:.3f}")
print(f"calipers moved {steps} times; all {len(pts) * len(pts)} pairs give {brute}")
