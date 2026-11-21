known = [(150.0, 7.0, "apple"), (170.0, 7.5, "apple"), (140.0, 6.8, "apple"), (130.0, 6.0, "lemon"), (110.0, 5.8, "lemon"), (120.0, 5.5, "lemon"), (300.0, 9.5, "grapefruit"), (330.0, 10.0, "grapefruit"), (280.0, 9.0, "grapefruit")]
for g, c in [(160.0, 7.2), (115.0, 5.6), (290.0, 9.6), (135.0, 6.4), (220.0, 8.2)]:
    d = [(((k[0] - g) / 100.0) ** 2 + (k[1] - c) ** 2) ** 0.5 for k in known]
    near = sorted(range(len(known)), key=lambda i: int(d[i] * 1000000.0))
    names = [known[near[j]][2] for j in range(3)]; votes = {}
    for n in names: votes[n] = votes.get(n, 0) + 1
    pick = names[0]
    for n in names:
        if votes[n] > votes[pick]: pick = n
    print(f"{g:.0f} g, {c:.1f} cm: neighbours {', '.join(names)} -> {pick}")
