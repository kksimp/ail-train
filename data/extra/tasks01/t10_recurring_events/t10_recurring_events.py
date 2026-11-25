import re
import sys
from datetime import date, timedelta


def days_in(y, m):
    return [31, 29 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]


def parse(line):
    f = line.split(" ")
    if len(f) != 4:
        return None
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", f[1]):
        return None
    y, m, d = int(f[1][:4]), int(f[1][5:7]), int(f[1][8:])
    if y < 1970 or y > 2100 or m < 1 or m > 12 or d < 1 or d > days_in(y, m):
        return None
    if f[2] not in ("daily", "weekly", "monthly", "yearly"):
        return None
    t = f[3][1:] if f[3].startswith("-") else f[3]
    if not (t.isascii() and t.isdigit()):
        return None
    k = int(f[3])
    if k < 1 or k > 20:
        return None
    return (f[0], y, m, d, f[2], k)


def occ(r, k):
    name, y, m, d, freq, _ = r
    if freq == "daily":
        x = date(y, m, d) + timedelta(days=k)
        return x.isoformat()
    if freq == "weekly":
        x = date(y, m, d) + timedelta(days=7 * k)
        return x.isoformat()
    months = k if freq == "monthly" else 12 * k
    total = y * 12 + (m - 1) + months
    yy, mm = total // 12, total % 12 + 1
    return f"{yy:04d}-{mm:02d}-{min(d, days_in(yy, mm)):02d}"


occs = []
bad = []
seq = 0
for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line.strip() == "":
        continue
    r = parse(line)
    if r is None:
        bad.append(n)
        continue
    for k in range(r[5]):
        occs.append((occ(r, k), r[0].encode(), seq, r[0]))
        seq += 1
occs.sort()
for o in occs:
    print(f"{o[0]} {o[3]}")
print(f"total {len(occs)}")
for b in bad:
    print(f"bad line {b}")
