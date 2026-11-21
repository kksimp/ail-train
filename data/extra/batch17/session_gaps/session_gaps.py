def split_sessions(ts, gap):
    out = []
    start = ts[0]
    prev = ts[0]
    for t in ts[1:]:
        if t - prev > gap:
            out.append([start, prev])
            start = t
        prev = t
    out.append([start, prev])
    return out

events = [("ana", 0), ("ben", 3), ("ana", 5), ("ana", 12), ("ben", 20), ("cy", 22), ("ana", 50), ("ben", 51), ("ben", 70), ("ana", 95), ("cy", 100), ("ana", 110), ("ana", 130), ("cy", 131), ("ben", 200)]
times = {}
for who, t in events:
    times.setdefault(who, []).append(t)
total = 0
minutes = 0
for who, ts in times.items():
    sessions = split_sessions(ts, 30)
    spans = ", ".join(f"{s[0]}-{s[1]}" for s in sessions)
    print(f"{who:<4} {len(sessions)} sessions: {spans}")
    total += len(sessions)
    for s in sessions:
        minutes += s[1] - s[0]
avg = minutes / total
print(f"{total} sessions, average length {avg:.1f} minutes")
