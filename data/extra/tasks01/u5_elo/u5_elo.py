import sys
def rdiv(n, d):
    a = abs(n)
    q = (2 * a + d) // (2 * d)
    return -q if n < 0 else q
pl = {}
ok = 0
for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    f = line.split()
    if not f: continue
    if len(f) != 3 or f[0] == f[1] or f[2] not in ("W", "L", "D"):
        print("line %d: invalid" % k); continue
    a, b, r = f
    ra, ga = pl.get(a, (1500, 0))
    rb, gb = pl.get(b, (1500, 0))
    d = ra - rb
    hi = 50 + min(abs(d), 400) // 10
    ea = hi if d >= 0 else 100 - hi
    sa = {"W": 100, "D": 50, "L": 0}[r]
    ka = 32 if ga < 10 else 16
    kb = 32 if gb < 10 else 16
    na = max(100, ra + rdiv(ka * (sa - ea), 100))
    nb = max(100, rb + rdiv(kb * ((100 - sa) - (100 - ea)), 100))
    print("%s %d->%d %s %d->%d" % (a, ra, na, b, rb, nb))
    pl[a] = (na, ga + 1)
    pl[b] = (nb, gb + 1)
    ok += 1
for n in sorted(pl, key=lambda x: (-pl[x][0], x)):
    print("%s %d %d" % (n, pl[n][0], pl[n][1]))
if ok == 0:
    print("no games")
