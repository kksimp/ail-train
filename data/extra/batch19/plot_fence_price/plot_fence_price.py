def at(g, r, c):
    return '.' if r < 0 or r >= len(g) or c < 0 or c >= len(g[0]) else g[r][c]

rows = ["AAAABB", "ACCABB", "ACCAAD", "EEADDD", "EEAADF"]
g = [list(r) for r in rows]
done = set(); p1 = p2 = 0
for r0 in range(len(g)):
    for c0 in range(len(g[0])):
        if r0 * 100 + c0 in done: continue
        done.add(r0 * 100 + c0)
        plant = g[r0][c0]
        cells = [[r0, c0]]; i = 0; perim = 0; corners = 0
        while i < len(cells):
            r, c = cells[i]; i += 1
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if at(g, r + d[0], c + d[1]) != plant:
                    perim += 1
                elif (r + d[0]) * 100 + c + d[1] not in done:
                    done.add((r + d[0]) * 100 + c + d[1]); cells.append([r + d[0], c + d[1]])
            for d in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                a = at(g, r + d[0], c) == plant
                b = at(g, r, c + d[1]) == plant
                diag = at(g, r + d[0], c + d[1]) == plant
                if (not a and not b) or (a and b and not diag):
                    corners += 1
        print(f"plot {plant}: area {len(cells)}, perimeter {perim}, sides {corners}")
        p1 += len(cells) * perim; p2 += len(cells) * corners
print(f"part 1: fencing costs {p1}")
print(f"part 2: with the discount {p2}")
