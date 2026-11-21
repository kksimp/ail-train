sc = [0.95, 0.9, 0.82, 0.77, 0.7, 0.64, 0.55, 0.48, 0.4, 0.33, 0.25, 0.12]; lab = [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0]
pos = sum(lab); neg = len(lab) - pos; tp = fp = 0; px = py = 0.0; area = 0.0
print("threshold  TPR    FPR")
for i in range(len(sc)):
    if lab[i] == 1: tp += 1
    else: fp += 1
    y = tp / pos; x = fp / neg; area += (x - px) * (y + py) / 2.0; px = x; py = y
    print(f"{sc[i]:>9.2f} {y:>6.3f} {x:>6.3f}")
print(f"area under curve {area:.3f}")
