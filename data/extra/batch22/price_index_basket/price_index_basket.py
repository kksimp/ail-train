import math
basket = [("bread", 250, 50, 270, 48), ("milk", 120, 80, 125, 85), ("coffee", 900, 6, 1100, 4), ("apples", 300, 20, 280, 26), ("fuel", 180, 100, 210, 90)]

def index(num, den):
    return float(num) / float(den) * 100.0

for name, p0, q0, p1, q1 in basket:
    rel = index(p1, p0)
    print(f"{name:<7} {p0:>4} -> {p1:>4}  ({rel:.1f})")
las = index(sum(i[3] * i[2] for i in basket), sum(i[1] * i[2] for i in basket))
paa = index(sum(i[3] * i[4] for i in basket), sum(i[1] * i[4] for i in basket))
fisher = math.sqrt(las * paa)
print(f"Laspeyres {las:.2f}, Paasche {paa:.2f}, Fisher {fisher:.2f}")
print(f"shoppers who switched goods saw {las - paa:.2f} points less inflation")
