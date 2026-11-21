jobs = [("J1", 4, 6), ("J2", 3, 7), ("J3", 2, 8), ("J4", 5, 12), ("J5", 3, 13), ("J6", 4, 15)]
kept = []
dropped = []
t = 0
for j in sorted(jobs, key=lambda x: x[2]):
    kept.append(j)
    t += j[1]
    if t > j[2]:
        longest = 0
        for i in range(1, len(kept)):
            if kept[i][1] > kept[longest][1]:
                longest = i
        t -= kept[longest][1]
        dropped.append(kept.pop(longest))
t = 0
for name, time, due in kept:
    t += time
    print(f"{name}: done day {t:>2}, due {due:>2}")
for name, time, due in dropped:
    t += time
    print(f"{name}: done day {t:>2}, due {due:>2} (late)")
print(f"{len(dropped)} late of {len(jobs)}")
