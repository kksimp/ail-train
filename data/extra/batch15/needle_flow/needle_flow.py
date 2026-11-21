def poiseuille(radius, dp, mu, length):
    pi = 3.141592653589793
    r4 = radius * radius * radius * radius
    return pi * r4 * dp / (8.0 * mu * length)
dp = 1005.0 * 9.81 * 1.0
print(f"pressure from 1 m of saline: {dp:.0f} Pa")
rates = {}
for gauge, bore in [(14, 1.69), (16, 1.32), (18, 0.84), (20, 0.6), (22, 0.41)]:
    r = bore / 2000.0
    q = poiseuille(r, dp, 0.00102, 0.032)
    per_min = q * 1000000.0 * 60.0
    rates[gauge] = per_min
    print(f"{gauge}G, bore {bore:.2f} mm: {per_min:>7.1f} mL/min")
ratio = rates[14] / rates[22]
print(f"14G carries {ratio:.0f} times the flow of 22G")
half = poiseuille(0.0005, dp, 0.00102, 0.032) / poiseuille(0.001, dp, 0.00102, 0.032)
print(f"half the radius: {half:.4f} of the flow")
