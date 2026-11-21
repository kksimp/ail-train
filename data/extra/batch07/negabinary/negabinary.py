def tn(n):
    if n == 0: return "0"
    d = []
    while n != 0:
        r = 0 if n % 2 == 0 else 1; n = (n - r) // -2
        d.append(str(r))
    return "".join(reversed(d))
import math
def fn_(s):
    v = 0
    for c in s: v = v * -2 + (1 if c == "1" else 0)
    return v
for n in [0, 1, 2, 3, 6, -1, -2, -5, 13, -13, 100]: s = tn(n); print(f"{n:>4} = {s:>10} (back {fn_(s)})")
