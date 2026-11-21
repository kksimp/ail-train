parts = [("warehouse", lambda q, c: q <= 12), ("wallet", lambda q, c: q * c <= 500), ("courier", lambda q, c: q <= 8)]
orders = [(5, 40), (10, 30), (6, 90), (8, 60), (3, 200)]
done = 0
for qty, cost in orders:
    votes = []
    yes = True
    for name, rule in parts:
        v = rule(qty, cost)
        votes.append(f"{name} {'yes' if v else 'no'}")
        if not v:
            yes = False
    decision = "COMMIT" if yes else "ABORT"
    if yes:
        done += 1
    print(f"order {qty} x {cost}: {', '.join(votes)} -> {decision}")
print(f"{done} of {len(orders)} orders committed")
