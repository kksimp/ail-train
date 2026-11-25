import sys
g = [list(l) for l in sys.stdin.read().split("\n") if l != ""]
pos = [(r, c) for r in range(len(g)) for c in range(len(g[r])) if g[r][c] == "@"]
if len(pos) != 1:
    print("error: need exactly one @"); sys.exit(0)
r0, c0 = pos[0]
def sign(x): return (x > 0) - (x < 0)
out = [row[:] for row in g]
k = 0
for r in range(len(g)):
    for c in range(len(g[r])):
        if g[r][c] != ".":
            continue
        dr, dc = r - r0, c - c0
        n = max(abs(dr), abs(dc))
        ok = True
        for i in range(1, n):
            rr = r0 + sign(dr) * ((2 * abs(dr) * i + n) // (2 * n))
            cc = c0 + sign(dc) * ((2 * abs(dc) * i + n) // (2 * n))
            if g[rr][cc] == "#":
                ok = False; break
        if ok:
            out[r][c] = "*"; k += 1
for row in out:
    print("".join(row))
print(f"visible {k}")
