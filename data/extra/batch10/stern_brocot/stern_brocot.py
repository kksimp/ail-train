def mediant(a, b):
    return (a[0] + b[0], a[1] + b[1])

def path_to(p, q):
    lo, hi = (0, 1), (1, 0)
    steps = []
    while True:
        m = mediant(lo, hi)
        if m == (p, q):
            break
        if p * m[1] < m[0] * q:
            steps.append("L")
            hi = m
        else:
            steps.append("R")
            lo = m
    return steps

def follow(steps):
    lo, hi = (0, 1), (1, 0)
    for s in steps:
        m = mediant(lo, hi)
        if s == "L":
            hi = m
        else:
            lo = m
    return mediant(lo, hi)

def letters(steps):
    return "".join(steps) if steps else "(root)"

for p, q in [(1, 1), (3, 7), (5, 8), (22, 7), (355, 113), (13, 21)]:
    steps = path_to(p, q)
    b = follow(steps)
    print(f"{p}/{q}: {letters(steps)} ({len(steps)} steps), decodes to {b[0]}/{b[1]}")
