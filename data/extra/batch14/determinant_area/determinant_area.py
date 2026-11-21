def shoelace2(pts):
    s = 0
    for i in range(len(pts)):
        j = (i + 1) % len(pts)
        s += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
    return s
def apply(m, pts):
    return [[m[0] * x + m[1] * y, m[2] * x + m[3] * y] for x, y in pts]
plot = [[0, 0], [4, 0], [5, 2], [1, 3]]
base = shoelace2(plot)
print(f"plot [{', '.join('[' + str(x) + ', ' + str(y) + ']' for x, y in plot)}]: twice the signed area {base}")
maps = [("shear x += 2y", [1, 2, 0, 1]), ("stretch 3 by 2", [3, 0, 0, 2]), ("turn 90", [0, -1, 1, 0]), ("flip and stretch", [2, 1, 4, -1]), ("squash to a line", [1, 2, 2, 4])]
for name, m in maps:
    det = m[0] * m[3] - m[1] * m[2]
    after = shoelace2(apply(m, plot))
    side = "anticlockwise" if after > 0 else ("clockwise" if after < 0 else "flat")
    print(f"{name:<17} det {det:>3}: twice the area {after:>4} = {det} x {base}, {side}")
