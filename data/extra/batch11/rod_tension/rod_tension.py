PI = 3.141592653589793
mats = [("mild steel", 200.0, 250.0), ("aluminium", 69.0, 95.0), ("titanium", 114.0, 880.0), ("brass", 100.0, 200.0)]
def stress_mpa(force_n, dia_mm):
    area = PI * dia_mm * dia_mm / 4.0
    return force_n / area
force = 20000.0
length = 2000.0
for dia in [12.0, 16.0]:
    s = stress_mpa(force, dia)
    print(f"{dia} mm rod, 20 kN: stress {s:.1f} MPa")
    for name, e, y in mats:
        strain = s / (e * 1000.0)
        stretch = strain * length
        factor = y / s
        flag = " LOW" if factor < 2.0 else ""
        print(f"  {name:<10} stretch {stretch:.3f} mm, safety {factor:.2f}{flag}")
