ms = [("standup", 900, 915), ("design", 910, 1030), ("1:1", 1000, 1030), ("lunch", 1200, 1300), ("review", 1030, 1130), ("sync", 905, 1005)]
ev = sorted([(s, 1) for _, s, _ in ms] + [(e, -1) for _, _, e in ms])
cur = most = 0
for _, d in ev:
    cur += d; most = max(most, cur)
print(f"rooms needed: {most}")
lg = ms[0]
for m in ms:
    if m[2] - m[1] > lg[2] - lg[1]: lg = m
print(f"{lg[0]} clashes with " + ", ".join(m[0] for m in ms if m[0] != lg[0] and m[1] < lg[2] and lg[1] < m[2]))
print("lunch alone: 1")
