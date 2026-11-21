etas = [2, 7, 12, 20]; dep = 0
for m in range(1, 7):
    etas = [e - 1 for e in etas]
    while etas and etas[0] <= 0:
        etas.pop(0); dep += 1
        print(f"minute {m}: a bus has left the stop")
    if m % 3 == 0:
        etas.append((etas[-1] if etas else 0) + 8)
    print(f"minute {m}: due in {etas}")
print(f"{dep} departed, next in {etas[0]} min")
