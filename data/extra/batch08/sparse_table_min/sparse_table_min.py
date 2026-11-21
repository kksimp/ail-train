def build(xs):
    t = [xs]; w = 1
    while w * 2 <= len(xs):
        pr = t[-1]; t.append([min(pr[i], pr[i + w]) for i in range(len(xs) - w * 2 + 1)]); w *= 2
    return t
def query(t, lo, hi):
    lv = 0
    while (2 << lv) <= hi - lo + 1: lv += 1
    return min(t[lv][lo], t[lv][hi - (1 << lv) + 1])
lows = [6, 4, 7, 2, 5, 8, 3, 9, 1, 6, 4, 7, 5, 3]; t = build(lows)
print(f"{len(t)} levels for {len(lows)} nights")
for lo, hi in [(0, 2), (3, 7), (4, 7), (0, 13), (9, 13), (5, 5)]: print(f"nights {lo + 1}-{hi + 1}: coldest {query(t, lo, hi)} C")
