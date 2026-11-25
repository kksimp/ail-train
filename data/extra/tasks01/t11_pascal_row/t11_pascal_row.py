import sys
from math import comb

def is_digits(s):
    return len(s) > 0 and all(c in "0123456789" for c in s)

for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    k = int(t) if is_digits(t) and len(t) <= 9 else -1
    if k < 0 or k > 60:
        print(f"{t} invalid"); continue
    r = [comb(k, i) for i in range(k + 1)]
    print(f"{k}: {' '.join(map(str, r))} | sum {sum(r)}")
