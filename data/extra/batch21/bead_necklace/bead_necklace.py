designs = [("choker", "RGB", 360, 6), ("princess", "RRWBBW", 480, 8), ("bracelet", "GY", 190, 4), ("opera", "RWGWBW", 800, 10)]
grand = {}
for name, pattern, length, bead in designs:
    n = (length - 20) // bead
    counts = {}
    for i in range(n):
        c = pattern[i % len(pattern)]
        counts[c] = counts.get(c, 0) + 1
        grand[c] = grand.get(c, 0) + 1
    joined = " ".join(f"{c}{counts[c]}" for c in sorted(counts))
    tail = n % len(pattern)
    note = "ends on a full repeat" if tail == 0 else f"ends {tail} beads into a repeat"
    print(f"{name:<8} {n} beads: {joined}; {note}")
print("beads to buy: " + " ".join(f"{c}{grand[c]}" for c in sorted(grand)))
