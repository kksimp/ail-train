MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(month, day):
    return day + sum(DAYS[0:month - 1])

def date(n):
    left = n
    m = 0
    while left > DAYS[m]:
        left -= DAYS[m]
        m += 1
    return f"{MONTHS[m]} {left}"

frost = day_of_year(4, 20)
print(f"last frost: {date(frost)} (day {frost})")
crops = [("tomato", -6, "indoors"), ("pepper", -8, "indoors"), ("broccoli", -5, "indoors"), ("pea", -4, "outdoors"), ("carrot", -2, "outdoors"), ("bean", 1, "outdoors"), ("squash", 2, "outdoors"), ("tomato", 2, "transplant")]
for name, weeks, how in crops:
    when = frost + weeks * 7
    rel = f"{-weeks} weeks before" if weeks < 0 else f"{weeks} weeks after"
    print(f"{name:<9} {how:<10} {date(when):<7} ({rel})")
