def cp(g):
    ways = []
    for r in range(len(g)):
        row = []
        for c in range(len(g[0])):
            if g[r][c] == "#": row.append(0)
            elif r == 0 and c == 0: row.append(1)
            else: row.append((ways[r - 1][c] if r > 0 else 0) + (row[c - 1] if c > 0 else 0))
        ways.append(row)
    return ways[-1][-1]
for g in [["......"] * 5, ["......", "..#...", "....#.", ".#....", "......"], ["..#", "#..", "..."]]:
    for line in g: print(line)
    print(f"{cp(g)} routes")
