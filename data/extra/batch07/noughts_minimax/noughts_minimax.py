L = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
def wi(b):
    for l in L:
        if b[l[0]] != "." and b[l[0]] == b[l[1]] == b[l[2]]: return b[l[0]]
    return "."
def sc(b, t, d):
    w = wi(b)
    if w == "X": return 10 - d
    if w == "O": return d - 10
    if "." not in b: return 0
    bs = -100 if t == "X" else 100
    for i in range(9):
        if b[i] == ".":
            nb = b[:]; nb[i] = t; s = sc(nb, "O" if t == "X" else "X", d + 1)
            if t == "X" and s > bs: bs = s
            if t == "O" and s < bs: bs = s
    return bs
for p, t in [("X.O.X..O.", "X"), ("XO.XO....", "X"), ("XX.OO....", "O"), ("X...O....", "X"), ("OX.XO.X..", "O")]:
    b = list(p); bm = -1; bs = -100 if t == "X" else 100
    for i in range(9):
        if b[i] == ".":
            nb = b[:]; nb[i] = t; s = sc(nb, "O" if t == "X" else "X", 1)
            if (t == "X" and s > bs) or (t == "O" and s < bs): bs = s; bm = i
    print(f"{p} {t} to play: square {bm + 1}, {'X wins' if bs > 0 else 'O wins' if bs < 0 else 'draw'}")
