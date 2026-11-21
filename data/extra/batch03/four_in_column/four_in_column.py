g = [["."] * 7 for _ in range(6)]
def cd(r, c, dr, dc, p):
    n = 0; r += dr; c += dc
    while 0 <= r < 6 and 0 <= c < 7 and g[r][c] == p: n += 1; r += dr; c += dc
    return n
def wa(r, c):
    p = g[r][c]
    return any(1 + cd(r, c, a, b, p) + cd(r, c, -a, -b, p) >= 4 for a, b in [(0, 1), (1, 0), (1, 1), (1, -1)])
pl = "R"
for i, col in enumerate([3, 4, 3, 4, 2, 2, 1, 6, 0]):
    row = -1
    for r in range(6):
        if g[r][col] == ".": row = r
    if row < 0: print(f"column {col} is full"); continue
    g[row][col] = pl
    if wa(row, col): print(f"move {i + 1}: {pl} wins in column {col}"); break
    pl = "Y" if pl == "R" else "R"
for line in g[3:]: print("".join(line))
