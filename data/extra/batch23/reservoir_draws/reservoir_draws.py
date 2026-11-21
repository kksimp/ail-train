class Lcg:
    def __init__(self, state):
        self.state = state

    def below(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def sample(stream, k, rng):
    keep = []
    for i in range(len(stream)):
        if i < k:
            keep.append(stream[i])
        else:
            j = rng.below(i + 1)
            if j < k:
                keep[j] = stream[i]
    return keep

orders = ["A101", "B202", "C303", "D404", "E505", "F606", "G707", "H808", "I909", "J010"]
rng = Lcg(99)
for day in range(1, 4):
    picked = " ".join(sample(orders, 3, rng))
    print(f"day {day} audit sample: {picked}")
trials = 6000
hits = {}
for _ in range(trials):
    drawn = sample(orders, 3, rng)
    for o in drawn:
        hits[o] = hits.get(o, 0) + 1
counts = [hits.get(o2, 0) for o2 in orders]
print(f"times each order was picked in {trials} audits: {counts}")
print(f"expected for every order: {trials * 3 // len(orders)}")
