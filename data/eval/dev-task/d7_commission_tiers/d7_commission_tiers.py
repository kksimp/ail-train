import re
import sys


def money(c):
    return "%s$%d.%02d" % ("-" if c < 0 else "", abs(c) // 100, abs(c) % 100)


def commission(total):
    base = max(0, total)
    c = min(base, 1000000) * 500 // 10000
    c += max(0, min(base, 5000000) - 1000000) * 800 // 10000
    c += max(0, base - 5000000) * 1200 // 10000
    return c


totals = {}
for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line == "":
        continue
    f = line.split(",")
    if len(f) != 2 or f[0] == "" or not re.fullmatch(r"-?[0-9]+", f[1]):
        print("error: line %d: bad sale" % k)
        continue
    totals[f[0]] = totals.get(f[0], 0) + int(f[1])
rows = sorted(((-commission(t), n, t) for n, t in totals.items()))
payout = 0
for negc, n, t in rows:
    print("%s total=%s commission=%s" % (n, money(t), money(-negc)))
    payout += -negc
print("reps: %d" % len(rows))
print("payout: %s" % money(payout))
