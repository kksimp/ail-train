def limits(c):
    return {0: [5, 3], 3: [10, 3], 5: [10, 5], 6: [5, 3], 8: [100, 5], 9: [15, 5]}.get(c // 100, [10, 5])

year = 2026
items = [("Windows 7 basics", 5, 2010, 2016, False), ("Local history atlas", 911, 1998, 2025, False), ("Gardening month by month", 635, 2008, 2019, False), ("Pride and Prejudice", 823, 1990, 2026, True), ("Moby-Dick", 813, 1985, 2018, False), ("Birds of the coast", 598, 2015, 2024, False), ("Tax guide 2019", 336, 2019, 2020, False), ("Chemistry primer", 540, 2012, 2023, False)]
weed = 0
for title, c, published, last_loan, worn in items:
    lim = limits(c)
    age = year - published
    idle = year - last_loan
    reasons = []
    if age > lim[0] and idle > lim[1]:
        reasons.append(f"{age} years old, {idle} since a loan")
    if worn:
        reasons.append("worn")
    cls = str(c).rjust(3, '0')
    if not reasons:
        print(f"keep   {cls} {title}")
    else:
        weed += 1
        print(f"weed   {cls} {title}: {'; '.join(reasons)}")
print(f"{weed} of {len(items)} items to review")
