lifetimes = [1, 2, 30, 1, 3, 1, 50, 2, 1, 9, 1, 1, 40, 2, 1, 6]
nursery = []
old = []
copied = 0
for t in range(len(lifetimes)):
    nursery.append([t, t + lifetimes[t], 0])
    now = t + 1
    if now % 4 == 0:
        keep = []
        dead = 0
        promoted = []
        for o in nursery:
            if o[1] <= now:
                dead += 1
            elif o[2] + 1 >= 2:
                old.append([o[0], o[1], o[2] + 1])
                promoted.append(o[0])
            else:
                keep.append([o[0], o[1], o[2] + 1])
                copied += 1
        nursery = keep
        print(f"minor gc at {now:>2}: freed {dead}, kept {len(keep)}, promoted {promoted}")
end = len(lifetimes) + 20
live_old = [o for o in old if o[1] > end]
print(f"old space before major gc: {len(old)}")
print(f"major gc at {end}: {len(live_old)} live")
print(f"nursery copies made: {copied}")
