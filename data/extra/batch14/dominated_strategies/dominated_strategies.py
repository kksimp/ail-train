def dominated(pay, mine, theirs, as_row):
    for s in mine:
        for t in mine:
            if s != t:
                worse = True
                for o in theirs:
                    vs = pay[s][o] if as_row else pay[o][s]
                    vt = pay[t][o] if as_row else pay[o][t]
                    if vs >= vt:
                        worse = False
                if worse:
                    return s
    return -1
rn = ["Up", "Middle", "Down"]
cn = ["Left", "Centre", "Right"]
a = [[4, 5, 6], [2, 8, 3], [3, 9, 2]]
b = [[3, 1, 2], [1, 4, 6], [0, 6, 8]]
rows, cols = [0, 1, 2], [0, 1, 2]
changed = True
while changed:
    changed = False
    r = dominated(a, rows, cols, True)
    if r >= 0:
        rows = [x for x in rows if x != r]
        print(f"row player drops {rn[r]}")
        changed = True
    c = dominated(b, cols, rows, False)
    if c >= 0:
        cols = [x for x in cols if x != c]
        print(f"column player drops {cn[c]}")
        changed = True
print(f"left: rows {', '.join(rn[i] for i in rows)}; columns {', '.join(cn[i] for i in cols)}")
if len(rows) == 1 and len(cols) == 1:
    print(f"predicted play pays {a[rows[0]][cols[0]]} and {b[rows[0]][cols[0]]}")
