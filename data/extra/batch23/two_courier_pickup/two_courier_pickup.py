NEG = -1000000

def best_two(g):
    rows = len(g)
    cols = len(g[0])
    dp = [[g[0][0] if r1 == 0 and r2 == 0 else NEG for r2 in range(rows)] for r1 in range(rows)]
    steps = rows + cols - 2
    for k in range(1, steps + 1):
        nxt = []
        for r1 in range(rows):
            row = []
            for r2 in range(rows):
                c1 = k - r1
                c2 = k - r2
                v = NEG
                if 0 <= c1 < cols and 0 <= c2 < cols:
                    prev = dp[r1][r2]
                    if r1 > 0:
                        prev = max(prev, dp[r1 - 1][r2])
                    if r2 > 0:
                        prev = max(prev, dp[r1][r2 - 1])
                    if r1 > 0 and r2 > 0:
                        prev = max(prev, dp[r1 - 1][r2 - 1])
                    if prev > NEG:
                        gain = g[r1][c1] if r1 == r2 else g[r1][c1] + g[r2][c2]
                        v = prev + gain
                row.append(v)
            nxt.append(row)
        dp = nxt
    return dp[rows - 1][rows - 1]

def best_one(g):
    best = []
    for r in range(len(g)):
        row = []
        for c in range(len(g[0])):
            v = g[r][c]
            if r > 0 and c > 0:
                v += max(best[r - 1][c], row[c - 1])
            elif r > 0:
                v += best[r - 1][c]
            elif c > 0:
                v += row[c - 1]
            row.append(v)
        best.append(row)
    return best[len(g) - 1][len(g[0]) - 1]

g = [[0, 3, 1, 1, 0], [2, 0, 0, 4, 1], [1, 5, 0, 0, 2], [0, 0, 3, 1, 0], [4, 0, 1, 0, 2]]
for row in g:
    print(" ".join(str(x) for x in row))
one = best_one(g)
two = best_two(g)
print(f"one courier: {one} parcels")
print(f"two couriers together: {two} parcels ({two - one} more)")
