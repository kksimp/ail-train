def ls(sq):
    n = len(sq)
    return [sum(r) for r in sq] + [sum(sq[r][c] for r in range(n)) for c in range(n)] + [sum(sq[i][i] for i in range(n)), sum(sq[i][n - 1 - i] for i in range(n))]
def magic(sq):
    n = len(sq); s = {x for r in sq for x in r}
    if len(s) != n * n or any(x < 1 or x > n * n for x in s): return False
    t = ls(sq); return all(x == t[0] for x in t)
def siamese(n):
    sq = [[0] * n for _ in range(n)]; r, c = 0, n // 2
    for k in range(1, n * n + 1):
        sq[r][c] = k
        nr, nc = (r - 1) % n, (c + 1) % n
        if sq[nr][nc]: r = (r + 1) % n
        else: r, c = nr, nc
    return sq
b = lambda x: str(x).lower()
print(f"lo shu: {b(magic([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))}")
print(f"swapped: {b(magic([[9, 4, 2], [3, 5, 7], [8, 1, 6]]))}")
print(f"all fives: {b(magic([[5, 5, 5]] * 3))}")
for n in [3, 5]:
    sq = siamese(n)
    for row in sq: print("".join(f"{x:>3}" for x in row))
    print(f"n={n}: magic {b(magic(sq))}, total {ls(sq)[0]}")
