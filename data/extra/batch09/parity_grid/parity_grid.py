def bits_of(c):
    n = ord(c)
    return [(n >> (6 - k)) & 1 for k in range(7)]

def with_parity(rows):
    out = []
    for r in rows:
        out.append(r + [sum(r) % 2])
    last = []
    for c in range(8):
        last.append(sum(r[c] for r in out) % 2)
    out.append(last)
    return out

def show(grid):
    for r in grid:
        print("".join(str(b) for b in r))

word = "PARITY"
grid = with_parity([bits_of(c) for c in word])
show(grid)
grid[2][4] = 1 - grid[2][4]
bad_row = -1
bad_col = -1
for r in range(len(grid)):
    if sum(grid[r]) % 2 != 0:
        bad_row = r
for c in range(8):
    if sum(r[c] for r in grid) % 2 != 0:
        bad_col = c
print(f"after noise: row {bad_row} and column {bad_col} fail")
grid[bad_row][bad_col] = 1 - grid[bad_row][bad_col]
letters = []
for r in range(len(word)):
    n = 0
    for k in range(7):
        n = n * 2 + grid[r][k]
    letters.append(chr(n))
print("repaired text: " + "".join(letters))
