import math
patients = [("child", 110.0, 19.0), ("teen", 160.0, 52.0), ("adult", 178.0, 80.0), ("tall adult", 195.0, 102.0)]
def mosteller(p):
    return math.sqrt(p[1] * p[2] / 3600.0)
def du_bois(p):
    return 0.007184 * p[2] ** 0.425 * p[1] ** 0.725
for p in patients:
    m = mosteller(p)
    d = du_bois(p)
    dose = m * 75.0
    print(f"{p[0]:<10} {p[1]} cm {p[2]} kg: Mosteller {m:.3f} m2, Du Bois {d:.3f} m2, dose {dose:.1f} mg")
biggest = max(patients, key=lambda p: int(mosteller(p) * 1000.0))
print(f"largest surface: {biggest[0]}")
