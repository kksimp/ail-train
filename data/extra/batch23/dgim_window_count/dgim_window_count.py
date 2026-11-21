class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def add(buckets, t, bit, window):
    while len(buckets) > 0 and buckets[-1][0] <= t - window:
        buckets.pop()
    if bit == 1:
        buckets.insert(0, [t, 1])
        size = 1
        while True:
            idx = [k for k in range(len(buckets)) if buckets[k][1] == size]
            if len(idx) < 3:
                break
            buckets[idx[1]][1] = size * 2
            buckets.pop(idx[2])
            size *= 2

def estimate(buckets):
    if len(buckets) == 0:
        return 0
    total = sum(b[1] for b in buckets)
    return total - buckets[-1][1] // 2

window = 64
rng = Lcg(8)
buckets = []
bits = []
for t in range(1, 401):
    chance = 3 if t < 200 else 8
    bit = 1 if rng.next(10) < chance else 0
    bits.append(bit)
    add(buckets, t, bit, window)
    if t % 50 == 0:
        start = max(len(bits) - window, 0)
        exact = sum(bits[start:])
        sizes = [b[1] for b in buckets]
        print(f"t={t:>3}: exact {exact:>2}, estimate {estimate(buckets):>2}, buckets {sizes}")
