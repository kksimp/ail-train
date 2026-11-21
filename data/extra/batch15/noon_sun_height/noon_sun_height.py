import math
def declination(day):
    pi = 3.141592653589793
    return 23.44 * math.sin(2.0 * pi * float(284 + day) / 365.0)
def noon_altitude(lat, day): return 90.0 - abs(lat - declination(day))
days = [("Mar 20", 79), ("Jun 21", 172), ("Sep 22", 265), ("Dec 21", 355)]
for label, n in days:
    print(f"{label}: declination {declination(n):>6.2f} deg")
for name, lat in [("Oslo", 59.91), ("London", 51.51), ("Cairo", 30.04), ("Singapore", 1.35), ("Cape Town", -33.92)]:
    cells = []
    for d in days:
        alt = noon_altitude(lat, d[1])
        cells.append(f"{alt:5.1f}")
    print(f"{name:<10} {lat:>6.2f}: {' '.join(cells)}")
