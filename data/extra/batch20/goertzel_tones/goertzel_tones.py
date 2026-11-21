import math
PI = 3.141592653589793

def power(xs, hz, rate):
    w = 2.0 * PI * hz / rate
    coeff = 2.0 * math.cos(w)
    s1 = 0.0
    s2 = 0.0
    for x in xs:
        s = x + coeff * s1 - s2
        s2 = s1
        s1 = s
    return s1 * s1 + s2 * s2 - coeff * s1 * s2

def tone(f1, f2, n, rate):
    return [math.sin(2.0 * PI * f1 * float(i) / rate) + math.sin(2.0 * PI * f2 * float(i) / rate) for i in range(n)]

def strongest(xs, freqs, rate):
    best = 0
    for i in range(1, len(freqs)):
        if power(xs, freqs[i], rate) > power(xs, freqs[best], rate):
            best = i
    return best

rate = 8000.0
rows = [697.0, 770.0, 852.0, 941.0]
cols = [1209.0, 1336.0, 1477.0]
keys = ["123", "456", "789", "*0#"]
heard = []
for r, c in [(1, 1), (2, 2), (3, 0), (0, 2), (3, 1)]:
    xs = tone(rows[r], cols[c], 205, rate)
    rr = strongest(xs, rows, rate)
    cc = strongest(xs, cols, rate)
    key = keys[rr][cc]
    heard.append(key)
    levels = " ".join(f"{power(xs, f, rate) / 1000.0:.1f}" for f in rows)
    print(f"{rows[r]:.0f} + {cols[c]:.0f} Hz: row powers {levels} (thousands) -> {key}")
print(f"decoded: {''.join(heard)}")
