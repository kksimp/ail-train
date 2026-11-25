import re
import sys


def toi(s):
    return int(s) if re.fullmatch(r"-?[0-9]+", s) else None


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


def leap(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0


def month_days(y, m):
    if m == 2:
        return 29 if leap(y) else 28
    if m in (4, 6, 9, 11):
        return 30
    return 31


def day_number(y, m, d):
    yy = y - 1 if m <= 2 else y
    era = yy // 400
    yoe = yy - era * 400
    mp = (m + 9) % 12
    doy = (153 * mp + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe


def parse_date(s):
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", s):
        return None
    y, m, d = int(s[0:4]), int(s[5:7]), int(s[8:10])
    if y < 1900 or y > 2100 or m < 1 or m > 12 or d < 1 or d > month_days(y, m):
        return None
    return day_number(y, m, d)


def bucket(overdue):
    if overdue <= 0:
        return 0
    if overdue <= 30:
        return 1
    if overdue <= 60:
        return 2
    if overdue <= 90:
        return 3
    return 4


def main():
    lines = sys.stdin.read().splitlines()
    asof = parse_date(lines[0].strip()) if lines else None
    if asof is None:
        print("error: bad date")
        return
    labels = ["current", "1-30", "31-60", "61-90", "90+"]
    counts = [0] * 5
    sums = [0] * 5
    for k in range(1, len(lines)):
        w = lines[k].split()
        if not w:
            continue
        if len(w) != 3:
            print("line %d: bad invoice" % (k + 1))
            continue
        amt = toi(w[1])
        due = parse_date(w[2])
        if amt is None or amt < 1 or amt > 1000000000 or due is None:
            print("line %d: bad invoice" % (k + 1))
            continue
        b = bucket(asof - due)
        counts[b] += 1
        sums[b] += amt
    for i in range(5):
        print("%s: %d invoices, %s" % (labels[i], counts[i], money(sums[i])))
    print("total: %d invoices, %s" % (sum(counts), money(sum(sums))))


main()
