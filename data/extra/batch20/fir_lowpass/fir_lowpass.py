def filt(xs, taps):
    out = []
    for n in range(len(xs)):
        acc = 0
        for k in range(len(taps)):
            if n - k >= 0:
                acc += taps[k] * xs[n - k]
        out.append(acc)
    return out

def show(ys, scale):
    return " ".join(f"{float(y) / float(scale):.2f}" for y in ys)

taps = [1, 2, 3, 2, 1]
total = sum(taps)
impulse = [9, 0, 0, 0, 0, 0, 0, 0]
print(f"impulse response: {show(filt(impulse, taps), 9 * total)}")
step = [0, 0, 9, 9, 9, 9, 9, 9, 9, 9]
print(f"step in:  {show(step, 9)}")
print(f"step out: {show(filt(step, taps), 9 * total)}")
buzz = [9 if i % 2 == 0 else -9 for i in range(12)]
print(f"buzz in:  {show(buzz, 9)}")
print(f"buzz out: {show(filt(buzz, taps), 9 * total)}")
nyquist = sum(t if i % 2 == 0 else -t for i, t in enumerate(taps))
print(f"gain at DC {total}/{total}, at Nyquist {nyquist}/{total}")
