import sys

prev = -1
dist = legs = n = 0
for line in sys.stdin.read().split("\n"):
    s = line.strip()
    if not (s.isascii() and s.isdigit()):
        continue
    r = int(s)
    if r < prev:
        continue
    if r == prev:
        if legs > 0:
            n += 1
            print("trip %d: %d km in %d legs" % (n, dist, legs))
            dist = legs = 0
    elif prev >= 0:
        dist += r - prev
        legs += 1
    prev = r
if legs > 0:
    n += 1
    print("trip %d: %d km in %d legs" % (n, dist, legs))
print("trips %d" % n)
