class Job:
    def __init__(self, name, time, weight):
        self.name = name
        self.time = time
        self.weight = weight

def cost(jobs):
    clock = 0
    total = 0
    for j in jobs:
        clock += j.time
        total += j.weight * clock
    return total

def smith(jobs):
    out = []
    for j in jobs:
        i = len(out)
        out.append(j)
        while i > 0 and out[i].time * out[i - 1].weight < out[i - 1].time * out[i].weight:
            out[i], out[i - 1] = out[i - 1], out[i]
            i -= 1
    return out

def best_order(jobs, used, current, best):
    if len(current) == len(jobs):
        best[0] = min(best[0], cost(current))
        return
    for i in range(len(jobs)):
        if not used[i]:
            used[i] = True
            current.append(jobs[i])
            best_order(jobs, used, current, best)
            current.pop()
            used[i] = False

jobs = [Job("A", 3, 1), Job("B", 1, 1), Job("C", 4, 5), Job("D", 2, 4), Job("E", 6, 3), Job("F", 5, 2)]
s = smith(jobs)
names = "".join(j.name for j in s)
print(f"Smith's order {names}: weighted finish {cost(s)}")
spt = sorted(jobs, key=lambda j: j.time)
spt_names = "".join(j.name for j in spt)
print(f"shortest first {spt_names}: weighted finish {cost(spt)}")
print(f"given order ABCDEF: weighted finish {cost(jobs)}")
used = [False] * 6
current = []
best = [1000000]
best_order(jobs, used, current, best)
print(f"best of all 720 orders: {best[0]}")
