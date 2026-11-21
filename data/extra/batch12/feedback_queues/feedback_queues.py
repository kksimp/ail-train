procs = [("edit", 0, 3), ("build", 0, 14), ("chat", 1, 2), ("render", 2, 9), ("ping", 6, 1)]
slices = [2, 4, 8]
queues = [[], [], []]
left = [p[2] for p in procs]
arrived = 0
t = 0
finished = 0
segs = []
while finished < len(procs):
    while arrived < len(procs) and procs[arrived][1] <= t:
        queues[0].append(arrived)
        arrived += 1
    lvl = 0
    while lvl < 3 and len(queues[lvl]) == 0:
        lvl += 1
    if lvl == 3:
        t += 1
        continue
    p = queues[lvl].pop(0)
    run = min(slices[lvl], left[p])
    t += run
    left[p] -= run
    segs.append(f"{procs[p][0]}@{lvl}:{run}")
    while arrived < len(procs) and procs[arrived][1] <= t:
        queues[0].append(arrived)
        arrived += 1
    if left[p] == 0:
        finished += 1
        print(f"{procs[p][0]:<6} done at {t:>2}, turnaround {t - procs[p][1]}")
    else:
        down = min(lvl + 1, 2)
        queues[down].append(p)
print(f"runs: {' '.join(segs)}")
