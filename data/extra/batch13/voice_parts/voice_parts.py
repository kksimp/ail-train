parts = ["soprano", "alto", "tenor", "bass"]
ranges = [(60, 79), (55, 74), (48, 67), (40, 62)]

def overlap(a, b):
    return max(min(a[1], b[1]) - max(a[0], b[0]), 0)

singers = [("Ama", 58, 81), ("Bo", 53, 72), ("Cyd", 47, 69), ("Dov", 38, 60), ("Eun", 56, 76), ("Fin", 45, 64), ("Gil", 52, 70)]
counts = {}
for name, lo, hi in singers:
    voice = (lo, hi)
    best = 0
    for i in range(1, 4):
        if overlap(voice, ranges[i]) > overlap(voice, ranges[best]):
            best = i
    counts[parts[best]] = counts.get(parts[best], 0) + 1
    print(f"{name:<4} {lo}-{hi}: {parts[best]} (covers {overlap(voice, ranges[best])} of {ranges[best][1] - ranges[best][0]} semitones)")
for p in parts:
    print(f"{p}: {counts.get(p, 0)}")
