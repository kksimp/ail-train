MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def month_day(n):
    left = n
    m = 0
    while left > DAYS[m]:
        left -= DAYS[m]
        m += 1
    return [m, left]

first_tuesday = 59
holidays = [100, 121]
for week in range(10):
    tuesday = first_tuesday + week * 7
    moved = (tuesday - 1) in holidays
    day = tuesday + 1 if moved else tuesday
    md = month_day(day)
    bins = ["general" if week % 2 == 0 else "recycling"]
    if week % 2 == 1 and 2 <= md[0] <= 10:
        bins.append("garden")
    name = "Wed" if moved else "Tue"
    note = " (bank holiday)" if moved else ""
    shown = ", ".join(bins)
    print(f"{name} {md[1]:>2} {MONTHS[md[0]]}: {shown}{note}")
