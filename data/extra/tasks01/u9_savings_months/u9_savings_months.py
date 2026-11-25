import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    sign = "-" if c < 0 else ""
    a = abs(c)
    return "%s%d.%02d" % (sign, a // 100, a % 100)


def parse(line):
    w = line.split()
    if len(w) != 4:
        return None
    v = [toi(x) for x in w]
    if any(x is None for x in v):
        return None
    g, s, d, r = v
    if not (1 <= g <= 10**9 and 0 <= s <= 10**9 and 0 <= d <= 10**9 and 0 <= r <= 2000):
        return None
    return v


def describe(v):
    goal, bal, dep, rate = v
    months = 0
    while bal < goal and months < 600:
        bal += (bal * rate + 60000) // 120000
        bal += dep
        months += 1
    if bal >= goal:
        return "%d months, balance %s" % (months, money(bal))
    return "unreachable in 600 months"


def main():
    k = 0
    for line in sys.stdin.read().splitlines():
        if not line.strip():
            continue
        k += 1
        v = parse(line)
        if v is None:
            print("scenario %d: bad input" % k)
        else:
            print("scenario %d: %s" % (k, describe(v)))


main()
