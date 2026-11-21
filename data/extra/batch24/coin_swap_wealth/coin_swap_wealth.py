state = 2024
def pick(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def top_share(coins):
    best = sorted(coins, reverse=True)
    return (best[0] + best[1] + best[2]) * 100 // sum(coins)
coins = [10] * 12
for rnd in range(1, 301):
    for giver in range(12):
        if coins[giver] > 0:
            taker = pick(11)
            if taker >= giver: taker += 1
            coins[giver] -= 1
            coins[taker] += 1
    if rnd % 60 == 0:
        broke = coins.count(0)
        print(f"round {rnd:>3}: richest {max(coins)}, broke {broke}, top three hold {top_share(coins)}%")
print(f"final purses: {sorted(coins, reverse=True)}")
