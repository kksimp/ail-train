import sys
sys.setrecursionlimit(10000)
def walk(g, r, c, dry, seen):
    if r == len(g) - 1:
        return 0
    best = -1
    for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ch = g[r][c]
        allowed = dry or ch == '.'
        if not allowed:
            allowed = (ch == '>' and d[1] == 1) or (ch == 'v' and d[0] == 1) or (ch == '<' and d[1] == -1) or (ch == '^' and d[0] == -1)
        nr = r + d[0]; nc = c + d[1]
        if allowed and nr >= 0 and nc >= 0 and nc < len(g[0]) and g[nr][nc] != '#' and (nr * 100 + nc) not in seen:
            seen.add(nr * 100 + nc)
            sub = walk(g, nr, nc, dry, seen)
            if sub >= 0 and sub + 1 > best:
                best = sub + 1
            seen.discard(nr * 100 + nc)
    return best

rows = ["#.#####", "#...>.#", "#.#v#.#", "#.>.>.#", "###v#.#", "#...<.#", "#.###v#", "#.....#", "#####.#"]
g = [list(r) for r in rows]
for r in rows:
    print(r)
print(f"part 1: longest downhill walk {walk(g, 0, 1, False, {1})} steps")
print(f"part 2: longest walk on dry slopes {walk(g, 0, 1, True, {1})} steps")
