def card(rounds):
    a = b = 0
    for r in rounds:
        if r == 'A':
            a += 10; b += 9
        elif r == 'B':
            a += 9; b += 10
        elif r == 'a':
            a += 10; b += 8
        elif r == 'b':
            a += 8; b += 10
        else:
            a += 10; b += 10
    return [a, b]

def decision(wa, wb, draws):
    if wa == 3 or wb == 3:
        return "unanimous decision"
    if (wa == 2 or wb == 2) and draws == 1:
        return "majority decision"
    if wa == 2 or wb == 2:
        return "split decision"
    if draws == 3:
        return "unanimous draw"
    if draws == 2:
        return "majority draw"
    return "split draw"

fights = [("Ortiz", "Banks", ["AABBAaABBAAB", "AABBABABBAAB", "ABBBAaABBBAB"]), ("Cole", "Diaz", ["ABABAB=BABAB", "AAABBBbAAABB", "ABAB=BABA=BA"])]
for red, blue, cards in fights:
    wins = [0, 0, 0]
    for c in cards:
        s = card(c)
        winner = red if s[0] > s[1] else (blue if s[1] > s[0] else "even")
        print(f"  {s[0]}-{s[1]} {winner}")
        if s[0] > s[1]:
            wins[0] += 1
        elif s[1] > s[0]:
            wins[1] += 1
        else:
            wins[2] += 1
    leader = red if wins[0] > wins[1] else (blue if wins[1] > wins[0] else "nobody")
    result = decision(wins[0], wins[1], wins[2])
    if wins[0] == wins[1]:
        print(f"{red} v {blue}: {result}")
    else:
        print(f"{red} v {blue}: {leader} by {result}")
