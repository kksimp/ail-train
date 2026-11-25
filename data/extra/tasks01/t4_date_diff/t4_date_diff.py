import sys
import datetime


def parse(t):
    if len(t) != 10 or t[4] != "-" or t[7] != "-":
        return None
    y, m, d = t[:4], t[5:7], t[8:]
    if not (y.isascii() and m.isascii() and d.isascii() and y.isdigit() and m.isdigit() and d.isdigit()):
        return None
    try:
        return datetime.date(int(y), int(m), int(d))
    except ValueError:
        return None


for line in sys.stdin.read().split("\n"):
    toks = line.split()
    if not toks:
        continue
    if len(toks) != 2:
        print("invalid")
        continue
    a, b = parse(toks[0]), parse(toks[1])
    if a is None or b is None:
        print("invalid")
    else:
        print((b - a).days)
