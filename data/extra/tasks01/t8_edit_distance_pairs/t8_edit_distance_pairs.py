import sys


def dist(a, b):
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i]
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost))
        prev = cur
    return prev[len(b)]


pairs = bad = 0
lines = sys.stdin.read().splitlines()
for k, line in enumerate(lines, 1):
    if line == "":
        continue
    parts = line.split("|")
    if len(parts) != 2:
        print("line %d: malformed" % k)
        bad += 1
        continue
    pairs += 1
    print("%s -> %s: %d" % (parts[0], parts[1], dist(parts[0], parts[1])))
print("pairs: %d, malformed: %d" % (pairs, bad))
