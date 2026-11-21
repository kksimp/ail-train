names = ["A", "B", "C"]
tickets = [100, 50, 25]
total = sum(tickets)
seed = 2026
wins = [0, 0, 0]
timeline = []
quanta = 70
for q in range(quanta):
    seed = (seed * 1103515245 + 12345) % 2147483648
    draw = (seed // 65536) % total
    acc = 0
    winner = 0
    for i in range(3):
        acc += tickets[i]
        if draw < acc:
            winner = i
            break
    wins[winner] += 1
    timeline.append(names[winner])
for k in range(0, len(timeline), 35):
    print("".join(timeline[k:k + 35]))
for i in range(3):
    expected = quanta * tickets[i] // total
    print(f"{names[i]}: {tickets[i]:>3} tickets, won {wins[i]:>2} slices, expected {expected}")
