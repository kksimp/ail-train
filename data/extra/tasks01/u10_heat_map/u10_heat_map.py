import re, sys
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
def pint(t):
    return int(t) if re.fullmatch(r"-?[0-9]+", t) else None
hdr = lines[0].split() if lines else []
hv = [pint(t) for t in hdr]
if len(hdr) != 3 or None in hv or min(hv) < 1:
    print("error: bad header"); sys.exit(0)
W, H, B = hv
rows, cols = (H + B - 1) // B, (W + B - 1) // B
g = [[0] * cols for _ in range(rows)]
ign = bad = tot = 0
for l in lines[1:]:
    t = l.split()
    if not t:
        continue
    v = [pint(x) for x in t]
    if len(t) not in (2, 3) or None in v or (len(t) == 3 and v[2] < 1):
        bad += 1; continue
    x, y = v[0], v[1]
    wt = v[2] if len(t) == 3 else 1
    if not (0 <= x < W and 0 <= y < H):
        ign += 1; continue
    g[y // B][x // B] += wt; tot += wt
wd = max(len(str(v)) for row in g for v in row)
for row in g:
    print(" ".join(str(v).rjust(wd) for v in row))
print(f"total {tot} ignored {ign} bad {bad}")
if tot == 0:
    print("hottest none")
else:
    m = max(max(row) for row in g)
    for r in range(rows):
        if m in g[r]:
            print(f"hottest {r},{g[r].index(m)} {m}"); break
