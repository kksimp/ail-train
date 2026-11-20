class Lcg:
    def __init__(self, s): self.s = s
    def next(self):
        self.s = (self.s * 1103515245 + 12345) % 2147483648
        return self.s
    def below(self, n): return self.next() % n
def shuffle(xs, seed):
    out = list(xs); r = Lcg(seed); i = len(out) - 1
    while i > 0:
        j = r.below(i + 1)
        out[i], out[j] = out[j], out[i]; i -= 1
    return out
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for seed in [1, 42, 2024]:
    print(f"seed {seed}: " + " ".join(shuffle(deck, seed)))
print("repeatable: true")
r = Lcg(99)
print(" ".join(str(r.below(100)) for _ in range(5)))
