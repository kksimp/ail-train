import sys, re

W, H = 12, 6
grid = [["."] * W for _ in range(H)]
x = y = 0
d = 1
pen = True
grid[0][0] = "#"
bad = 0
DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]
for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c == "F" and len(w) == 2 and re.fullmatch(r"[0-9]+", w[1]):
        for _ in range(int(w[1])):
            nx, ny = x + DX[d], y + DY[d]
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                break
            x, y = nx, ny
            if pen:
                grid[y][x] = "#"
    elif c == "R" and len(w) == 1:
        d = (d + 1) % 4
    elif c == "L" and len(w) == 1:
        d = (d + 3) % 4
    elif c == "U" and len(w) == 1:
        pen = False
    elif c == "D" and len(w) == 1:
        pen = True
        grid[y][x] = "#"
    else:
        bad += 1
for row in grid:
    print("".join(row))
print("pos=%d,%d dir=%s bad=%d" % (x, y, "NESW"[d], bad))
