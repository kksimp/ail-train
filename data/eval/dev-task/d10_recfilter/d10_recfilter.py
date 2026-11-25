import re
import sys

lines = sys.stdin.read().splitlines()
if not lines:
    sys.exit(0)
fields = lines[0].split()
recs = []
i = 1
while i < len(lines) and lines[i].strip():
    w = lines[i].split()
    if len(w) == len(fields):
        recs.append(w)
    i += 1
OPS = ["=", "!=", "<", "<=", ">", ">=", "~"]
isint = lambda s: re.fullmatch(r"-?[0-9]+", s) is not None


def holds(a, op, b):
    if op == "~":
        return b in a
    if isint(a) and isint(b):
        a, b = int(a), int(b)
    return {"=": a == b, "!=": a != b, "<": a < b, "<=": a <= b, ">": a > b, ">=": a >= b}[op]


q = 0
for line in lines[i:]:
    t = line.split()
    if not t:
        continue
    q += 1
    terms = []
    ok = len(t) % 4 == 3
    if ok:
        for k in range(0, len(t), 4):
            if t[k + 1] not in OPS or (k + 3 < len(t) and t[k + 3] not in ("and", "or")):
                ok = False
    if not ok:
        print("%d: error: bad query" % q)
        continue
    bad = [t[k] for k in range(0, len(t), 4) if t[k] not in fields]
    if bad:
        print("%d: error: unknown field %s" % (q, bad[0]))
        continue
    # or of ands
    groups = [[]]
    for k in range(0, len(t), 4):
        groups[-1].append((t[k], t[k + 1], t[k + 2]))
        if k + 3 < len(t) and t[k + 3] == "or":
            groups.append([])
    names = []
    for r in recs:
        if any(all(holds(r[fields.index(f)], op, v) for f, op, v in g) for g in groups):
            names.append(r[0])
    print("%d: %d%s" % (q, len(names), (" " + ",".join(names)) if names else ""))
