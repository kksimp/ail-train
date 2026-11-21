class Quad:
    def __init__(s, x, y, size):
        s.x, s.y, s.size, s.pts, s.kids = x, y, size, [], []

def insert(pool, node, p, xs, ys):
    if not pool[node].kids:
        if len(pool[node].pts) < 2 or pool[node].size == 1:
            pool[node].pts.append(p)
            return
        half = pool[node].size // 2
        for k in range(4):
            pool.append(Quad(pool[node].x + (k % 2) * half, pool[node].y + (k // 2) * half, half))
            pool[node].kids.append(len(pool) - 1)
        old = pool[node].pts
        pool[node].pts = []
        for q in old:
            insert(pool, node, q, xs, ys)
    q = pool[node]
    half = q.size // 2
    kx = 1 if xs[p] >= q.x + half else 0
    ky = 1 if ys[p] >= q.y + half else 0
    insert(pool, q.kids[ky * 2 + kx], p, xs, ys)

def count(pool, node, r, opened):
    q = pool[node]
    if q.x >= r[2] or q.x + q.size <= r[0] or q.y >= r[3] or q.y + q.size <= r[1]:
        return 0
    opened[0] += 1
    if not q.kids:
        return len(q.pts)
    acc = 0
    for k in q.kids:
        acc += count(pool, k, r, opened)
    return acc

xs = [3, 5, 6, 7, 40, 41, 50, 60, 10, 12, 33, 34, 35, 36, 2, 58]
ys = [4, 6, 5, 7, 40, 44, 10, 60, 50, 52, 33, 35, 34, 36, 60, 2]
pool = [Quad(0, 0, 64)]
for p in range(len(xs)):
    insert(pool, 0, p, xs, ys)
leaves = [q for q in pool if not q.kids]
smallest = min([64] + [q.size for q in leaves])
print(f"{len(xs)} points, {len(pool)} cells, {len(leaves)} leaves, smallest cell {smallest}")
for r in [[0, 0, 16, 16], [32, 32, 48, 48], [0, 32, 64, 64], [20, 0, 30, 30]]:
    opened = [0]
    got = count(pool, 0, r, opened)
    brute = sum(1 for p in range(len(xs)) if r[0] <= xs[p] < r[2] and r[1] <= ys[p] < r[3])
    print(f"box {r}: {got} points (check {brute}), opened {opened[0]} of {len(pool)} cells")
