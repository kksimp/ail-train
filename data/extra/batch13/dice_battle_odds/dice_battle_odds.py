def losses(a, d):
    n = a + d
    combos = 6 ** n
    pairs = min(a, d)
    hist = [0] * (pairs + 1)
    for code in range(combos):
        x = code
        att = []
        de = []
        for k in range(n):
            face = x % 6 + 1
            x //= 6
            if k < a:
                att.append(face)
            else:
                de.append(face)
        hi_a = sorted(att)[::-1]
        hi_d = sorted(de)[::-1]
        lost = 0
        for k in range(pairs):
            if hi_a[k] <= hi_d[k]:
                lost += 1
        hist[lost] += 1
    return hist

for m in [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2]]:
    hist = losses(m[0], m[1])
    total = sum(hist)
    parts = []
    for k, c in enumerate(hist):
        pct = float(c) * 100.0 / float(total)
        parts.append(f"lose {k}: {pct:.2f}%")
    print(f"{m[0]} v {m[1]} ({total} rolls): {', '.join(parts)}")
