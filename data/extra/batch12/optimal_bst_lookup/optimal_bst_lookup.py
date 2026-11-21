def build(f, root):
    n = len(f)
    e = [[0] * (n + 1) for _ in range(n + 1)]
    root.extend([[-1] * (n + 1) for _ in range(n + 1)])
    for size in range(1, n + 1):
        for i in range(0, n - size + 1):
            j = i + size
            w = sum(f[i:j])
            best = -1
            for r in range(i, j):
                c = e[i][r] + e[r + 1][j]
                if best < 0 or c < best:
                    best = c
                    root[i][j] = r
            e[i][j] = best + w
    return e[0][n]

def show(i, j, depth, root, keys, out):
    if i >= j:
        return
    r = root[i][j]
    out.append("  " * depth + keys[r])
    show(i, r, depth + 1, root, keys, out)
    show(r + 1, j, depth + 1, root, keys, out)

def balanced(i, j, depth, f):
    if i >= j:
        return 0
    m = (i + j) // 2
    return f[m] * (depth + 1) + balanced(i, m, depth + 1, f) + balanced(m + 1, j, depth + 1, f)

keys = ["add", "commit", "diff", "log", "merge", "pull", "push", "status"]
freq = [30, 25, 8, 12, 3, 20, 22, 41]
root = []
cost = build(freq, root)
lines = []
show(0, len(keys), 0, root, keys, lines)
for l in lines:
    print(l)
total = sum(freq)
avg = cost / total
print(f"optimal cost {cost}, {avg:.3f} comparisons per lookup")
print(f"middle-split tree cost {balanced(0, len(keys), 0, freq)}")
