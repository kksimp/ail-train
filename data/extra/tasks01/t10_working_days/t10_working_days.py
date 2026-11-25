import re
import sys
from datetime import date, timedelta


def parse(s):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", s):
        return None
    y, m, d = int(s[:4]), int(s[5:7]), int(s[8:])
    if y < 1970 or y > 2100:
        return None
    try:
        return date(y, m, d)
    except ValueError:
        return None


lines = sys.stdin.read().splitlines()
holidays = set()
for line in lines:
    f = line.split(" ")
    if len(f) == 2 and f[0] == "holiday":
        d = parse(f[1])
        if d is not None:
            holidays.add(d)
for k, line in enumerate(lines, 1):
    if line.strip() == "":
        continue
    f = line.split(" ")
    if len(f) != 2:
        print(f"bad line {k}")
        continue
    if f[0] == "holiday":
        if parse(f[1]) is None:
            print(f"bad line {k}")
        continue
    a, b = parse(f[0]), parse(f[1])
    if a is None or b is None:
        print(f"{f[0]} {f[1]}: invalid")
        continue
    if b < a:
        print(f"{f[0]} {f[1]}: reversed")
        continue
    cnt = 0
    d = a
    while d <= b:
        if d.weekday() < 5 and d not in holidays:
            cnt += 1
        d += timedelta(days=1)
    print(f"{f[0]} {f[1]}: {cnt}")
