def next_state(s):
    return (s * 1103515245 + 12345) % 2147483648

class Shoe:
    def __init__(self, seed):
        self.cards = []
        self.pos = 0
        self.seed = seed
    def draw(self):
        if self.pos == 0:
            self.cards = list(range(30))
            i = 29
            while i > 0:
                self.seed = next_state(self.seed)
                j = (self.seed >> 16) % (i + 1)
                self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
                i -= 1
        c = self.cards[self.pos]
        self.pos = (self.pos + 1) % 30
        return c

colours = "RGBYP"
players = [("Ada", 2), ("Ben", 3), ("Cy", 4), ("Di", 5)]
shoe = Shoe(12)
totals = [0, 0, 0, 0]
for rnd in range(1, 3):
    for p, (name, stop) in enumerate(players):
        held = set()
        shown = []
        sum_v = 0
        bust = False
        while len(shown) < stop:
            c = shoe.draw()
            col = c // 6
            shown.append(f"{colours[col]}{c % 6 + 1}")
            if col in held:
                bust = True
                break
            held.add(col)
            sum_v += c % 6 + 1
        pts = 0 if bust else sum_v
        totals[p] += pts
        print(f"round {rnd} {name:<3} {' '.join(shown):<14} -> {pts}")
for p, (name, stop) in enumerate(players):
    print(f"{name} stops at {stop}: {totals[p]} points")
