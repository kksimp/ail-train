talks = [("Keynote", 540, 600), ("Rust in prod", 570, 630), ("Typed errors", 600, 660), ("Lunch demo", 690, 780), ("GC tuning", 660, 720), ("Closing", 960, 1000), ("Workshop", 720, 990)]
hm = lambda m: f"{m // 60:02d}:{m % 60:02d}"
out, free = [], 0
for t in sorted(talks, key=lambda t: (t[2], t[1])):
    if t[1] >= free: out.append(t); free = t[2]
for t in out: print(f"{hm(t[1])}-{hm(t[2])} {t[0]}")
print(f"{len(out)} of {len(talks)} talks")
