import math

class Lcg:
    def __init__(self, state):
        self.state = state

    def step(self):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return self.state

def z_score(bits):
    n = len(bits)
    n1 = sum(bits)
    n0 = n - n1
    runs = 1
    for i in range(1, n):
        if bits[i] != bits[i - 1]:
            runs += 1
    mu = 2.0 * float(n1) * float(n0) / float(n) + 1.0
    var = (mu - 1.0) * (mu - 2.0) / float(n - 1)
    return (float(runs) - mu) / math.sqrt(var)

def report(name, bits):
    z = z_score(bits)
    verdict = "not random" if z > 1.96 or z < -1.96 else "looks random"
    print(f"{name:<22} ones {sum(bits):>3} of {len(bits)}  z = {z:>7.2f}  {verdict}")

a = Lcg(1)
high = [(a.step() >> 30) & 1 for i in range(400)]
b = Lcg(1)
low = [b.step() & 1 for i in range(400)]
c = Lcg(9)
sticky = []
last = 0
for i in range(400):
    if c.step() % 10 < 2:
        last = 1 - last
    sticky.append(last)
d = Lcg(5)
mid = [(d.step() >> 16) & 1 for i in range(400)]
report("LCG top bit", high)
report("LCG bit 16", mid)
report("LCG lowest bit", low)
report("flips 20% of the time", sticky)
