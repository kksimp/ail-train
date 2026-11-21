def parse(s):
    return ("A23456789TJQK".find(s[0]) + 1, s[1])

def red(c):
    return c[1] in "HD"

def fits_on(c, top):
    if top == "":
        return c[0] == 13
    t = parse(top)
    return red(t) != red(c) and t[0] == c[0] + 1

columns = ["9S", "", "QH", "4D", "7C", "8D"]
foundation = {'H': 2, 'S': 0, 'D': 3, 'C': 1}
moving = ["8H", "KC", "3S", "4H", "JS", "2C", "AS", "6S"]
for m in moving:
    c = parse(m)
    spots = []
    for i, top in enumerate(columns):
        if fits_on(c, top):
            spots.append(f"column {i + 1}")
    if foundation.get(c[1], 0) == c[0] - 1:
        spots.append("foundation")
    where = "nowhere" if not spots else ", ".join(spots)
    print(f"{m}: {where}")
