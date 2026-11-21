import math
def pn(a):
    for lim, n in [(1.85, "new moon"), (5.54, "waxing crescent"), (9.23, "first quarter"), (12.92, "waxing gibbous"), (16.61, "full moon"), (20.30, "waning gibbous"), (23.99, "last quarter"), (27.68, "waning crescent")]:
        if a < lim: return n
    return "new moon"
for l, d in [("2000-01-06", 5), ("2000-01-21", 20), ("2024-04-08", 8864), ("2026-11-21", 9821), ("2027-01-01", 9862)]:
    x = float(d) - 5.763; a = x - math.floor(x / 29.530588) * 29.530588
    lt = (1.0 - math.cos(a / 29.530588 * 2.0 * 3.141592653589793)) / 2.0
    print(f"{l}: age {a:.1f} days, {pn(a)}, {lt * 100.0:.0f}% lit")
