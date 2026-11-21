import math

def table(lam, upto):
    out = []
    term = math.exp(-lam)
    for k in range(upto + 1):
        out.append(term)
        term = term * lam / float(k + 1)
    return out

for lam in [0.5, 2.0, 4.5]:
    t = table(lam, 12)
    cum = 0.0
    cells = []
    mode = 0
    for k in range(7):
        cells.append(f"{t[k]:.4f}")
        if t[k] > t[mode]:
            mode = k
    for k in range(4):
        cum += t[k]
    print(f"lambda {lam:.1f}: P(0..6) {' '.join(cells)}")
    print(f"    at most 3: {cum:.4f}, more than 3: {1.0 - cum:.4f}, most likely count {mode}")
t = table(2.0, 40)
mean = 0.0
sq = 0.0
for k in range(41):
    mean += float(k) * t[k]
    sq += float(k) * float(k) * t[k]
print(f"lambda 2: mean {mean:.6f}, variance {sq - mean * mean:.6f}")
