import re
import sys


def duration(s):
    m = re.fullmatch(r"(?:([0-9]+)h)?(?:([0-9]+)m)?", s)
    if not m or s == "":
        return None
    total = int(m.group(1) or 0) * 60 + int(m.group(2) or 0)
    return total if total >= 1 else None


def parse(line):
    f = line.split(" ")
    if len(f) != 3 or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", f[0]):
        return None
    d = duration(f[2])
    if d is None:
        return None
    return (f[0], f[1].lower(), d)


def hm(m):
    return f"{m // 60}h{m % 60:02d}m"


entries = []
for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line.strip() == "":
        continue
    e = parse(line)
    if e is None:
        print(f"bad line {n}")
        continue
    entries.append(e)
if not entries:
    print("no entries")
    sys.exit(0)
by_cat = {}
by_day = {}
total = 0
for d, c, m in entries:
    by_cat[c] = by_cat.get(c, 0) + m
    by_day[d] = by_day.get(d, 0) + m
    total += m
for c in sorted(by_cat, key=lambda c: (-by_cat[c], c.encode())):
    m = by_cat[c]
    print(f"{c} {m}m ({hm(m)}) {100 * m // total}%")
print(f"total {total}m ({hm(total)})")
day = sorted(by_day, key=lambda d: (-by_day[d], d))[0]
print(f"busiest {day} {by_day[day]}m")
