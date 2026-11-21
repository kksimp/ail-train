def stay_chance(r0, c0, k):
    jumps = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
    p = [[0.0] * 8 for _ in range(8)]
    p[r0][c0] = 1.0
    for _ in range(k):
        q = [[0.0] * 8 for _ in range(8)]
        for r in range(8):
            for c in range(8):
                if p[r][c] > 0.0:
                    for j in jumps:
                        nr = r + j[0]
                        nc = c + j[1]
                        if nr >= 0 and nr < 8 and nc >= 0 and nc < 8:
                            q[nr][nc] += p[r][c] / 8.0
        p = q
    total = 0.0
    for row in p:
        for x in row:
            total += x
    return total

squares = [("a1", 0, 0), ("b1", 0, 1), ("d4", 3, 3)]
for name, r, c in squares:
    parts = []
    for k in range(1, 5):
        v = stay_chance(r, c, k)
        parts.append(f"{v:.6f}")
    print(f"{name}: {'  '.join(parts)}")
print("columns are 1 to 4 moves")
