names = ["Ali", "Bea", "Cai", "Dom", "Eva", "Fay", "Gus", "Hana"]
bad = {"Ali|Bea", "Bea|Cai", "Cai|Dom", "Ali|Cai", "Eva|Fay", "Dom|Eva", "Fay|Gus"}
seats = [""] * 8
used = set()
tries = [0]

def clash(a, b):
    return f"{a}|{b}" in bad or f"{b}|{a}" in bad

def place(i):
    if i == len(seats):
        return True
    for n in names:
        if n in used:
            continue
        if i % 4 != 0 and clash(seats[i - 1], n):
            continue
        tries[0] += 1
        seats[i] = n
        used.add(n)
        if place(i + 1):
            return True
        used.remove(n)
        seats[i] = ""
    return False

if place(0):
    print(f"front: {'  '.join(seats[0:4])}")
    print(f"back:  {'  '.join(seats[4:8])}")
    print(f"placed after {tries[0]} tries")
else:
    print("no arrangement works")
