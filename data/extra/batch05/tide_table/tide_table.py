import math
def ht(h): return 2.0 + 1.6 * math.cos(2 * math.pi * h / 12.42)
def rd(x): return int(math.floor(abs(x) + 0.5)) * (1 if x >= 0 else -1)
for h in range(13):
    x = ht(h * 2.0); print(f"{h * 2:>2}:00 {x:.2f} m {'#' * rd(x * 5)}")
a = sum(1 for m in range(24 * 60) if ht(m / 60) > 2.5); print(f"above 2.5 m for {a // 60}h {a % 60}m")
