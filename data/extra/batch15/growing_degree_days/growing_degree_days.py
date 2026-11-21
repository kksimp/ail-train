def gdd(tmax, tmin):
    hi = 30.0 if tmax > 30.0 else tmax
    lo = 10.0 if tmin < 10.0 else tmin
    v = (hi + lo) / 2.0 - 10.0
    return v if v > 0.0 else 0.0
weeks = [(16.0, 4.0), (19.0, 7.0), (22.0, 9.0), (24.0, 12.0), (27.0, 14.0), (29.0, 16.0), (32.0, 18.0), (34.0, 19.0), (31.0, 17.0), (30.0, 16.0), (28.0, 15.0), (27.0, 14.0)]
stages = [(100.0, "emergence"), (400.0, "six leaves"), (700.0, "ten leaves"), (1100.0, "tassel")]
total = 0.0; nxt = 0
for i, (tmax, tmin) in enumerate(weeks):
    week = gdd(tmax, tmin) * 7.0
    total += week
    reached = []
    while nxt < len(stages) and total >= stages[nxt][0]:
        reached.append(stages[nxt][1]); nxt += 1
    note = "" if not reached else "  reached " + ", ".join(reached)
    print(f"week {i + 1:>2}: {tmax:.0f}/{tmin:.0f} C, +{week:>5.1f}, total {total:>6.1f}{note}")
print(f"stages reached: {nxt} of {len(stages)}")
