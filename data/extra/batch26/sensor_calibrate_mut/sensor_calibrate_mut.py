raw = [212, 215, 230, 990, 218, 140, 221]
clean = [x - 12 for x in raw]
n = 0
for i, x in enumerate(clean):
    if x < 150 or x > 260:
        clean[i] = min(max(x, 150), 260); n += 1
print(f"raw:       {raw}")
print(f"corrected: {clean}")
print(f"clamped {n} spikes")
avg = sum(clean) // len(clean)
t = lambda v: f"{v // 10}.{v % 10}"
print(f"mean {t(avg)} C, max {t(max(clean))} C")
