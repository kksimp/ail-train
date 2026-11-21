F = ["legumes", "brassicas", "roots", "alliums"]; B = ["north", "east", "south", "west"]; H = {b: [] for b in B}
for y in range(6):
    ln = []
    for i, b in enumerate(B): c = F[(i + y) % 4]; H[b].append(c); ln.append(f"{b}={c}")
    print(f"year {y + 1}: {' '.join(ln)}")
ok = all(not (H[b][i] == H[b][j] and j - i < 4) for b in B for i in range(6) for j in range(i + 1, 6)); print(f"rule kept: {'true' if ok else 'false'}")
