def biggest(field):
    rows = len(field)
    cols = len(field[0])
    side = []
    best = 0
    br = 0
    bc = 0
    for r in range(rows):
        cs = field[r]
        row = []
        for c in range(cols):
            v = 0
            if cs[c] == '.':
                v = 1
                if r > 0 and c > 0:
                    v = 1 + min(min(side[r - 1][c], row[c - 1]), side[r - 1][c - 1])
            row.append(v)
            if v > best:
                best = v
                br = r
                bc = c
        side.append(row)
    return [best, br - best + 1, bc - best + 1]

field = ["..T.......", ".....T....", "T.........", ".......T..", "...T......", "..........", ".T.....T..", "....T....."]
for line in field:
    print(line)
b = biggest(field)
print(f"largest clear square: {b[0]} x {b[0]}, top-left at row {b[1]}, column {b[2]}")
marked = biggest(["...", "...", "..T"])
print(f"3 x 3 with one tree in a corner: {marked[0]} x {marked[0]}")
