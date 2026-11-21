def rank_value(card):
    return "23456789TJQKA".find(card[0])

def winner(trick, trumps):
    led = trick[0][1]
    best = 0
    best_power = -1
    for i, card in enumerate(trick):
        suit = card[1]
        power = 100 + rank_value(card) if suit == trumps else (rank_value(card) if suit == led else -1)
        if power > best_power:
            best = i
            best_power = power
    return best

seats = ["North", "East", "South", "West"]
trumps = "S"
tricks = [["KH", "2H", "AH", "5H"], ["4D", "KD", "3S", "AD"], ["QC", "2C", "TC", "9C"], ["7H", "6H", "4S", "8H"], ["JD", "QD", "5D", "2S"], ["AS", "6S", "9S", "KS"]]
leader = 0
won = [0, 0]
for n, trick in enumerate(tricks):
    w = (leader + winner(trick, trumps)) % 4
    cards = " ".join(trick)
    print(f"trick {n + 1}: {seats[leader]} leads {cards}, {seats[w]} wins")
    won[w % 2] += 1
    leader = w
print(f"North-South {won[0]}, East-West {won[1]}")
