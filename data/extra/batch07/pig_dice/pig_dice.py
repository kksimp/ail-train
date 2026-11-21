R = [4, 6, 3, 5, 2, 6, 1, 5, 5, 6, 4, 3, 6, 2, 5, 6, 1, 4, 4, 6, 5, 3, 2, 6, 6, 1, 5, 4, 6, 3, 2, 5, 6, 4, 1, 6, 6, 5, 3, 4, 2, 6, 5, 6, 4, 3, 1, 5, 6, 6, 2, 4, 5, 3, 6, 6, 4, 2, 5, 1, 6, 3, 4, 5, 6, 2, 6, 4, 3, 5, 6, 6, 1, 4, 5, 2, 3, 6, 4, 6]
H = [20, 15]; S = [0, 0]; p = 0; tp = 0; tu = 0; w = -1
for r in R:
    if r == 1: tp = 0; p = 1 - p; tu += 1; continue
    tp += r
    if S[p] + tp >= 100: S[p] += tp; w = p; break
    if tp >= H[p]: S[p] += tp; print(f"P{p + 1} holds {tp} -> {S[p]}"); tp = 0; p = 1 - p; tu += 1
print(f"P{w + 1} wins {S[w]} to {S[1 - w]} after {tu + 1} turns" if w >= 0 else f"rolls ran out at {S[0]} to {S[1]}")
