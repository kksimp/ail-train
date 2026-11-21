rects = [[1, 1, 6, 4], [3, 2, 9, 7], [5, 0, 8, 3], [2, 5, 4, 9], [7, 6, 10, 8]]
xs = sorted({v for r in rects for v in (r[0], r[2])})
ys = sorted({v for r in rects for v in (r[1], r[3])})
by_depth = {}
for i in range(len(xs) - 1):
    for j in range(len(ys) - 1):
        depth = 0
        for r in rects:
            if r[0] <= xs[i] and xs[i + 1] <= r[2] and r[1] <= ys[j] and ys[j + 1] <= r[3]:
                depth += 1
        if depth > 0:
            by_depth[depth] = by_depth.get(depth, 0) + (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])
union = 0
for d in sorted(by_depth):
    print(f"covered by exactly {d}: {by_depth[d]}")
    union += by_depth[d]
total = sum((r[2] - r[0]) * (r[3] - r[1]) for r in rects)
print(f"union area {union}, sum of areas {total}, grid {len(xs) - 1} x {len(ys) - 1} cells")
