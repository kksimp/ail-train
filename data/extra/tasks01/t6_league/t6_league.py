import sys
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
t = {}
bad = []
for k, line in enumerate(lines, 1):
    f = line.rstrip("\r").split(",")
    ok = len(f) == 4 and f[0] != "" and f[1] != "" and f[0] != f[1] and f[2].isdigit() and f[3].isdigit() and f[2].isascii() and f[3].isascii()
    if not ok:
        bad.append(k)
        continue
    hg, ag = int(f[2]), int(f[3])
    for name, gf, ga in ((f[0], hg, ag), (f[1], ag, hg)):
        r = t.setdefault(name, [0, 0, 0, 0, 0, 0])
        r[0] += 1
        r[4] += gf
        r[5] += ga
        if gf > ga:
            r[1] += 1
        elif gf == ga:
            r[2] += 1
        else:
            r[3] += 1
rows = []
for name, r in t.items():
    pts = 3 * r[1] + r[2]
    rows.append((-pts, -(r[4] - r[5]), -r[4], name, r, pts))
rows.sort(key=lambda x: x[:4])
for i, (_, _, _, name, r, pts) in enumerate(rows, 1):
    print(f"{i:>2}. {name:<10} {r[0]:>2} {r[1]:>2} {r[2]:>2} {r[3]:>2} {r[4]:>3} {r[5]:>3} {r[4]-r[5]:>4} {pts:>3}")
for k in bad:
    print("bad line %d" % k)
