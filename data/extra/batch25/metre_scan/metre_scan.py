def fit(stress, foot):
    hits = 0
    for i in range(len(stress)):
        if stress[i] == foot[i % len(foot)]:
            hits += 1
    return hits

feet = [("iambic", "01"), ("trochaic", "10"), ("anapaestic", "001"), ("dactylic", "100")]
counts = ["", "monometer", "dimeter", "trimeter", "tetrameter", "pentameter", "hexameter"]
lines = [("Shall I compare thee to a summer's day", "0101010101"), ("Tyger Tyger burning bright", "1010101"), ("Twas the night before Christmas and all through the house", "001001001001"), ("This is the forest primeval the murmuring pines and the hemlocks", "10010010010010010"), ("Because I could not stop for Death", "01010101"), ("Double double toil and trouble", "10101010"), ("The Assyrian came down like the wolf on the fold", "001001001001")]
for text, stress in lines:
    best = 0
    best_hits = -1
    for i, f in enumerate(feet):
        h = fit(stress, f[1])
        if h > best_hits:
            best = i
            best_hits = h
    size = len(feet[best][1])
    n = (len(stress) + size - 1) // size
    print(text)
    print(f"    {stress} {feet[best][0]} {counts[n]} ({best_hits}/{len(stress)})")
