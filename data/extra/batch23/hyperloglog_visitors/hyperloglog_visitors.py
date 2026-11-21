class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self, n):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return (self.state >> 8) % n

def mix(x):
    h = x * 73244475 % 4294967296
    h = (h >> 16) ^ h
    h = h * 73244475 % 4294967296
    return (h >> 16) ^ h

def rank(w):
    r = 1
    bit = 1 << 23
    while r <= 24 and (w & bit) == 0:
        r += 1
        bit = bit >> 1
    return r

def estimate(regs):
    total = 0.0
    for m in regs:
        total += 1.0 / float(1 << m)
    alpha = 0.7213 / (1.0 + 1.079 / 256.0)
    return alpha * 256.0 * 256.0 / total

regs = [0] * 256
exact = set()
rng = Lcg(7)
seen = 0
for stop in [1000, 4000, 16000, 40000]:
    while seen < stop:
        i = rng.next(60000)
        exact.add(i)
        h = mix(i)
        j = h & 255
        regs[j] = max(regs[j], rank(h >> 8))
        seen += 1
    e = estimate(regs)
    err = (e - float(len(exact))) / float(len(exact)) * 100.0
    print(f"{seen:>5} visits: {len(exact):>5} distinct, estimate {e:>8.1f} ({err:>5.1f}% off)")
print("memory: 256 small registers instead of a set of every id")
