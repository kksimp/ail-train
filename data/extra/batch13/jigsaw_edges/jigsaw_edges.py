def grid(n):
    best = [1, n]
    best_err = abs(3 * n - 4)
    r = 1
    while r * r <= n:
        if n % r == 0:
            c = n // r
            e = abs(3 * c - 4 * r)
            if e < best_err:
                best = [r, c]
                best_err = e
        r += 1
    return best

for n in [100, 300, 500, 1000, 1500, 2000]:
    r, c = grid(n)
    edge = 2 * (r + c) - 4
    print(f"{n:>4} pieces: {r} x {c}, 4 corners, {edge - 4} other edges, {n - edge} inside")
