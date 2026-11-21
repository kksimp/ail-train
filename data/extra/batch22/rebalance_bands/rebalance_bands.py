def check(names, values, targets):
    total = sum(values)
    worst = 0
    for i in range(len(values)):
        drift = abs(values[i] * 1000 // total - targets[i] * 10)
        worst = max(worst, drift)
    print(f"total {total}, largest drift {worst // 10}.{worst % 10} points")
    if worst <= 50:
        print("  inside the band: no trades")
        return
    for i in range(len(values)):
        goal = total * targets[i] // 100
        move = goal - values[i]
        verb = "buy" if move > 0 else "sell"
        print(f"  {names[i]:<8} {values[i]:>6} -> {goal:>6}: {verb} {abs(move)}")

names = ["equity", "bonds", "property", "cash"]
targets = [60, 25, 10, 5]
check(names, [61000, 24000, 10500, 4500], targets)
check(names, [72000, 20000, 9000, 4000], targets)
check(names, [55000, 31000, 9500, 4500], targets)
