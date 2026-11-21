class Dice:
    def __init__(self, seed):
        self.seed = seed
    def roll(self):
        self.seed = (self.seed * 1103515245 + 12345) % 2147483648
        a = (self.seed // 65536) % 6 + 1
        self.seed = (self.seed * 1103515245 + 12345) % 2147483648
        b = (self.seed // 65536) % 6 + 1
        return a + b

dice = Dice(4242)
bank = 100
wins = 0
for rnd in range(1, 10):
    first = dice.roll()
    won = False
    note = ""
    if first in (7, 11):
        won = True
        note = f"natural {first}"
    elif first in (2, 3, 12):
        note = f"craps {first}"
    else:
        rolls = 1
        r = dice.roll()
        while r != first and r != 7:
            rolls += 1
            r = dice.roll()
        won = r == first
        note = f"point {first}, settled after {rolls + 1} rolls"
    if won:
        bank += 10
        wins += 1
    else:
        bank -= 10
    result = "win" if won else "lose"
    print(f"round {rnd}: {note}: {result}, bank {bank}")
print(f"won {wins} of 9 rounds")
