def makespan(jobs):
    t1 = t2 = 0
    for name, a, b in jobs:
        t1 += a
        t2 = max(t2, t1) + b
    return t2

def johnson(jobs):
    front = sorted([j for j in jobs if j[1] <= j[2]], key=lambda j: j[1])
    back = sorted([j for j in jobs if j[1] > j[2]], key=lambda j: -j[2])
    return front + back

def names(jobs):
    return " ".join(j[0] for j in jobs)

jobs = [("A", 3, 6), ("B", 5, 2), ("C", 1, 2), ("D", 6, 6), ("E", 7, 5), ("F", 2, 4)]
best = johnson(jobs)
print(f"given order   {names(jobs)}: done at {makespan(jobs)}")
print(f"Johnson order {names(best)}: done at {makespan(best)}")
t1 = t2 = 0
for name, a, b in best:
    start2 = max(t2, t1 + a)
    t1 += a
    t2 = start2 + b
    print(f"  {name}: cut {t1 - a:>2}-{t1:<2} polish {start2:>2}-{t2}")
