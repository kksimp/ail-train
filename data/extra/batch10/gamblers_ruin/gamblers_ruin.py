def success(i, n, p):
    if p == 0.5:
        return float(i) / float(n)
    r = (1.0 - p) / p
    return (1.0 - r ** float(i)) / (1.0 - r ** float(n))

seed = 99
def unit():
    global seed
    seed = (seed * 1103515245 + 12345) % 2147483648
    return float(seed) / 2147483648.0

def simulate(i, n, p, runs):
    wins = 0
    for _ in range(runs):
        chips = i
        while 0 < chips < n:
            if unit() < p:
                chips += 1
            else:
                chips -= 1
        if chips == n:
            wins += 1
    return float(wins) / float(runs)

for p in [0.5, 0.49, 0.47, 0.4]:
    for start in [10, 50]:
        exact = success(start, 100, p)
        sim = simulate(start, 100, p, 400)
        print(f"p {p:.2f}, start {start:>2} of 100: exact {exact:.4f}, simulated {sim:.4f}")
print(f"fair game expected rounds from 10 to 0 or 100: {10 * (100 - 10)}")
