import math
def ds(D, hole, h): r = D / (hole / 100.0); return r * r * math.sqrt(2.0 * h / 9.81)
def clock(s): w = int(s); return f"{w // 60} min {w % 60} s"
for n, D, hole, h in [("rain barrel", 0.6, 2.0, 0.9), ("water butt", 0.8, 2.5, 1.2), ("cistern", 1.5, 5.0, 2.0), ("bath", 0.7, 4.0, 0.4)]:
    f = ds(D, hole, h); print(f"{n:<12} empties in {clock(f)}, top half in {clock(f - ds(D, hole, h / 2.0))}")
