games = [("prisoners' dilemma", ["quiet", "confess"], ["quiet", "confess"], [[3, 0], [5, 1]], [[3, 5], [0, 1]]), ("stag hunt", ["stag", "hare"], ["stag", "hare"], [[4, 0], [3, 3]], [[4, 3], [0, 3]]), ("matching pennies", ["heads", "tails"], ["heads", "tails"], [[1, -1], [-1, 1]], [[-1, 1], [1, -1]]), ("concert or match", ["concert", "match"], ["concert", "match"], [[2, 0], [0, 1]], [[1, 0], [0, 2]]), ("price war", ["high", "mid", "low"], ["high", "mid", "low"], [[6, 2, 1], [7, 4, 2], [5, 3, 3]], [[6, 7, 5], [2, 4, 3], [1, 2, 3]])]
for name, rows, cols, a, b in games:
    eq = []
    for i in range(len(rows)):
        for j in range(len(cols)):
            rb = all(a[k][j] <= a[i][j] for k in range(len(rows)))
            cb = all(b[i][k] <= b[i][j] for k in range(len(cols)))
            if rb and cb:
                eq.append(f"({rows[i]}, {cols[j]}) pays {a[i][j]}/{b[i][j]}")
    text = "none in pure strategies" if not eq else ", ".join(eq)
    print(f"{name}: {text}")
