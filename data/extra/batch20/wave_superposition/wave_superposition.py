import math
PI = 3.141592653589793

def sample(t):
    return math.sin(2.0 * PI * 440.0 * t) + math.sin(2.0 * PI * 444.0 * t)

rate = 8000
print(f"beat frequency {444 - 440} Hz, one swell every {1000 // (444 - 440)} ms")
for w in range(11):
    peak = 0.0
    for i in range(200):
        t = float(w * 200 + i) / float(rate)
        v = abs(sample(t))
        if v > peak:
            peak = v
    mid = (float(w) * 0.025 + 0.0125)
    env = 2.0 * abs(math.cos(PI * 4.0 * mid))
    bar = "*" * int(round(peak * 10.0))
    print(f"{w * 25:>3} ms peak {peak:.2f} envelope {env:.2f} {bar}")
