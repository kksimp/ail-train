squad = ["Ari", "Bel", "Cas", "Dom", "Eve", "Flo", "Gus", "Hal"]
mins = [0] * 8

def pick(mins, k):
    return sorted(sorted(range(len(mins)), key=lambda i: (mins[i], i))[:k])

for block in range(5):
    on = pick(mins, 5)
    for i in on:
        mins[i] += 8
    start = block * 8
    print(f"block {block + 1} ({start}-{start + 8} min): {', '.join(squad[i] for i in on)}")
for i, name in enumerate(squad):
    print(f"{name}: {mins[i]} min")
print(f"spread between most and least: {max(mins) - min(mins)} min")
