import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


def parse(line):
    w = line.split()
    if len(w) != 4:
        return None
    total, pct, people = toi(w[0]), toi(w[1]), toi(w[2])
    if total is None or pct is None or people is None:
        return None
    if not (0 <= total <= 100000000 and 0 <= pct <= 100 and 1 <= people <= 20):
        return None
    if w[3] not in ("half", "up", "down"):
        return None
    return total, pct, people, w[3]


def main():
    k = 0
    for line in sys.stdin.read().splitlines():
        if not line.strip():
            continue
        k += 1
        b = parse(line)
        if b is None:
            print("bill %d: bad input" % k)
            continue
        total, pct, people, mode = b
        q, r = divmod(total * pct, 100)
        if mode == "up":
            t = q + (1 if r > 0 else 0)
        elif mode == "half":
            t = q + (1 if r >= 50 else 0)
        else:
            t = q
        grand = total + t
        print("bill %d: tip %s total %s" % (k, money(t), money(grand)))
        base, extra = divmod(grand, people)
        for i in range(people):
            print("person %d: %s" % (i + 1, money(base + (1 if i < extra else 0))))


main()
