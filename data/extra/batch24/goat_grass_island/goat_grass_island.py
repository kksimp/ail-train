grass = [5, 1, 0, 3, 5, 2, 0, 4, 1, 3]
goats = [[0, 4], [5, 4], [7, 3]]
def graze(g, grass):
    n = len(grass)
    best = g[0]
    for p in [(g[0] + n - 1) % n, (g[0] + 1) % n]:
        if grass[p] > grass[best]: best = p
    g[0] = best
    bite = min(grass[best], 2)
    grass[best] -= bite
    g[1] += bite - 1
for day in range(1, 13):
    nh = []
    for g in goats:
        graze(g, grass)
        if g[1] >= 8:
            nh.append([g[0], g[1] // 2]); nh.append([g[0], g[1] - g[1] // 2])
        elif g[1] > 0:
            nh.append(g)
    goats = nh
    for i in range(len(grass)): grass[i] = min(grass[i] + 1, 5)
    print(f"day {day:>2}: {len(goats)} goats, grass {sum(grass)} {grass}")
