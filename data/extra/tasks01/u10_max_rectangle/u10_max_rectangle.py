import sys
g = [l for l in sys.stdin.read().split("\n") if l != ""]
if any(set(l) - set("01") for l in g):
    print("error: bad grid"); sys.exit(0)
R = len(g); C = len(g[0]) if g else 0
best = (0, 0, 0, 0, 0)
for r in range(R):
    for c in range(C):
        w = C - c
        for h in range(1, R - r + 1):
            k = 0
            while k < w and g[r + h - 1][c + k] == "1":
                k += 1
            w = k
            if w == 0:
                break
            if h * w > best[0]:
                best = (h * w, r, c, h, w)
if best[0] == 0:
    print("area 0")
else:
    print(f"area {best[0]} at {best[1]},{best[2]} size {best[3]}x{best[4]}")
