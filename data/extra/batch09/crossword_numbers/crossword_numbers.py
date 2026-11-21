def is_open(g, r, c):
    return r >= 0 and c >= 0 and r < len(g) and c < len(g[0]) and g[r][c] != '#'

def read(g, r, c, dr, dc):
    out = []
    i, j = r, c
    while is_open(g, i, j):
        out.append(g[i][j])
        i += dr
        j += dc
    return "".join(out)

rows = ["SPA#C", "HOLDS", "ORE#A", "PET#R", "#S#BY"]
g = [list(r) for r in rows]
n = 0
across = []
down = []
for r in range(len(g)):
    cells = []
    for c in range(len(g[0])):
        if not is_open(g, r, c):
            cells.append("##")
            continue
        starts_across = not is_open(g, r, c - 1) and is_open(g, r, c + 1)
        starts_down = not is_open(g, r - 1, c) and is_open(g, r + 1, c)
        if starts_across or starts_down:
            n += 1
            cells.append(f"{n:>2}")
            if starts_across:
                across.append(f"{n} {read(g, r, c, 0, 1)}")
            if starts_down:
                down.append(f"{n} {read(g, r, c, 1, 0)}")
        else:
            cells.append(" .")
    print(" ".join(cells))
print("across: " + ", ".join(across))
print("down: " + ", ".join(down))
