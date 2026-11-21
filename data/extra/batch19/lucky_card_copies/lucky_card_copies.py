def matches(line):
    a, b = line.split(": ")[1].split(" | ")
    wins = [int(t) for t in a.split()]
    return sum(1 for n in (int(t) for t in b.split()) if n in wins)

cards = ["Card 1: 5 17 23 | 17 8 5 30 23 2", "Card 2: 9 14 40 | 1 2 3 14 9", "Card 3: 3 6 11 | 7 8 10 12 13", "Card 4: 21 22 33 | 33 1 5 9 2", "Card 5: 2 4 8 | 4 5 6 7 9", "Card 6: 10 19 31 | 3 11 12 15 16"]
ks = [matches(c) for c in cards]
points = 0
for i, k in enumerate(ks):
    p = 0 if k == 0 else 1 << (k - 1)
    print(f"card {i + 1}: {k} matches, {p} points")
    points += p
print(f"part 1: {points} points")
copies = [1 for k in ks]
for i in range(len(ks)):
    for j in range(i + 1, min(i + 1 + ks[i], len(ks))):
        copies[j] += copies[i]
print(f"copies held: {copies}")
print(f"part 2: {sum(copies)} cards in all")
