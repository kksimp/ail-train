PI = 3.141592653589793
ends_list = [("FixedFree", 2.0), ("PinnedPinned", 1.0), ("FixedPinned", 0.7), ("FixedFixed", 0.5)]
def euler_kn(dia_mm, length, k):
    d = dia_mm / 1000.0
    i = PI * d * d * d * d / 64.0
    kl = k * length
    return PI * PI * 200000000000.0 * i / (kl * kl) / 1000.0
for name, k in ends_list:
    a = euler_kn(40.0, 3.0, k)
    b = euler_kn(60.0, 3.0, k)
    print(f"{name:<13} K {k}: 40 mm bar {a:>7.1f} kN, 60 mm bar {b:>7.1f} kN")
need = 50.0
dia = 20.0
while euler_kn(dia, 3.0, 1.0) < need:
    dia += 2.0
print(f"pinned 3 m strut for {need} kN needs {dia} mm")
