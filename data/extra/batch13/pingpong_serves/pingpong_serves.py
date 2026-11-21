def server(a, b, first):
    played = a + b
    turns = 10 + (played - 20) if a >= 10 and b >= 10 else played // 2
    return (first + turns) % 2

names = ["Rui", "Sam"]
games = ["ABBAABABBBAAABABABAAB", "ABABABABABABABABABABBAABAABB", "BBBBABBBBBABBB"]
for gi, points in enumerate(games):
    first = gi % 2
    a = b = 0
    order = []
    for p in points:
        if (a >= 11 or b >= 11) and abs(a - b) >= 2:
            break
        s = server(a, b, first)
        order.append(names[s][0])
        if p == 'A':
            a += 1
        else:
            b += 1
    winner = names[0] if a > b else names[1]
    shown = "".join(order)
    print(f"game {gi + 1}: {a}-{b} to {winner}")
    print(f"  servers {shown}")
