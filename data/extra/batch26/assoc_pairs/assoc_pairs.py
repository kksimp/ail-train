plugs = {}
for k, v in [("UK", "G"), ("DE", "F"), ("US", "A"), ("IT", "L"), ("US", "B")]:
    plugs[k] = v
for c in ["UK", "DE", "JP", "US"]:
    print(f"{c}: plug type {plugs.get(c, '?')}")
print(f"{len(plugs)} countries known")
rooms = {}
for k, v in [(101, "Osei"), (102, "Lind"), (101, "Park")]:
    rooms[k] = v
for r in [101, 102, 103]:
    print(f"room {r}: {rooms.get(r, 'empty')}")
