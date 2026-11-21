class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def happiness(seats, like):
    total = 0
    for i in range(len(seats)):
        j = (i + 1) % len(seats)
        total += like[seats[i]][seats[j]]
    return total

def improve(start, like, top, rounds, seed):
    rng = Lcg(seed)
    seats = list(start)
    cur = happiness(seats, like)
    best = cur
    for t in range(rounds):
        limit = top * (rounds - t) // rounds
        a = rng.next(len(seats))
        b = rng.next(len(seats))
        seats[a], seats[b] = seats[b], seats[a]
        h = happiness(seats, like)
        if h >= cur - limit:
            cur = h
            best = max(best, cur)
        else:
            seats[a], seats[b] = seats[b], seats[a]
    return best

n = 12
rng = Lcg(314)
like = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        v = rng.next(21) - 10
        like[i][j] = v
        like[j][i] = v
start = list(range(n))
print(f"{n} guests, neighbour likes from -10 to 10; seated in order: {happiness(start, like)}")
for seed in [1, 2, 3]:
    hill = improve(start, like, 0, 3000, seed)
    thresh = improve(start, like, 8, 3000, seed)
    print(f"run {seed}: hill climbing {hill:>3}, threshold accepting {thresh:>3}")
