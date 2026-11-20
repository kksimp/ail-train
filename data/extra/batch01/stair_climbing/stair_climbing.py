from functools import lru_cache
def cw(n, steps):
    @lru_cache(None)
    def f(k):
        if k == 0: return 1
        if k < 0: return 0
        return sum(f(k - s) for s in steps)
    return f(n)
def routes(n, steps):
    if n == 0: return [[]]
    return [[s] + r for s in steps if s <= n for r in routes(n - s, steps)]
for steps in [[1, 2], [1, 3], [2, 3, 5]]:
    print(f"steps {'/'.join(map(str, steps))}: " + " ".join(str(cw(n, tuple(steps))) for n in range(1, 11)))
for r in routes(4, [1, 2]):
    print("+".join(map(str, r)))
print(f"50 stairs by 1 or 2: {cw(50, (1, 2))}")
