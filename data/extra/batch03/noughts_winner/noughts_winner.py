L = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
def w(c, p): return any(all(c[i] == p for i in l) for l in L)
def v(rows):
    c = "".join(rows); x = c.count("X"); o = c.count("O")
    if x != o and x != o + 1: return "impossible counts"
    xw, ow = w(c, "X"), w(c, "O")
    if xw and ow: return "impossible, both won"
    if xw: return "X wins"
    if ow: return "O wins"
    return "still going" if "." in c else "draw"
for b in [["XXX", "OO.", "..."], ["XOX", "XOO", "OXX"], ["XO.", "XO.", ".O."], ["XXX", "OOO", "..."], ["XX.", "...", "..."], ["X..", ".O.", "..."], ["OXX", "XOO", "XXO"]]:
    print(f"{'/'.join(b)}: {v(b)}")
