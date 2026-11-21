import math
def sm(sc, t):
    top = max(sc); e = [math.exp((s - top) / t) for s in sc]; tot = sum(e); return [x / tot for x in e]
names = ["pasta", "curry", "salad", "tacos"]
for t in [0.25, 0.5, 1.0, 2.0, 10.0]:
    p = sm([2.0, 1.5, 0.3, 1.0], t)
    print(f"T {t:>5.2f}: {', '.join(f'{names[i]} {p[i]:.3f}' for i in range(4))}")
