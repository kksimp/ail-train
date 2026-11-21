plots = {}
holders = [(1, 1, "Ada"), (1, 2, "Ben"), (1, 4, "Cara"), (2, 1, "Dev"), (2, 3, "Eve"), (3, 2, "Finn"), (3, 3, "Gus"), (3, 4, "Hal")]
for r, c, n in holders: plots[(r, c)] = n
vac = lambda: [(r, c) for r in range(1, 4) for c in range(1, 5) if (r, c) not in plots]
print(f"{len(plots)} of 12 plots taken, {len(vac())} vacant")
for who, friend in [("Ines", "Eve"), ("Jon", "Ada"), ("Kim", "Hal")]:
    free = vac(); pick = free[0]; found = False
    for f in free:
        for fr, fc, n in holders:
            if not found and n == friend and abs(f[0] - fr) + abs(f[1] - fc) == 1:
                pick = f; found = True
    plots[pick] = who
    print(f"{who} gets plot {pick[0]}-{pick[1]}, {'next to' if found else 'away from'} {friend}")
print(f"still vacant: {', '.join(f'{a}-{b}' for a, b in vac())}")
