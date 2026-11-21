def settle(g, step):
    h = len(g); w = len(g[0])
    done = set()
    for k in range(h - 1):
        r = h - 2 - k
        for c in range(w):
            if g[r][c] == 'w' and (r * w + c) not in done:
                if g[r+1][c] == '.':
                    g[r][c] = '.'; g[r+1][c] = 'w'
                else:
                    first = -1 if step % 2 == 0 else 1
                    for side in [first, -first]:
                        cc = c + side
                        if 0 <= cc < w and g[r][cc] == '.':
                            g[r][c] = '.'; g[r][cc] = 'w'
                            done.add(r * w + cc)
                            break

rows = [".........", ".........", "..#####..", ".........", "#.......#", "##.....##", "#########"]
g = [list(l) for l in rows]
for step in range(1, 31):
    if g[0][4] == '.': g[0][4] = 'w'
    settle(g, step)
    if step % 10 == 0:
        wet = sum(row.count('w') for row in g)
        print(f"step {step}: {wet} units of water")
for row in g: print("".join(row))
