def change(v):
    if v == 0: return [1]
    s = str(v)
    if len(s) % 2 == 0:
        h = len(s) // 2
        return [int(s[:h]), int(s[h:])]
    return [v * 2025]

def blink(counts):
    out = {}
    for v, n in counts.items():
        for w in change(v):
            out[w] = out.get(w, 0) + n
    return out

counts = {}
for v in [7, 41, 0, 2309]:
    counts[v] = counts.get(v, 0) + 1
for t in range(1, 41):
    counts = blink(counts)
    if t in (5, 15, 25, 40):
        print(f"after {t} blinks: {sum(counts.values())} pebbles, {len(counts)} distinct values")
    if t == 15:
        print(f"part 1: {sum(counts.values())} pebbles")
print(f"part 2: {sum(counts.values())} pebbles")
