def seen_full(g, r, c, far):
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0: continue
            y, x = r + dr, c + dc
            while 0 <= y < len(g) and 0 <= x < len(g[0]):
                if g[y][x] == '#':
                    n += 1; break
                if g[y][x] == 'L' or not far:
                    break
                y += dr; x += dc
    return n

def settle(start, far, limit):
    g = [list(r) for r in start]
    changed = True
    while changed:
        changed = False
        nxt = [list(r) for r in g]
        for r in range(len(g)):
            for c in range(len(g[0])):
                n = seen_full(g, r, c, far)
                if g[r][c] == 'L' and n == 0:
                    nxt[r][c] = '#'; changed = True
                elif g[r][c] == '#' and n >= limit:
                    nxt[r][c] = 'L'; changed = True
        g = nxt
    return sum(row.count('#') for row in g)

rows = ["L.LL.LLL", "LLLLLL.L", "L.L.L..L", "LLLL.LLL", "L.LL.LL.", "L.LLLLLL", "..L.L...", "LLLLLLLL"]
g = [list(r) for r in rows]
print(f"{sum(row.count('L') for row in g)} seats in the lounge")
print(f"part 1: {settle(g, False, 4)} seats taken when it settles")
print(f"part 2: {settle(g, True, 5)} seats taken with line-of-sight rules")
