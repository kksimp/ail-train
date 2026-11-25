import sys
def dg(s, lo, hi):
    return lo <= len(s) <= hi and all(c in "0123456789" for c in s)
def pt(s):
    parts = s.split(":")
    if len(parts) > 2:
        return None
    mins = 0
    sec = parts[-1]
    if len(parts) == 2:
        if not dg(parts[0], 1, 2):
            return None
        mins = int(parts[0])
    sp = sec.split(".")
    if len(sp) != 2 or not dg(sp[1], 2, 2):
        return None
    if len(parts) == 2:
        if not dg(sp[0], 2, 2):
            return None
    elif not dg(sp[0], 1, 2):
        return None
    w = int(sp[0])
    if w >= 60:
        return None
    t = (mins * 60 + w) * 100 + int(sp[1])
    return t if t > 0 else None
TABLE = [9, 7, 6, 5, 4, 3, 2, 1]
events = {}
bad = 0
for line in sys.stdin.read().split("\n"):
    f = line.split()
    if not f:
        continue
    if len(f) != 4:
        bad += 1; continue
    t = pt(f[3])
    if t is None or any(e[0] == f[1] for e in events.get(f[0], [])):
        bad += 1; continue
    events.setdefault(f[0], []).append((f[1], f[2], t, f[3]))
if not events:
    print("no results")
teams = {}
for ev, es in events.items():
    print("== %s ==" % ev)
    es = sorted(es, key=lambda e: (e[2], e[0]))
    i = 0
    while i < len(es):
        j = i
        while j < len(es) and es[j][2] == es[i][2]:
            j += 1
        pts = sum(TABLE[p] for p in range(i, j) if p < 8) // (j - i)
        for k in range(i, j):
            print("%d %s %s %s pts=%d" % (i + 1, es[k][0], es[k][1], es[k][3], pts))
            teams[es[k][1]] = teams.get(es[k][1], 0) + pts
        i = j
if events:
    print("== teams ==")
    for tm in sorted(teams, key=lambda k: (-teams[k], k)):
        print("%s %d" % (tm, teams[tm]))
if bad:
    print("malformed: %d" % bad)
