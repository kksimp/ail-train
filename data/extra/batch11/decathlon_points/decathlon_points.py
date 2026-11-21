events = [("100 m", 25.4347, 18.0, 1.81, True), ("long jump", 0.14354, 220.0, 1.4, False), ("shot put", 51.39, 1.5, 1.05, False), ("high jump", 0.8465, 75.0, 1.42, False), ("400 m", 1.53775, 82.0, 1.81, True)]
def points(ev, mark):
    gap = ev[2] - mark if ev[4] else mark - ev[2]
    if gap <= 0.0:
        return 0
    return int(ev[1] * gap ** ev[3])
totals = []
for name, marks in [("Ruiz", [10.9, 720.0, 14.2, 201.0, 49.1]), ("Okafor", [11.3, 690.0, 15.8, 195.0, 50.6]), ("Berg", [10.6, 745.0, 13.1, 189.0, 47.9])]:
    parts = []
    total = 0
    for i, ev in enumerate(events):
        p = points(ev, marks[i])
        total += p
        parts.append(f"{p}")
    joined = " ".join(parts)
    print(f"{name:<7} {joined} = {total}")
    totals.append((name, total))
ranked = sorted(totals, key=lambda t: 0 - t[1])
leader, pts = ranked[0]
print(f"leader after day one: {leader} with {pts}")
