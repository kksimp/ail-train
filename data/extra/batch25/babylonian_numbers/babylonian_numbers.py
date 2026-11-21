import math

def wedges(d):
    if d == 0:
        return "."
    return "<" * (d // 10) + "Y" * (d % 10)

def digits60(n):
    ds = []
    x = n
    while x > 0:
        ds.insert(0, x % 60)
        x = x // 60
    return ds

def reciprocal(n):
    parts = []
    rem = 1
    while rem != 0 and len(parts) < 6:
        rem = rem * 60
        parts.append(str(rem // n))
        rem = rem % n
    return "0;" + ",".join(parts)

for n in [75, 3600, 4000, 424000]:
    ds = digits60(n)
    shown = " ".join(wedges(d) for d in ds)
    print(f"{n} = [{', '.join(str(d) for d in ds)}] = {shown}")
for n in [2, 8, 9, 16, 27, 45]:
    print(f"1/{n} = {reciprocal(n)}")
v = 1.0 + 24.0 / 60.0 + 51.0 / 3600.0 + 10.0 / 216000.0
gap = (math.sqrt(2.0) - v) * 1000000.0
print(f"1;24,51,10 = {v:.8f}, below root 2 by {gap:.3f} millionths")
