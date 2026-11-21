def jdn_greg(y, m, d):
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
def jdn_jul(y, m, d):
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - 32083
def greg_date(j):
    a = j + 32044
    b = (4 * a + 3) // 146097
    c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = 100 * b + d - 4800 + m // 10
    return f"{year}-{month:02}-{day:02}"
for y in [1500, 1582, 1700, 1752, 1900, 2026, 2100, 2200]:
    gap = jdn_jul(y, 3, 1) - jdn_greg(y, 3, 1)
    print(f"{y}: Julian calendar runs {gap} days behind")
events = [("Julian 1582-10-04, last day before the switch", 1582, 10, 4), ("Julian 1752-09-02, Britain switches", 1752, 9, 2), ("Julian 1917-10-25, Russian revolution", 1917, 10, 25), ("Julian 2026-12-25, Orthodox Christmas", 2026, 12, 25)]
for name, y, m, d in events:
    print(f"{name}: next day is Gregorian {greg_date(jdn_jul(y, m, d) + 1)}")
