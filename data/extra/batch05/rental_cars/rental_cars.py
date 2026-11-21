F = [["K1", "small", 35, []], ["K2", "small", 32, []], ["V1", "van", 70, []], ["E1", "estate", 48, []]]; inc = 0
fr = lambda c, a, b: all(b < r[0] or a > r[1] for r in c[3])
for cl, a, b in [("small", 1, 3), ("small", 2, 4), ("small", 3, 5), ("van", 1, 7), ("van", 6, 8), ("estate", 4, 4), ("small", 5, 6)]:
    p = -1
    for i, c in enumerate(F):
        if c[1] == cl and fr(c, a, b) and (p < 0 or c[2] < F[p][2]): p = i
    if p < 0: print(f"{cl} days {a}-{b}: refused")
    else: F[p][3].append((a, b)); co = F[p][2] * (b - a + 1); inc += co; print(f"{cl} days {a}-{b}: {F[p][0]} for {co}")
print(f"income {inc}")
