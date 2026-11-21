def run_from(r, c, h, memo):
    if memo[r][c] > 0:
        return memo[r][c]
    best = 1
    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr = r + d[0]
        nc = c + d[1]
        if nr >= 0 and nr < len(h) and nc >= 0 and nc < len(h[0]) and h[nr][nc] < h[r][c]:
            best = max(best, 1 + run_from(nr, nc, h, memo))
    memo[r][c] = best
    return best

h = [[92, 88, 85, 70, 64], [95, 81, 79, 66, 60], [90, 84, 72, 58, 55], [86, 77, 74, 51, 49], [80, 76, 68, 62, 40]]
memo = [[0] * 5 for _ in range(5)]
br = 0
bc = 0
for r in range(5):
    for c in range(5):
        if run_from(r, c, h, memo) > memo[br][bc]:
            br = r
            bc = c
path = [h[br][bc]]
r = br
c = bc
while memo[r][c] > 1:
    moved = False
    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr = r + d[0]
        nc = c + d[1]
        if not moved and nr >= 0 and nr < 5 and nc >= 0 and nc < 5 and h[nr][nc] < h[r][c] and memo[nr][nc] == memo[r][c] - 1:
            r = nr
            c = nc
            moved = True
    path.append(h[r][c])
print(f"longest run: {len(path)} cells from row {br + 1}, column {bc + 1}")
print(f"heights: {path}")
for row in memo:
    print("".join(f"{x:>3}" for x in row))
