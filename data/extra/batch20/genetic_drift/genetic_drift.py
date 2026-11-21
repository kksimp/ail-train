class Rng:
    def __init__(self, s):
        self.state = s
    def uniform(self):
        self.state = (self.state * 1103515245 + 12345) % 2147483648
        return float(self.state) / 2147483648.0

def drift(n, p0, gens, rng):
    p = p0
    path = [p]
    for _ in range(gens):
        hits = 0
        for c in range(2 * n):
            if rng.uniform() < p:
                hits += 1
        p = float(hits) / float(2 * n)
        path.append(p)
    return path

rng = Rng(7)
for n in [5, 25, 250]:
    path = drift(n, 0.5, 100, rng)
    marks = " ".join(f"{path[g]:.2f}" for g in [0, 10, 20, 40, 60, 80, 100])
    fixed = [g for g in range(len(path)) if path[g] == 0.0 or path[g] == 1.0]
    ending = "both alleles remain" if not fixed else f"settled at generation {fixed[0]}"
    print(f"N {n:>3}: {marks} ({ending})")
