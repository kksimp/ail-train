import sys


def parse_int(w):
    body = w[1:] if w.startswith("-") else w
    if body == "" or not all("0" <= c <= "9" for c in body):
        return None
    return int(w)


def parse_grid(text):
    g = []
    for line in text.splitlines():
        if line.strip() == "":
            continue
        row = []
        for w in line.split():
            n = parse_int(w)
            if n is None:
                return None
            row.append(n)
        g.append(row)
    return g


def verdict(g):
    n = len(g)
    if n == 0 or any(len(r) != n for r in g):
        return "invalid"
    flat = [x for r in g for x in r]
    if sorted(flat) != list(range(1, n * n + 1)):
        return "not magic: numbers"
    target = n * (n * n + 1) // 2
    for r in range(n):
        if sum(g[r]) != target:
            return f"not magic: row {r + 1}"
    for c in range(n):
        if sum(g[r][c] for r in range(n)) != target:
            return f"not magic: column {c + 1}"
    if sum(g[i][i] for i in range(n)) != target:
        return "not magic: diagonal"
    if sum(g[i][n - 1 - i] for i in range(n)) != target:
        return "not magic: anti-diagonal"
    return f"magic {target}"


def main():
    g = parse_grid(sys.stdin.read())
    if g is None:
        print("invalid")
        return
    print(verdict(g))


main()
