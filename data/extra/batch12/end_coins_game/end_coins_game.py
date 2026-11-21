def lead_table(coins):
    n = len(coins)
    d = [[coins[i] if i == j else 0 for j in range(n)] for i in range(n)]
    for gap in range(1, n):
        for i in range(0, n - gap):
            j = i + gap
            d[i][j] = max(coins[i] - d[i + 1][j], coins[j] - d[i][j - 1])
    return d

coins = [5, 3, 7, 10, 2, 14, 6, 1]
d = lead_table(coins)
print(f"coins {coins}; first player can lead by {d[0][len(coins) - 1]}")
i = 0
j = len(coins) - 1
score = [0, 0]
turn = 0
names = ["Ada", "Ben"]
while i <= j:
    take_left = i == j or coins[i] - d[i + 1][j] >= coins[j] - d[i][j - 1]
    if take_left:
        print(f"{names[turn]} takes {coins[i]} from the left")
        score[turn] += coins[i]
        i += 1
    else:
        print(f"{names[turn]} takes {coins[j]} from the right")
        score[turn] += coins[j]
        j -= 1
    turn = 1 - turn
print(f"final: Ada {score[0]}, Ben {score[1]}")
