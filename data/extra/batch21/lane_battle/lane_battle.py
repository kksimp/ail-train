def lane_totals(cards):
    out = [[0, 0], [0, 0], [0, 0]]
    for v, lane in cards:
        out[lane][0] += v
        out[lane][1] += 1
    return out

def lane_winner(a, b):
    if a[0] != b[0]:
        return 0 if a[0] > b[0] else 1
    if a[1] != b[1]:
        return 0 if a[1] < b[1] else 1
    return -1

matches = [([[9, 0], [2, 0], [7, 1], [3, 1], [8, 2], [1, 2]], [[6, 0], [4, 0], [10, 1], [5, 2], [3, 2], [2, 2]]), ([[10, 0], [9, 1], [1, 1], [4, 2], [3, 2], [2, 2]], [[5, 0], [5, 0], [6, 1], [4, 1], [8, 2], [1, 2]]), ([[6, 0], [6, 1], [6, 2], [1, 0], [1, 1], [1, 2]], [[7, 0], [5, 1], [3, 2], [4, 2], [2, 1], [2, 1]])]
names = ["Ash", "Bay"]
for m, game in enumerate(matches):
    a = lane_totals(game[0])
    b = lane_totals(game[1])
    won = [0, 0]
    parts = []
    for lane in range(3):
        w = lane_winner(a[lane], b[lane])
        label = "drawn" if w < 0 else names[w]
        if w >= 0:
            won[w] += 1
        parts.append(f"lane {lane + 1} {a[lane][0]}-{b[lane][0]} {label}")
    result = names[0] if won[0] >= 2 else (names[1] if won[1] >= 2 else "nobody")
    print(f"match {m + 1}: {', '.join(parts)}; winner {result}")
