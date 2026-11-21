def sp(F, C):
    t = k = s = 0
    for i in range(len(F)):
        g = F[i] - C[i]; t += g; k += g
        if k < 0: s = i + 1; k = 0
    return -1 if t < 0 else s
for F, C in [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), ([2, 3, 4], [3, 4, 3]), ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), ([4, 6, 7, 4], [6, 5, 3, 5])]:
    s = sp(F, C); print(f"fuel {sum(F)} < cost {sum(C)}: no start works" if s < 0 else f"start at depot {s + 1} (fuel {sum(F)}, cost {sum(C)})")
