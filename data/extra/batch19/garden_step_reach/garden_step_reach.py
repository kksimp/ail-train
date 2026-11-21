def reach(g, steps, endless):
    h = len(g); w = len(g[0])
    for r in range(h):
        c = g[r].find('S')
        if c >= 0: sr, sc = r, c
    dist = {f"{sr},{sc}": 0}
    queue = [[sr, sc, 0]]; head = 0; hits = 0
    while head < len(queue):
        q = queue[head]; head += 1
        if q[2] % 2 == steps % 2: hits += 1
        if q[2] == steps: continue
        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr = q[0] + d[0]; nc = q[1] + d[1]
            if not endless and (nr < 0 or nr >= h or nc < 0 or nc >= w):
                continue
            tile = g[(nr % h + h) % h][(nc % w + w) % w]
            key = f"{nr},{nc}"
            if tile != '#' and key not in dist:
                dist[key] = q[2] + 1; queue.append([nr, nc, q[2] + 1])
    return hits

g = ["........", ".##.#..#", "...#....", ".#..S.#.", "....##..", "#.#.....", "...#..#."]
for row in g:
    print(row)
print(f"part 1: {reach(g, 6, False)} plots in exactly 6 steps")
for n in [8, 14, 20]:
    print(f"part 2: {reach(g, n, True)} plots in exactly {n} steps on the endless field")
