def square(r, c):
    return f"{chr(97 + c)}{8 - r}"

NAMES = {'q': "queen", 'r': "rook", 'b': "bishop", 'n': "knight", 'p': "pawn"}

def attackers(rows):
    g = [list(row) for row in rows]
    kr = kc = 0
    for r in range(8):
        for c in range(8):
            if g[r][c] == 'K':
                kr, kc = r, c
    out = []
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for i, d in enumerate(dirs):
        r = kr + d[0]
        c = kc + d[1]
        while 0 <= r < 8 and 0 <= c < 8 and g[r][c] == '.':
            r += d[0]
            c += d[1]
        if 0 <= r < 8 and 0 <= c < 8:
            p = g[r][c]
            straight = i < 4
            if p == 'q' or (straight and p == 'r') or (not straight and p == 'b'):
                out.append(f"{NAMES.get(p, 'piece')} on {square(r, c)}")
    for j in [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]:
        r = kr + j[0]
        c = kc + j[1]
        if 0 <= r < 8 and 0 <= c < 8 and g[r][c] == 'n':
            out.append(f"knight on {square(r, c)}")
    for dc in [-1, 1]:
        r = kr - 1
        c = kc + dc
        if r >= 0 and 0 <= c < 8 and g[r][c] == 'p':
            out.append(f"pawn on {square(r, c)}")
    return out

positions = [["....r...", "........", "........", "........", "........", ".....n..", "........", "....K..."], ["........", "...b....", "........", ".....P..", "........", "...p....", "....K...", "........"], ["q.......", "........", "........", "........", "........", "........", "........", ".r.K...."], ["........", "........", "..b.....", "........", "....K...", "........", "........", "....r..."]]
for i, pos in enumerate(positions):
    found = attackers(pos)
    text = "not in check" if not found else ", ".join(found)
    print(f"position {i + 1}: {text}")
