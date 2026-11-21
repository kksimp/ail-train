class Gen:
    def __init__(self, value, factor, picky):
        self.value, self.factor, self.picky = value, factor, picky
    def next(self):
        self.value = self.value * self.factor % 2147483647
        while self.value % self.picky != 0:
            self.value = self.value * self.factor % 2147483647
        return self.value

def judge(sa, sb, pairs, picky):
    a = Gen(sa, 16807, 4 if picky else 1); b = Gen(sb, 48271, 8 if picky else 1)
    hits = 0
    for _ in range(pairs):
        if (a.next() & 65535) == (b.next() & 65535):
            hits += 1
    return hits

a = Gen(618, 16807, 1); b = Gen(883, 48271, 1)
for i in range(1, 4):
    print(f"pair {i}: {a.next():>10} {b.next():>10}")
print(f"part 1: {judge(618, 883, 200000, False)} matches in 200000 pairs")
print(f"part 2: {judge(618, 883, 50000, True)} matches in 50000 picky pairs")
