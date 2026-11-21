import math
for n, a, k in [("Mercury", 0.387, 88.0), ("Venus", 0.723, 224.7), ("Earth", 1.0, 365.256), ("Mars", 1.524, 687.0), ("Jupiter", 5.203, 4331.0)]:
    y = math.sqrt(a * a * a); d = y * 365.256; print(f"{n:<8} {y:>7.3f} years {d:>8.1f} days (off by {abs(d - k) / k * 100.0:.2f}%)")
