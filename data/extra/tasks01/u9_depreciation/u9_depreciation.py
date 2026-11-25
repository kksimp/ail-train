import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


def parse(line):
    w = line.split()
    if len(w) < 5 or len(w) > 6:
        return None
    cost, salvage, life = toi(w[1]), toi(w[2]), toi(w[3])
    if cost is None or salvage is None or life is None:
        return None
    if salvage < 0 or cost < salvage or cost > 100000000 or life < 1 or life > 30:
        return None
    rate = 0
    if w[4] == "SL":
        if len(w) != 5:
            return None
    elif w[4] == "DB":
        if len(w) != 6:
            return None
        rate = toi(w[5])
        if rate is None or rate < 1 or rate > 100:
            return None
    else:
        return None
    return w[0], cost, salvage, life, w[4], rate


def main():
    k = 0
    for line in sys.stdin.read().splitlines():
        if not line.strip():
            continue
        k += 1
        a = parse(line)
        if a is None:
            print("line %d: bad input" % k)
            continue
        name, cost, salvage, life, method, rate = a
        print("%s (%s)" % (name, "SL" if method == "SL" else "DB %d%%" % rate))
        book = cost
        for y in range(1, life + 1):
            if method == "SL":
                q, r = divmod(cost - salvage, life)
                d = q + (1 if y <= r else 0)
            elif y == life:
                d = book - salvage
            else:
                d = min((book * rate + 50) // 100, book - salvage)
            book -= d
            print("year %d: depreciation %s book %s" % (y, money(d), money(book)))


main()
