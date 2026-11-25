import sys
order = []
t = {}
bad = 0
for line in sys.stdin.read().split("\n"):
    f = line.split()
    if not f:
        continue
    if len(f) != 2 or f[1] not in ("P", "L", "A", "E"):
        bad += 1
        continue
    if f[0] not in t:
        t[f[0]] = {"P": 0, "L": 0, "A": 0, "E": 0}
        order.append(f[0])
    t[f[0]][f[1]] += 1
if not order and bad == 0:
    print("no records")
for n in order:
    c = t[n]
    d = c["P"] + c["L"] + c["A"]
    r = "n/a" if d == 0 else "%d%%" % ((c["P"] + c["L"]) * 100 // d)
    print("%s P=%d L=%d A=%d E=%d RATE=%s" % (n, c["P"], c["L"], c["A"], c["E"], r))
if bad:
    print("malformed: %d" % bad)
