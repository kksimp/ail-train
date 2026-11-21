def clearance(p):
    base = float(140 - p[1]) * p[2] / (72.0 * p[4])
    return base * 0.85 if p[3] else base
def dose_share(c):
    if c >= 50.0: return 100
    if c >= 30.0: return 75
    if c >= 10.0: return 50
    return 25
usual = 1000
patients = [("Mr A", 45, 82.0, False, 0.9), ("Mrs B", 78, 58.0, True, 1.4), ("Mr C", 66, 70.0, False, 2.1), ("Ms D", 52, 64.0, True, 1.1), ("Mr E", 84, 61.0, False, 4.6)]
for p in patients:
    c = clearance(p)
    share = dose_share(c)
    dose = usual * share // 100
    print(f"{p[0]:<6} age {p[1]}, {p[2]:.0f} kg, SCr {p[4]:.1f}: CrCl {c:>5.1f} mL/min -> {share}% dose, {dose} mg")
low = len([p for p in patients if clearance(p) < 30.0])
print(f"{low} patients need at least a halved dose")
