P = [("Ash", 0, 3), ("Bly", 5, 1), ("Cor", 10, 2), ("Dex", 12, 1), ("Eda", 20, 3), ("Fio", 22, 2), ("Gil", 50, 1)]; W = []; ni = 0; t = 0; s = 0
while s < len(P):
    while ni < len(P) and P[ni][1] <= t: W.append(P[ni]); ni += 1
    if not W: t = P[ni][1]; continue
    p = min(W, key=lambda p: (p[2], p[1])); W.remove(p); print(f"{t:>3}: {p[0]} (level {p[2]}, waited {t - p[1]})"); t += 15; s += 1
