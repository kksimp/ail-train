def update(tree, n, i, v):
    p = i + n; tree[p] = v
    while p > 1: p //= 2; tree[p] = max(tree[2 * p], tree[2 * p + 1])
def query(tree, n, lo, hi):
    best = 0; l = lo + n; r = hi + n
    while l < r:
        if l % 2 == 1: best = max(best, tree[l]); l += 1
        if r % 2 == 1: r -= 1; best = max(best, tree[r])
        l //= 2; r //= 2
    return best
vis = [42, 87, 130, 155, 98, 120, 176, 140, 95, 60]; n = len(vis); tree = [0] * (2 * n)
for i in range(n): update(tree, n, i, vis[i])
for lo, hi in [(0, 4), (4, 8), (0, 10), (7, 10)]: print(f"{9 + lo}:00 to {9 + hi}:00 busiest {query(tree, n, lo, hi)}")
update(tree, n, 6, 112); update(tree, n, 8, 190); print("after corrections:")
for lo, hi in [(4, 8), (0, 10)]: print(f"{9 + lo}:00 to {9 + hi}:00 busiest {query(tree, n, lo, hi)}")
