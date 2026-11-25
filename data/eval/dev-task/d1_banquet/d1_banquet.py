import sys


def number(s):
    if s == "" or len(s) > 6 or not all(c in "0123456789" for c in s):
        return None
    return int(s)


def label(gs, sep):
    return sep.join(f"{n}({s})" for n, s in gs)


lines = sys.stdin.read().splitlines()
count = cap = 0
have = False
groups = []
apart = set()
bad = []
for k, line in enumerate(lines, 1):
    w = line.split()
    if not w:
        continue
    a = b = 0
    if len(w) == 3:
        a = number(w[1]) or 0
        b = number(w[2]) or 0
    if not have:
        if w[0] != "tables" or a < 1 or a > 12 or b < 1 or b > 1000:
            print("error: no tables line")
            sys.exit(0)
        count, cap, have = a, b, True
    elif w[0] == "group" and len(w) == 3 and b > 0 and all(g[0] != w[1] for g in groups):
        groups.append((w[1], b))
    elif w[0] == "apart" and len(w) == 3 and w[1] != w[2]:
        apart.add((w[1], w[2]))
        apart.add((w[2], w[1]))
    else:
        print(f"line {k}: bad line")
if not have:
    print("error: no tables line")
    sys.exit(0)
tables = [[] for _ in range(count)]
unseated = []
for g in sorted(groups, key=lambda g: -g[1]):
    for t in tables:
        used = sum(x[1] for x in t)
        clash = any((x[0], g[0]) in apart for x in t)
        if used + g[1] <= cap and not clash:
            t.append(g)
            break
    else:
        unseated.append(g)
for i, t in enumerate(tables, 1):
    used = sum(x[1] for x in t)
    print(f"Table {i} ({used}/{cap}): {label(t, ' ') if t else '-'}")
print("Unseated: " + (label(unseated, ", ") if unseated else "none"))
total = sum(g[1] for g in groups)
print(f"Seated: {total - sum(g[1] for g in unseated)} of {total} guests")
