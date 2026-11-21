import math
def rd(x): return int(math.floor(x + 0.5))
for n, m in [("Mercury", 57.9), ("Venus", 108.2), ("Earth", 149.6), ("Mars", 227.9), ("Jupiter", 778.6), ("Saturn", 1433.5), ("Uranus", 2872.5), ("Neptune", 4495.1)]:
    s = rd(m * 1000000.0 / 299792.458); print(f"{n:<8} {s // 60:>3}m {s % 60:02}s  x{m / 149.6:.2f}")
