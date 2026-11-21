import math
PI = 3.141592653589793

def allowed(l, h, k, m):
    if l == "Fcc":
        return (h % 2 == k % 2) and (k % 2 == m % 2)
    return (h + k + m) % 2 == 0

def two_theta(lam, a, s):
    d = a / math.sqrt(float(s))
    x = lam / (2.0 * d)
    return 2.0 * math.atan(x / math.sqrt(1.0 - x * x)) * 180.0 / PI

def peaks(l, a, lam, count):
    seen = set()
    out = []
    for h in range(5):
        for k in range(h + 1):
            for m in range(k + 1):
                s = h * h + k * k + m * m
                if s > 0 and allowed(l, h, k, m) and s not in seen:
                    seen.add(s)
                    out.append([s, h, k, m])
    out = sorted(out, key=lambda p: p[0])[:count]
    return [f"({p[1]}{p[2]}{p[3]}) {two_theta(lam, a, p[0]):.2f}" for p in out]

lam = 0.15406
print(f"Cu K-alpha X-rays, {lam} nm; peaks as 2-theta in degrees")
for name, lat, a in [("aluminium", "Fcc", 0.4050), ("copper", "Fcc", 0.3615), ("iron", "Bcc", 0.2866), ("tungsten", "Bcc", 0.3165)]:
    print(f"{name} (Lattice.{lat}, a {a} nm): {', '.join(peaks(lat, a, lam, 5))}")
