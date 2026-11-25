import re, sys

def main():
    toks = sys.stdin.read().split()
    pos = 0
    def nxt():
        nonlocal pos
        if pos >= len(toks) or not re.fullmatch(r"-?[0-9]+", toks[pos]):
            raise ValueError
        v = int(toks[pos])
        pos += 1
        return v
    try:
        r1, c1 = nxt(), nxt()
        if r1 < 1 or c1 < 1:
            raise ValueError
        a = [[nxt() for _ in range(c1)] for _ in range(r1)]
        r2, c2 = nxt(), nxt()
        if r2 < 1 or c2 < 1:
            raise ValueError
        b = [[nxt() for _ in range(c2)] for _ in range(r2)]
    except ValueError:
        print("error: bad input")
        return
    if c1 != r2:
        print(f"error: cannot multiply {r1}x{c1} by {r2}x{c2}")
        return
    p = [[sum(a[i][k] * b[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]
    width = max(len(str(v)) for row in p for v in row)
    for row in p:
        print(" ".join(str(v).rjust(width) for v in row))
    if r1 == c2:
        print(f"trace {sum(p[i][i] for i in range(r1))}")
    else:
        print(f"shape {r1}x{c2}")

main()
