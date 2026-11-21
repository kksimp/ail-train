from functools import lru_cache
def run(size, bl):
    memo = {}
    def p(r, c):
        if r < 0 or c < 0 or (r, c) in bl: return 0
        if r == 0 and c == 0: return 1
        if (r, c) in memo: return memo[(r, c)]
        memo[(r, c)] = p(r - 1, c) + p(r, c - 1); return memo[(r, c)]
    return p(size - 1, size - 1), len(memo)
B = {(1, 1), (2, 3), (4, 2)}
for s in [3, 5, 8]:
    n, m = run(s, B); print(f"{s}x{s}: {n} paths, {m} cells cached")
print(f"16x16 with no blocks: {run(16, set())[0]}")
