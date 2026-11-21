def grow(start, days):
    b = [0] * 7
    for t in start:
        b[t] += 1
    for _ in range(days):
        born = b[0]
        for i in range(6):
            b[i] = b[i + 1]
        b[6] = born
        b[4] += born
    return sum(b)

school = [3, 1, 4, 1, 2, 0, 4]
print(f"{len(school)} glowfish at the start")
for d in [5, 10, 20]:
    print(f"after {d} days: {grow(school, d)}")
print(f"part 1: after 30 days: {grow(school, 30)}")
print(f"part 2: after 150 days: {grow(school, 150)}")
