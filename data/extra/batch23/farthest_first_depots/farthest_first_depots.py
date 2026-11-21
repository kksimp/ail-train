import math

def d2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy

def radius2(towns, centres):
    worst = 0
    for t in towns:
        near = -1
        for c in centres:
            d = d2(t, towns[c])
            if near < 0 or d < near:
                near = d
        worst = max(worst, near)
    return worst

towns = [[0, 0], [2, 1], [1, 3], [10, 2], [11, 0], [12, 3], [5, 9], [6, 11], [4, 10], [9, 9], [3, 6], [8, 5]]
centres = [0]
while len(centres) < 3:
    far = 0
    far_d = -1
    for i in range(len(towns)):
        near = -1
        for c in centres:
            d = d2(towns[i], towns[c])
            if near < 0 or d < near:
                near = d
        if near > far_d:
            far_d = near
            far = i
    centres.append(far)
g = radius2(towns, centres)
print(f"farthest-first depots at towns {centres}: worst distance {math.sqrt(float(g)):.2f}")
best = -1
best_set = [0, 0, 0]
n = len(towns)
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            r = radius2(towns, [a, b, c])
            if best < 0 or r < best:
                best = r
                best_set = [a, b, c]
print(f"best possible depots {best_set}: worst distance {math.sqrt(float(best)):.2f}")
ratio = math.sqrt(float(g) / float(best))
print(f"ratio {ratio:.2f} (never above 2)")
