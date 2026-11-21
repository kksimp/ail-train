rooms = {101: [2, 3], 102: [2, 3], 103: [2, 3]}
for room, kind in [(101, "water"), (102, "snacks"), (101, "water"), (103, "water"), (101, "snacks")]:
    rooms[room][0 if kind == "water" else 1] -= 1
for room, (w, s) in rooms.items():
    c = (2 - w) * 250 + (3 - s) * 400
    print(f"room {room}: water {w}, snacks {s}, charge {c // 100}.{c % 100:02}")
print(f"restocked copy has 3 snacks, room 102 still {rooms[102][1]}")
rooms[102][1] = 3
print(f"after storing it back room 102 has {rooms[102][1]}")
