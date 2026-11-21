import math

def ranks(values):
    order = sorted(range(len(values)), key=lambda i: values[i])
    r = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = float(i + j + 2) / 2.0
        i = j + 1
    return r

def pearson(x, y):
    n = float(len(x))
    mx = my = 0.0
    for i in range(len(x)):
        mx += x[i]
        my += y[i]
    mx = mx / n
    my = my / n
    sxy = sxx = syy = 0.0
    for i in range(len(x)):
        sxy += (x[i] - mx) * (y[i] - my)
        sxx += (x[i] - mx) * (x[i] - mx)
        syy += (y[i] - my) * (y[i] - my)
    return sxy / math.sqrt(sxx * syy)

hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
skill = [2, 3, 5, 9, 15, 24, 39, 60, 98, 150]
noisy = [3, 1, 4, 4, 9, 7, 12, 10, 15, 14]
hf = [float(v) for v in hours]
for name, ys in [("skill", skill), ("noisy", noisy)]:
    yf = [float(v) for v in ys]
    rp = pearson(hf, yf)
    rs = pearson(ranks(hours), ranks(ys))
    print(f"hours vs {name}: Pearson {rp:.4f}, Spearman {rs:.4f}")
print(f"ranks of noisy: {ranks(noisy)}")
