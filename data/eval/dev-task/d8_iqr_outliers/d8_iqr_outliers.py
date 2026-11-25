import sys
from fractions import Fraction

toks = sys.stdin.read().split()
for t in toks:
    if not (t.isascii() and t.isdigit()):
        print("bad value: " + t)
        sys.exit(0)
xs = [int(t) for t in toks]
if len(xs) < 4:
    print("need at least 4 values")
    sys.exit(0)


def median(v):
    n = len(v)
    if n % 2:
        return Fraction(v[n // 2])
    return Fraction(v[n // 2 - 1] + v[n // 2], 2)


def fmt(f):
    q = int(f * 4)
    sign = "-" if q < 0 else ""
    q = abs(q)
    return "%s%d.%02d" % (sign, q // 4, (q % 4) * 25)


s = sorted(xs)
n = len(s)
q1 = median(s[:n // 2])
q3 = median(s[n - n // 2:])
iqr = q3 - q1
lo = q1 - Fraction(3, 2) * iqr
hi = q3 + Fraction(3, 2) * iqr
print("n: %d" % n)
print("q1: " + fmt(q1))
print("q3: " + fmt(q3))
print("iqr: " + fmt(iqr))
print("fences: %s %s" % (fmt(lo), fmt(hi)))
out = [(i + 1, x) for i, x in enumerate(xs) if x < lo or x > hi]
if out:
    for p, x in out:
        print("outlier: %d %d" % (p, x))
else:
    print("outliers: none")
