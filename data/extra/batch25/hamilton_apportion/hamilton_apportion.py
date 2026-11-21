def hamilton(people, house):
    total = sum(people)
    seats = [p * house // total for p in people]
    rems = [p * house % total for p in people]
    left = house - sum(seats)
    order = sorted(range(len(people)), key=lambda i: -rems[i])
    for k in range(left):
        seats[order[k]] += 1
    return seats

def show(xs):
    return "[" + ", ".join(str(x) for x in xs) + "]"

names = ["Avon", "Bale", "Crane", "Dorn"]
people = [6000, 6000, 2000, 1000]
prev = []
for house in range(10, 15):
    seats = hamilton(people, house)
    notes = []
    if prev:
        for i in range(len(names)):
            if seats[i] < prev[i]:
                notes.append(f"{names[i]} loses a seat")
    note = "" if not notes else " <- " + ", ".join(notes)
    print(f"house {house}: {show(seats)}{note}")
    prev = seats
print(f"populations {show(people)}")
