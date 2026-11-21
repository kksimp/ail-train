hr = [58, 57, 59, 58, 60, 57, 58, 59, 61, 60, 63, 66, 68, 67, 64, 61, 59, 58, 62, 64, 66]

def avg(xs):
    return float(sum(xs)) / float(len(xs))

base = avg(hr[:7])
print(f"baseline {base:.1f} bpm")
flagged = first = 0
for i in range(2, len(hr)):
    roll = avg(hr[i - 2:i + 1])
    if roll >= base + 5.0:
        flagged += 1
        if first == 0:
            first = i + 1
        print(f"day {i + 1}: 3-day average {roll:.1f} (+{roll - base:.1f})")
print(f"{flagged} days flagged, first on day {first}")
print(f"highest single reading {max(hr)}")
