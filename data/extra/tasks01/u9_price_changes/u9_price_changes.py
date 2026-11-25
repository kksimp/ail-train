import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


def change_bps(old, new):
    d = new - old
    a = abs(d) * 10000
    q, r = divmod(a, old)
    if r * 2 >= old:
        q += 1
    return -q if d < 0 else q


def percent(bps):
    a = abs(bps)
    sign = "+" if bps > 0 else "-" if bps < 0 else ""
    return "%s%d.%02d%%" % (sign, a // 100, a % 100)


def main():
    items = []
    for k, line in enumerate(sys.stdin.read().splitlines(), 1):
        if not line.strip():
            continue
        w = line.split()
        old = toi(w[1]) if len(w) == 3 else None
        new = toi(w[2]) if len(w) == 3 else None
        if old is None or new is None or not (0 <= old <= 10**9) or not (0 <= new <= 10**9):
            print("line %d: bad line" % k)
            continue
        items.append((w[0], old, new))
    def key(it):
        name, old, new = it
        if old == 0:
            return (1, 0, name.encode())
        return (0, -change_bps(old, new), name.encode())
    up = down = same = na = 0
    for name, old, new in sorted(items, key=key):
        text = "n/a" if old == 0 else percent(change_bps(old, new))
        print("%s %s -> %s %s" % (name, money(old), money(new), text))
        if old == 0:
            na += 1
        elif new > old:
            up += 1
        elif new < old:
            down += 1
        else:
            same += 1
    print("up %d, down %d, same %d, n/a %d" % (up, down, same, na))


main()
