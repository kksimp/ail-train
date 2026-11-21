for H in [[3, 4, 5], [1, 2, 3], [7, 7], [2, 5, 6, 9], [10, 1]]:
    x = 0
    for h in H: x ^= h
    s = " ".join(map(str, H))
    if x == 0: print(f"[{s}] nim-sum 0: player to move loses with best play"); continue
    for i, h in enumerate(H):
        if h ^ x < h: print(f"[{s}] nim-sum {x}: take {h - (h ^ x)} from heap {i + 1} (leaves {h ^ x})"); break
