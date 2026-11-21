people = [("Ann", 0, 5, 3), ("Ben", 1, 4, 2), ("Cal", 2, 6, 1), ("Dee", 3, 3, 3), ("Eve", 4, 2, 2), ("Fay", 9, 4, 1), ("Gus", 10, 3, 4), ("Hal", 12, 5, 0), ("Ivy", 24, 2, 0)]
finishes = []
free = 0
lost = 0
for name, arrive, service, accept in people:
    ahead = sum(1 for f in finishes if f > arrive)
    if ahead > accept:
        lost += 1
        print(f"{name} at {arrive:>2}: {ahead} ahead, walks away")
        continue
    start = max(arrive, free)
    free = start + service
    finishes.append(free)
    print(f"{name} at {arrive:>2}: {ahead} ahead, served {start:>2}-{free:>2}")
print(f"served {len(finishes)}, lost {lost}, clerk done at {free}")
