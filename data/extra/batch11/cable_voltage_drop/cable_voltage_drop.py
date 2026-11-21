def drop_volts(amps, metres, mm2):
    resistance = 0.0172 * 2.0 * metres / mm2
    return amps * resistance

def pick(sizes, amps, metres, volts):
    for s in sizes:
        if drop_volts(amps, metres, s) / volts * 100.0 < 3.0:
            return s
    return None

sizes = [1.5, 2.5, 4.0, 6.0, 10.0, 16.0]
for name, amps, metres in [("garden shed", 16.0, 25.0), ("garage", 20.0, 40.0), ("workshop", 32.0, 60.0), ("pump house", 25.0, 150.0)]:
    s = pick(sizes, amps, metres, 230.0)
    if s is not None:
        d = drop_volts(amps, metres, s)
        loss = d * amps
        print(f"{name:<12} {amps} A over {metres} m: {s} mm2, drop {d:.2f} V, loss {loss:.1f} W")
    else:
        print(f"{name:<12} {amps} A over {metres} m: needs more than 16 mm2")
