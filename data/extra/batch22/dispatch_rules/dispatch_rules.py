jobs = [("A", 6, 8), ("B", 2, 6), ("C", 8, 18), ("D", 3, 15), ("E", 9, 23)]

def score(order):
    t = 0
    flow = 0
    late = 0
    count = 0
    seq = []
    for name, work, due in order:
        t += work
        flow += t
        late += max(t - due, 0)
        if t > due:
            count += 1
        seq.append(name)
    n = float(len(order))
    return f"{''.join(seq)}: mean flow {flow / n:.1f} days, mean lateness {late / n:.1f}, {count} late"

print(f"arrival  {score(jobs)}")
print(f"shortest {score(sorted(jobs, key=lambda j: j[1]))}")
print(f"due date {score(sorted(jobs, key=lambda j: j[2]))}")
print(f"ratio    {score(sorted(jobs, key=lambda j: j[2] / j[1]))}")
