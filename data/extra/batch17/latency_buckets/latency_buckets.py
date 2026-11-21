def estimate(bounds, cum, q):
    total = cum[-1]
    rank = q * float(total)
    prev = 0
    lower = 0
    for i in range(len(bounds)):
        if float(cum[i]) >= rank:
            inb = cum[i] - prev
            frac = (rank - float(prev)) / float(inb)
            return float(lower) + float(bounds[i] - lower) * frac
        prev = cum[i]
        lower = bounds[i]
    return float(bounds[-1])

bounds = [5, 10, 25, 50, 100, 250, 500, 1000]
times = [3, 7, 8, 12, 15, 18, 22, 24, 26, 31, 35, 42, 48, 55, 61, 70, 88, 95, 110, 130, 160, 210, 240, 260, 320, 480, 520, 900, 1500, 40]
cum = []
for b in bounds:
    cum.append(len([t for t in times if t <= b]))
cum.append(len(times))
for i, b in enumerate(bounds):
    print(f"le={b:<5} {cum[i]:>3}")
print(f"le=+Inf  {cum[-1]:>3}")
for q in [0.5, 0.9, 0.99]:
    est = estimate(bounds, cum, q)
    print(f"q{q}: about {est:.1f} ms")
