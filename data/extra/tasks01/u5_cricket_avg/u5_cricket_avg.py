import sys
def dg(s, lo, hi):
    return lo <= len(s) <= hi and all(c in "0123456789" for c in s)
st = {}
bad = 0
for line in sys.stdin.read().split("\n"):
    f = line.split()
    if not f: continue
    if len(f) != 2:
        bad += 1; continue
    s = f[1]
    no = s.endswith("*")
    if no: s = s[:-1]
    if not dg(s, 1, 3):
        bad += 1; continue
    r = int(s)
    p = st.setdefault(f[0], {"i": 0, "no": 0, "runs": 0, "hs": -1, "hsno": False, "f": 0, "c": 0})
    p["i"] += 1
    p["no"] += 1 if no else 0
    p["runs"] += r
    if r > p["hs"]:
        p["hs"] = r; p["hsno"] = no
    if r >= 100: p["c"] += 1
    elif r >= 50: p["f"] += 1
rows = []
for n, p in st.items():
    d = p["i"] - p["no"]
    if d == 0:
        key, avg = 10**12, "-"
    else:
        v = (p["runs"] * 200 + d) // (2 * d)
        key, avg = v, "%d.%02d" % (v // 100, v % 100)
    rows.append((-key, -p["runs"], n, p, avg))
rows.sort(key=lambda r: (r[0], r[1], r[2]))
if not rows:
    print("no innings")
for _, _, n, p, avg in rows:
    print("%s inns=%d no=%d runs=%d hs=%d%s avg=%s 50=%d 100=%d" % (n, p["i"], p["no"], p["runs"], p["hs"], "*" if p["hsno"] else "", avg, p["f"], p["c"]))
if bad:
    print("invalid: %d" % bad)
