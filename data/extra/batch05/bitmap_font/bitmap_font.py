F = [[7, 5, 5, 5, 7], [2, 6, 2, 2, 7], [7, 1, 7, 4, 7], [7, 1, 7, 1, 7], [5, 5, 7, 1, 1], [7, 4, 7, 1, 7], [7, 4, 7, 5, 7], [7, 1, 2, 2, 2], [7, 5, 7, 5, 7], [7, 5, 7, 1, 7]]
for num in ["2026", "8.1"]:
    for r in range(5):
        p = []
        for c in num:
            if c == ".": p.append("#" if r == 4 else " "); continue
            p.append("".join("#" if F[int(c)][r] & b else " " for b in (4, 2, 1)))
        print(" ".join(p).rstrip())
    print("")
