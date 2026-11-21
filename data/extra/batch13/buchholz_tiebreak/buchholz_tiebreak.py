def half(n):
    return f"{n // 2}" if n % 2 == 0 else f"{n // 2}.5"

players = ["Anand", "Botez", "Caruana", "Ding", "Erigaisi", "Firouzja"]
games = [[0, 1, 2], [2, 3, 1], [4, 5, 0], [0, 2, 1], [1, 4, 2], [3, 5, 2], [0, 3, 0], [1, 5, 1], [2, 4, 2]]
score = [0] * 6
for g in games:
    score[g[0]] += g[2]
    score[g[1]] += 2 - g[2]
buch = [0] * 6
sb = [0] * 6
for g in games:
    a, b = g[0], g[1]
    buch[a] += score[b]
    buch[b] += score[a]
    sb[a] += score[b] * g[2]
    sb[b] += score[a] * (2 - g[2])
order = sorted(range(6), key=lambda i: (-score[i], -buch[i], -sb[i]))
print("player     pts  buch  SB")
for i in order:
    print(f"{players[i]:<9} {half(score[i]):>4} {half(buch[i]):>5} {half(sb[i] // 2):>4}")
