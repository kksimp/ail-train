import sys
lines = sys.stdin.read().split("\n")
pars = lines[0].split()
def dg(s, lo, hi):
    return lo <= len(s) <= hi and all(c in "0123456789" for c in s)
if not (1 <= len(pars) <= 36) or not all(dg(p, 1, 1) and 3 <= int(p) <= 6 for p in pars):
    print("error: bad pars"); sys.exit(0)
pars = [int(p) for p in pars]
n = len(pars)
rows = []
names = set()
bad = 0
for line in lines[1:]:
    f = line.split()
    if not f:
        continue
    sc = f[1:]
    if len(sc) != n or f[0] in names or not all(s == "-" or (dg(s, 1, 2) and int(s) >= 1) for s in sc):
        bad += 1; continue
    names.add(f[0])
    strokes = [pars[i] + 3 if s == "-" else int(s) for i, s in enumerate(sc)]
    cnt = [0] * 5
    for i, s in enumerate(strokes):
        d = s - pars[i]
        cnt[0 if d <= -2 else 1 if d == -1 else 2 if d == 0 else 3 if d == 1 else 4] += 1
    rows.append((sum(strokes) - sum(pars), f[0], sum(strokes), cnt))
rows.sort(key=lambda r: (r[0], r[1]))
if not rows:
    print("no scorecards")
def tp(x):
    return "E" if x == 0 else ("+%d" % x if x > 0 else "%d" % x)
i = 0
while i < len(rows):
    j = i
    while j < len(rows) and rows[j][0] == rows[i][0]:
        j += 1
    for k in range(i, j):
        r = rows[k]
        rk = ("T%d" if j - i > 1 else "%d") % (i + 1)
        print("%s %s %d %s %s" % (rk, r[1], r[2], tp(r[0]), "/".join(str(c) for c in r[3])))
    i = j
if bad:
    print("skipped: %d" % bad)
