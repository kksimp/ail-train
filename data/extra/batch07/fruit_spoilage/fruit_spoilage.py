def ho(G):
    C = [list(r) for r in G]; fr = []; f = 0
    for r in range(len(C)):
        for c in range(len(C[r])):
            if C[r][c] == "R": fr.append((r, c))
            elif C[r][c] == "F": f += 1
    t = 0
    while f > 0 and fr:
        nx = []
        for a, b in fr:
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = a + x; c = b + y
                if 0 <= r < len(C) and 0 <= c < len(C[r]) and C[r][c] == "F": C[r][c] = "R"; f -= 1; nx.append((r, c))
        fr = nx; t += 1
    return -1 if f > 0 else t
for g in [["RFF", "FF.", ".FF"], ["RFF", ".FF", "F.F"], ["..", ".."], ["F.R", "FFF", "R.F"]]: print(f"{'/'.join(g)}: {ho(g)}")
