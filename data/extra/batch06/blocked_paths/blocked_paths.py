G = ["....#", ".#...", "...#.", "#....", "..#.."]; W = [[0] * 5 for _ in range(5)]
for r in range(5):
    for c in range(5):
        if G[r][c] == "#": W[r][c] = 0
        elif r == 0 and c == 0: W[r][c] = 1
        else: W[r][c] = (W[r - 1][c] if r > 0 else 0) + (W[r][c - 1] if c > 0 else 0)
for r in W: print("".join(f"{w:>3}" for w in r))
print(f"paths: {W[4][4]}")
