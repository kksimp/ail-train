import datetime
N = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for y, m, d in [(2027, 1, 1), (2026, 12, 31), (2027, 3, 15), (2026, 6, 30), (2020, 12, 31), (2021, 1, 3), (2028, 12, 31)]:
    i = datetime.date(y, m, d).isocalendar(); print(f"{y}-{m:02}-{d:02} is {N[i[2] - 1]}, week {i[1]:02} of {i[0]}")
