PI = 3.141592653589793
def energy(i, rpm):
    w = 2.0 * PI * rpm / 60.0
    return i * w * w / 2.0
disc = 100.0 * 0.5 * 0.5 / 2.0
rim = 100.0 * 0.5 * 0.5
print(f"100 kg, 0.5 m radius: disc I {disc} kg m2, rim I {rim} kg m2")
for rpm in [1000.0, 3000.0, 6000.0, 10000.0]:
    a = energy(disc, rpm) / 1000.0
    b = energy(rim, rpm) / 1000.0
    wh = energy(rim, rpm) / 3600.0
    print(f"{rpm:>7.1f} rpm: disc {a:>7.1f} kJ, rim {b:>7.1f} kJ ({wh:.1f} Wh)")
gain = energy(disc, 6000.0) - energy(disc, 3000.0)
seconds = gain / 5000.0
print(f"spinning the disc from 3000 to 6000 rpm with 5 kW takes {seconds:.1f} s")
