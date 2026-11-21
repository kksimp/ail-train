import math
def ch(t, v): p = v ** 0.16; return 13.12 + 0.6215 * t - 11.37 * p + 0.3965 * t * p
def rd(x): return int(math.floor(abs(x) + 0.5)) * (1 if x >= 0 else -1)
W = [10.0, 20.0, 40.0, 60.0]
print("temp " + "".join(f"{int(w):>5}" for w in W))
for t in [5.0, 0.0, -10.0, -20.0, -30.0]: print(f"{int(t):>4} " + "".join(f"{rd(ch(t, w)):>5}" for w in W))
