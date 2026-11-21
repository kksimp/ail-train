names = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

def name_of(k):
    return names[k % 12]

order = [(i * 7) % 12 for i in range(12)]
for day in range(4):
    parts = []
    for j in range(3):
        k = order[day * 3 + j]
        parts.append(f"{name_of(k)}/{name_of(k + 9)}m")
    print(f"day {day + 1}: {', '.join(parts)}")
pos = order.index(6)
days = [pos // 3 + 1 + 4 * c for c in range(3)]
print(f"F# major comes up on days [{', '.join(str(d) for d in days)}]")
print(f"first seven round the circle: {' '.join(name_of(k) for k in order[:7])}")
