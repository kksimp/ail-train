jobs = [("school", 12, 60, False, True), ("cafe menus", 2, 40, True, True), ("thesis", 87, 3, False, False), ("flyers", 1, 150, True, False), ("minutes", 5, 10, False, True)]

def sheets(pages, copies, duplex):
    return (pages + 1) // 2 * copies if duplex else pages * copies

def money(c):
    return f"{c // 100}.{c % 100:02d}"

day = 0
for cust, pages, copies, colour, duplex in jobs:
    sides = pages * copies
    rate = 35 if colour else 8
    off = 20 if sides > 500 else (10 if sides > 100 else 0)
    p = sides * rate * (100 - off) // 100 + sheets(pages, copies, duplex) * 2
    day += p
    kind = "colour" if colour else "b&w"
    print(f"{cust:<10} {sides:>4} {kind:<6} sides on {sheets(pages, copies, duplex):>3} sheets: {money(p)}")
print(f"day's printing: {money(day)}")
