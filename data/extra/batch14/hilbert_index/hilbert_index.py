def d2xy(n, d):
    x = y = 0
    t = d
    s = 1
    while s < n:
        rx = (t // 2) % 2
        ry = (t ^ rx) % 2
        if ry == 0:
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return [x, y]
n = 8
grid = [[0] * n for r in range(n)]
for d in range(n * n):
    x, y = d2xy(n, d)
    grid[y][x] = d
for r in range(n - 1, -1, -1):
    print("".join(f"{v:>3}" for v in grid[r]))
ok = True
for d in range(1, n * n):
    a, b = d2xy(n, d - 1), d2xy(n, d)
    if abs(a[0] - b[0]) + abs(a[1] - b[1]) != 1:
        ok = False
print(f"every step moves to an adjacent cell: {'true' if ok else 'false'}")
a, b = d2xy(n, 0), d2xy(n, n * n - 1)
print(f"the curve starts at [{a[0]}, {a[1]}] and ends at [{b[0]}, {b[1]}]")
