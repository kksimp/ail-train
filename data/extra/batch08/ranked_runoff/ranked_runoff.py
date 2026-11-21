cands = ["Ana", "Ben", "Cy", "Dee"]
groups = [(4, ["Ana", "Ben", "Cy", "Dee"]), (3, ["Ben", "Cy", "Ana", "Dee"]), (2, ["Cy", "Ben", "Ana", "Dee"]), (2, ["Dee", "Cy", "Ben", "Ana"])]
dropped = set(); rnd = 1
while True:
    counts = {c: 0 for c in cands if c not in dropped}
    for n, b in groups:
        for c in b:
            if c not in dropped: counts[c] += n; break
    live = [c for c in cands if c not in dropped]; total = sum(counts[c] for c in live); weak = ""
    for c in live:
        if weak == "" or counts[c] <= counts[weak]: weak = c
    print(f"round {rnd}: {', '.join(f'{c} {counts[c]}' for c in live)}")
    win = [c for c in live if counts[c] * 2 > total]
    if win: print(f"{win[0]} wins with a majority"); break
    print(f"  drop {weak}"); dropped.add(weak); rnd += 1
