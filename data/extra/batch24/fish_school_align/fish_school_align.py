x = [0.0, 1.5, 2.5, 6.0, 7.0, 12.0]
v = [1.0, 2.0, 0.5, 1.5, 3.0, 0.8]
for step in range(21):
    if step % 4 == 0:
        fast = v[0]
        for s in v: fast = s if s > fast else fast
        slow = v[0]
        for s in v: slow = s if s < slow else slow
        print(f"step {step:>2}: speeds from {slow:.3f} to {fast:.3f}")
    nv = []
    for i in range(6):
        total = 0.0; n = 0
        for j in range(6):
            if abs(x[j] - x[i]) <= 3.0:
                total += v[j]; n += 1
        nv.append(v[i] + (total / float(n) - v[i]) / 2.0)
    v = nv
    for i in range(6): x[i] += v[i] * 0.5
print(f"final speeds {' '.join(f'{s:.2f}' for s in v)}")
