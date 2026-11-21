def climb(g, r, c, peaks):
    if g[r][c] == 9:
        peaks.add(r * 100 + c); return 1
    t = 0
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nr = r + d[0]; nc = c + d[1]
        if 0 <= nr < len(g) and 0 <= nc < len(g[0]) and g[nr][nc] == g[r][c] + 1:
            t += climb(g, nr, nc, peaks)
    return t

rows = ["0123210", "1234321", "8765456", "9876567", "0109878", "1218989"]
g = [[int(ch) for ch in r] for r in rows]
score = rating = 0
for r in range(len(g)):
    for c in range(len(g[0])):
        if g[r][c] == 0:
            peaks = set()
            t = climb(g, r, c, peaks)
            print(f"trailhead ({r},{c}): {len(peaks)} peaks, {t} trails")
            score += len(peaks); rating += t
print(f"part 1: total score {score}")
print(f"part 2: total rating {rating}")
