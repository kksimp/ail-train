def plan(i, j, last, vals, out):
    if j - i < 2:
        return
    k = last[i][j]
    plan(i, k, last, vals, out)
    plan(k, j, last, vals, out)
    out.append(vals[k])

balloons = [3, 1, 5, 8, 2]
vals = [1] + balloons + [1]
n = len(vals)
best = [[0] * n for _ in range(n)]
last = [[0] * n for _ in range(n)]
for gap in range(2, n):
    for i in range(0, n - gap):
        j = i + gap
        for k in range(i + 1, j):
            score = best[i][k] + best[k][j] + vals[i] * vals[k] * vals[j]
            if score > best[i][j]:
                best[i][j] = score
                last[i][j] = k
order = []
plan(0, n - 1, last, vals, order)
print(f"balloons: {balloons}")
print(f"pop in order: {order}")
print(f"best score: {best[0][n - 1]}")
left = list(balloons)
naive = 0
while len(left) > 0:
    a = left[1] if len(left) > 1 else 1
    naive += left[0] * a
    left.pop(0)
print(f"popping left to right scores {naive}")
