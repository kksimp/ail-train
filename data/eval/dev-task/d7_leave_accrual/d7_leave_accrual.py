import re
import sys


def accrued(t):
    return 10 * min(t, 12) + 12 * (min(t, 60) - min(t, 12)) + 16 * max(0, t - 60)


count = total = 0
for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    if line == "":
        continue
    f = line.split(",")
    if len(f) != 3 or f[0] == "" or not re.fullmatch(r"[0-9]+", f[1]) or not re.fullmatch(r"[0-9]+", f[2]):
        print("error: line %d: bad record" % k)
        continue
    t, h = int(f[1]), int(f[2])
    a = accrued(t)
    raw = a - h
    flag = " CAPPED" if raw > 240 else (" OVERDRAWN" if raw < 0 else "")
    bal = min(raw, 240)
    print("%s accrued=%d taken=%d balance=%d%s" % (f[0], a, h, bal, flag))
    count += 1
    total += bal
print("employees: %d" % count)
print("total balance: %d" % total)
