import math
PI = 3.141592653589793
speeds = [("Aluminium", 250.0), ("Brass", 90.0), ("MildSteel", 30.0), ("Stainless", 18.0)]
def spindle(cs, dia):
    rpm = int(cs * 1000.0 / (PI * dia))
    return min(rpm, 2500)
for name, cs in speeds:
    parts = []
    for dia in [10.0, 25.0, 60.0]:
        parts.append(f"{spindle(cs, dia):>4}")
    row = " ".join(parts)
    print(f"{name:<10} rpm at 10/25/60 mm: {row}")
rpm = spindle(30.0, 40.0)
minutes = 120.0 / (0.15 * float(rpm))
print(f"120 mm cut on 40 mm mild steel at 0.15 mm/rev: {rpm} rpm, {minutes:.2f} min")
