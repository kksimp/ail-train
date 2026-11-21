def water_near(g, r, c):
    n = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(g) and 0 <= cc < len(g[0]) and g[rr][cc] == '~': n += 1
    return n

def melt_day(g):
    out = [row[:] for row in g]
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '#' and water_near(g, r, c) >= 2: out[r][c] = '~'
    return out

def ice_count(g): return sum(row.count('#') for row in g)

lake = ["~~~~~~~~~~", "~########~", "~##o#####~", "~#oo####o~", "~##o###oo~", "~########~", "~~~~~~~~~~"]
g = [list(l) for l in lake]
print(f"day 0: {ice_count(g)} ice cells")
day = 0
while True:
    nxt = melt_day(g)
    if nxt == g: break
    g = nxt
    day += 1
    print(f"day {day}: {ice_count(g)} ice cells")
print(f"no more melting after day {day}:")
for row in g: print("".join(row))
