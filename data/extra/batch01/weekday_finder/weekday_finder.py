import datetime, calendar
for y, m, d in [(2000, 1, 1), (1969, 7, 20), (2024, 2, 29), (1900, 3, 1), (2038, 1, 19)]:
    print(f"{y}-{m:02d}-{d:02d} is a {calendar.day_name[datetime.date(y, m, d).weekday()]}")
for y in range(2023, 2027):
    ms = [m for m in range(1, 13) if datetime.date(y, m, 13).weekday() == 4]
    print(f"{y}: Friday 13th in months " + ", ".join(map(str, ms)))
