import math
def vo2(metres):
    return (float(metres) - 504.9) / 44.73
def band(v):
    return "Poor" if v < 30.0 else ("Fair" if v < 40.0 else ("Good" if v < 50.0 else "Excellent"))
counts = {}
for name, metres in [("Ines", 2850), ("Tomas", 2100), ("Priya", 2400), ("Kofi", 3150), ("Lena", 1750)]:
    v = vo2(metres)
    b = band(v)
    counts[b] = counts.get(b, 0) + 1
    print(f"{name:<6} {metres} m: VO2max {v:.1f} -> Band.{b}")
for b in ["Poor", "Fair", "Good", "Excellent"]:
    print(f"{b}: {counts.get(b, 0)}")
goal = int(math.ceil(45.0 * 44.73 + 504.9))
print(f"a VO2max of 45 needs {goal} m in 12 minutes")
