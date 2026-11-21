for t in ["12:34:56", "07:08:09", "23:59:59"]:
    D = [int(c) for c in t if c != ":"]; print(t)
    for b in [8, 4, 2, 1]:
        r = ""
        for i, d in enumerate(D): r += ("  " if i in (2, 4) else "" if i == 0 else " ") + ("o" if d & b else ".")
        print(f"{b} {r}")
