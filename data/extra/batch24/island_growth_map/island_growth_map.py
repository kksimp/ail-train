state = 1212
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def touches_land(g, r, c):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(g) and 0 <= cc < len(g[0]) and g[rr][cc]: return True
    return False
g = [[r == 4 and c == 7 for c in range(15)] for r in range(9)]
for step in range(40):
    edge = [[r, c] for r in range(9) for c in range(15) if not g[r][c] and touches_land(g, r, c)]
    pick = edge[below(len(edge))]
    g[pick[0]][pick[1]] = True
shore = 0
for r in range(9):
    line = []
    for c in range(15):
        if g[r][c]: line.append("#")
        else:
            line.append("~")
            if touches_land(g, r, c): shore += 1
    print("".join(line))
print(f"41 land cells, {shore} sea cells on the shore")
