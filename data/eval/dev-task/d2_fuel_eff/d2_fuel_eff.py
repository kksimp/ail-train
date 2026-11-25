import sys

km = {}
lit = {}
for line in sys.stdin.read().split("\n"):
    w = line.split()
    if len(w) != 3:
        continue
    if not (w[1].isascii() and w[1].isdigit() and w[2].isascii() and w[2].isdigit()):
        continue
    km[w[0]] = km.get(w[0], 0) + int(w[2])
    lit[w[0]] = lit.get(w[0], 0) + int(w[1])
for v in km:
    d, l = km[v], lit[v]
    if d == 0:
        print("%s %d %d n/a" % (v, d, l))
    else:
        t = (l * 2000 + d) // (2 * d)
        print("%s %d %d %d.%d" % (v, d, l, t // 10, t % 10))
