def over(a, b):
    lead = abs(a - b)
    return a == 30 or b == 30 or ((a >= 21 or b >= 21) and lead >= 2)

names = ["Lin", "Mei"]
seed = 808
games = [0, 0]
number = 0
while games[0] < 2 and games[1] < 2:
    number += 1
    a = b = 0
    longest = 0
    run = 0
    last = -1
    while not over(a, b):
        seed = (seed * 1103515245 + 12345) % 2147483648
        winner = 0 if (seed // 65536) % 100 < 52 else 1
        if winner == 0:
            a += 1
        else:
            b += 1
        run = run + 1 if winner == last else 1
        last = winner
        longest = max(longest, run)
    w = 0 if a > b else 1
    games[w] += 1
    print(f"game {number}: {a}-{b} to {names[w]}, longest run {longest}")
champion = names[0] if games[0] == 2 else names[1]
print(f"{champion} wins {max(games)}-{min(games)}")
