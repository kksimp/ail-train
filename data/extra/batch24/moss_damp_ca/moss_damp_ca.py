def moss_near(g, r, c):
    n = 0
    if r > 0: n += g[r-1][c]
    if r + 1 < len(g): n += g[r+1][c]
    if c > 0: n += g[r][c-1]
    if c + 1 < len(g[r]): n += g[r][c+1]
    return n

def next_state(cur, wet, n):
    if cur == 1 and (wet or n >= 3): return 1
    if cur == 0 and wet and n >= 2: return 1
    return 0

damp = ["~~~~......", "~~~~~.....", ".~~~~~~...", "...~~~~~..", "....~~~...", ".....~...."]
g = [[0]*len(l) for l in damp]
g[0][0] = 1; g[1][1] = 1; g[0][3] = 1; g[2][6] = 1
for gen in range(1, 6):
    nxt = []
    for r in range(len(g)):
        cells = list(damp[r])
        nxt.append([next_state(g[r][c], cells[c] == '~', moss_near(g, r, c)) for c in range(len(cells))])
    g = nxt
    total = sum(sum(x) for x in g)
    print(f"generation {gen}: {total} moss cells")
for r in range(len(g)):
    print("".join('#' if g[r][c] == 1 else damp[r][c] for c in range(len(damp[r]))))
