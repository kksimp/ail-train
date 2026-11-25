import re
import sys

NUM = re.compile(r"-?[0-9]+")


def money(c):
    sign = "-" if c < 0 else "+"
    a = abs(c)
    return "%s$%d.%02d" % (sign, a // 100, a % 100)


net = gross = 0
for line in sys.stdin.read().splitlines():
    f = line.split(",")
    if len(f) != 4:
        continue
    if not all(NUM.fullmatch(x) for x in f[1:]):
        continue
    system, counted, cost = (int(x) for x in f[1:])
    v = counted - system
    if v == 0:
        continue
    val = v * cost
    print("%s %+d %s" % (f[0], v, money(val)))
    net += val
    gross += abs(val)
print("net: " + money(net))
print("gross: " + money(gross))
