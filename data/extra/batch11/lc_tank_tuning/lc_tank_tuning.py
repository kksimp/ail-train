import math
PI = 3.141592653589793

def resonance(l, c):
    return 1.0 / (2.0 * PI * math.sqrt(l * c))

def needed_c(l, f):
    w = 2.0 * PI * f
    return 1.0 / (w * w * l)

coil = 0.00024
for pf in [50, 100, 200, 365]:
    c = float(pf) / 1000000000000.0
    khz = resonance(coil, c) / 1000.0
    print(f"{pf:>4} pF -> {khz:>7.1f} kHz")
for name, k in [("North AM", 540), ("City Talk", 1010), ("Coast", 1700)]:
    need = needed_c(coil, float(k) * 1000.0) * 1000000000000.0
    fits = "in range" if need <= 365.0 and need >= 50.0 else "out of range"
    print(f"{name:<10} {k:>5} kHz needs {need:>6.1f} pF ({fits})")
