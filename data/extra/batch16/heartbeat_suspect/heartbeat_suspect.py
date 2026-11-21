def status(p, now):
    name, beats = p
    last = -1
    gap = 5
    for b in beats:
        if b <= now:
            if last >= 0:
                gap = max(gap, b - last)
            last = b
    timeout = 2 * gap
    silent = now - last
    verdict = "SUSPECT" if silent > timeout else "alive"
    return f"{name} {verdict:<7} silent {silent:>2}/{timeout:<2}"

peers = [("A", [0, 10, 20, 30, 40, 50, 60, 70, 80]), ("B", [0, 4, 8, 12, 30, 34, 38, 42, 46]), ("C", [0, 10, 20, 30]), ("D", [0, 3, 6, 9, 12, 15, 18, 40, 43, 46, 49])]
for now in [15, 25, 35, 55, 75, 90]:
    row = [status(p, now) for p in peers]
    print(f"t={now:>2}: {' | '.join(row)}")
