import math
PI = 3.141592653589793

def cutoff(r, c):
    return 1.0 / (2.0 * PI * r * c)

def gain(f, fc):
    ratio = f / fc
    return 1.0 / math.sqrt(1.0 + ratio * ratio)

fc = cutoff(1000.0, 0.0000001)
print(f"R 1 kOhm, C 100 nF: cutoff {fc:.1f} Hz")
for f in [100.0, 500.0, 1000.0, 1600.0, 5000.0, 20000.0]:
    g = gain(f, fc)
    db = 20.0 * math.log10(g)
    print(f"{f:>8.1f} Hz: gain {g:.3f}, {db:>7.2f} dB")
target = 3000.0
c = 1.0 / (2.0 * PI * 1000.0 * target)
nano = c * 1000000000.0
print(f"for a 3000 Hz cutoff with 1 kOhm use {nano:.1f} nF")
