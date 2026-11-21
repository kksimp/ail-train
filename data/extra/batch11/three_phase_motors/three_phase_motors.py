import math
motors = [("saw", 5.5, 0.85, 0.88), ("compressor", 11.0, 0.86, 0.9), ("extractor", 3.0, 0.8, 0.85), ("lathe", 7.5, 0.84, 0.89)]
def line_amps(m, volts):
    return m[1] * 1000.0 / (math.sqrt(3.0) * volts * m[2] * m[3])
total = 0.0
for m in motors:
    amps = line_amps(m, 400.0)
    single = m[1] * 1000.0 / (230.0 * m[2] * m[3])
    total += amps
    print(f"{m[0]:<10} {m[1]:>5.1f} kW: {amps:>5.1f} A per line (single phase would be {single:.1f} A)")
spare = 63.0 - total
print(f"total {total:.1f} A, spare {spare:.1f} A")
best = motors[0]
for m in motors:
    if int(line_amps(m, 400.0)) > int(line_amps(best, 400.0)):
        best = m
print(f"largest load: {best[0]}")
