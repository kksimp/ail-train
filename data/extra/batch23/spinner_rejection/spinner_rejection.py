class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

weights = [9, 3, 6, 1, 4, 7]
top = max(weights)
n = len(weights)
rng = Lcg(2025)
counts = [0, 0, 0, 0, 0, 0]
proposals = 0
accepted = 0
while accepted < 6000:
    x = rng.next(n)
    u = rng.next(top)
    proposals += 1
    if u < weights[x]:
        counts[x] += 1
        accepted += 1
total = sum(weights)
for i in range(n):
    expect = 6000 * weights[i] // total
    bar = "#" * (counts[i] // 100)
    print(f"sector {i + 1} weight {weights[i]}: {counts[i]:>4} (expected {expect:>4}) {bar}")
rate = accepted / proposals
ideal = total / (n * top)
print(f"accepted {accepted} of {proposals} proposals: rate {rate:.3f}, theory {ideal:.3f}")
