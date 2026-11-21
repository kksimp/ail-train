import math

def pearson(a, b):
    n = float(len(a))
    ma = 0.0
    for x in a:
        ma = ma + x
    ma = ma / n
    mb = 0.0
    for x in b:
        mb = mb + x
    mb = mb / n
    sab = saa = sbb = 0.0
    for i in range(len(a)):
        da = a[i] - ma
        db = b[i] - mb
        sab += da * db
        saa += da * da
        sbb += db * db
    return sab / math.sqrt(saa * sbb)

seed = 2024
master = []
for i in range(40):
    seed = (seed * 1103515245 + 12345) % 2147483648
    master.append(0.5 + (seed % 1000) / 1000.0)
start = 1700
sample = []
for i in range(12):
    seed = (seed * 1103515245 + 12345) % 2147483648
    noise = ((seed % 200) - 100) / 1000.0
    sample.append(master[23 + i] * 1.3 + noise)
scores = []
for off in range(len(master) - len(sample) + 1):
    scores.append((off, pearson(sample, master[off:off + len(sample)])))
best = sorted(scores, key=lambda s: -int(s[1] * 1000000.0))
for k in range(3):
    off, r = best[k]
    print(f"rings {start + off}-{start + off + 11}: r = {r:.3f}")
off0 = best[0][0]
print(f"outermost ring dated to {start + off0 + 11}, master covers {start}-{start + len(master) - 1}")
