import sys
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
i = 0
g = []
while i < len(lines) and lines[i] != "":
    g.append(lines[i]); i += 1
def num(t, lo, hi=None):
    if not (t.isascii() and t.isdigit()):
        return None
    v = int(t)
    if v < lo or (hi is not None and v > hi):
        return None
    return v
for n in range(i + 1, len(lines)):
    toks = lines[n].split()
    if not toks:
        continue
    ok = False
    if toks[0] == "crop" and len(toks) == 5:
        a = [num(toks[1], 0), num(toks[2], 0), num(toks[3], 1), num(toks[4], 1)]
        if None not in a and g and a[0] + a[2] <= len(g) and a[1] + a[3] <= len(g[0]):
            g = [row[a[1]:a[1] + a[3]] for row in g[a[0]:a[0] + a[2]]]; ok = True
    elif toks[0] == "zoom" and len(toks) == 2 and num(toks[1], 1, 9):
        k = int(toks[1])
        g = [ "".join(ch * k for ch in row) for row in g for _ in range(k)]; ok = True
    elif toks[0] == "shrink" and len(toks) == 2 and num(toks[1], 1, 9):
        k = int(toks[1])
        g = [row[::k] for row in g[::k]]; ok = True
    if not ok:
        print(f"error: line {n + 1}: bad command"); sys.exit(0)
for row in g:
    print(row)
print(f"size {len(g)}x{len(g[0]) if g else 0}")
