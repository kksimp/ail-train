class Token:
    def __init__(self, name, start, pos):
        self.name, self.start, self.pos = name, start, pos
    def square(self):
        return (self.start + self.pos) % 52

tokens = [Token("Red", 0, -1), Token("Green", 13, -1), Token("Yellow", 26, -1), Token("Blue", 39, -1)]
safe = [0, 13, 26, 39]
seed = 5
turn = 0
winner = -1
while winner < 0 and turn < 200:
    p = turn % 4
    turn += 1
    seed = (seed * 1103515245 + 12345) % 2147483648
    roll = (seed // 65536) % 6 + 1
    if tokens[p].pos < 0:
        if roll == 6:
            tokens[p].pos = 0
        continue
    if tokens[p].pos + roll > 56:
        continue
    tokens[p].pos += roll
    if tokens[p].pos == 56:
        winner = p
        break
    if tokens[p].pos > 50:
        continue
    sq = tokens[p].square()
    for q in range(4):
        if q != p and tokens[q].pos >= 0 and tokens[q].pos <= 50 and tokens[q].square() == sq and sq not in safe:
            print(f"turn {turn}: {tokens[p].name} lands on square {sq} and sends {tokens[q].name} home")
            tokens[q].pos = -1
print(f"{tokens[winner].name} reaches home on turn {turn}")
for t in tokens:
    where_now = "waiting" if t.pos < 0 else ("home stretch" if t.pos > 50 else f"square {t.square()}")
    print(f"{t.name:<6} {where_now}")
