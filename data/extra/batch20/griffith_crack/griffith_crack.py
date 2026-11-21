import math
PI = 3.141592653589793

def break_stress(k, a):
    return k / (1.12 * math.sqrt(PI * a))

def critical_mm(k, w):
    x = k / (1.12 * w)
    return x * x / PI * 1000.0

mats = [("window glass", 0.75, 20.0), ("alumina", 4.0, 150.0), ("aluminium alloy", 30.0, 200.0), ("structural steel", 50.0, 250.0)]
cracks = [0.000001, 0.0001, 0.001, 0.01]
print("breaking stress in MPa for cracks of 1 um, 0.1 mm, 1 mm, 10 mm")
for name, k, w in mats:
    cells = " ".join(f"{break_stress(k, a):>7.1f}" for a in cracks)
    print(f"{name:<16} {cells}")
for name, k, w in mats:
    print(f"{name} at {w:.0f} MPa fails once a crack reaches {critical_mm(k, w):.3f} mm")
