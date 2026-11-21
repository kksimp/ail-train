def find(parent, x):
    r = x
    while parent[r] != r:
        r = parent[r]
    c = x
    while parent[c] != r:
        up = parent[c]
        parent[c] = r
        c = up
    return r

def join(parent, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra != rb:
        parent[ra] = rb

def percolates(rows):
    h = len(rows)
    w = len(rows[0])
    top = h * w
    bottom = h * w + 1
    parent = list(range(h * w + 2))
    for r in range(h):
        for c in range(w):
            if rows[r][c] == '.':
                i = r * w + c
                if r == 0:
                    join(parent, i, top)
                if r == h - 1:
                    join(parent, i, bottom)
                if c + 1 < w and rows[r][c + 1] == '.':
                    join(parent, i, i + 1)
                if r + 1 < h and rows[r + 1][c] == '.':
                    join(parent, i, i + w)
    return find(parent, top) == find(parent, bottom)

samples = [["#.###", "#..##", "##.#.", "#..#.", "#.###"], ["..#..", "#.#.#", "#.###", "###..", "....."], [".#.#.", ".#.#.", "...#.", "####.", "....."], ["#####", ".....", ".....", ".....", "....."]]
for i, s in enumerate(samples):
    opened = sum(r.count(".") for r in s)
    verdict = "seeps through" if percolates(s) else "holds water"
    print(f"sample {i + 1}: {opened:>2} of 25 cells open, {verdict}")
