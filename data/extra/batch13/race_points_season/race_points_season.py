table = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
races = [("Bahrain", ["VER", "LEC", "HAM", "NOR", "SAI", "RUS", "PIA", "ALO", "OCO", "GAS", "STR", "TSU"], "LEC"), ("Imola", ["LEC", "VER", "NOR", "HAM", "PIA", "SAI", "ALO", "RUS", "GAS", "STR", "OCO", "TSU"], "TSU"), ("Monaco", ["NOR", "LEC", "VER", "PIA", "HAM", "RUS", "SAI", "GAS", "ALO", "OCO", "TSU", "STR"], "NOR"), ("Suzuka", ["VER", "NOR", "LEC", "PIA", "SAI", "HAM", "RUS", "ALO", "TSU", "GAS", "OCO", "STR"], "HAM")]
points = {}
wins = {}
for name, order, fastest in races:
    for i, d in enumerate(order):
        points[d] = points.get(d, 0) + (table[i] if i < 10 else 0)
    wins[order[0]] = wins.get(order[0], 0) + 1
    place = order.index(fastest) if fastest in order else 99
    extra = " (+1)" if place < 10 else " (no point)"
    if place < 10:
        points[fastest] += 1
    print(f"{name:<8} won by {order[0]}, fastest lap {fastest}{extra}")
ranked = sorted(points.keys(), key=lambda d: (-points[d], -wins.get(d, 0)))
for i, d in enumerate(ranked):
    if i < 6:
        print(f"{i + 1}. {d} {points[d]:>3} pts, {wins.get(d, 0)} wins")
