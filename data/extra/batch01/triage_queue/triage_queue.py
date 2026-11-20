arrivals = [("Ray", 3), ("Sue", 1), ("Tim", 2), ("Una", 1), ("Vic", 3), ("Wes", 2)]
ps = sorted((u, i, n) for i, (n, u) in enumerate(arrivals))
print(f"waiting: {len(ps)}")
print(f"next: {ps[0][2]}")
for slot, (u, i, n) in enumerate(ps, 1):
    print(f"{slot}. {n} (urgency {u}, arrived {i + 1})")
print("empty: true")
print(sorted([5, 1, 4, 1]))
