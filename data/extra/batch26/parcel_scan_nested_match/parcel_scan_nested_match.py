def say(s):
    k, p = s
    if k == "out": return f"out for delivery on van {p}"
    pk = p[0]
    if k == "at":
        if pk == "depot": return f"sorted at depot {p[1]}"
        if pk == "locker": return f"waiting in locker {p[1]}"
        return "left at the door, unsigned"
    if pk == "door": return "delivered to the door"
    if pk == "locker": return f"collected from locker {p[1]}"
    return "collected at the depot"
parcels = [
    ("P1", [("at", ("depot", "LHR2")), ("out", 14), ("done", ("door",))]),
    ("P2", [("at", ("depot", "MAN1")), ("at", ("locker", 31)), ("done", ("locker", 31))]),
    ("P3", [("at", ("depot", "BRS1")), ("out", 9)]),
    ("P4", [("at", ("depot", "LHR2")), ("at", ("locker", 7))]),
    ("P5", [("at", ("depot", "GLA3")), ("out", 2), ("at", ("door",))]),
]
done = 0
for i, sc in parcels:
    last = sc[-1]
    if last[0] == "done": done += 1
    print(f"{i} ({len(sc)} scans): {say(last)}")
print(f"{done} of {len(parcels)} parcels finished")
