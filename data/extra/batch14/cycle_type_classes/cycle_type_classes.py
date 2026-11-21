from math import factorial
from itertools import permutations
from collections import Counter
def partitions(n, most):
    if n == 0:
        return [[]]
    out = []
    for first in range(min(most, n), 0, -1):
        for rest in partitions(n - first, first):
            out.append([first] + rest)
    return out
def class_size(p, n):
    den = 1
    for k in p:
        den *= k
    for k, m in Counter(p).items():
        den *= factorial(m)
    return factorial(n) // den
def cycle_type(p):
    seen = [False] * len(p)
    lens = []
    for s in range(len(p)):
        if not seen[s]:
            x = s
            l = 0
            while not seen[x]:
                seen[x] = True
                x = p[x]
                l += 1
            lens.append(l)
    return "+".join(str(k) for k in sorted(lens, reverse=True))
n = 5
found = Counter(cycle_type(p) for p in permutations(range(n)))
total = 0
even = 0
for p in partitions(n, n):
    key = "+".join(str(k) for k in p)
    size = class_size(p, n)
    parity = "even" if (n - len(p)) % 2 == 0 else "odd"
    if parity == "even":
        even += size
    total += size
    print(f"{key:<10} {size:>3} permutations ({parity}), counted {found.get(key, 0)}")
print(f"{total} in all, {even} even (the group A5)")
