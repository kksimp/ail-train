import math
def co(L): return 10.0 * math.log10(sum(10.0 ** (l / 10.0) for l in L))
for n, L in [("office", [55.0, 52.0, 48.0]), ("workshop", [82.0, 79.0, 80.0, 75.0]), ("print room", [70.0, 70.0]), ("plant room", [88.0, 84.0])]:
    t = co(L); print(f"{n}: {len(L)} sources, {t:.1f} dB, {'over the limit' if t > 85.0 else 'ok'}")
