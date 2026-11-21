class Blocks:
    def __init__(self, vals, size):
        self.vals = list(vals)
        self.size = size
        self.sums = []
        for i in range(len(vals)):
            if i % size == 0:
                self.sums.append(0)
            self.sums[i // size] += vals[i]

    def set(self, i, v):
        self.sums[i // self.size] += v - self.vals[i]
        self.vals[i] = v

    def range_sum(self, lo, hi):
        total = 0
        reads = 0
        i = lo
        while i <= hi:
            if i % self.size == 0 and i + self.size - 1 <= hi:
                total += self.sums[i // self.size]
                i += self.size
            else:
                total += self.vals[i]
                i += 1
            reads += 1
        return [total, reads]

readings = [4, 8, 1, 9, 3, 7, 2, 6, 5, 5, 8, 1, 4, 7, 3, 9, 2, 6, 8, 4, 1, 5, 7, 3, 6]
b = Blocks(readings, 5)
print(f"block sums: {b.sums}")
for q in [[0, 24], [3, 17], [6, 8], [10, 19]]:
    r = b.range_sum(q[0], q[1])
    brute = sum(b.vals[q[0]:q[1] + 1])
    print(f"sum of {q[0]:>2}..{q[1]:>2} = {r[0]:>3} after {r[1]:>2} reads (check {brute})")
b.set(12, 20)
b.set(3, 0)
print(f"after two updates, block sums: {b.sums}")
r = b.range_sum(3, 17)
print(f"sum of 3..17 = {r[0]}")
