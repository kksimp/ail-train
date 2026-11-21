def line(x0, y0, x1, y1):
    dx = abs(x1 - x0); dy = -abs(y1 - y0); sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
    err = dx + dy; x = x0; y = y0; out = []
    while True:
        out.append([x, y])
        if x == x1 and y == y1: break
        e2 = 2 * err
        if e2 >= dy: err += dy; x += sx
        if e2 <= dx: err += dx; y += sy
    return out
canvas = [["."] * 24 for r in range(10)]
for l in [[0, 0, 23, 9], [0, 9, 23, 0], [2, 4, 21, 4], [12, 0, 12, 9], [0, 2, 6, 9]]:
    pts = line(*l)
    for p in pts: canvas[p[1]][p[0]] = "#"
    print(f"({l[0]}, {l[1]}) to ({l[2]}, {l[3]}): {len(pts)} pixels")
for row in canvas: print("".join(row))
