import math
def speed_at(v0, h0, h):
    sq = v0 * v0 + 2.0 * 9.81 * (h0 - h)
    if sq < 0.0:
        return None
    return math.sqrt(sq)
track = [("lift hill top", 45.0), ("first drop", 2.0), ("camel back", 30.0), ("loop top", 25.0), ("helix", 12.0), ("final hill", 47.0), ("brake run", 4.0)]
v0 = 1.5
h0 = 45.0
reach = h0 + v0 * v0 / (2.0 * 9.81)
print(f"energy reaches {reach:.2f} m")
for name, h in track:
    v = speed_at(v0, h0, h)
    if v is not None:
        kmh = v * 3.6
        print(f"{name:<13} {h:>4.1f} m: {v:>5.2f} m/s ({kmh:.1f} km/h)")
    else:
        print(f"{name:<13} {h:>4.1f} m: the train rolls back before here")
        break
