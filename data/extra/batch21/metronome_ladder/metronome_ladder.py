sessions = ["cccccc", "ccmcc", "cmmcc", "ccccccccc", "cmcmcc", "cccccc", "mmccc", "cccccccc", "ccccccc"]
bpm, clean, miss = 60, 0, 0
reached = 0
for i, s in enumerate(sessions):
    start = bpm
    for run in s:
        if run == "c":
            clean += 1
            miss = 0
            if clean == 3:
                bpm += 4
                clean = 0
        else:
            miss += 1
            clean = 0
            if miss == 2:
                bpm = max(bpm - 4, 60)
                miss = 0
    print(f"session {i + 1}: {start} -> {bpm} bpm ({len(s)} runs, {s.count('m')} missed)")
    if bpm >= 96 and reached == 0:
        reached = i + 1
print(f"goal of 96 bpm first reached in session {reached}")
