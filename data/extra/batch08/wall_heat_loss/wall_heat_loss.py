b = a = 0.0
for n, ar, uo, un in [("walls", 95.0, 1.6, 0.3), ("roof", 60.0, 2.3, 0.15), ("windows", 18.0, 4.8, 1.4), ("floor", 60.0, 0.9, 0.25), ("door", 2.0, 3.0, 1.0)]:
    wo = uo * ar * 22.0; wn = un * ar * 22.0; b += wo; a += wn
    print(f"{n:<8} {ar:>5.1f} m2: {wo:>6.0f} W -> {wn:>5.0f} W")
print(f"total {b / 1000.0:.2f} kW -> {a / 1000.0:.2f} kW at 22 degrees difference")
print(f"yearly saving about {(b - a) / 22.0 * 2500.0 * 24.0 / 1000.0:.0f} kWh")
