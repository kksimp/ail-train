import math
N = ["small", "x-small", "body", "h6", "h5", "h4", "h3", "h2"]
for i, n in enumerate(N):
    px = 16.0 * 1.2 ** float(i - 2); print(f"{n:<8} {px:>7.3f} px {px / 16:.4f} rem ~{int(math.floor(px + 0.5))} px")
