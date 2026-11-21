import math
PI = 3.141592653589793
C = 0.299792458

def na(core, clad):
    return math.sqrt(core * core - clad * clad)

def half_angle(core, clad):
    a = na(core, clad)
    return math.atan(a / math.sqrt(1.0 - a * a)) * 180.0 / PI

def spread(core, clad):
    return 1000.0 * core * (core - clad) / (C * clad)

fibres = [("plastic", 1.49, 1.41), ("glass multimode", 1.48, 1.46), ("glass narrow step", 1.4475, 1.444)]
for name, core, clad in fibres:
    dt = spread(core, clad)
    rate = 1000.0 / (2.0 * dt)
    print(f"{name:<17} NA {na(core, clad):.3f}, accepts {half_angle(core, clad):.1f} degrees, spread {dt:.1f} ns/km, about {rate:.1f} Mbit/s over 1 km")
long = spread(1.48, 1.46) * 5.0
print(f"5 km of glass multimode smears a pulse by {long:.0f} ns")
