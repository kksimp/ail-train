import sys
ps = []
seen = set()
bad = 0
for line in sys.stdin.read().split("\n"):
    f = line.split()
    if not f: continue
    if len(f) != 2 or not (1 <= len(f[1]) <= 3 and all(c in "0123456789" for c in f[1])) or not (1 <= int(f[1]) <= 100) or f[0] in seen:
        bad += 1; continue
    seen.add(f[0])
    ps.append((-int(f[1]), f[0]))
ps.sort()
if len(ps) < 2:
    print("need at least 2 players")
else:
    cap = (len(ps) + 1) // 2
    t = {"A": [], "B": []}
    sm = {"A": 0, "B": 0}
    for neg, name in ps:
        if len(t["A"]) == cap: pick = "B"
        elif len(t["B"]) == cap: pick = "A"
        elif sm["A"] < sm["B"]: pick = "A"
        elif sm["B"] < sm["A"]: pick = "B"
        elif len(t["A"]) <= len(t["B"]): pick = "A"
        else: pick = "B"
        t[pick].append(name)
        sm[pick] += -neg
    for k in "AB":
        print("Team %s: %s (total %d)" % (k, " ".join(t[k]), sm[k]))
    print("difference: %d" % abs(sm["A"] - sm["B"]))
if bad:
    print("invalid: %d" % bad)
