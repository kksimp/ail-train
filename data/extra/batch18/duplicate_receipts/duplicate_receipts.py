claims = [("ana", "Cafe Rio", 1250, 3), ("ben", "TrainCo", 4590, 3), ("ana", "Cafe Rio", 1250, 3), ("cyd", "Cafe Rio", 1250, 4), ("ben", "TrainCo", 4590, 3), ("cyd", "Hotel Lux", 12900, 4), ("ana", "TrainCo", 4590, 5)]
seen = set(); pp = {}; d = 0
for w, s, c, day in claims:
    if (s, c, day) not in seen: seen.add((s, c, day)); pp[w] = pp.get(w, 0) + c
    else: d += 1; print(f"duplicate: {w} {s} {c} on day {day}")
for w, t in pp.items(): print(f"{w}: {t // 100}.{t % 100:02}")
print(f"{d} duplicates, {len(seen)} unique receipts")
