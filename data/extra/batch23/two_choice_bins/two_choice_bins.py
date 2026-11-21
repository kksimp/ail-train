class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def throw(balls, bins, choices, seed):
    rng = Lcg(seed)
    load = [0] * bins
    for b in range(balls):
        pick = rng.next(bins)
        for c in range(1, choices):
            other = rng.next(bins)
            if load[other] < load[pick]:
                pick = other
        load[pick] += 1
    return load

bins = 200
print(f"{bins} servers; requests placed at random")
for balls in [200, 2000, 20000]:
    one = throw(balls, bins, 1, 17)
    two = throw(balls, bins, 2, 17)
    mean = balls // bins
    print(f"{balls:>5} requests (mean {mean:>3}): busiest with one choice {max(one):>3}, with two choices {max(two):>3}")
three = throw(2000, bins, 3, 17)
print(f"three choices for 2000 requests: busiest {max(three)}")
idle = throw(200, bins, 1, 17).count(0)
print(f"servers left idle by 200 requests with one choice: {idle}")
