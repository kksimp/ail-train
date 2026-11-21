def duel(ballots, a, b):
    margin = 0
    for count, order in ballots:
        ia = order.index(a) if a in order else 99
        ib = order.index(b) if b in order else 99
        if ia < ib:
            margin += count
        elif ib < ia:
            margin -= count
    return margin

def report(title, cands, ballots):
    halves = []
    winner = ""
    for a in cands:
        score = 0
        beaten = 0
        for b in cands:
            if a != b:
                m = duel(ballots, a, b)
                if m > 0:
                    score += 2
                    beaten += 1
                elif m == 0:
                    score += 1
        halves.append(score)
        if beaten == len(cands) - 1:
            winner = a
    order = sorted(range(len(cands)), key=lambda i: -halves[i])
    parts = [f"{cands[i]} {halves[i] // 2}{'.5' if halves[i] % 2 == 1 else ''}" for i in order]
    found = "no Condorcet winner" if winner == "" else f"Condorcet winner {winner}"
    print(f"{title}: {', '.join(parts)}; {found}")

lunch = [(4, ["pizza", "curry", "salad"]), (3, ["curry", "salad", "pizza"]), (2, ["salad", "curry", "pizza"])]
report("lunch", ["pizza", "curry", "salad"], lunch)
cycle = [(3, ["rock", "scissors", "paper"]), (3, ["paper", "rock", "scissors"]), (3, ["scissors", "paper", "rock"])]
report("cycle", ["rock", "paper", "scissors"], cycle)
trip = [(5, ["lake", "hills", "city", "coast"]), (4, ["coast", "city", "hills", "lake"]), (3, ["city", "hills", "coast", "lake"]), (2, ["hills", "lake", "city", "coast"]), (2, ["hills", "coast", "lake", "city"])]
report("trip", ["lake", "hills", "city", "coast"], trip)
print(f"pizza against curry: margin {duel(lunch, 'pizza', 'curry')}")
