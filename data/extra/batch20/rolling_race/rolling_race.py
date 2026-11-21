import math
PI = 3.141592653589793

def speed(k, h):
    return math.sqrt(2.0 * 9.81 * h / (1.0 + k))

def time(k, h, d):
    a = d * PI / 180.0
    length = h / math.sin(a)
    return 2.0 * length / speed(k, h)

bodies = [("hoop", 1.0), ("solid disc", 0.5), ("solid ball", 0.4), ("hollow ball", 2.0 / 3.0), ("sliding block", 0.0)]
h = 1.5
ranked = sorted(bodies, key=lambda b: time(b[1], h, 30.0))
for i, (name, k) in enumerate(ranked):
    print(f"{i + 1}. {name:<14} k {k:.3f}  v {speed(k, h):.3f} m/s  t {time(k, h, 30.0):.3f} s")
first = ranked[0]
last = ranked[-1]
gap = time(last[1], h, 30.0) - time(first[1], h, 30.0)
print(f"{first[0]} beats {last[0]} by {gap:.3f} s")
