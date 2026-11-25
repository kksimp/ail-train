import re
import sys

ivs = []
for k, line in enumerate(sys.stdin.read().splitlines(), 1):
    if not line.strip():
        continue
    w = line.split()
    if len(w) != 2 or not all(re.fullmatch(r"-?[0-9]+", x) for x in w) or int(w[0]) > int(w[1]):
        print("bad line %d" % k)
        continue
    ivs.append((int(w[0]), int(w[1])))
ivs.sort()
covered = 0
if ivs:
    s, e = ivs[0]
    for a, b in ivs[1:]:
        if a <= e:
            e = max(e, b)
        else:
            print("%d-%d" % (s, e))
            covered += e - s + 1
            s, e = a, b
    print("%d-%d" % (s, e))
    covered += e - s + 1
print("covered: %d" % covered)
