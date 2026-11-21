rooms = [("Harbour View", 120, 4), ("Old Mill", 95, 3), ("Garden Suite", 120, 5), ("Station Inn", 95, 3), ("Loft 9", 140, 5)]
key = lambda r: (r[1], -r[2], r[0])
s = sorted(rooms, key=key)
for i, r in enumerate(s): print(f"{i + 1}. {r[0]:<13} {r[1]:>4} {'*' * r[2]}")
print(f"first pick: {s[0][0]}")
print(f"Garden Suite before Harbour View: {str(key(rooms[2]) < key(rooms[0])).lower()}")
print(f"within 110: {', '.join(r[0] for r in rooms if r[1] <= 110)}")
