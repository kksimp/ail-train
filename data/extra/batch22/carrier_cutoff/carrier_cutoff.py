orders = [(1, 25, "ground", 1020), (2, 15, "express", 870), (3, 30, "ground", 1020), (4, 10, "express", 870), (5, 20, "freight", 960), (6, 35, "ground", 1020), (7, 15, "express", 870), (8, 25, "freight", 960)]

def clock(m):
    return f"{m // 60:02d}:{m % 60:02d}"

def pack(orders, show):
    t = 780
    missed = 0
    for oid, minutes, carrier, cutoff in orders:
        t += minutes
        late = t > cutoff
        if late:
            missed += 1
        if show or late:
            note = "misses" if late else "makes"
            print(f"  order {oid} ({carrier}) done {clock(t)}, {note} the {clock(cutoff)} collection")
    return missed

print("arrival order, late orders only:")
first = pack(orders, False)
print("earliest cutoff first:")
second = pack(sorted(orders, key=lambda o: o[3]), True)
print(f"missed: {first} in arrival order, {second} by cutoff")
