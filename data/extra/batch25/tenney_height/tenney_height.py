import math

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def log2(x):
    return math.log(x) / math.log(2.0)

raw = [("tritone", 45, 32), ("fifth", 6, 4), ("major third", 5, 4), ("octave", 2, 1), ("whole tone", 9, 8), ("fourth", 8, 6), ("minor third", 6, 5), ("harmonic seventh", 7, 4), ("major sixth", 5, 3), ("minor sixth", 8, 5), ("semitone", 16, 15), ("major seventh", 15, 8)]
reduced = []
for name, p, q in raw:
    g = gcd(p, q)
    reduced.append((name, p // g, q // g))
for name, p, q in sorted(reduced, key=lambda r: r[1] * r[2]):
    h = log2(float(p * q))
    size = 1200.0 * log2(p / q)
    frac = f"{p}/{q}"
    print(f"{name:<17} {frac:>5}  height {h:>5.2f}  {size:>7.1f} cents")
