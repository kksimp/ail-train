def next_state(s):
    return (s * 1103515245 + 12345) % 2147483648

s = 4242
bank, bet, streak, worst, spins, capped = 1000, 10, 0, 0, 0, 0
while spins < 60 and bank > 0:
    spins += 1
    stake = min(bet, bank)
    s = next_state(s)
    pocket = (s >> 16) % 37
    if pocket < 18:
        bank += stake
        bet = 10
        streak = 0
    else:
        bank -= stake
        streak += 1
        worst = max(worst, streak)
        bet = stake * 2
        if bet > 320:
            bet = 320
            capped += 1
    if spins % 10 == 0:
        print(f"after {spins} spins: bank {bank}, next bet {bet}")
print(f"stopped after {spins} spins with {bank}")
print(f"longest losing run {worst}; table limit hit {capped} times")
