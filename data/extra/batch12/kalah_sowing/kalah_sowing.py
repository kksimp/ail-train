def on_side(player, pos):
    if player == 0:
        return pos < 6
    return pos >= 7 and pos < 13

def sow(pits, player, choice):
    start = choice if player == 0 else 7 + choice
    store = 6 if player == 0 else 13
    skip = 13 if player == 0 else 6
    seeds = pits[start]
    pits[start] = 0
    pos = start
    while seeds > 0:
        pos = (pos + 1) % 14
        if pos != skip:
            pits[pos] += 1
            seeds -= 1
    if pos == store:
        return True
    if on_side(player, pos) and pits[pos] == 1:
        opp = 12 - pos
        if pits[opp] > 0:
            pits[store] += pits[opp] + 1
            pits[opp] = 0
            pits[pos] = 0
    return False

def show(pits):
    a = " ".join(str(x) for x in pits[0:6])
    b = " ".join(str(x) for x in pits[7:13])
    return f"A {a} [{pits[6]}]  B {b} [{pits[13]}]"

pits = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
moves = [2, 3, 0, 5, 1, 4, 2, 0, 3, 5, 1, 4]
players = ["A", "B"]
turn = 0
for m in moves:
    base = 0 if turn == 0 else 7
    pick = m
    while pits[base + pick] == 0:
        pick = (pick + 1) % 6
    again = sow(pits, turn, pick)
    note = ", goes again" if again else ""
    print(f"{players[turn]} sows pit {pick + 1}{note}: {show(pits)}")
    if not again:
        turn = 1 - turn
