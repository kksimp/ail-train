import math
PI = 3.141592653589793
SHIFT = 0.0024263

def scattered(lam, deg):
    return lam + SHIFT * (1.0 - math.cos(deg * PI / 180.0))

lam = 0.0709
e_in = 1.23984 / lam
print(f"molybdenum X-rays {lam} nm, {e_in:.2f} keV")
for deg in [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0]:
    out = scattered(lam, deg)
    e_out = 1.23984 / out
    given = e_in - e_out
    print(f"{deg:>5.0f} deg: {out:.5f} nm, electron gets {given:.3f} keV ({given / e_in * 100.0:.2f}%)")
gamma = 0.00188
back = scattered(gamma, 180.0)
print(f"a 660 keV gamma ray backscattered keeps {gamma / back * 100.0:.1f}% of its energy")
