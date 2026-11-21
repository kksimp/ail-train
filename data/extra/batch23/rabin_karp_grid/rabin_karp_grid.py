MOD = 1000003
B1 = 257
B2 = 263

def power(b, e):
    r = 1
    for _ in range(e):
        r = r * b % MOD
    return r

def row_hashes(cs, w):
    top = power(B1, w - 1)
    out = []
    h = 0
    for i in range(len(cs)):
        if i >= w:
            h = (h - ord(cs[i - w]) * top % MOD + MOD) % MOD
        h = (h * B1 + ord(cs[i])) % MOD
        if i >= w - 1:
            out.append(h)
    return out

def verify(grid, pattern, top, left):
    w = len(pattern[0])
    for k in range(len(pattern)):
        if grid[top + k][left:left + w] != pattern[k]:
            return False
    return True

grid = ["xabxxabx", "xcdxxcdx", "xxxabxxx", "abxcdxab", "cdxxxxcd", "xxabcdxx"]
pattern = ["ab", "cd"]
w = len(pattern[0])
ph = len(pattern)
rows = [row_hashes(list(line), w) for line in grid]
target = 0
for p in pattern:
    target = (target * B2 + row_hashes(list(p), w)[0]) % MOD
down = power(B2, ph - 1)
hits = []
for c in range(len(rows[0])):
    h = 0
    for r in range(len(grid)):
        if r >= ph:
            h = (h - rows[r - ph][c] * down % MOD + MOD) % MOD
        h = (h * B2 + rows[r][c]) % MOD
        if r >= ph - 1 and h == target:
            top = r - ph + 1
            if verify(grid, pattern, top, c):
                hits.append(f"({top}, {c})")
for line in grid:
    print(line)
print(f"pattern ab/cd: {len(hits)} matches confirmed cell by cell")
shown = " ".join(hits)
print(f"top-left corners (row, col): {shown}")
