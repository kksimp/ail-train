import math
PI = 3.141592653589793
R = 8.314

def rms(t, m):
    return math.sqrt(3.0 * R * t / m)

gases = [("hydrogen", 2.016), ("helium", 4.003), ("water", 18.02), ("nitrogen", 28.01), ("oxygen", 32.0), ("carbon dioxide", 44.01)]
t = 300.0
print(f"at {t:.0f} K (m/s): most likely, mean, rms")
for name, grams in gases:
    m = grams / 1000.0
    vp = math.sqrt(2.0 * R * t / m)
    mean = math.sqrt(8.0 * R * t / (PI * m))
    print(f"  {name:<15} {vp:>5.0f} {mean:>5.0f} {rms(t, m):>5.0f}")
exo = 1000.0
for pname, esc in [("Earth", 11200.0), ("Mars", 5030.0), ("Moon", 2380.0)]:
    kept = [g[0] for g in gases if esc > 6.0 * rms(exo, g[1] / 1000.0)]
    shown = "nothing" if not kept else ", ".join(kept)
    print(f"{pname} (escape {esc:.0f} m/s, 1000 K upper air) keeps: {shown}")
