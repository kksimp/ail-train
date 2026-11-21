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

class Kmv:
    def __init__(self, k):
        self.k = k
        self.vals = []

    def add(self, h):
        if h in self.vals:
            return
        if len(self.vals) < self.k:
            self.vals.append(h)
            self.vals.sort()
        elif h < self.vals[self.k - 1]:
            self.vals[self.k - 1] = h
            self.vals.sort()

    def estimate(self):
        if len(self.vals) < self.k:
            return len(self.vals)
        return (self.k - 1) * 4294967296 // self.vals[self.k - 1]

    def merge(self, other):
        out = Kmv(self.k)
        for h in self.vals:
            out.add(h)
        for h in other.vals:
            out.add(h)
        return out

rng = Lcg(3)
a = Kmv(48)
b = Kmv(48)
sa = set()
sb = set()
for i in range(30000):
    x = rng.next(9000)
    if i % 2 == 0:
        a.add(mix(x))
        sa.add(x)
    else:
        y = x + 4000
        b.add(mix(y))
        sb.add(y)
    if i == 2999 or i == 29999:
        print(f"after {i + 1} items: A {len(sa)} distinct (est {a.estimate()}), B {len(sb)} distinct (est {b.estimate()})")
u = a.merge(b)
print(f"union: {len(sa | sb)} distinct, estimate from merged sketches {u.estimate()}")
