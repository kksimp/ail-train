import sys

D = "0123456789"


def num(s):
    if not s or len(s) > 6 or any(c not in D for c in s):
        return -1
    return int(s)


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


total = 0
k = 0
for line in sys.stdin.read().split("\n"):
    k += 1
    w = line.split()
    if not w:
        continue
    t = w[0].split(":")
    if len(w) != 2 or len(t) != 2 or len(t[0]) != 2 or len(t[1]) != 2:
        print("line %d: bad" % k)
        continue
    h, m, km = num(t[0]), num(t[1]), num(w[1])
    if h < 0 or h > 23 or m < 0 or m > 59 or km < 0:
        print("line %d: bad" % k)
        continue
    mins = h * 60 + m
    if mins < 360:
        b, per = "night", 5
    elif 420 <= mins < 600 or 960 <= mins < 1140:
        b, per = "peak", 15
    else:
        b, per = "day", 10
    c = min(km * per, 2500)
    total += c
    print("%s %d %s %s" % (w[0], km, b, money(c)))
print("total " + money(total))
