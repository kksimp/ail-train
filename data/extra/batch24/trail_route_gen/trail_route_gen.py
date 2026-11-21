def walk(seed):
    state = seed
    def below(n):
        nonlocal state
        state = (state * 1103515245 + 12345) % 2147483648
        return (state // 65536) % n
    path = [40]
    while True:
        here = path[-1]
        r = here // 9; c = here % 9
        if r == 0 or r == 8 or c == 0 or c == 8: break
        options = [p for p in [here - 9, here + 9, here - 1, here + 1] if p not in path]
        if not options: break
        path.append(options[below(len(options))])
    return path
best = []
for seed in [11, 22, 33]:
    p = walk(seed)
    last = p[-1]
    edge = "reaches the edge" if last // 9 == 0 or last // 9 == 8 or last % 9 == 0 or last % 9 == 8 else "gets boxed in"
    print(f"seed {seed}: {len(p) - 1} steps, {edge}")
    if len(p) > len(best): best = p
for r in range(9):
    cells = []
    for c in range(9):
        cell = r * 9 + c
        cells.append('S' if cell == 40 else 'E' if cell == best[-1] else '*' if cell in best else '.')
    print("".join(cells))
