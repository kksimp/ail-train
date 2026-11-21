def schedule(jobs, preempt):
    left = [j[2] for j in jobs]
    done = [-1] * len(jobs)
    timeline = []
    t = 0
    running = -1
    while -1 in done:
        if running < 0 or preempt:
            pick = -1
            for i in range(len(jobs)):
                if jobs[i][1] <= t and left[i] > 0:
                    if pick < 0 or left[i] < left[pick]:
                        pick = i
            running = pick
        if running < 0:
            timeline.append(".")
        else:
            timeline.append(jobs[running][0])
            left[running] -= 1
            if left[running] == 0:
                done[running] = t + 1
                running = -1
        t += 1
    wait = 0
    for i in range(len(jobs)):
        wait += done[i] - jobs[i][1] - jobs[i][2]
    return ["".join(timeline), f"{wait}"]

jobs = [("A", 0, 7), ("B", 2, 4), ("C", 4, 1), ("D", 5, 4), ("E", 15, 2)]
for preempt in [False, True]:
    r = schedule(jobs, preempt)
    name = "SRTF" if preempt else "SJF "
    total = int(r[1])
    mean = total / len(jobs)
    print(f"{name} {r[0]}")
    print(f"     total wait {total}, mean {mean:.1f}")
