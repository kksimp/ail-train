rows = [("ops", "Ada", 52), ("dev", "Bo", 70), ("dev", "Cy", 85), ("ops", "Di", 52), ("dev", "Ed", 70), ("ops", "Flo", 61), ("dev", "Gil", 64), ("ops", "Hal", 47)]
ordered = sorted(rows, key=lambda r: (r[0], -r[2], r[1]))
print("team name  pay  row rank running lag")
team = ""
row_no = 0
rank = 0
running = 0
prev_pay = 0
for t, name, pay in ordered:
    if t != team:
        team = t
        row_no = 0
        running = 0
        prev_pay = -1
    row_no += 1
    if pay != prev_pay:
        rank = row_no
    running += pay
    lag = "-" if row_no == 1 else f"{prev_pay - pay}"
    print(f"{t:<4} {name:<4} {pay:>4} {row_no:>4} {rank:>4} {running:>7} {lag:>3}")
    prev_pay = pay
