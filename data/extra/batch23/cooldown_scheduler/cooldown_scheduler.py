def schedule(tasks, n):
    left = {}
    for c in tasks:
        left[c] = left.get(c, 0) + 1
    ready_at = {}
    out = []
    remaining = len(tasks)
    t = 0
    while remaining > 0:
        pick = ' '
        most = 0
        for c in sorted(left.keys()):
            if left[c] > most and ready_at.get(c, 0) <= t:
                most = left[c]
                pick = c
        if most == 0:
            out.append('.')
        else:
            out.append(pick)
            left[pick] -= 1
            ready_at[pick] = t + n + 1
            remaining -= 1
        t += 1
    return "".join(out)

def bound(tasks, n):
    counts = {}
    for c in tasks:
        counts[c] = counts.get(c, 0) + 1
    top = max(counts.values())
    ties = sum(1 for v in counts.values() if v == top)
    return max((top - 1) * (n + 1) + ties, len(tasks))

for tasks, n in [("AAABBB", 2), ("AAABBB", 0), ("AAAAAABCDEFG", 2), ("AABBCCDD", 3), ("AAAABBBCC", 1)]:
    plan = schedule(tasks, n)
    print(f"{tasks:<13} n={n}: {plan} ({len(plan)} slots, bound {bound(tasks, n)})")
