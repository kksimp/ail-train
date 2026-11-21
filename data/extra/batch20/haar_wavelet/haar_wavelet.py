def forward(xs):
    out = list(xs)
    n = len(xs)
    while n > 1:
        tmp = list(out)
        for i in range(n // 2):
            tmp[i] = (out[2 * i] + out[2 * i + 1]) / 2.0
            tmp[n // 2 + i] = (out[2 * i] - out[2 * i + 1]) / 2.0
        out = tmp
        n = n // 2
    return out

def inverse(cs):
    out = list(cs)
    n = 1
    while n < len(cs):
        tmp = list(out)
        for i in range(n):
            tmp[2 * i] = out[i] + out[n + i]
            tmp[2 * i + 1] = out[i] - out[n + i]
        out = tmp
        n = n * 2
    return out

signal = [10.0, 12.0, 14.0, 14.0, 13.0, 30.0, 31.0, 29.0]
cs = forward(signal)
print(f"signal:       {signal}")
print(f"coefficients: {cs}")
for limit in [0.5, 1.5, 4.0]:
    kept = [c if i == 0 or abs(c) >= limit else 0.0 for i, c in enumerate(cs)]
    zeros = sum(1 for c in kept if c == 0.0)
    back = inverse(kept)
    worst = 0.0
    for i in range(len(signal)):
        e = abs(back[i] - signal[i])
        if e > worst:
            worst = e
    print(f"drop details under {limit}: {zeros} zeros, rebuilt {back}, worst error {worst}")
