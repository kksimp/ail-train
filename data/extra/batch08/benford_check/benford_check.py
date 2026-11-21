import math
vals = [2 ** k for k in range(63)]; a = b = 1
for k in range(90): vals.append(a); a, b = b, a + b
cnt = [0] * 10
for v in vals: cnt[int(str(v)[0])] += 1
print(f"{len(vals)} numbers")
for d in range(1, 10):
    print(f"{d}: {cnt[d] / len(vals) * 100.0:>5.1f}% (Benford {math.log10(1.0 + 1.0 / d) * 100.0:>4.1f}%) {'#' * (cnt[d] // 2)}")
