metals = [("copper", 63.55, 2, 8.96), ("silver", 107.87, 1, 10.49), ("nickel", 58.69, 2, 8.91), ("zinc", 65.38, 2, 7.14), ("gold", 196.97, 3, 19.3)]
def grams(m, amps, seconds):
    return amps * seconds * m[1] / (float(m[2]) * 96485.0)
area = 50.0
microns = 10.0
for m in metals:
    hourly = grams(m, 2.0, 3600.0)
    need = m[3] * area * microns / 10000.0
    minutes = need / grams(m, 2.0, 60.0)
    print(f"{m[0]:<7} {hourly:>5.2f} g per hour at 2 A; {microns} um on {area} cm2 needs {need:.4f} g, {minutes:>5.1f} min")
