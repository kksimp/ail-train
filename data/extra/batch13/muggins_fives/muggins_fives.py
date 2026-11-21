class End:
    def __init__(self, pip, double):
        self.pip = pip
        self.double = double
    def count(self):
        return self.pip * 2 if self.double else self.pip

plays = [(5, 5, "R"), (5, 0, "R"), (5, 3, "L"), (0, 4, "R"), (3, 3, "L"), (4, 6, "R"), (2, 3, "L"), (6, 1, "R"), (2, 2, "L")]
left = End(5, True)
right = End(5, True)
scores = [0, 0]
for i, play in enumerate(plays):
    a, b, side = play
    player = i % 2
    if i == 0:
        sum0 = a + b
        if sum0 % 5 == 0:
            scores[player] += sum0
        print(f"player {player + 1} leads {a}-{b}, ends add to {sum0}")
        continue
    end = left if side == "L" else right
    if a != end.pip and b != end.pip:
        print(f"{a}-{b} does not fit the {side} end")
        continue
    outer = b if a == end.pip else a
    end = End(outer, a == b)
    if side == "L":
        left = end
    else:
        right = end
    total = left.count() + right.count()
    note = ""
    if total % 5 == 0:
        scores[player] += total
        note = f", scores {total}"
    print(f"player {player + 1} plays {a}-{b} on {side}: ends add to {total}{note}")
print(f"scores: {scores[0]} and {scores[1]}")
