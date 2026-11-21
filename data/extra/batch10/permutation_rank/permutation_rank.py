def rank(perm):
    n = len(perm)
    r = 0
    for i in range(n):
        smaller = sum(1 for j in range(i + 1, n) if perm[j] < perm[i])
        r = r * (n - i) + smaller
    return r

def unrank(k, n):
    pool = list(range(n))
    fact = 1
    for i in range(1, n):
        fact *= i
    rest = k
    out = []
    for i in range(n):
        idx = rest // fact
        rest = rest % fact
        out.append(pool.pop(idx))
        if n - 1 - i > 0:
            fact = fact // (n - 1 - i)
    return out

for p in [[0, 1, 2, 3], [3, 2, 1, 0], [1, 0, 3, 2], [2, 0, 3, 1]]:
    print(f"{p} has rank {rank(p)}")
for k in [0, 5, 17, 23]:
    print(f"rank {k:>2} of 4 items: {unrank(k, 4)}")
m = unrank(999999, 10)
print(f"millionth ordering of 0..9: {''.join(str(x) for x in m)}, rank back {rank(m)}")
