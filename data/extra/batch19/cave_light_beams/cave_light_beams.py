def lit(cave, r0, c0, d0):
    dr = [0, 1, 0, -1]; dc = [1, 0, -1, 0]
    rows = len(cave); cols = len(cave[0])
    seen = set(); cells = set()
    todo = [[r0, c0, d0]]
    while todo:
        b = todo.pop()
        r, c = b[0], b[1]
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue
        k = r * 1000 + c * 10 + b[2]
        if k in seen:
            continue
        seen.add(k)
        cells.add(r * 100 + c)
        ch = cave[r][c]
        if ch == '/':
            outs = [[3, 2, 1, 0][b[2]]]
        elif ch == '\\':
            outs = [[1, 0, 3, 2][b[2]]]
        elif ch == '|' and (b[2] == 0 or b[2] == 2):
            outs = [1, 3]
        elif ch == '-' and (b[2] == 1 or b[2] == 3):
            outs = [0, 2]
        else:
            outs = [b[2]]
        for d in outs:
            todo.append([r + dr[d], c + dc[d], d])
    return len(cells)

lines = [r".|..\.", r"..-...", r"/..|\.", r"......", r"\.-../", r"..|..."]
cave = [list(l) for l in lines]
for l in lines:
    print(l)
print(f"part 1, lamp at top-left facing right: {lit(cave, 0, 0, 0)} cells lit")
n = len(cave)
best = 0; entry = ""
for i in range(n):
    for e in [[i, 0, 0], [i, n - 1, 2], [0, i, 1], [n - 1, i, 3]]:
        v = lit(cave, e[0], e[1], e[2])
        if v > best:
            best = v; entry = f"row {e[0]} col {e[1]} heading {e[2]}"
print(f"part 2: best edge entry lights {best} cells ({entry})")
