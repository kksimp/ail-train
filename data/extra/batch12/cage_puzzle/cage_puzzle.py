def holds(cg, g):
    op, target, cells = cg
    vals = [g[c] for c in cells]
    if 0 in vals:
        return True
    a = vals[0]
    b = vals[-1]
    if op == '+':
        return sum(vals) == target
    if op == '*':
        p = 1
        for v in vals:
            p *= v
        return p == target
    if op == '-':
        return abs(a - b) == target
    if op == '/':
        return max(a, b) == min(a, b) * target
    return a == target

def solve(g, pos, cages, count, first):
    if pos == 16:
        count[0] += 1
        if count[0] == 1:
            first.extend(g)
        return
    r = pos // 4
    c = pos % 4
    for v in range(1, 5):
        clash = False
        for k in range(4):
            if g[r * 4 + k] == v or g[k * 4 + c] == v:
                clash = True
        if not clash:
            g[pos] = v
            if all(holds(cg, g) for cg in cages):
                solve(g, pos + 1, cages, count, first)
            g[pos] = 0

cages = [('-', 2, [0, 4]), ('*', 6, [1, 2]), ('/', 2, [3, 7]), ('-', 3, [5, 6]), ('+', 5, [8, 9]), ('+', 6, [10, 11, 15]), ('*', 6, [12, 13]), ('=', 4, [14])]
g = [0] * 16
count = [0]
first = []
solve(g, 0, cages, count, first)
for r in range(4):
    print(" ".join(str(x) for x in first[r * 4:r * 4 + 4]))
print(f"{count[0]} solution(s)")
