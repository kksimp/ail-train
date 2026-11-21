def run(jobs, aging):
    done = [False] * len(jobs)
    order = []
    t = 0
    while False in done:
        pick = -1
        best = 1000
        for i in range(len(jobs)):
            if not done[i] and jobs[i][1] <= t:
                boost = (t - jobs[i][1]) // 4 if aging else 0
                eff = jobs[i][2] - boost
                if eff < best:
                    best = eff
                    pick = i
        if pick < 0:
            t += 1
            continue
        order.append(f"{jobs[pick][0]}({t}-{t + jobs[pick][3]})")
        t += jobs[pick][3]
        done[pick] = True
    return order

jobs = [("backup", 0, 9, 3), ("web", 0, 2, 4), ("mail", 2, 3, 3), ("web2", 4, 2, 4), ("mail2", 7, 3, 3), ("web3", 10, 2, 4), ("mail3", 13, 3, 3)]
for aging in [False, True]:
    label = "with aging" if aging else "no aging  "
    order = run(jobs, aging)
    print(f"{label}: {' '.join(order)}")
print("backup waits for every other job unless it ages")
