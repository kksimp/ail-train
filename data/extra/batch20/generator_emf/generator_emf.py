import math
PI = 3.141592653589793

def peak(hz):
    return float(100) * 0.5 * 0.02 * 2.0 * PI * hz

def emf(hz, t):
    return peak(hz) * math.sin(2.0 * PI * hz * t)

def bar(v, pk):
    n = int(round(v / pk * 10.0))
    if n >= 0:
        return " " * 10 + "|" + "+" * n
    return " " * (10 + n) + "-" * (-n) + "|"

hz = 50.0
pk = peak(hz)
print(f"peak {pk:.1f} V, rms {pk / math.sqrt(2.0):.1f} V")
for ms in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]:
    e = emf(hz, float(ms) / 1000.0)
    print(f"{ms:>2} ms {e:>7.1f} V {bar(e, pk)}")
faster = peak(60.0)
print(f"at 60 Hz the peak rises to {faster:.1f} V")
