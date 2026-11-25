import sys
lines = sys.stdin.read().split("\n")
def dg(s, lo, hi):
    return lo <= len(s) <= hi and all(c in "0123456789" for c in s)
def ym(s):
    p = s.split("-")
    if len(p) != 2 or not dg(p[0], 4, 4) or not dg(p[1], 2, 2): return None
    m = int(p[1])
    if m < 1 or m > 12: return None
    return int(p[0]) * 12 + m
def fm(i):
    y, m = divmod(i - 1, 12)
    return "%04d-%02d" % (y, m + 1)
h = lines[0].split() if lines else []
if len(h) != 2 or h[0] != "today" or ym(h[1]) is None:
    print("error: bad date"); sys.exit(0)
today = ym(h[1])
PL = {"monthly": (1, 15), "quarterly": (3, 40), "annual": (12, 140)}
rows = []
bad = 0
for line in lines[1:]:
    f = line.split()
    if not f: continue
    if len(f) != 3 or (f[1] != "life" and f[1] not in PL):
        bad += 1; continue
    if f[1] == "life":
        if f[2] != "-": bad += 1; continue
        rows.append((10**9, f[0], f[1], "-", "active", "-", 0)); continue
    e = ym(f[2])
    if e is None: bad += 1; continue
    term, base = PL[f[1]]
    d = e - today
    if d < 0:
        st, rn, fee = "lapsed", fm(today + term), base + (base * 10 // 100 if d < -3 else 0)
    elif d <= 2:
        st, rn, fee = "expiring", fm(e + term), base
    else:
        st, rn, fee = "active", "-", 0
    rows.append((e, f[0], f[1], f[2], st, rn, fee))
rows.sort(key=lambda r: (r[0], r[1]))
for r in rows:
    print("%s %s %s %s %s %d" % (r[1], r[2], r[3], r[4], r[5], r[6]))
if rows:
    print("due: %d (%d renewals)" % (sum(r[6] for r in rows), sum(1 for r in rows if r[4] != "active")))
else:
    print("no members")
if bad:
    print("skipped: %d" % bad)
