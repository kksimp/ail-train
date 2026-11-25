import sys

lines = sys.stdin.read().splitlines()

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

def main():
    if not lines:
        print("bad grid")
        return
    h = lines[0].split()
    if len(h) != 2 or to_int(h[0]) is None or to_int(h[1]) is None:
        print("bad grid")
        return
    R, C = to_int(h[0]), to_int(h[1])
    if not (1 <= R <= 20 and 1 <= C <= 20) or len(lines) < 1 + R:
        print("bad grid")
        return
    g = []
    for i in range(R):
        row = lines[1 + i].split()
        if len(row) != C or any(to_int(x) is None for x in row):
            print("bad grid")
            return
        g.append([to_int(x) for x in row])

    def build():
        p = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(R):
            for j in range(C):
                p[i + 1][j + 1] = g[i][j] + p[i][j + 1] + p[i + 1][j] - p[i][j]
        return p

    p = build()
    for line in lines[1 + R:]:
        w = line.split()
        if not w:
            continue
        c = w[0]
        nums = [to_int(x) for x in w[1:]]
        ok = all(n is not None for n in nums)
        if c == "sum" and len(w) == 5 and ok:
            r1, c1, r2, c2 = nums
            if 0 <= r1 <= r2 < R and 0 <= c1 <= c2 < C:
                print(p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1])
            else:
                print("out of range")
        elif c in ("set", "add") and len(w) == 4 and ok:
            r, cc, v = nums
            if 0 <= r < R and 0 <= cc < C:
                g[r][cc] = v if c == "set" else g[r][cc] + v
                p = build()
                print("ok")
            else:
                print("out of range")
        elif c == "total" and len(w) == 1:
            print(p[R][C])
        elif c == "rowsums" and len(w) == 1:
            print(" ".join(str(sum(row)) for row in g))
        else:
            print("error")

main()
