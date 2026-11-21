class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def build(w, prob, alias):
    n = len(w)
    total = sum(w)
    scaled = [x * n for x in w]
    small = []
    large = []
    for i in range(n):
        prob.append(total)
        alias.append(i)
        if scaled[i] < total:
            small.append(i)
        else:
            large.append(i)
    while len(small) > 0 and len(large) > 0:
        s = small.pop()
        l = large.pop()
        prob[s] = scaled[s]
        alias[s] = l
        scaled[l] = scaled[l] + scaled[s] - total
        if scaled[l] < total:
            small.append(l)
        else:
            large.append(l)

names = ["common", "uncommon", "rare", "epic", "legend"]
w = [50, 25, 15, 8, 2]
total = sum(w)
prob = []
alias = []
build(w, prob, alias)
for i in range(len(w)):
    print(f"column {i}: keep {names[i]} if coin < {prob[i]}/{total}, else {names[alias[i]]}")
rng = Lcg(5)
counts = [0, 0, 0, 0, 0]
draws = 12000
for _ in range(draws):
    col = rng.next(len(w))
    coin = rng.next(total)
    pick = col if coin < prob[col] else alias[col]
    counts[pick] += 1
for i in range(len(w)):
    expect = draws * w[i] // total
    print(f"{names[i]:<9} drawn {counts[i]:>5}, expected {expect:>5}")
