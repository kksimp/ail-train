import re
import sys


def parse(s):
    if not re.fullmatch(r"-?[0-9]+", s):
        return None
    v = int(s)
    if abs(v) > 10**9:
        return None
    return v


for raw in sys.stdin.read().split("\n"):
    t = raw.strip()
    if t == "":
        continue
    parts = t.split("/")
    if len(parts) != 2 or parse(parts[0]) is None or parse(parts[1]) is None:
        print(t + ": invalid")
        continue
    a, b = parse(parts[0]), parse(parts[1])
    if b == 0:
        print(t + ": zero denominator")
        continue
    x, y = a, b
    if y < 0:
        x, y = -x, -y
    terms = []
    while y != 0:
        terms.append(x // y)
        x, y = y, x % y
    if len(terms) == 1:
        shape = "[%d]" % terms[0]
    else:
        shape = "[%d; %s]" % (terms[0], ", ".join(str(q) for q in terms[1:]))
    print("%d/%d = %s" % (a, b, shape))
    convs = []
    for n in range(len(terms)):
        # evaluate [t0; ..., tn] as an exact fraction from the back
        p, q = terms[n], 1
        for i in range(n - 1, -1, -1):
            p, q = terms[i] * p + q, p
        convs.append("%d/%d" % (p, q))
    print("  convergents: " + " ".join(convs))
