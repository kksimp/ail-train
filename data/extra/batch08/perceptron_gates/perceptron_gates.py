def train(t):
    ins = [[0, 0], [0, 1], [1, 0], [1, 1]]; w1 = w2 = b = 0
    for ep in range(1, 21):
        errs = 0
        for i in range(4):
            x = ins[i]; out = 1 if w1 * x[0] + w2 * x[1] + b > 0 else 0; e = t[i] - out
            if e != 0: w1 += e * x[0]; w2 += e * x[1]; b += e; errs += 1
        if errs == 0: return (w1, w2, b, ep, True)
    return (w1, w2, b, 20, False)
for n, t in [("AND", [0, 0, 0, 1]), ("OR", [0, 1, 1, 1]), ("NAND", [1, 1, 1, 0]), ("XOR", [0, 1, 1, 0])]:
    w1, w2, b, ep, ok = train(t)
    st = f"learned in {ep} epochs" if ok else f"not learned after {ep} epochs"
    print(f"{n:<4} weights {w1}, {w2}, bias {b}: {st}")
