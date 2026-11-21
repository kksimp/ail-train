orders = [(101, "post", 12, 960), (102, "express", 8, 840), (103, "post", 15, 960), (104, "courier", 20, 900), (105, "express", 14, 840), (106, "post", 9, 960), (107, "courier", 6, 900), (108, "express", 11, 840), (109, "post", 7, 960), (110, "courier", 13, 900)]

def clock(m):
    return f"{m // 60:02d}:{m % 60:02d}"

by_carrier = {}
for o in sorted(orders, key=lambda o: (o[3], o[0])):
    by_carrier.setdefault(o[1], []).append(o)
wave = 0
for carrier, group in by_carrier.items():
    ids = []
    lines = 0
    for i, o in enumerate(group):
        if lines + o[2] > 30:
            wave += 1
            print(f"wave {wave}: {carrier} by {clock(o[3])}, orders {ids}, {lines} lines")
            ids = []
            lines = 0
        ids.append(o[0])
        lines += o[2]
        if i == len(group) - 1:
            wave += 1
            print(f"wave {wave}: {carrier} by {clock(o[3])}, orders {ids}, {lines} lines")
print(f"{wave} waves for {len(orders)} orders")
