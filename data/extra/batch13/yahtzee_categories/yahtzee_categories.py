NAMES = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "ThreeKind", "FourKind", "FullHouse", "SmallStraight", "LargeStraight", "Yahtzee", "Chance"]

def counts(dice):
    c = [0] * 7
    for d in dice:
        c[d] += 1
    return c

def has_run(c, n):
    run = 0
    for f in range(1, 7):
        if c[f] > 0:
            run += 1
            if run >= n:
                return True
        else:
            run = 0
    return False

def score(b, dice):
    c = counts(dice)
    total = sum(dice)
    most = max(c)
    if b < 6:
        return c[b + 1] * (b + 1)
    name = NAMES[b]
    if name == "ThreeKind":
        return total if most >= 3 else 0
    if name == "FourKind":
        return total if most >= 4 else 0
    if name == "FullHouse":
        return 25 if 3 in c and 2 in c else 0
    if name == "SmallStraight":
        return 30 if has_run(c, 4) else 0
    if name == "LargeStraight":
        return 40 if has_run(c, 5) else 0
    if name == "Yahtzee":
        return 50 if most == 5 else 0
    return total

rolls = [[3, 3, 3, 5, 5], [1, 2, 3, 4, 6], [2, 3, 4, 5, 6], [6, 6, 6, 6, 2], [4, 4, 4, 4, 4], [1, 1, 2, 5, 6], [6, 5, 6, 2, 6]]
for r in rolls:
    best = 0
    top = -1
    for b in range(13):
        s = score(b, r)
        if s > top:
            best = b
            top = s
    shown = " ".join(str(x) for x in r)
    print(f"{shown}: {NAMES[best]} for {top}, chance {score(12, r)}")
