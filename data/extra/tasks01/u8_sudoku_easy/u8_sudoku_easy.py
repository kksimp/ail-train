import sys

lines = [l.strip() for l in sys.stdin.read().split("\n") if l.strip() != ""]
valid = len(lines) == 9 and all(len(l) == 9 and all(c in "123456789." for c in l) for l in lines)
if not valid:
    print("invalid input")
    sys.exit(0)

g = [0 if c == "." else int(c) for l in lines for c in l]

def ok(g, pos, v):
    r, c = divmod(pos, 9)
    for i in range(9):
        if i != c and g[r * 9 + i] == v:
            return False
        if i != r and g[i * 9 + c] == v:
            return False
    br, bc = r // 3 * 3, c // 3 * 3
    for i in range(3):
        for j in range(3):
            p = (br + i) * 9 + bc + j
            if p != pos and g[p] == v:
                return False
    return True

def solve(g, pos):
    while pos < 81 and g[pos] != 0:
        pos += 1
    if pos == 81:
        return True
    for v in range(1, 10):
        if ok(g, pos, v):
            g[pos] = v
            if solve(g, pos + 1):
                return True
            g[pos] = 0
    return False

clash = any(g[p] != 0 and not ok(g, p, g[p]) for p in range(81))
if clash or not solve(g, 0):
    print("no solution")
else:
    for r in range(9):
        print("".join(str(x) for x in g[r * 9:r * 9 + 9]))
