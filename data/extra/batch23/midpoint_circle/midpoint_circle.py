def circle_points(r):
    pts = set()
    x = r
    y = 0
    err = 1 - r
    while x >= y:
        for p in [(x, y), (y, x), (-y, x), (-x, y), (-x, -y), (-y, -x), (y, -x), (x, -y)]:
            pts.add((p[0] + 50) * 100 + p[1] + 50)
        y += 1
        if err < 0:
            err += 2 * y + 1
        else:
            x -= 1
            err += 2 * (y - x) + 1
    return pts

r = 5
pts = circle_points(r)
for row in range(2 * r + 1):
    line = []
    for col in range(2 * r + 1):
        key = (col - r + 50) * 100 + (r - row) + 50
        line.append("#" if key in pts else ".")
    print("".join(line))
counts = [len(circle_points(k)) for k in range(1, 9)]
print(f"pixels for radius 1..8: {counts}")
