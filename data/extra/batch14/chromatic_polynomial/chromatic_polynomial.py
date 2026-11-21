def relabel(v, a, b):
    w = a if v == b else v
    return w - 1 if w > b else w

def chrom(n, edges):
    if not edges:
        return [0] * n + [1]
    a, b = edges[0]
    rest = edges[1:]
    d = chrom(n, rest)
    seen = set()
    con = []
    for f in rest:
        x = relabel(f[0], a, b)
        y = relabel(f[1], a, b)
        lo, hi = min(x, y), max(x, y)
        if lo != hi and (lo * 100 + hi) not in seen:
            seen.add(lo * 100 + hi)
            con.append([lo, hi])
    c = chrom(n - 1, con)
    return [d[i] - (c[i] if i < n else 0) for i in range(n + 1)]

def show(p):
    parts = []
    for i in range(len(p) - 1, -1, -1):
        c = p[i]
        if c != 0:
            mag = abs(c)
            pw = "" if i == 0 else ("x" if i == 1 else f"x^{i}")
            num = "" if mag == 1 and i > 0 else f"{mag}"
            if not parts:
                sign = "-" if c < 0 else ""
            else:
                sign = " - " if c < 0 else " + "
            parts.append(f"{sign}{num}{pw}")
    return "".join(parts)

def at(p, k):
    t = 0
    for i in range(len(p) - 1, -1, -1):
        t = t * k + p[i]
    return t

graphs = [("triangle", 3, [[0, 1], [1, 2], [0, 2]]), ("square", 4, [[0, 1], [1, 2], [2, 3], [3, 0]]), ("house", 5, [[0, 1], [1, 2], [2, 3], [3, 0], [2, 4], [3, 4]]), ("wheel", 5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [2, 3], [3, 4], [4, 1]])]
for name, n, edges in graphs:
    p = chrom(n, edges)
    k = 1
    while at(p, k) == 0:
        k += 1
    print(f"{name}: P(x) = {show(p)}")
    print(f"    3 colours: {at(p, 3)} ways, 4 colours: {at(p, 4)} ways, chromatic number {k}")
