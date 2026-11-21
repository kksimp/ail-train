trip = [("OSL", "AMS", 420, 525), ("AMS", "LIS", 610, 790), ("LIS", "PDL", 820, 955)]
hm = lambda m: f"{m // 60}h{m % 60:02d}"
for i in range(1, len(trip)):
    print(f"layover at {trip[i][0]}: {hm(trip[i][2] - trip[i - 1][3])}")
print(f"total {hm(trip[-1][3] - trip[0][2])}")
pr = []
for i in range(1, len(trip)):
    a, b = trip[i - 1], trip[i]
    if a[1] != b[0]: pr.append(f"{a[1]} is not {b[0]}")
    elif b[2] - a[3] < 45: pr.append(f"only {b[2] - a[3]} min at {a[1]}")
if not pr: print("all connections ok")
for p in pr: print(f"problem: {p}")
