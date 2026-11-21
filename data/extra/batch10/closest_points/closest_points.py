import math

def d2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def brute(ps, checks):
    best = -1
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            checks[0] += 1
            d = d2(ps[i], ps[j])
            if best < 0 or d < best:
                best = d
    return best

def split(ps, checks):
    if len(ps) <= 3:
        return brute(ps, checks)
    mid = len(ps) // 2
    midx = ps[mid][0]
    left = split(ps[:mid], checks)
    right = split(ps[mid:], checks)
    best = min(left, right)
    strip = sorted([p for p in ps if (p[0] - midx) ** 2 < best], key=lambda p: p[1])
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) ** 2 < best:
            checks[0] += 1
            best = min(best, d2(strip[i], strip[j]))
            j += 1
    return best

seed = 4242
pts = []
for _ in range(60):
    seed = (seed * 1103515245 + 12345) % 2147483648
    x = (seed // 65536) % 1000
    seed = (seed * 1103515245 + 12345) % 2147483648
    y = (seed // 65536) % 1000
    pts.append((x, y))
sorted_pts = sorted(pts)
c1, c2 = [0], [0]
a = brute(pts, c1)
b = split(sorted_pts, c2)
print(f"60 points: closest squared distance {a} (distance {math.sqrt(float(a)):.3f})")
print(f"every pair: {c1[0]} checks; divide and conquer: {b} after {c2[0]} checks")
for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
        if d2(pts[i], pts[j]) == a:
            print(f"pair ({pts[i][0]}, {pts[i][1]}) and ({pts[j][0]}, {pts[j][1]})")
