plants = [("fern", 2, 1), ("cactus", 7, 3), ("basil", 1, 5), ("orchid", 4, 2)]
def due(p, day):
    return day >= p[2] and (day - p[2]) % p[1] == 0
quiet = []
w = 0
for day in range(1, 15):
    names = [p[0] for p in plants if due(p, day)]
    w += len(names)
    if not names:
        quiet.append(day)
    else:
        print(f"day {day:>2}: {', '.join(names)}")
print("quiet days: " + " ".join(str(d) for d in sorted(quiet)))
print(f"waterings: {w}")
