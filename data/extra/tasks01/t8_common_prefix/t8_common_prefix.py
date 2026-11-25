import sys

groups = []
cur = []
for line in sys.stdin.read().splitlines():
    w = line.strip()
    if not w:
        if cur:
            groups.append(cur)
            cur = []
    else:
        cur.append(w)
if cur:
    groups.append(cur)
longest = 0
for i, g in enumerate(groups, 1):
    p = g[0]
    for w in g[1:]:
        n = 0
        while n < len(p) and n < len(w) and p[n] == w[n]:
            n += 1
        p = p[:n]
    print('group %d: "%s"' % (i, p))
    longest = max(longest, len(p))
print("longest: %d" % longest)
