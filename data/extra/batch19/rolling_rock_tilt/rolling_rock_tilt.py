def tilt_north(g):
    for c in range(len(g[0])):
        free = 0
        for r in range(len(g)):
            if g[r][c] == '#':
                free = r + 1
            elif g[r][c] == 'O':
                g[r][c] = '.'; g[free][c] = 'O'; free += 1

def turn_cw(g):
    n = len(g)
    return [[g[n - 1 - r][c] for r in range(n)] for c in range(len(g[0]))]

def load(g):
    return sum((len(g) - r) * g[r].count('O') for r in range(len(g)))

rows = ["..OO.O", ".##...", "....#.", ".OO.#.", ".O#..O", "..O##."]
g = [list(r) for r in rows]
once = [list(r) for r in rows]
tilt_north(once)
print(f"part 1: load after tilting north {load(once)}")
seen = {}; loads = []; i = 0; total = 1000000
while i < total:
    key = "/".join("".join(r) for r in g)
    if key in seen:
        start = seen[key]; period = i - start
        print(f"layout after {i} spins repeats spin {start} (period {period})")
        i = start + (total - start) % period
        break
    seen[key] = i
    loads.append(load(g))
    for _ in range(4):
        tilt_north(g); g = turn_cw(g)
    i += 1
print(f"part 2: load after {total} spins {loads[i]}")
