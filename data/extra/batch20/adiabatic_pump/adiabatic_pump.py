import math

def compress(s, ratio, gamma):
    p, v, t = s
    return (p * math.pow(ratio, gamma), v / ratio, t * math.pow(ratio, gamma - 1.0))

gamma = 1.4
start = (101325.0, 0.0005, 293.15)
print("pump barrel: 0.5 litres of air at 1 atm and 20 C")
for ratio in [2.0, 4.0, 8.0, 16.0, 22.0]:
    s = compress(start, ratio, gamma)
    w_adi = (s[0] * s[1] - start[0] * start[1]) / (gamma - 1.0)
    w_iso = start[0] * start[1] * math.log(ratio)
    c = s[2] - 273.15
    print(f"ratio {ratio:>4}: {s[0] / 100000.0:>6.2f} bar, {c:>5.0f} C, work {w_adi:>5.1f} J (isothermal {w_iso:.1f} J)")
hot = compress(start, 16.0, gamma)
print(f"a diesel at 16:1 reaches {hot[2]:.0f} K, above the 530 K at which fuel ignites: {str(hot[2] > 530.0).lower()}")
