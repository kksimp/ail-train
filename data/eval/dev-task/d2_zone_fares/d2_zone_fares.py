import sys


def money(c):
    return "%d.%02d" % (c // 100, c % 100)


total = 0
for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    w = line.split()
    if not w:
        continue
    if len(w) != 2 or any(len(z) != 1 or z not in "123456789" for z in w):
        print("line %d: bad" % k)
        continue
    a, b = int(w[0]), int(w[1])
    x = abs(a - b)
    fare = 240 + 110 * x + (50 if a == 1 or b == 1 else 0)
    total += fare
    print("%d->%d x%d %s" % (a, b, x, money(fare)))
print("total " + money(total))
