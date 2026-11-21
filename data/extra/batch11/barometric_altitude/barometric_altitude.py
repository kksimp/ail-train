def altitude(p, p0):
    return 44330.0 * (1.0 - (p / p0) ** (1.0 / 5.255))
def pressure(h, p0):
    return p0 * (1.0 - h / 44330.0) ** 5.255
p0 = 1013.25
log = [("08:00 car park", 978.4), ("09:30 hut", 921.7), ("11:00 col", 862.0), ("12:15 summit", 821.3), ("14:00 lake", 889.5)]
last = 0.0
climb = 0.0
for i, (label, p) in enumerate(log):
    h = altitude(p, p0)
    if i > 0 and h > last:
        climb += h - last
    last = h
    print(f"{label:<15} {p:>6.1f} hPa -> {h:>6.1f} m")
print(f"total climb {climb:.1f} m")
for h in [0.0, 1500.0, 4808.0, 8849.0]:
    print(f"at {h:>6.1f} m the air pressure is {pressure(h, p0):>7.2f} hPa")
