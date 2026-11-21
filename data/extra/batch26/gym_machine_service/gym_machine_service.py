hall = [("treadmill T1", 512, 500, None), ("treadmill T2", 230, 500, None), ("bike B1", 298, 300, None), ("rower R1", 120, 400, 950000), ("rower R2", 390, 400, 400000)]
def due(m):
    if m[3] is not None:
        return m[1] >= 400 or m[3] >= 900000
    return m[1] >= m[2]
def left(m):
    return m[2] - m[1]
for m in hall:
    if due(m):
        print(f"{m[0]}: service due at {m[1]} h")
    else:
        print(f"{m[0]}: {left(m)} h to go")
print(f"due now: {sum(1 for m in hall if due(m))} of {len(hall)}")
soonest = "none"; gap = 1000000
for m in hall:
    if not due(m) and left(m) < gap:
        gap = left(m); soonest = m[0]
print(f"next up: {soonest} in {gap} h")
