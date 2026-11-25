import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    sign = "-" if c < 0 else ""
    a = abs(c)
    return "%s%d.%02d" % (sign, a // 100, a % 100)


def main():
    lines = sys.stdin.read().splitlines()
    first = lines[0] if lines else ""
    w = first.split()
    if len(w) != 3:
        print("error: bad input")
        return
    v = [toi(x) for x in w]
    if any(x is None for x in v):
        print("error: bad input")
        return
    p, rate, years = v
    if not (0 <= p <= 10000000 and 0 <= rate <= 2000 and 1 <= years <= 40):
        print("error: bad input")
        return
    bal = p
    total = 0
    for y in range(1, years + 1):
        interest = (bal * rate + 5000) // 10000
        bal += interest
        total += interest
        print("year %d: interest %s balance %s" % (y, money(interest), money(bal)))
    print("total interest: " + money(total))


main()
