tutors = [("Ines", "maths", True), ("Omar", "maths", False), ("Kofi", "physics", True), ("Lena", "chemistry", False), ("Tom", "physics", True)]
rooms = {"Ines": "B12", "Kofi": "A7", "Omar": "C3"}
helped = 0
for subj in ["maths", "physics", "chemistry", "history"]:
    avail = [t for t in tutors if t[1] == subj and t[2]]
    who = avail[0][0] if avail else "nobody"
    room = rooms.get(who, "-")
    if who != "nobody":
        helped += 1
    print(f"{subj:<10} {who:<7} room {room} ({len(avail)} free)")
print(f"subjects covered: {helped} of 4")
print(f"first busy tutor: {next(t[0] for t in tutors if not t[2])}")
print(f"Tom meets students in the {rooms.get('Tom', 'staff room')}")
