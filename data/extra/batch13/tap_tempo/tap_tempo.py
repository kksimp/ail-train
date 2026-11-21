def tempo(taps):
    gaps = [taps[i] - taps[i - 1] for i in range(1, len(taps))]
    sorted_gaps = sorted(gaps)
    median = sorted_gaps[len(sorted_gaps) // 2]
    kept = [g for g in gaps if abs(g - median) * 4 <= median]
    mean = float(sum(kept)) / float(len(kept))
    return [60000.0 / mean, float(len(gaps) - len(kept))]

sessions = [("steady", [0, 500, 1001, 1499, 2000, 2502]), ("missed tap", [0, 430, 860, 1720, 2150, 2580]), ("double tap", [0, 600, 750, 1200, 1800, 2400, 3000]), ("drifting", [0, 380, 770, 1170, 1580, 2000, 2430])]
for label, taps in sessions:
    r = tempo(taps)
    dropped = int(r[1])
    print(f"{label:<10} {r[0]:>6.1f} bpm, {dropped} gap(s) dropped")
