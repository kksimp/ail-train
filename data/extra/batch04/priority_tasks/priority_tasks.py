R = {"Urgent": 0, "High": 1, "Normal": 2, "Low": 3}
T = [("fix login", "Urgent", 3), ("write docs", "Low", 2), ("review PR", "High", 1), ("plan sprint", "Normal", 2), ("patch server", "Urgent", 2), ("tidy backlog", "Normal", 3), ("team lunch", "Low", 1)]
left = 8; d = []
for n, p, h in sorted(T, key=lambda t: (R[t[1]], t[2], t[0])):
    if h <= left: left -= h; print(f"do {n} ({h}h, {p})")
    else: d.append(n)
print(f"spare {left}h, deferred: {', '.join(d)}")
