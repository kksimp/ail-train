import math

def mean(v):
    s = 0.0
    for x in v:
        s += x
    return s / float(len(v))

def var(v):
    m = mean(v)
    s = 0.0
    for x in v:
        s += (x - m) * (x - m)
    return s / float(len(v) - 1)

def welch(a, b):
    va = var(a) / float(len(a))
    vb = var(b) / float(len(b))
    t = (mean(a) - mean(b)) / math.sqrt(va + vb)
    df = (va + vb) * (va + vb) / (va * va / float(len(a) - 1) + vb * vb / float(len(b) - 1))
    return [t, df]

old = ("old bulbs", [812.0, 798.0, 830.0, 805.0, 790.0, 821.0, 809.0, 815.0])
new = ("new bulbs", [845.0, 902.0, 830.0, 868.0, 915.0, 851.0])
same = ("rerun", [801.0, 826.0, 812.0, 795.0, 818.0, 807.0, 822.0])
for name, v in [old, new, same]:
    print(f"{name:<9}: n {len(v)}, mean {mean(v):.2f}, sd {math.sqrt(var(v)):.2f}")
for a, b in [[old, new], [old, same]]:
    r = welch(a[1], b[1])
    verdict = "a real difference" if abs(r[0]) > 2.2 else "no clear difference"
    print(f"{a[0]} vs {b[0]}: t = {r[0]:.3f}, df = {r[1]:.1f} -> {verdict}")
