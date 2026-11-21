doses = [450, 690, 900, 1140, 1380, 1710, 1950, 2200]

def clock(t):
    days = ["Mon", "Tue", "Wed"]
    m = t % 1440
    return f"{days[t // 1440]} {m // 60:02d}:{m % 60:02d}"

for i, t in enumerate(doses):
    notes = []
    if i > 0 and t - doses[i - 1] < 240:
        notes.append(f"only {t - doses[i - 1]} min after the last")
    in_day = sum(1 for d in doses[:i + 1] if d > t - 1440)
    if in_day > 4:
        notes.append(f"dose {in_day} within 24 h")
    print(f"{clock(t)}: {'ok' if not notes else '; '.join(notes)}")
last = doses[-1]
window = [d for d in doses if d > last - 1440]
by_gap = last + 240
by_count = window[-4] + 1440 if len(window) >= 4 else 0
print(f"next dose allowed {clock(max(by_gap, by_count))}")
