class Lcg:
    def __init__(self, state):
        self.state = state

    def next(self):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return self.state >> 4

def bump(c, rng):
    for i in range(len(c)):
        if rng.next() % (1 << c[i]) == 0:
            c[i] += 1

rng = Lcg(4242)
regs = [0, 0, 0, 0, 0, 0, 0, 0]
events = 0
for stop in [10, 100, 1000, 10000, 50000]:
    while events < stop:
        bump(regs, rng)
        events += 1
    ests = [(1 << c) - 1 for c in regs]
    avg = sum(ests) // len(ests)
    print(f"{events:>5} events: registers {regs}, mean estimate {avg}")
top = max(regs)
print(f"largest register {top} fits in 5 bits; an exact count of {events} needs 16")
