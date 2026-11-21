def proper_sum(n):
    if n == 1:
        return 0
    s = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            s += d
            if d * d != n:
                s += n // d
        d += 1
    return s

def follow(start, limit):
    chain = [start]
    while len(chain) <= limit:
        nxt = proper_sum(chain[-1])
        if nxt == 0:
            return "reaches 0 through a prime"
        if nxt == chain[-1]:
            return f"settles on the perfect number {nxt}"
        if nxt in chain:
            idx = chain.index(nxt)
            return f"enters a loop of {len(chain) - idx} at {nxt}"
        chain.append(nxt)
    return "still going after 30 steps"

for start in [12, 95, 25, 220, 562, 12496, 1264460, 276]:
    print(f"{start:>7}: {follow(start, 30)}")
steps = [12]
while len(steps) < 8 and steps[-1] > 0:
    steps.append(proper_sum(steps[-1]))
print(f"chain from 12: {steps}")
