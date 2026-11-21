def jdn(y, m, d):
    a = (14 - m) // 12; yy = y + 4800 - a; mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
wd = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for y, m, d in [(1582, 10, 15), (1969, 7, 20), (2000, 1, 1), (2000, 2, 29), (2024, 3, 1), (2026, 11, 21)]:
    j = jdn(y, m, d); print(f"{y}-{m:02}-{d:02}: day {j}, a {wd[(j + 1) % 7]}")
print(f"{jdn(2026, 11, 21) - jdn(1969, 7, 20)} days from the Moon landing to 2026-11-21")
