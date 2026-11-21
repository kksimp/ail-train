def wavelength(period):
    pi = 3.141592653589793
    return 9.81 * period * period / (2.0 * pi)
storm_km = 2000.0
print(f"swell from a storm {storm_km:.0f} km away")
arrivals = []
for t in [6.0, 10.0, 14.0, 18.0, 22.0]:
    l = wavelength(t)
    c = l / t
    cg = c / 2.0
    hours = storm_km * 1000.0 / cg / 3600.0
    arrivals.append((hours, t))
    print(f"T {t:>4.0f} s: length {l:>5.0f} m, speed {c:>4.1f} m/s, group {cg:>4.1f} m/s, deep beyond {l / 2.0:>3.0f} m, arrives after {hours:>5.1f} h")
first = sorted(arrivals)[0]
print(f"first to arrive: the {first[1]:.0f} s swell")
