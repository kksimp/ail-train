import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


def parse_brackets(line):
    w = line.split()
    if not w:
        return None
    out = []
    prev = 0
    for i, item in enumerate(w):
        parts = item.split(":")
        if len(parts) != 2:
            return None
        rate = toi(parts[1])
        if rate is None or rate < 0 or rate > 10000:
            return None
        last = i == len(w) - 1
        if parts[0] == "inf":
            if not last:
                return None
            out.append((-1, rate))
        else:
            if last:
                return None
            lim = toi(parts[0])
            if lim is None or lim <= prev:
                return None
            prev = lim
            out.append((lim, rate))
    return out


def tax(bs, income):
    total = 0
    lower = 0
    for limit, rate in bs:
        if income <= lower:
            break
        upper = income if limit < 0 else min(income, limit)
        total += ((upper - lower) * rate + 5000) // 10000
        lower = upper
    return total


def main():
    lines = sys.stdin.read().splitlines()
    bs = parse_brackets(lines[0]) if lines else None
    if bs is None:
        print("error: bad brackets")
        return
    for k in range(1, len(lines)):
        s = lines[k].strip()
        if not s:
            continue
        income = toi(s)
        if income is None or income < 0 or income > 100000000000:
            print("line %d: bad income" % (k + 1))
            continue
        t = tax(bs, income)
        eff = 0 if income == 0 else (t * 10000 * 2 + income) // (income * 2)
        print("income %s tax %s effective %d.%02d%%" % (money(income), money(t), eff // 100, eff % 100))


main()
