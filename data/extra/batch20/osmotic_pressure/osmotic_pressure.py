def tonicity(osm):
    if osm < 0.26:
        return "Hypotonic"
    elif osm > 0.32:
        return "Hypertonic"
    return "Isotonic"

t = 310.0
sols = [("pure water", 0.0, 1), ("0.9% saline", 0.154, 2), ("5% glucose", 0.278, 1), ("0.45% saline", 0.077, 2), ("seawater", 0.6, 2), ("3% saline", 0.513, 2)]
effects = {"Hypotonic": "cells swell", "Isotonic": "cells keep their shape", "Hypertonic": "cells shrivel"}
for name, molar, particles in sols:
    osm = molar * float(particles)
    atm = osm * 0.08206 * t
    k = tonicity(osm)
    print(f"{name:<13} {osm:.3f} osmol/L, {atm:>5.2f} atm, Tonicity.{k}: {effects[k]}")
sea = 0.6 * float(2) * 0.08206 * 298.0 * 1.01325
print(f"reverse osmosis of seawater needs more than {sea:.1f} bar")
