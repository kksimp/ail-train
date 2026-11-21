import math
PI = 3.141592653589793
R, L, C = 10.0, 0.01, 0.000001

def reactance(hz):
    w = 2.0 * PI * hz
    return w * L - 1.0 / (w * C)

def size(hz):
    x = reactance(hz)
    return math.sqrt(R * R + x * x)

f0 = 1.0 / (2.0 * PI * math.sqrt(L * C))
q = math.sqrt(L / C) / R
print(f"resonance {f0:.1f} Hz, Q {q:.2f}, bandwidth {f0 / q:.1f} Hz")
for hz in [200.0, 800.0, 1400.0, 1550.0, 1700.0, 3000.0, 10000.0]:
    x = reactance(hz)
    z = size(hz)
    phase = math.atan2(x, R) * 180.0 / PI
    kind = "capacitive" if x < 0.0 else "inductive"
    amps = 5.0 / z * 1000.0
    print(f"{hz:>7.0f} Hz: |Z| {z:>8.2f} ohm, phase {phase:>6.1f} deg, {amps:>6.2f} mA at 5 V, {kind}")
