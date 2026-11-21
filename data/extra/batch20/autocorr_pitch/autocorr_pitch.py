import math
PI = 3.141592653589793

def voice(f0, rate, n):
    xs = []
    for i in range(n):
        t = float(i) / rate
        xs.append(math.sin(2.0 * PI * f0 * t) + 0.6 * math.sin(4.0 * PI * f0 * t) + 0.3 * math.sin(6.0 * PI * f0 * t))
    return xs

def autocorr(xs, lag):
    s = 0.0
    for i in range(len(xs) - lag):
        s += xs[i] * xs[i + lag]
    return s

def best_lag(xs, lo, hi):
    best = lo
    for lag in range(lo, hi + 1):
        if autocorr(xs, lag) > autocorr(xs, best):
            best = lag
    return best

rate = 8000.0
for f0 in [100.0, 160.0, 200.0, 250.0, 320.0]:
    xs = voice(f0, rate, 800)
    lag = best_lag(xs, 20, 160)
    est = rate / float(lag)
    zero = autocorr(xs, 0)
    print(f"{f0:.0f} Hz voice: best lag {lag} samples -> {est:.1f} Hz, peak {autocorr(xs, lag) / zero:.3f} of r(0)")
