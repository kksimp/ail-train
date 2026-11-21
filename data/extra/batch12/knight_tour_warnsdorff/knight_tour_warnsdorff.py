def onward(b, r, c, jumps):
    n = 0
    for j in jumps:
        nr = r + j[0]; nc = c + j[1]
        if 0 <= nr < 6 and 0 <= nc < 6 and b[nr][nc] == 0:
            n += 1
    return n

def tour(b, r, c, step, jumps, tries):
    b[r][c] = step
    tries[0] += 1
    if step == 36:
        return True
    options = []
    for j in jumps:
        nr = r + j[0]; nc = c + j[1]
        if 0 <= nr < 6 and 0 <= nc < 6 and b[nr][nc] == 0:
            options.append([onward(b, nr, nc, jumps), nr, nc])
    for o in sorted(options):
        if tour(b, o[1], o[2], step + 1, jumps, tries):
            return True
    b[r][c] = 0
    return False

jumps = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
b = [[0] * 6 for _ in range(6)]
tries = [0]
if tour(b, 0, 0, 1, jumps, tries):
    for row in b:
        print("".join(f"{x:>3}" for x in row))
    print(f"tour found after {tries[0]} placements")
else:
    print("no tour")
