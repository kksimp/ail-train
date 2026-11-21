import sys
sys.setrecursionlimit(10000)

class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def sort(xs, lo, hi, random, rng, count):
    if lo >= hi:
        return
    if random:
        j = lo + rng.next(hi - lo + 1)
        xs[lo], xs[j] = xs[j], xs[lo]
    pivot = xs[lo]
    store = lo
    for i in range(lo + 1, hi + 1):
        count[0] += 1
        if xs[i] < pivot:
            store += 1
            xs[store], xs[i] = xs[i], xs[store]
    xs[lo], xs[store] = xs[store], xs[lo]
    sort(xs, lo, store - 1, random, rng, count)
    sort(xs, store + 1, hi, random, rng, count)

def comparisons(inp, random, seed):
    xs = list(inp)
    rng = Lcg(seed)
    count = [0]
    sort(xs, 0, len(xs) - 1, random, rng, count)
    return count[0]

n = 300
sorted_in = list(range(n))
shuffled = list(sorted_in)
rng = Lcg(77)
i = n - 1
while i > 0:
    j = rng.next(i + 1)
    shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    i -= 1
print(f"{n} keys; n(n-1)/2 = {n * (n - 1) // 2}")
print(f"first pivot,  sorted input:   {comparisons(sorted_in, False, 1):>6}")
print(f"first pivot,  shuffled input: {comparisons(shuffled, False, 1):>6}")
for seed in [1, 2, 3]:
    print(f"random pivot (seed {seed}), sorted: {comparisons(sorted_in, True, seed):>6}")
