def regulars(count):
    h = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    while len(h) < count:
        a = h[i2] * 2
        b = h[i3] * 3
        c = h[i5] * 5
        v = min(min(a, b), c)
        h.append(v)
        if v == a:
            i2 += 1
        if v == b:
            i3 += 1
        if v == c:
            i5 += 1
    return h

h = regulars(1000)
first = h[0:20]
print(f"first 20: {first}")
print(f"100th: {h[99]}, 1000th: {h[999]}")
for length in [1000, 1100, 4097, 30001, 100000]:
    k = 0
    while h[k] < length:
        k += 1
    waste = h[k] - length
    print(f"signal of {length:>6} samples -> FFT size {h[k]:>6} ({waste} padding)")
