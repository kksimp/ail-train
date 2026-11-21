def hooks(shape):
    grid = []
    for r in range(len(shape)):
        row = []
        for c in range(shape[r]):
            below = sum(1 for r2 in range(r + 1, len(shape)) if shape[r2] > c)
            row.append(shape[r] - c - 1 + below + 1)
        grid.append(row)
    return grid

def tableaux(shape):
    n = sum(shape)
    f = 1
    for i in range(2, n + 1):
        f *= i
    for row in hooks(shape):
        for h in row:
            f = f // h
    return f

def shapes(n, max_part):
    if n == 0:
        return [[]]
    out = []
    top = n if n < max_part else max_part
    for first in range(top, 0, -1):
        for rest in shapes(n - first, first):
            out.append([first] + rest)
    return out

for row in hooks([3, 2, 1]):
    print(f"hooks {row}")
for n in [4, 5, 6]:
    total = 0
    parts = []
    for s in shapes(n, n):
        f = tableaux(s)
        total += f * f
        parts.append(str(f))
    print(f"n = {n}: counts {' '.join(parts)}; sum of squares {total}")
