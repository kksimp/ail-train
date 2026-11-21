def tile(seed):
    x = seed; px = []
    for _ in range(64):
        x = (x * 1103515245 + 12345) % 2147483648
        px.append((x // 65536) % 256)
    return px
res = []
for s in [11, 22, 33, 44, 55, 66]:
    px = tile(s)
    res.append([sum(px) // len(px), max(px), sum(1 for p in px if p < 40)])
for i, r in enumerate(res):
    print(f"tile {i + 1}: mean {r[0]:>3}, max {r[1]:>3}, dark pixels {r[2]:>2}")
means = [r[0] for r in res]
print(f"brightest tile: {means.index(max(means)) + 1}")
