P = [("fern", 2), ("cactus", 7), ("basil", 1), ("orchid", 4), ("ivy", 3)]; b = (0, 0)
for d in range(1, 15):
    due = [n for n, k in P if d % k == 0]
    if len(due) > b[1]: b = (d, len(due))
    print(f"day {d:>2}: {', '.join(due)}")
print(f"busiest: day {b[0]} with {b[1]} plants")
