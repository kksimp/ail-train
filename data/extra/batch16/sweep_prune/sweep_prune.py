boxes = [("ship", 10, 30, 5, 15), ("rock", 25, 35, 12, 20), ("buoy", 32, 34, 40, 42), ("gull", 28, 31, 14, 16), ("reef", 60, 90, 0, 10), ("boat", 85, 95, 8, 12), ("dock", 0, 8, 0, 50), ("kite", 70, 72, 30, 33)]
order = sorted(boxes, key=lambda b: b[1])
active = []
tests = 0
hits = []
for b in order:
    active = [a for a in active if a[2] >= b[1]]
    for a in active:
        tests += 1
        if a[3] <= b[4] and b[3] <= a[4]:
            hits.append(f"{a[0]}+{b[0]}")
    active.append(b)
n = len(boxes)
print(f"overlapping: {', '.join(hits)}")
print(f"y tests after the sweep: {tests}; every pair would be {n * (n - 1) // 2}")
