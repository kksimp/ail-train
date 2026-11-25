import re
import sys

WINDOW = {"electronics": 30, "clothing": 60, "grocery": 7, "software": 14}
FEE = {"electronics": 15, "clothing": 10}
CONDS = ("sealed", "opened", "defective")


def settle(cents, cash):
    if cents > 50000:
        return ("review", cents)
    return ("cash" if cash else "credit", cents)


def decide(cat, paid, days, cond):
    if cat not in WINDOW:
        return ("reject", "unknown category")
    w = WINDOW[cat]
    if cond == "defective":
        if days > 2 * w:
            return ("reject", "window expired")
        return settle(paid, True)
    if days > w:
        return ("reject", "window expired")
    cash = days * 2 <= w
    if cond == "sealed":
        return settle(paid, cash)
    if cat not in FEE:
        return ("reject", "opened " + cat)
    return settle(paid - paid * FEE[cat] // 100, cash)


cash = credit = approved = reviews = rsum = rejected = bad = 0
for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line == "":
        continue
    f = line.split(",")
    ok = (
        len(f) == 5
        and f[0] != ""
        and re.fullmatch(r"[0-9]+", f[2])
        and re.fullmatch(r"[0-9]+", f[3])
        and int(f[2]) >= 1
        and f[4] in CONDS
    )
    if not ok:
        print("line %d: malformed request" % k)
        bad += 1
        continue
    kind, val = decide(f[1], int(f[2]), int(f[3]), f[4])
    if kind == "cash":
        print("%s APPROVE cash %d" % (f[0], val))
        approved += 1
        cash += val
    elif kind == "credit":
        print("%s APPROVE credit %d" % (f[0], val))
        approved += 1
        credit += val
    elif kind == "review":
        print("%s REVIEW %d" % (f[0], val))
        reviews += 1
        rsum += val
    else:
        print("%s REJECT %s" % (f[0], val))
        rejected += 1
print("approved: %d cash=%d credit=%d" % (approved, cash, credit))
print("review: %d amount=%d" % (reviews, rsum))
print("rejected: %d" % rejected)
print("malformed: %d" % bad)
