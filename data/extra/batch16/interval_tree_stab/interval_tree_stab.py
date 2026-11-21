def build(starts, ends, maxe, lo, hi):
    if lo >= hi:
        return -1
    mid = (lo + hi) // 2
    m = max(max(ends[mid], build(starts, ends, maxe, lo, mid)), build(starts, ends, maxe, mid + 1, hi))
    maxe[mid] = m
    return m

def stab(starts, ends, maxe, lo, hi, t, out, visits):
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    visits[0] += 1
    if maxe[mid] < t:
        return
    stab(starts, ends, maxe, lo, mid, t, out, visits)
    if starts[mid] <= t:
        if ends[mid] >= t:
            out.append(mid)
        stab(starts, ends, maxe, mid + 1, hi, t, out, visits)

raw = [(540, 600), (555, 570), (600, 690), (615, 630), (660, 780), (700, 720), (720, 840), (780, 800), (810, 900), (870, 885), (900, 960), (930, 1020), (990, 1005), (1000, 1080)]
items = sorted(raw, key=lambda p: p[0])
starts = [p[0] for p in items]
ends = [p[1] for p in items]
n = len(items)
maxe = [0] * n
build(starts, ends, maxe, 0, n)
for t in [560, 625, 715, 850, 1001, 1100]:
    out = []
    visits = [0]
    stab(starts, ends, maxe, 0, n, t, out, visits)
    spans = " ".join(f"{starts[i]}-{ends[i]}" for i in out)
    shown = "none" if spans == "" else spans
    print(f"t={t:>4}: {shown:<26} ({visits[0]} of {n} nodes visited)")
