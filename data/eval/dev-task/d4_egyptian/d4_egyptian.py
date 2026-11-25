import re
import sys
from fractions import Fraction

for raw in sys.stdin.read().split("\n"):
    t = raw.strip()
    if t == "":
        continue
    m = re.fullmatch(r"([0-9]+)/([0-9]+)", t)
    if not m:
        print(t + ": invalid")
        continue
    a, b = int(m.group(1)), int(m.group(2))
    if a < 1 or b > 1000 or a >= b:
        print(t + ": invalid")
        continue
    f = Fraction(a, b)
    terms = []
    too_large = False
    while f > 0:
        if f.denominator > 10**9:
            too_large = True
            break
        d = -((-f.denominator) // f.numerator)
        terms.append(d)
        f -= Fraction(1, d)
    if too_large:
        print("%d/%d: denominator too large" % (a, b))
    else:
        print("%d/%d = %s" % (a, b, " + ".join("1/%d" % d for d in terms)))
