masses = {"C": 12.011, "H": 1.008, "O": 15.999, "N": 14.007, "Fe": 55.845, "P": 30.974}
def near_whole(x):
    return abs(x - round(x)) < 0.1
def formula(els):
    moles = [p / masses[s] for s, p in els]
    low = moles[0]
    for x in moles:
        if x < low:
            low = x
    for mult in range(1, 7):
        counts = [m / low * float(mult) for m in moles]
        if all(near_whole(c) for c in counts):
            parts = []
            for i, (s, p) in enumerate(els):
                n = int(round(counts[i]))
                parts.append(s if n == 1 else f"{s}{n}")
            return "".join(parts)
    return "none under 6"
samples = [[("C", 40.0), ("H", 6.71), ("O", 53.29)], [("C", 85.6), ("H", 14.4)], [("Fe", 69.94), ("O", 30.06)], [("P", 43.64), ("O", 56.36)], [("N", 30.45), ("O", 69.55)], [("C", 92.26), ("H", 7.74)]]
for els in samples:
    shares = ", ".join(f"{p}% {s}" for s, p in els)
    print(f"{shares} -> {formula(els)}")
