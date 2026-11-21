def read_version(n, w, r):
    versions = [2 if i < w else 1 for i in range(n)]
    best = 0
    for i in range(n - r, n):
        best = max(best, versions[i])
    return best

n = 5
for w, r in [(1, 1), (2, 3), (3, 3), (3, 2), (5, 1), (1, 5), (2, 2), (4, 2)]:
    got = read_version(n, w, r)
    overlap = "yes" if w + r > n else "no"
    result = "sees v2" if got == 2 else "STALE v1"
    print(f"W={w} R={r}: R+W={w + r:>2} overlap {overlap:<3} -> {result}")
print(f"rule: R + W > {n} guarantees a fresh read")
