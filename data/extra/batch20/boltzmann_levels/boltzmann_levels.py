import math
K_EV = 0.00008617

def log10_ratio(gap, t):
    return -gap / (K_EV * t) / 2.302585092994046

def show(gap, t):
    e = log10_ratio(gap, t)
    if e > -4.0:
        return f"{math.pow(10.0, e) * 100.0:.3f}%"
    return f"10^{e:.1f}"

gaps = [("molecular rotation", 0.001), ("molecular vibration", 0.1), ("sodium yellow line", 2.1)]
temps = [77.0, 300.0, 1000.0, 6000.0]
for name, gap in gaps:
    cells = [f"{t:.0f} K {show(gap, t)}" for t in temps]
    warm = gap / (K_EV * math.log(100.0))
    print(f"{name} ({gap} eV): {', '.join(cells)}; 1% at {warm:.0f} K")
