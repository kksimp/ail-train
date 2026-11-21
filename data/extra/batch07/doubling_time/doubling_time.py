import math
for p in [1.0, 2.0, 4.0, 6.0, 8.0, 12.0, 20.0]:
    r = 72.0 / p; e = math.log(2.0) / math.log(1.0 + p / 100.0); er = (r - e) / e * 100.0
    print(f"{p:>4.0f}%: rule {r:.2f} years, exact {e:.2f}, error {er:.2f}%")
