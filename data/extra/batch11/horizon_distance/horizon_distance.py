import math
def horizon_km(h_m):
    r = 6371000.0
    return math.sqrt(2.0 * r * h_m + h_m * h_m) / 1000.0
for name, h in [("standing on a beach", 1.7), ("ship's lookout", 25.0), ("cliff top", 100.0), ("tall tower", 330.0), ("airliner", 11000.0)]:
    print(f"{name:<20} {h:>8.1f} m: horizon {horizon_km(h):>6.1f} km")
lighthouse = horizon_km(60.0)
eye = horizon_km(25.0)
seen = lighthouse + eye
print(f"a 60 m lighthouse is visible from the lookout up to {seen:.1f} km away")
for gap in [30.0, 40.0, 50.0]:
    verdict = "light visible" if gap <= seen else "below the horizon"
    print(f"  at {gap} km: {verdict}")
