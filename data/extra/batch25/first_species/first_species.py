def motion(dl, du, same):
    if dl == 0 or du == 0:
        return "Oblique"
    if (dl > 0) != (du > 0):
        return "Contrary"
    return "Parallel" if same else "Similar"

def review(cf, cp):
    faults = []
    counts = {}
    for i in range(len(cf)):
        iv = (cp[i] - cf[i]) % 12
        if iv not in [0, 3, 4, 7, 8, 9]:
            faults.append(f"bar {i + 1}: dissonance ({cp[i] - cf[i]} semitones)")
        if i > 0:
            prev = (cp[i - 1] - cf[i - 1]) % 12
            m = motion(cf[i] - cf[i - 1], cp[i] - cp[i - 1], prev == iv)
            counts[m] = counts.get(m, 0) + 1
            if m == "Parallel" and (iv == 0 or iv == 7):
                faults.append(f"bar {i + 1}: parallel perfect interval")
    summary = ", ".join(f"{k} {v}" for k, v in counts.items())
    faults.append(f"motion: {summary}")
    return faults

cf = [62, 65, 64, 62, 67, 65, 69, 67, 65, 64, 62]
good = [69, 69, 67, 69, 71, 72, 72, 71, 74, 73, 74]
bad = [69, 69, 71, 69, 71, 72, 74, 71, 74, 73, 74]
for label, cp in [("Fux's line", good), ("student line", bad)]:
    notes = review(cf, cp)
    print(f"{label}: {len(notes) - 1} faults")
    for n in notes:
        print(f"  {n}")
