G = [list(r) for r in ["xx..xx..", "x......x", "..xx.x..", "x.x.x.x.", "...xx..."]]
P = [(r, c) for r in range(2, 5) for c in range(7) if G[r][c] == "." and G[r][c + 1] == "."]
print("pairs (row, seat): " + " ".join(f"{r + 1}{c + 1}" for r, c in P))
b = min(P, key=lambda p: (-p[0], abs(2 * p[1] + 1 - 7), p[1]))
for r in range(5): print("".join("B" if r == b[0] and c in (b[1], b[1] + 1) else G[r][c] for c in range(8)))
